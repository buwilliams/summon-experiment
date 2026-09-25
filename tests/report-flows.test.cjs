const {test}=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');

function setup(){
 const h={id:'h',name:'Hypothesis',statement:'Claim'},e={id:'e',hypothesis_id:'h',name:'Experiment'};
 const a={id:'a',session:'sa',experiment:e,hypothesis:h,included:true,view:{id:'v',name:'Perspective'},style:{name:'Style A'}};
 const b={...a,id:'b',session:'sb',style:{name:'Style B'}};
 const batch={id:'batch',name:'Batch',hypothesis:h,experiment:e,total:2,completed:2,session_ids:['sa','sb'],interviews:[{id:'sa',status:'submitted'},{id:'sb',status:'submitted'}]};
 const report={id:'r',name:'Report',batch_id:'batch',hypothesis:h,experiment:e,status:'complete',submissions:[a,b],pairs:[{key:'pair',ids:['a','b'],stage:'within',scores:{a:.731,b:.269},orders:[{},{}],order_gap:0}],rankings:{v:[{id:'a',score:.731,comparisons:1},{id:'b',score:.269,comparisons:1}]},cross_ranking:[],human:{records:[],votes:0,reviewers:0}};
 const state={catalog:{hypotheses:[h],experiments:[e]},batches:[batch],submissions:[a,b],reports:[report]},app={innerHTML:''};
 const context=vm.createContext({state,reviewer:'Buddy',judgmentSaving:false,judging:null,page:'dashboard',selectedExperiment:'e',document:{querySelectorAll:()=>[]},$:()=>app,on:()=>{},esc:x=>String(x??''),title:(name,intro)=>`<h1>${name}</h1>${intro}`,humanResults:()=>'<p>Human results</p>'});
 vm.runInContext(fs.readFileSync(path.join(__dirname,'../src/summon/static/reports.js'),'utf8'),context);
 function show(depth='report',detail='tests'){
  vm.runInContext(`Object.assign(reportFlows.dashboard,{depth:${JSON.stringify(depth)},hypothesis:'h',experiment:'e',batch:'batch',report:'r',detail:${JSON.stringify(detail)},item:'v'});reportScreen('dashboard');`,context);
  return app.innerHTML;
 }
 return {context,state,report,batch,show};
}
test('results stay blinded even when a detail screen is selected directly',()=>{
 const {show}=setup();
 const html=show('pair');
 assert.match(html,/Compare responses/);
 assert.doesNotMatch(html,/73\.1%|Style A|Mean Jev preference/);
});
test('another reviewer cannot unlock the current reviewer’s rankings',()=>{
 const {report,show}=setup();report.human.records=[{reviewer:'Someone else'}];
 assert.match(show('pair'),/Compare responses/);
 report.human.records.push({reviewer:' buddy '});
 assert.match(show('pair'),/73\.1%/);
});
test('report overview reveals choices, not every table at once',()=>{
 const {report,show}=setup();report.human.records=[{reviewer:'Buddy'}];
 const html=show();assert.match(html,/Within each test/);assert.match(html,/Comparison records/);
 assert.doesNotMatch(html,/<table|73\.1%/);
});
test('deleted live definitions remain discoverable through batch snapshots',()=>{
 const {context,state}=setup();state.catalog.hypotheses=[];state.catalog.experiments=[];
 const directory=context.reportDirectory();
 assert.equal(directory.hypotheses[0].id,'h');assert.equal(directory.experiments[0].id,'e');
});
test('batch readiness requires current included responses for every session',()=>{
 const {context,state,batch}=setup();assert.equal(context.batchReadiness(batch).ready,true);
 state.submissions[1].included=false;assert.equal(context.batchReadiness(batch).ready,false);
 state.submissions.push({...state.submissions[1],session:'superseded-session',included:true});
 assert.equal(context.batchReadiness(batch).ready,false);
});
