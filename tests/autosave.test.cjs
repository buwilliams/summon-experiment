const {test}=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');
function setup(fetch,storage=new Map()){
 const timers=new Map(),nodes=new Map();let id=0;
 const context=vm.createContext({structuredClone,fetch,state:{catalog:{revision:1},submissions:[]},
  document:{getElementById:key=>{if(!nodes.has(key))nodes.set(key,{});return nodes.get(key);}},
  localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v),removeItem:k=>storage.delete(k)},
  window:{addEventListener(){}},setTimeout:fn=>{timers.set(++id,fn);return id;},clearTimeout:id=>timers.delete(id)});
 vm.runInContext(fs.readFileSync(path.join(__dirname,'../src/summon/static/autosave.js'),'utf8'),context);
 return {context,storage,timers,nodes};
}
const ok=value=>({ok:true,json:async()=>value});
test('edits debounce and submission metadata saves without a button',async()=>{
 const calls=[];const {context,storage,timers}=setup(async(url,options)=>{calls.push(JSON.parse(options.body));return ok(JSON.parse(options.body));});
 const e=context.automaticEdit('submission-one',{notes:'',included:true},'submissions/one','PATCH');
 e.data.notes='first';e.changed();e.data.notes='final';e.data.included=false;e.changed();
 assert.equal(timers.size,1);assert.equal(calls.length,0);assert.ok(storage.has('summon-edit-submission-one'));
 await context.flushEditorSaves();assert.equal(calls.length,1);assert.deepEqual(calls[0],{notes:'final',included:false});
 assert.equal(e.status,'Saved');assert.equal(storage.size,0);
});
test('typing during a catalog request retains newer text and uses the new revision',async()=>{
 const requests=[];const {context,storage}=setup((url,options)=>new Promise(resolve=>requests.push({body:JSON.parse(options.body),resolve})));
 const e=context.automaticEdit('catalog',{revision:1,name:'original'},'catalog','PUT');
 e.data.name='first';e.changed();const first=e.flush();
 e.data.name='newer';e.changed();requests[0].resolve(ok({revision:2,name:'first'}));await first;
 assert.equal(e.data.name,'newer');assert.equal(e.data.revision,2);assert.equal(e.dirty,true);assert.ok(storage.has('summon-edit-catalog'));
 const second=e.flush();assert.equal(requests[1].body.revision,2);assert.equal(requests[1].body.name,'newer');
 requests[1].resolve(ok({revision:3,name:'newer'}));await second;
 assert.equal(e.status,'Saved');assert.equal(e.data.revision,3);assert.equal(storage.size,0);
});
test('incomplete fields stay in a local draft and save when completed',async()=>{
 let count=0;const {context,storage}=setup(async()=>{count++;return ok({revision:2,name:'done'});});
 const e=context.automaticEdit('catalog',{revision:1,name:''},'catalog','PUT',data=>!!data.name);
 e.changed();await e.flush();assert.equal(count,0);assert.match(e.status,/complete the required fields/);assert.ok(storage.has('summon-edit-catalog'));
 e.data.name='done';e.changed();await e.flush();assert.equal(count,1);assert.equal(e.dirty,false);
});
test('conflicts keep drafts and concurrent flushes do not spin',async()=>{
 let resolve,count=0;const {context,storage}=setup(()=>{count++;return new Promise(r=>resolve=r);});
 const e=context.automaticEdit('catalog',{revision:1,name:'draft'},'catalog','PUT');e.changed();
 const one=e.flush(),two=e.flush();resolve({ok:false,status:409,json:async()=>({detail:'Catalog changed elsewhere'})});
 await Promise.all([one,two]);assert.equal(count,1);assert.equal(e.dirty,true);assert.ok(storage.has('summon-edit-catalog'));assert.match(e.status,/Not saved/);
});
test('a draft already accepted before reload is recognized as saved',()=>{
 const storage=new Map([['summon-edit-catalog',JSON.stringify({revision:1,name:'same'})]]);
 const {context}=setup(async()=>{throw Error('No save needed');},storage);
 const e=context.automaticEdit('catalog',{revision:2,name:'same'},'catalog','PUT');
 assert.equal(e.dirty,false);assert.equal(e.status,'Saved');assert.equal(storage.size,0);
});
