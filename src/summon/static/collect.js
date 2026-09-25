let collectDepth='overview',collectHypothesis=null;
function collectionBreadcrumbs(batch){
 const e=state.catalog.experiments.find(x=>x.id===selectedExperiment);
 const h=state.catalog.hypotheses.find(x=>x.id===(collectHypothesis||e?.hypothesis_id));
 const path=[['overview','Collect']];
 if(collectDepth!=='overview'&&h)path.push(['hypothesis',h.name]);
 if(['experiment','batch','conversation'].includes(collectDepth)&&e)path.push(['experiment',e.name]);
 if(['batch','conversation'].includes(collectDepth)&&batch)path.push(['batch',batch.name]);
 if(collectDepth==='conversation')path.push(['conversation','Conversation']);
 return `<nav class="editor-breadcrumbs collect-breadcrumbs" aria-label="Collection hierarchy">${path.map(([level,name],i)=>`${i?'<span aria-hidden="true">›</span>':''}<button data-collect-level="${level}" ${level===collectDepth?'aria-current="page"':''}>${esc(name)}</button>`).join('')}</nav>`;
}
function bindCollectionBreadcrumbs(){
 document.querySelectorAll('[data-collect-level]').forEach(b=>b.onclick=()=>{if(sending)return;collectDepth=b.dataset.collectLevel;notice('');chat();window.scrollTo({top:0});});
}
function collectionScreen(){
 conversationDockObserver?.disconnect();
 const e=state.catalog.experiments.find(x=>x.id===selectedExperiment);
 const h=state.catalog.hypotheses.find(x=>x.id===collectHypothesis)||state.catalog.hypotheses.find(x=>x.id===e?.hypothesis_id);
 if(h)collectHypothesis=h.id;
 if(collectDepth==='hypothesis'&&!h)collectDepth='overview';
 if(['experiment','batch'].includes(collectDepth)&&!e)collectDepth='overview';
 const batches=e?scopeBatches():[],batch=batches.find(x=>x.id===selectedBatch);
 if(collectDepth==='batch'&&!batch)collectDepth='experiment';
 const card=(kind,id,name,detail)=>`<button class="drill-item" data-collect-${kind}="${esc(id)}"><span><strong>${esc(name)}</strong><small>${esc(detail)}</small></span><span aria-hidden="true">→</span></button>`;
 let content='',heading='',intro='';
 if(collectDepth==='overview'){
  heading='Collect';intro='Which hypothesis will you explore?';
  content=`<div class="drill-items">${state.catalog.hypotheses.map(h=>card('hypothesis',h.id,h.name,h.statement)).join('')}</div>`;
 }
 if(collectDepth==='hypothesis'){
  heading=h.name;intro=h.statement;
  const experiments=state.catalog.experiments.filter(x=>x.hypothesis_id===h.id);
  content=`<div class="drill-items">${experiments.map(x=>card('experiment',x.id,x.name,x.text.length>190?x.text.slice(0,187)+'…':x.text)).join('')||'<p class="muted">No experiments yet. Add one in Hypotheses.</p>'}</div>`;
 }
 if(collectDepth==='experiment'){
  heading=e.name;intro='Question Astra’s recommendations. Submit the responses you find convincing.';
  const total=state.catalog.views.filter(v=>e.view_ids.includes(v.id)).reduce((n,v)=>n+v.styles.length,0);
  content=`<section class="panel collect-start"><p class="scenario">${esc(e.text)}</p><div class="actions"><button id="collect-new" class="primary">${batches.length?'Start a new batch':'Start collecting'} →</button><span class="muted">${total} sessions · pause anytime</span></div><p class="muted">Astra will make the first recommendation.</p></section>${batches.length?`<section><h2>Your batches</h2><div class="drill-items">${batches.slice().reverse().map(b=>card('batch',b.id,b.name,`${b.completed} of ${b.total} submitted${b.in_progress?' · conversation in progress':''}`)).join('')}</div></section>`:''}`;
 }
 if(collectDepth==='batch'){
  heading=batch.name;intro=`${batch.completed} of ${batch.total} recommendations submitted`;
  const finished=batch.completed===batch.total;
  content=`<section class="panel"><progress value="${batch.completed}" max="${batch.total}" aria-label="Batch progress"></progress><div class="actions">${finished?'<button id="collect-analyze" class="primary">Analyze this batch →</button>':`<button id="collect-continue" class="primary">${batch.in_progress?'Continue conversation':'Start next conversation'} →</button>`}</div></section>${batch.interviews.length?`<div class="drill-items">${batch.interviews.map(s=>card('session',s.id,`${s.view} · ${s.style}`,s.status==='submitted'?'Submitted · review or revise':'In progress')).join('')}</div>`:''}`;
 }
 $('app').innerHTML=`<section class="interview collect-flow">${collectionBreadcrumbs(batch)}${title(heading,intro)}${content}</section>`;
 bindCollectionBreadcrumbs();
 document.querySelectorAll('[data-collect-hypothesis]').forEach(b=>b.onclick=()=>{if(sending)return;collectHypothesis=b.dataset.collectHypothesis;collectDepth='hypothesis';chat();});
 document.querySelectorAll('[data-collect-experiment]').forEach(b=>b.onclick=()=>{if(sending)return;selectedExperiment=b.dataset.collectExperiment;localStorage.setItem('summon-experiment',selectedExperiment);selectedBatch=null;current=null;collectDepth='experiment';chat();});
 document.querySelectorAll('[data-collect-batch]').forEach(b=>b.onclick=()=>{if(sending)return;selectedBatch=b.dataset.collectBatch;localStorage.setItem('summon-batch',selectedBatch);current=null;collectDepth='batch';chat();});
 document.querySelectorAll('[data-collect-session]').forEach(b=>b.onclick=()=>{if(sending)return;current=b.dataset.collectSession;collectDepth='conversation';chat();window.scrollTo({top:0});});
 on('collect-new',async()=>{
  if(sending)return;sending=true;$('collect-new').disabled=true;
  try{const b=await api('batches?experiment_id='+encodeURIComponent(selectedExperiment),{});selectedBatch=b.id;current=null;await refresh();collectDepth='conversation';}
  catch(error){sending=false;chat();throw error;}
  sending=false;await beginInterview();
 });
 on('collect-continue',async()=>{if(sending)return;collectDepth='conversation';await beginInterview();});
 on('collect-analyze',()=>{runnerBatch=batch.id;page='runner';render();});
}
