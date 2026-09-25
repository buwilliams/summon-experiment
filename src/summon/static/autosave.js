const automaticEdits=new Map();

function automaticEdit(key, initial, path, method, valid=()=>true){
 if(automaticEdits.has(key)){
  const edit=automaticEdits.get(key);
  if(!edit.dirty&&!edit.running)edit.data=structuredClone(initial);
  return edit;
 }
 let recovered;
 try{recovered=JSON.parse(localStorage.getItem('summon-edit-'+key)||'null');}catch{}
 if(key==='catalog'&&recovered&&recovered.schema_version!==initial.schema_version){localStorage.setItem('summon-legacy-edit-catalog',JSON.stringify(recovered));localStorage.removeItem('summon-edit-catalog');recovered=null;}
 if(recovered&&JSON.stringify({...recovered,...(key==='catalog'?{revision:initial.revision}:{})})===JSON.stringify(initial)){recovered=null;localStorage.removeItem('summon-edit-'+key);}
 const edit={data:recovered||structuredClone(initial),dirty:!!recovered,version:0,running:null,timer:null,status:recovered?'Draft restored':'Saved'};
 const status=text=>{edit.status=text;const node=document.getElementById(key==='catalog'?'editor-save-state':'save-status-'+key);if(node)node.textContent=text;};
 const persist=()=>localStorage.setItem('summon-edit-'+key,JSON.stringify(edit.data));
 edit.changed=()=>{edit.version++;edit.dirty=true;persist();status('Saving…');clearTimeout(edit.timer);edit.timer=setTimeout(edit.flush,650);};
 edit.flush=async()=>{
  clearTimeout(edit.timer);
  if(edit.running){await edit.running;if(edit.dirty&&edit.failedVersion!==edit.version)return edit.flush();return;}
  if(!edit.dirty)return;
  if(!valid(edit.data)){status('Draft saved on this device · complete the required fields');return;}
  const version=edit.version,body=structuredClone(edit.data);
  status('Saving…');
  edit.running=(async()=>{
   try{
    const response=await fetch('/api/'+path,{method,headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const saved=await response.json();
    if(!response.ok){const error=new Error(typeof saved.detail==='string'?saved.detail:'Unable to save changes');error.status=response.status;throw error;}
    if(key==='catalog'){edit.data.revision=saved.revision;state.catalog=structuredClone(saved);}
    else{const submission=state.submissions.find(s=>'submission-'+s.id===key);if(submission)Object.assign(submission,saved);}
    if(version===edit.version){edit.dirty=false;localStorage.removeItem('summon-edit-'+key);status('Saved');}
    else{persist();status('Saving…');}
   }catch(error){
    status('Not saved · '+error.message+' · draft kept on this device');
    // Network/server failures retry automatically; validation/conflicts need corrected input.
    if(!error.status||error.status>=500)edit.timer=setTimeout(edit.flush,3000);
    edit.failedVersion=edit.version;
   }
  })();
  await edit.running;edit.running=null;
  if(edit.dirty&&edit.failedVersion!==edit.version&&valid(edit.data))edit.timer=setTimeout(edit.flush,100);
 };
 automaticEdits.set(key,edit);
 if(recovered)edit.timer=setTimeout(edit.flush,650);
 return edit;
}

function validCatalogDraft(c){
 return c.hypotheses.every(h=>h.name.trim()&&h.statement.trim())
  &&c.experiments.every(e=>e.name.trim()&&e.text.trim()&&e.view_ids.length)
  &&c.views.every(v=>v.name.trim()&&v.styles.every(s=>s.name.trim()&&s.opening.trim()&&Object.values(s.openings||{}).every(x=>x.trim())));
}
function submissionEdit(s){return automaticEdit('submission-'+s.id,{notes:s.notes,included:s.included},'submissions/'+s.id,'PATCH');}
async function flushEditorSaves(){await Promise.all([...automaticEdits.values()].map(edit=>edit.flush()));}
// Persisted local drafts cover closing/reloading while a request is still in flight.
window.addEventListener('pagehide',()=>{for(const [key,edit] of automaticEdits)if(edit.dirty)localStorage.setItem('summon-edit-'+key,JSON.stringify(edit.data));});
