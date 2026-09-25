let cleanupSelection={scope:'batch',id:null}, cleanupPreview=null, dataLoading=0;
const recordNames={batch:'Batches',session:'Sessions (including revisions)',submission:'Selected responses',report:'Jev reports',ballot:'Human judgments (including pending)'};
const dataCounts=counts=>`<dl class="data-counts">${Object.entries(recordNames).map(([k,label])=>`<div><dt>${label}</dt><dd>${counts[k]||0}</dd></div>`).join('')}</dl>`;

async function dataManager(){
 const request=++dataLoading;
 $('app').innerHTML=title('Data','Manage collected data and restore development cleanups.')+'<div class="panel">Loading data…</div>';
 try{
  await refresh();const inventory=await api('data',undefined,'GET');
  if(page!=='dataManager'||request!==dataLoading)return;
  const targets=()=>{
   switch(cleanupSelection.scope){
    case 'experiment':return state.catalog.experiments.map(e=>({...e,name:`${state.catalog.hypotheses.find(h=>h.id===e.hypothesis_id)?.name} / ${e.name}`}));
    case 'batch':return state.batches.map(b=>({...b,name:`${b.experiment?.name||'Experiment'} / ${b.name} · ${b.completed}/${b.total}`}));
    case 'test':return state.sessions.map(s=>({...s,name:`${s.batch} / ${s.scenario.name} / ${s.view.name} / ${s.style.name} · ${s.status}`}));
    case 'report':return state.reports;
    default:return [];
   }
  };
  const list=targets();if(!list.some(x=>x.id===cleanupSelection.id))cleanupSelection.id=list[0]?.id||null;
  $('app').innerHTML=title('Data','Manage collected data and restore development cleanups.')+`<section class="panel"><h2>Collected data</h2>${dataCounts(inventory.counts)}<p><a href="/api/export">Download workspace JSON ↗</a></p></section><section class="panel"><h2>Clean up</h2><p>Hypotheses, experiment definitions, tests, styles, and catalog history are kept. Removed records are archived locally and can be restored below.</p>${inventory.busy?'<p class="muted">A model request or report is running. Wait for it to finish before cleaning up.</p>':''}<label for="cleanup-scope">What to clean up</label><select id="cleanup-scope">${[
   ['batch','One batch and its collected data'],['test','One session, all its revisions, and dependent results'],['report','One Jev report and its human judgments'],['experiment','All collected data for one experiment'],['judgments','All human judgments only'],['all','All collected data across all experiments']
  ].map(([id,label])=>`<option value="${id}" ${cleanupSelection.scope===id?'selected':''}>${label}</option>`).join('')}</select>${['all','judgments'].includes(cleanupSelection.scope)?'':`<label for="cleanup-target">Select record</label><select id="cleanup-target" ${!list.length?'disabled':''}>${list.length?opts(list,cleanupSelection.id):'<option>No records available</option>'}</select>`}<p class="muted">Removing a session also removes reports that used its responses and their human judgments. The batch remains available to collect that session again.</p><button id="preview-cleanup" ${inventory.busy||(!list.length&&!['all','judgments'].includes(cleanupSelection.scope))?'disabled':''}>Preview cleanup</button><div id="cleanup-preview"></div></section><section class="panel"><h2>Trash</h2><p class="muted">Archives stay on this computer and are excluded from Git. Restore returns records to their original locations and never overwrites changed data.</p>${inventory.trash.map(a=>`<div class="list-item"><h3>${esc(a.title)}</h3><p class="muted">${esc(a.created)} · ${esc(a.status)}</p>${dataCounts(a.counts)}<button data-restore="${a.id}" ${inventory.busy?'disabled':''}>Restore</button></div>`).join('')||'<p>No cleanup archives yet.</p>'}</section>`;
  on('cleanup-scope',()=>{cleanupSelection={scope:$('cleanup-scope').value,id:null};cleanupPreview=null;dataManager();},'change');
  on('cleanup-target',()=>{cleanupSelection.id=$('cleanup-target').value;cleanupPreview=null;$('cleanup-preview').innerHTML='';},'change');
  on('preview-cleanup',async()=>{
   $('preview-cleanup').disabled=true;
   try{
    cleanupPreview=await api('data/preview',cleanupSelection);
    const total=Object.values(cleanupPreview.counts).reduce((n,x)=>n+x,0);
    $('cleanup-preview').innerHTML=`<div class="cleanup-preview"><h3>${esc(cleanupPreview.title)}</h3>${dataCounts(cleanupPreview.counts)}<p>${total?'These records will leave the active workspace and move to recoverable trash.':'There is nothing to remove in this selection.'}</p><button id="confirm-cleanup" ${!total?'disabled':''}>Move these records to trash</button><button id="cancel-cleanup">Cancel</button></div>`;
    const confirmed={...cleanupSelection,fingerprint:cleanupPreview.fingerprint};
    on('cancel-cleanup',()=>{$('cleanup-preview').innerHTML='';cleanupPreview=null;});
    on('confirm-cleanup',async()=>{
     $('confirm-cleanup').disabled=true;
     try{await api('data/cleanup',confirmed);cleanupPreview=null;judging=null;activeBallot=null;await dataManager();notice('Records moved to trash. You can restore them below.');}
     catch(e){$('cleanup-preview').innerHTML='';cleanupPreview=null;throw e;}
    });
   }finally{if($('preview-cleanup'))$('preview-cleanup').disabled=false;}
  });
  document.querySelectorAll('[data-restore]').forEach(button=>button.onclick=async()=>{
   button.disabled=true;
   try{await api(`data/trash/${button.dataset.restore}/restore`,{});await dataManager();notice('Records restored.');}
   catch(e){notice(e.message);button.disabled=false;}
  });
 }catch(e){if(page==='dataManager'){$('app').innerHTML=title('Data','Data management could not be loaded.');notice(e.message);}}
}
