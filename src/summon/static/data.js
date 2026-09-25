let cleanupSelection={scope:'batch',id:null},cleanupPreview=null,dataLoading=0,dataDepth='overview',dataArchive=null,dataWorking=false;
const recordNames={batch:'Batches',session:'Sessions (including revisions)',submission:'Selected responses',report:'Jev reports',ballot:'Human judgments (including pending)'};
const dataCounts=counts=>`<dl class="data-counts">${Object.entries(recordNames).map(([k,label])=>`<div><dt>${label}</dt><dd>${counts[k]||0}</dd></div>`).join('')}</dl>`;
const cleanupScopes=[['batch','A batch','Its sessions, responses, and results'],['test','A session','All revisions and dependent results'],['report','A report','Its Jev and human judgments'],['experiment','An experiment’s collected data','All its batches and results'],['judgments','Human judgments','Keep Jev reports and collected responses'],['all','All collected data','Start collecting afresh; keep definitions']];
async function dataManager(){
 const request=++dataLoading;
 try{
  await refresh();const inventory=await api('data',undefined,'GET');
  if(page!=='dataManager'||request!==dataLoading)return;
  const scopes=new Map(cleanupScopes.map(([id,name])=>[id,name]));
  const targets=()=>{
   switch(cleanupSelection.scope){
    case 'experiment':return state.catalog.experiments.map(e=>({...e,detail:state.catalog.hypotheses.find(h=>h.id===e.hypothesis_id)?.name}));
    case 'batch':return state.batches.map(b=>({...b,detail:`${b.experiment?.name||'Experiment'} · ${b.completed}/${b.total} submitted`}));
    case 'test':return state.sessions.map(s=>({...s,name:`${s.view.name} · ${s.style.name}`,detail:`${s.batch} · ${s.scenario.name} · ${s.status}`}));
    case 'report':return state.reports.map(r=>({...r,detail:r.status}));
    default:return [];
   }
  };
  const list=targets(),archive=inventory.trash.find(x=>x.id===dataArchive);
  if(dataDepth==='archive'&&!archive)dataDepth='trash';
  if(dataDepth==='preview'&&!cleanupPreview)dataDepth='cleanup';
  const path=[['overview','Data']];
  if(['cleanup','targets','preview'].includes(dataDepth))path.push(['cleanup','Clean up']);
  if(['targets','preview'].includes(dataDepth))path.push(['targets',scopes.get(cleanupSelection.scope)]);
  if(dataDepth==='preview')path.push(['preview','Review removal']);
  if(['trash','archive'].includes(dataDepth))path.push(['trash','Trash']);
  if(dataDepth==='archive')path.push(['archive',archive.title]);
  if(dataDepth==='export')path.push(['export','Export']);
  let name='Data',intro='What would you like to do?',content='';
  const cards=html=>`<div class="drill-items">${html}</div>`;
  const busy=inventory.busy||dataWorking;
  if(dataDepth==='overview')content=cards(flowCard('data-data-enter','cleanup','Clean up','Remove collected data')+flowCard('data-data-enter','trash','Trash',`${inventory.trash.length} recoverable cleanups`)+flowCard('data-data-enter','export','Export','Download the saved workspace'));
  if(dataDepth==='cleanup'){
   name='Clean up';intro='Choose what to remove.';
   content=cards(cleanupScopes.map(([id,label,detail])=>flowCard('data-cleanup-scope',id,label,detail)).join(''));
  }
  if(dataDepth==='targets'){
   name=scopes.get(cleanupSelection.scope);intro='Choose the record to review.';
   content=cards(list.map(x=>flowCard('data-cleanup-target',x.id,x.name,x.detail)).join('')||'<p class="muted">No records to remove here.</p>');
  }
  if(dataDepth==='preview'){
   name=cleanupPreview.title;intro='Review what will move to trash.';
   const total=Object.values(cleanupPreview.counts).reduce((n,x)=>n+x,0);
   content=`<section class="panel">${dataCounts(cleanupPreview.counts)}<p class="muted">Definitions stay. Dependent reports and judgments are included above. You can restore this cleanup from Trash.</p>${inventory.busy?'<p>A model request is running. Wait for it to finish.</p>':''}<div class="actions"><button id="confirm-cleanup" ${busy||!total?'disabled':''}>Move these records to trash</button><button id="cancel-cleanup" ${dataWorking?'disabled':''}>Cancel</button></div>${!total?'<p>Nothing to remove in this selection.</p>':''}</section>`;
  }
  if(dataDepth==='trash'){
   name='Trash';intro='Choose a cleanup to restore.';
   content=cards(inventory.trash.map(a=>flowCard('data-trash-item',a.id,a.title,new Date(a.created).toLocaleString())).join('')||'<p class="muted">Trash is empty.</p>');
  }
  if(dataDepth==='archive'){
   name=archive.title;intro='Restore this cleanup.';
   content=`<section class="panel">${dataCounts(archive.counts)}<p class="muted">Saved ${esc(new Date(archive.created).toLocaleString())}. Existing changed data will not be overwritten.</p>${inventory.busy?'<p>A model request is running. Wait for it to finish.</p>':''}<button id="restore-data" class="primary" ${busy?'disabled':''}>Restore records →</button></section>`;
  }
  if(dataDepth==='export'){
   name='Export workspace';intro='A snapshot of the active data and definitions.';
   content=`<section class="panel">${dataCounts(inventory.counts)}<a class="action-link" href="/api/export">Download workspace JSON ↗</a><p class="muted">Local trash archives are separate from this export.</p></section>`;
  }
  $('app').innerHTML=flowShell(flowCrumbs(path,'data-data-level','Data hierarchy'),name,intro,content);
  const go=depth=>{if(dataWorking)return;dataDepth=depth;cleanupPreview=null;notice('');dataManager();};
  document.querySelectorAll('[data-data-level]').forEach(b=>b.onclick=()=>{if(b.getAttribute('aria-current'))return;const level=b.dataset.dataLevel;go(level==='targets'&&['all','judgments'].includes(cleanupSelection.scope)?'cleanup':level);});
  document.querySelectorAll('[data-data-enter]').forEach(b=>b.onclick=()=>go(b.dataset.dataEnter));
  async function preview(){
   if(dataWorking)return;dataWorking=true;
   const chosen={...cleanupSelection};
   document.querySelectorAll('[data-cleanup-target],[data-cleanup-scope]').forEach(b=>b.disabled=true);
   try{const result=await api('data/preview',chosen);if(page==='dataManager'&&request===dataLoading){cleanupPreview={...result,selection:chosen};dataDepth='preview';}}
   catch(error){notice(error.message);}finally{dataWorking=false;if(page==='dataManager')await dataManager();}
  }
  document.querySelectorAll('[data-cleanup-scope]').forEach(b=>b.onclick=()=>{if(dataWorking)return;cleanupSelection={scope:b.dataset.cleanupScope,id:null};if(['all','judgments'].includes(cleanupSelection.scope))preview();else go('targets');});
  document.querySelectorAll('[data-cleanup-target]').forEach(b=>b.onclick=()=>{if(dataWorking)return;cleanupSelection.id=b.dataset.cleanupTarget;preview();});
  document.querySelectorAll('[data-trash-item]').forEach(b=>b.onclick=()=>{dataArchive=b.dataset.trashItem;go('archive');});
  on('cancel-cleanup',()=>go(['all','judgments'].includes(cleanupSelection.scope)?'cleanup':'targets'));
  on('confirm-cleanup',async()=>{
   if(dataWorking||!cleanupPreview)return;
   const confirmed={...cleanupPreview.selection,fingerprint:cleanupPreview.fingerprint};
   dataWorking=true;$('confirm-cleanup').disabled=true;$('cancel-cleanup').disabled=true;
   try{const removed=await api('data/cleanup',confirmed);cleanupPreview=null;judging=null;activeBallot=null;dataArchive=removed.id;dataDepth='archive';notice('Records moved to trash.');}
   catch(error){cleanupPreview=null;dataDepth='cleanup';notice(error.message);}
   finally{dataWorking=false;if(page==='dataManager')await dataManager();}
  });
  on('restore-data',async()=>{
   if(dataWorking)return;dataWorking=true;$('restore-data').disabled=true;
   try{await api(`data/trash/${archive.id}/restore`,{});dataDepth='trash';notice('Records restored.');}
   catch(error){notice(error.message);}
   finally{dataWorking=false;if(page==='dataManager')await dataManager();}
  });
 }catch(error){if(page==='dataManager'&&request===dataLoading){$('app').innerHTML=flowShell(flowCrumbs([['overview','Data']],'data-data-level','Data hierarchy'),'Data','Could not load the saved data.','<button id="retry-data">Try again</button>');on('retry-data',()=>{dataDepth='overview';dataManager();});notice(error.message);}}
}
