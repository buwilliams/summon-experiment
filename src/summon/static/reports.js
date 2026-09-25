const reportFlows={runner:{depth:'overview'},dashboard:{depth:'overview'}};
const flowCard=(attribute,id,name,detail='')=>`<button class="drill-item" ${attribute}="${esc(id)}"><span><strong>${esc(name)}</strong>${detail?`<small>${esc(detail)}</small>`:''}</span><span aria-hidden="true">→</span></button>`;
const flowCrumbs=(path,attribute,label)=>`<nav class="editor-breadcrumbs collect-breadcrumbs" aria-label="${label}">${path.map(([id,name],i)=>`${i?'<span aria-hidden="true">›</span>':''}<button ${attribute}="${esc(id)}" ${i===path.length-1?'aria-current="page"':''}>${esc(name)}</button>`).join('')}</nav>`;
const flowShell=(crumbs,name,intro,content,wide=false)=>`<section class="focused-flow ${wide?'wide':''}">${crumbs}${title(esc(name),esc(intro))}${content}</section>`;
function reportDirectory(){
 // Retain access to evidence even after its live definition is deleted.
 const hypotheses=new Map(state.catalog.hypotheses.map(h=>[h.id,h]));
 const experiments=new Map(state.catalog.experiments.map(e=>[e.id,e]));
 for(const record of [...state.batches,...state.reports]){
  const source=record.submissions?.[0]||record,h=record.hypothesis||source.hypothesis,e=record.experiment||source.experiment;
  if(h&&!hypotheses.has(h.id))hypotheses.set(h.id,h);
  if(e&&!experiments.has(e.id))experiments.set(e.id,e);
 }
 return {hypotheses:[...hypotheses.values()],experiments:[...experiments.values()]};
}
const reportsInBatch=b=>state.reports.filter(r=>r.batch_id===b.id||(!r.batch_id&&r.submissions.length&&r.submissions.every(s=>b.session_ids.includes(s.session))));
const ownJudgments=r=>(r.human?.records||[]).filter(b=>b.reviewer.trim().toLowerCase()===reviewer.trim().toLowerCase());
function batchReadiness(batch){
 const ids=new Set(batch.interviews.filter(i=>i.status==='submitted').map(i=>i.id));
 const included=state.submissions.filter(s=>s.included&&ids.has(s.session)).length;
 return {included,ready:batch.total>0&&batch.completed===batch.total&&included===batch.total};
}
function openReportBatch(surface,batch){
 reportFlows[surface]={depth:'batch',hypothesis:batch.hypothesis?.id,experiment:batch.experiment?.id,batch:batch.id};
 selectedExperiment=batch.experiment?.id;page=surface;judging=null;render();
}
function openReport(surface,id){
 const r=state.reports.find(r=>r.id===id);if(!r)return;
 const source=r.submissions[0],e=r.experiment||source?.experiment,h=r.hypothesis||source?.hypothesis;
 const batch=state.batches.find(b=>b.id===r.batch_id||b.session_ids.includes(source?.session));
 reportFlows[surface]={depth:'report',hypothesis:h?.id,experiment:e?.id,batch:batch?.id,report:id};
 selectedExperiment=e?.id;page=surface;judging=null;render();
}
function reportPath(surface,extra=[]){
 const f=reportFlows[surface],d=reportDirectory(),path=[['overview',surface==='runner'?'Analyze':'Results']];
 const h=d.hypotheses.find(x=>x.id===f.hypothesis),e=d.experiments.find(x=>x.id===f.experiment),b=state.batches.find(x=>x.id===f.batch),r=state.reports.find(x=>x.id===f.report);
 if(f.depth!=='overview'&&h)path.push(['hypothesis',h.name]);
 if(!['overview','hypothesis'].includes(f.depth)&&e)path.push(['experiment',e.name]);
 if(['batch','report','detail','pair'].includes(f.depth)&&b)path.push(['batch',b.name]);
 if(['report','detail','pair'].includes(f.depth)&&r)path.push(['report','Report']);
 if(['detail','pair'].includes(f.depth))path.push(['detail',({human:'Human judgments',tests:'Within each test',cross:'Across test winners',records:'Comparison records'})[f.detail]]);
 return [...path,...extra];
}
function reportBreadcrumbs(surface,extra=[]){return flowCrumbs(reportPath(surface,extra),'data-report-level','Report hierarchy');}
function bindReportBreadcrumbs(surface){
 document.querySelectorAll('[data-report-level]').forEach(b=>b.onclick=()=>{if(judgmentSaving||b.dataset.reportLevel==='judging')return;judging=null;reportFlows[surface].depth=b.dataset.reportLevel;notice('');render();window.scrollTo({top:0});});
}
function runner(){if(judging){judgingScreen();return;}reportScreen('runner');}
function dashboard(){reportScreen('dashboard');}
function reportScreen(surface){
 const f=reportFlows[surface],directory=reportDirectory();
 const h=directory.hypotheses.find(x=>x.id===f.hypothesis),e=directory.experiments.find(x=>x.id===f.experiment);
 const batch=state.batches.find(x=>x.id===f.batch),r=state.reports.find(x=>x.id===f.report);
 if(f.depth!=='overview'&&!h)f.depth='overview';
 if(['experiment','batch','report','detail','pair'].includes(f.depth)&&!e)f.depth='hypothesis';
 if(f.depth==='batch'&&!batch)f.depth='experiment';
 if(['report','detail','pair'].includes(f.depth)&&!r)f.depth=batch?'batch':'experiment';
 let name=surface==='runner'?'Analyze':'Results',intro=surface==='runner'?'Which hypothesis will you evaluate?':'Which hypothesis’s evidence will you review?',content='';
 const cards=html=>`<div class="drill-items">${html}</div>`;
 if(f.depth==='overview')content=cards(directory.hypotheses.map(h=>flowCard('data-report-hypothesis',h.id,h.name,h.statement)).join(''));
 if(f.depth==='hypothesis'){
  name=h.name;intro='Choose an experiment.';
  content=cards(directory.experiments.filter(x=>x.hypothesis_id===h.id).map(x=>flowCard('data-report-experiment',x.id,x.name,`${state.batches.filter(b=>b.experiment?.id===x.id).length} batches`)).join('')||'<p class="muted">No experiments in this hypothesis yet.</p>');
 }
 if(f.depth==='experiment'){
  name=e.name;intro='Choose a batch.';
  const batches=state.batches.filter(b=>b.experiment?.id===e.id);
  content=cards(batches.slice().reverse().map(b=>flowCard('data-report-batch',b.id,b.name,surface==='runner'?`${b.participant} · ${b.completed} of ${b.total} responses submitted`:`${b.participant} · ${reportsInBatch(b).length} reports`)).join(''));
  if(!batches.length)content=`<section class="panel empty"><p>No batches collected yet.</p><button id="report-collect" class="primary">Collect responses →</button></section>`;
 }
 if(f.depth==='batch'){
  name=batch.name;const runs=reportsInBatch(batch),readiness=batchReadiness(batch);
  intro=surface==='runner'?`${batch.completed} of ${batch.total} responses submitted`:'Choose a report to review.';
  if(surface==='runner')content=`<section class="panel"><progress value="${batch.completed}" max="${batch.total}" aria-label="Batch progress"></progress>${runs.some(r=>r.status==='running')?'<p>Jev is comparing responses.</p>':readiness.ready?`${runs.length?'<details><summary>Run another comparison</summary>':''}<button id="run-batch" class="primary">Run Jev comparison →</button>${runs.length?'</details>':''}`:`<p>${batch.completed<batch.total?'Finish collecting this batch before comparing it.':'Some submitted responses are excluded from reports.'}</p><button id="report-collect" class="primary">${batch.completed<batch.total?'Continue collecting':'Review submissions'} →</button>`}<details><summary>What Jev compares</summary><p>Only selected responses, every pair in both answer orders. Styles compete within each test; the winners advance across tests.</p></details></section>`;
  content+=cards(runs.slice().reverse().map(r=>flowCard('data-open-report',r.id,r.name,`${r.status} · ${r.pairs.filter(p=>p.scores).length} ${r.pairs.filter(p=>p.scores).length===1?'pair':'pairs'} compared`)).join(''));
  if(surface==='dashboard'&&!runs.length)content=`<section class="panel empty"><p>This batch has no report yet.</p><button id="report-analyze" class="primary">Analyze this batch →</button></section>`;
 }
 if(['report','detail','pair'].includes(f.depth)){
  name=r.name;intro=`${r.pairs.filter(p=>p.scores).length} ${r.pairs.filter(p=>p.scores).length===1?'pair':'pairs'} compared · ${r.status}`;
  const votes=ownJudgments(r),revealed=r.status==='complete'&&votes.length>=r.pairs.length;
  if(r.status!=='complete'){
   content=`<section class="panel"><p>${r.status==='running'?'Jev is comparing the selected responses.':'This comparison has not finished.'}</p>${r.error?`<p class="muted">${esc(r.error)}</p>`:''}${['failed','interrupted'].includes(r.status)?'<button id="resume-report" class="primary">Resume comparison →</button>':''}<p class="muted">${r.pairs.reduce((n,p)=>n+p.orders.length,0)} calls saved</p></section>`;
  }else if(surface==='runner'||!revealed){
   intro=surface==='runner'?'Choose your preferred responses before seeing Jev’s results.':'Add your judgments to reveal this report.';
   content=`<section class="panel"><p>Judging as <strong>${esc(reviewer)}</strong></p><p class="muted" id="reviewer-progress">${votes.length} of ${r.pairs.length} judgments saved</p><button id="compare-report" class="primary">${votes.length>=r.pairs.length?'Review judgments':votes.length?'Continue comparing':'Compare responses'} →</button>${revealed?'<button id="show-results">View results →</button>':''}</section>`;
  }else{
   const label=id=>{const s=r.submissions.find(s=>s.id===id);return s?`${s.view.name} / ${s.style.name}`:id;};
   const table=rows=>`<section class="panel table-scroll"><table><thead><tr><th>Response</th><th>Mean Jev preference</th><th>Pairs</th></tr></thead><tbody>${rows.map(x=>`<tr><td>${esc(label(x.id))}</td><td>${x.score===null?'—':(x.score*100).toFixed(1)+'%'}</td><td>${x.comparisons}</td></tr>`).join('')}</tbody></table><p class="muted">Pairwise preference scores, not confidence intervals or proof of effectiveness.</p></section>`;
   if(f.depth==='report'){
    intro=`${r.human?.votes||0} human ${r.human?.votes===1?'judgment':'judgments'} · ${r.human?.reviewers||0} ${r.human?.reviewers===1?'reviewer':'reviewers'}`;
    content=cards([['human','Human judgments','Preferences and agreement with Jev'],['tests','Within each test','Compare prompting styles'],['cross','Across test winners','Compare the finalists'],['records','Comparison records','Inspect individual pairs and calls']].map(([id,note,detail])=>flowCard('data-result-detail',id,note,detail)).join(''));
   }else if(f.detail==='human')content=humanResults(r,label);
   else if(f.detail==='cross'){name='Across test winners';content=r.cross_ranking.some(x=>x.comparisons)?table(r.cross_ranking):'<section class="panel">This report needs at least two complete tests to compare their winners.</section>';}
   else if(f.detail==='tests'){
    name='Within each test';
    if(f.depth==='pair'&&r.rankings[f.item]){name=r.submissions.find(s=>s.view.id===f.item)?.view.name||name;content=table(r.rankings[f.item]);}
    else content=cards(Object.entries(r.rankings).map(([id,rows])=>flowCard('data-result-item',id,r.submissions.find(s=>s.view.id===id)?.view.name||id,`${rows.length} styles`)).join(''));
   }else if(f.detail==='records'){
    name='Comparison records';const pair=r.pairs.find(p=>p.key===f.item);
    if(f.depth==='pair'&&pair){name=pair.ids.map(label).join(' ↔ ');content=`<section class="panel"><p>${pair.stage==='cross'?'Across tests':'Within one test'} · ${pair.scores?'Complete':'Incomplete'}</p>${pair.scores?`<p>Reversed-order difference: ${(pair.order_gap*100).toFixed(1)} percentage points.</p>`:''}<pre>${esc(JSON.stringify(pair,null,2))}</pre></section>`;}
    else content=cards(r.pairs.map(p=>flowCard('data-result-item',p.key,p.ids.map(label).join(' ↔ '),p.stage==='cross'?'Across tests':'Within one test')).join(''));
   }
  }
 }
 const extra=f.depth==='pair'?[['pair',name]]:[];
 $('app').innerHTML=flowShell(reportBreadcrumbs(surface,extra),name,intro,content);
 bindReportBreadcrumbs(surface);
 document.querySelectorAll('[data-report-hypothesis]').forEach(b=>b.onclick=()=>{Object.assign(f,{depth:'hypothesis',hypothesis:b.dataset.reportHypothesis});render();});
 document.querySelectorAll('[data-report-experiment]').forEach(b=>b.onclick=()=>{Object.assign(f,{depth:'experiment',experiment:b.dataset.reportExperiment});render();});
 document.querySelectorAll('[data-report-batch]').forEach(b=>b.onclick=()=>{f.depth='batch';f.batch=b.dataset.reportBatch;render();});
 document.querySelectorAll('[data-open-report]').forEach(b=>b.onclick=()=>openReport(surface,b.dataset.openReport));
 document.querySelectorAll('[data-result-detail]').forEach(b=>b.onclick=()=>{f.depth='detail';f.detail=b.dataset.resultDetail;f.item=null;render();});
 document.querySelectorAll('[data-result-item]').forEach(b=>b.onclick=()=>{f.depth='pair';f.item=b.dataset.resultItem;render();});
 on('report-collect',()=>{if(batch&&!sameUser(batch.participant,activeUser)){notice('Switch to '+batch.participant+' to continue their collection.');return;}if(batch&&batch.completed===batch.total&&!batchReadiness(batch).ready){editorDepth='overview';page='editor';render();const submissions=document.querySelector('.editor-submissions');if(submissions){submissions.open=true;submissions.scrollIntoView({block:'start'});}return;}selectedExperiment=e.id;collectHypothesis=h.id;selectedBatch=batch?.id;current=null;collectDepth=batch?(state.catalog.experiments.some(x=>x.id===e.id)?'batch':'conversation'):'experiment';page='chat';render();});
 on('report-analyze',()=>openReportBatch('runner',batch));
 on('run-batch',async()=>{const button=$('run-batch');button.disabled=true;button.textContent='Starting comparison…';try{const reports=await api('batches/'+batch.id+'/reports',{});await refresh();if(page===surface)openReport(surface,reports[0].id);}catch(error){if(page===surface)render();throw error;}});
 on('resume-report',async()=>{$('resume-report').disabled=true;try{await api('reports/'+r.id+'/resume',{});await refresh();}finally{if(page===surface)render();}});
 on('compare-report',async()=>{$('compare-report').disabled=true;try{await startJudging(r.id);}catch(error){if(page===surface)render();throw error;}});
 on('show-results',()=>openReport('dashboard',r.id));
}
