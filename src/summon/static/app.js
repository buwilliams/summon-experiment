let runnerBatch=null, conversationDockObserver;
let state, page='chat', current=null, sending=false, reportId=null, selectedBatch=localStorage.getItem('summon-batch');
const $=id=>document.getElementById(id);
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const opts=(items,value)=>items.map(x=>`<option value="${esc(x.id)}" ${x.id===value?'selected':''}>${esc(x.name)}</option>`).join('');
const title=(name,desc)=>`<h1>${name}</h1><p class="intro">${desc}</p>`;
const notice=text=>{$('notice').textContent=text;$('notice').hidden=!text;};
async function api(path,body,method='POST'){const r=await fetch('/api/'+path,{method,headers:{'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});const data=await r.json();if(!r.ok)throw Error(typeof data.detail==='string'?data.detail:JSON.stringify(data.detail));return data;}
async function refresh(){state=await api('state',undefined,'GET');
 const sessionIds=new Set(state.sessions.map(s=>s.id));
 Object.keys(localStorage).filter(k=>k.startsWith('summon-draft-')&&!sessionIds.has(k.slice('summon-draft-'.length))).forEach(k=>localStorage.removeItem(k));
 if(current&&!sessionIds.has(current))current=null;
 if(selectedBatch&&!state.batches.some(b=>b.id===selectedBatch)){selectedBatch=null;localStorage.removeItem('summon-batch');}
$('connection').textContent=state.connected?'● GPT-6 Astra · connected key':'API key required';}
function on(id,fn,event='click'){if($(id))$(id).addEventListener(event,async e=>{try{await fn(e);}catch(err){notice(err.message);}});}
function render(){document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.page===page));({chat,editor,runner,dashboard,dataManager})[page]();}
document.querySelectorAll('nav button').forEach(b=>b.onclick=async()=>{if(sending)return notice('Wait for the current response before switching screens.');await flushEditorSaves();page=b.dataset.page;notice('');render();});
async function beginInterview(){
 if(sending)return;
 sending=true;notice('Astra is preparing the first recommendation from the experiment, test, and style…');
 document.querySelectorAll('#next-interview,#new-batch,#batch-picker,[data-batch-session]').forEach(b=>b.disabled=true);
 try{if(!selectedBatch){const b=await api('batches?experiment_id='+encodeURIComponent(selectedExperiment),{});selectedBatch=b.id;}const session=await api('interview/next'+(selectedBatch?'?batch_id='+encodeURIComponent(selectedBatch):''),{});current=session.complete?null:session.id;notice('');}
 finally{sending=false;await refresh();if(current){selectedBatch=state.batches.find(b=>b.session_ids.includes(current))?.id;localStorage.setItem('summon-batch',selectedBatch);}chat();}
}
function chat(){
 if(collectDepth!=='conversation'){collectionScreen();return;}
 const batches=scopeBatches();
 const explicit=state.sessions.find(x=>x.id===current&&x.experiment?.id===selectedExperiment);
 if(explicit)selectedBatch=state.batches.find(b=>b.session_ids.includes(explicit.id))?.id;
 const batch=batches.find(b=>b.id===selectedBatch)||batches.at(-1);
 if(!batch){selectedBatch=null;current=null;}
 if(batch){selectedBatch=batch.id;localStorage.setItem('summon-batch',batch.id);}
 const inBatch=state.sessions.filter(x=>batch?.session_ids.includes(x.id));
 const s=explicit||inBatch.filter(x=>x.status==='open').at(-1)||inBatch.at(-1);
 if(s)current=s.id;
 collectHypothesis=batch?.hypothesis?.id||state.catalog.experiments.find(e=>e.id===selectedExperiment)?.hypothesis_id||collectHypothesis;
 const finished=batch&&batch.completed===batch.total;
 const draftKey='summon-draft-'+(s?.id||'new');
 $('app').innerHTML=`<section class="interview collect-conversation">${collectionBreadcrumbs(batch)}<div class="collect-chat-heading"><h1>${esc(s?.scenario.name||batch?.experiment.name||'Conversation')}</h1><span class="muted">${batch?.completed||0} / ${batch?.total||0} submitted</span></div>
 <div class="panel conversation" aria-label="Interview conversation">
 ${s?`<article class="message interviewer"><div class="who">EXPERIMENT</div><div class="body">${esc(s.scenario.text)}</div></article>
 <div id="messages">${s.messages.map((m,i)=>i===0&&s.initial_prompt?`<details class="opening-record"><summary>Initial prompt sent to Astra · experiment, test, and style</summary><pre>${esc(m.content)}</pre></details>`:`<article class="message ${m.role}"><div class="who">${m.role==='user'?'YOU':'ASTRA'}</div><div class="body markdown">${m.html||esc(m.content)}</div>${m.role==='assistant'&&s.status==='open'?`<button data-submit="${i}">Submit this recommendation</button>`:''}</article>`).join('')}</div>
 ${s.status==='open'?`${!s.messages.length?`<p class="muted">Astra will receive the experiment, test, and style to prepare its first recommendation.</p><button id="generate-opening" class="primary">${s.error?'Retry initial recommendation':'Generate initial recommendation'}</button>`:``}`:`<div class="interview-finished"><p>Your selected recommendation has been saved.</p><div class="actions"><button id="revise-interview">Revise this session</button>${finished?'<button id="collect-complete" class="primary">Review completed batch →</button>':'<button id="next-interview" class="primary">Continue to next session →</button>'}</div></div>`}`:
 `<article class="message interviewer"><div class="who">SUMMON</div><p>Astra will receive the experiment, test, and style and produce the first recommendation with reasons. Then question its responses until you find one acceptable to submit.</p><button id="next-interview" class="primary">Start session →</button></article>`}
 </div>${s?`<div class="conversation-dock">${s.status==='open'&&s.messages.length?`<div class="composer"><label for="prompt">${s.messages.length?'What would you like to ask next?':'What would you like to ask?'}</label><textarea id="prompt" aria-describedby="prompt-help" placeholder="Write your message…">${esc(s.pending||localStorage.getItem(draftKey)||'')}</textarea><div class="actions"><span id="prompt-help" class="muted">Enter to send · Shift+Enter for a new line</span><button id="send" class="primary">Send message ↑</button></div></div>`: ''}<section class="test-context" aria-label="Current session: test and style"><div class="test-context-names"><div><span class="label">Test</span><strong>${esc(s.view.name)}</strong></div><div><span class="label">Style</span><strong>${esc(s.style.name)}</strong></div></div><div class="test-context-instructions"><details><summary>Style instructions</summary><p>${esc(s.style.opening.replaceAll('{{SCENARIO}}','').replaceAll('{{EXPERIMENT}}','').trim()||'Ask about the experiment in plain language.')}</p></details></div></section></div>`:''}</section>`;
 conversationDockObserver?.disconnect();
 const dock=document.querySelector('.conversation-dock'),interview=document.querySelector('.interview');
 if(dock){conversationDockObserver=new ResizeObserver(()=>{interview.style.paddingBottom=(dock.getBoundingClientRect().height+40)+'px';});conversationDockObserver.observe(dock);}
 bindCollectionBreadcrumbs();
 on('revise-interview',async()=>{if(sending)return;$('revise-interview').disabled=true;try{const draft=await api(`sessions/${current}/revise`,{});current=draft.id;await refresh();chat();}catch(e){chat();throw e;}});
 on('next-interview',beginInterview);
 on('collect-complete',()=>{collectDepth='batch';chat();});
 on('generate-opening',async()=>{if(sending)return;sending=true;$('generate-opening').disabled=true;notice('Astra is preparing the initial recommendation…');try{await api(`sessions/${current}/opening`,{});notice('');}finally{sending=false;await refresh();chat();}});
 on('prompt',()=>localStorage.setItem(draftKey,$('prompt').value),'input');
 on('prompt',e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing&&e.keyCode!==229){e.preventDefault();if(!e.repeat&&!sending)$('send').click();}},'keydown');
 $('prompt')?.focus({preventScroll:true});
 on('send',async()=>{if(sending)return;const text=$('prompt').value;if(!text.trim())return;sending=true;$('send').disabled=true;$('send').textContent='Astra is thinking…';$('prompt').disabled=true;document.querySelectorAll('[data-submit],#use-opening,#new-batch,#batch-picker,[data-batch-session]').forEach(b=>b.disabled=true);notice('');try{await api(`sessions/${current}/messages`,{text});localStorage.removeItem(draftKey);}finally{sending=false;await refresh();chat();}});
 document.querySelectorAll('[data-submit]').forEach(b=>b.onclick=async()=>{if(sending)return;sending=true;document.querySelectorAll('[data-submit],#send,#new-batch,#batch-picker,[data-batch-session]').forEach(x=>x.disabled=true);try{await api(`sessions/${current}/submit`,{message:Number(b.dataset.submit)});localStorage.removeItem(draftKey);await refresh();chat();}catch(e){notice(e.message);chat();}finally{sending=false;}});
}
function runner(){
 if(judging){judgingScreen();return;}
 const picker=studyPicker(),batches=scopeBatches();
 const batch=batches.find(b=>b.id===(runnerBatch||selectedBatch))||batches.at(-1);
 if(batch)runnerBatch=batch.id;
 const latestIds=new Set(batch?.interviews.filter(i=>i.status==='submitted').map(i=>i.id)||[]);
 const subs=state.submissions.filter(s=>s.included&&latestIds.has(s.session));
 const ready=batch&&batch.completed===batch.total&&subs.length===batch.total&&batch.total>0;
 const runs=state.reports.filter(r=>r.batch_id===batch?.id||(batch&&r.submissions.every(s=>batch.session_ids.includes(s.session))));
 const running=runs.some(r=>r.status==='running');
 $('app').innerHTML=title('Analyze','Collect Jev and human preferences for the selected batch.')+picker+`<div class="workspace"><section class="panel"><label for="report-batch">Batch to evaluate</label><select id="report-batch" ${!batch?'disabled':''}>${batches.length?opts(batches.map(b=>({...b,name:b.name+' · '+b.completed+'/'+b.total+' complete'})),batch.id):'<option>No batches yet</option>'}</select>
 ${batch?`<h2 style="margin-top:24px">${batch.completed} of ${batch.total} sessions complete</h2><progress value="${batch.completed}" max="${batch.total}" aria-label="Selected batch progress"></progress><p class="muted">${ready?'Ready to run. Each experiment gets its own report, comparing styles within tests and then the test winners.':batch.completed<batch.total?'Finish the remaining sessions or revisions before running this batch.':'One or more submissions are excluded. Include them or submit replacements before running.'}</p>
 ${batch.catalog.scenarios.map(sc=>{const total=batch.catalog.views.reduce((n,v)=>n+v.styles.length,0);const count=subs.filter(s=>s.scenario.id===sc.id).length;return `<div class="list-item"><strong>${esc(sc.name)}</strong><p class="muted">${count} of ${total} responses ready</p></div>`;}).join('')}
 <div class="actions"><button id="run-batch" class="primary" ${!ready||running?'disabled':''}>${running?'Reports are running…':'Run batch reports ↗'}</button></div>`:'<div class="empty">Start a batch in Collect and submit its recommendations to create reports.</div>'}
 </section><aside><div class="panel soft"><h2>What will be compared</h2><p class="guidance">Only the selected response from each interview is judged. Every pair runs in both answer orders. Comparisons stay within the same experiment.</p><p class="muted">The latest submitted revision is used. Full conversations are retained as history and are not sent to Jev.</p></div><div class="panel"><h2>Reports for this batch</h2>${runs.slice().reverse().map(r=>`<div class="list-item"><strong>${esc(r.name)}</strong><p class="muted">${esc(r.status)} · ${r.pairs.filter(p=>p.scores).length} pairs saved</p><button data-report="${r.id}">View report ↗</button></div>`).join('')||'<p class="muted">No reports for this batch yet.</p>'}</div></aside></div>`+humanControls(runs);
 bindStudyPicker();bindHumanControls();
 on('report-batch',()=>{runnerBatch=$('report-batch').value;runner();},'change');
 on('run-batch',async()=>{const button=$('run-batch');button.disabled=true;button.textContent='Starting reports…';try{const reports=await api('batches/'+runnerBatch+'/reports',{});reportId=reports[0]?.id;await refresh();page='runner';render();}catch(e){await refresh();runner();throw e;}});
 bindReports();
}
function bindReports(){document.querySelectorAll('[data-report]').forEach(b=>b.onclick=()=>{reportId=b.dataset.report;page='dashboard';render();});}
function dashboard(){
 const picker=studyPicker(), reports=scopeReports();
 const r=reports.find(x=>x.id===reportId)||reports.at(-1);
 const mine=r?.human?.records.filter(b=>b.reviewer.trim().toLowerCase()===reviewer.trim().toLowerCase())||[];
 if(r&&(r.status!=='complete'||mine.length<r.pairs.length)){
 $('app').innerHTML=title('Results','Jev results are revealed after your anonymous judgments are saved.')+picker+`<section class="panel"><label for="report-select">Report</label><select id="report-select">${opts(reports,r.id)}</select><p>${esc(r.status)} · ${r.pairs.filter(p=>p.scores).length} pairs compared by Jev</p>${r.error?`<p>${esc(r.error)}</p>`:''}${['failed','interrupted'].includes(r.status)?'<button id="resume">Resume unfinished comparisons</button>':''}<p>Save your preference for each pair in Analyze to view the complete comparison with Jev.</p></section>`+humanControls([r]);
 bindStudyPicker();bindHumanControls();on('report-select',()=>{reportId=$('report-select').value;dashboard();},'change');on('resume',async()=>{await api('reports/'+r.id+'/resume',{});await refresh();dashboard();});return;
 }
 const label=id=>{const s=r.submissions.find(x=>x.id===id);return s?`${s.view.name} / ${s.style.name}`:id;};
 const table=rows=>`<table><thead><tr><th>Solution</th><th>Mean preference</th><th>Pairs</th></tr></thead><tbody>${rows.map(x=>`<tr><td>${esc(label(x.id))}</td><td>${x.score===null?'—':(x.score*100).toFixed(1)+'%'}<div class="bar"><i style="width:${(x.score||0)*100}%"></i></div></td><td>${x.comparisons}</td></tr>`).join('')}</tbody></table>`;
 $('app').innerHTML=title('Results','Compare human preferences with Jev’s judgments.')+picker+`<div class="stat-grid"><div class="stat"><span class="label">HUMAN SESSIONS</span><strong>${state.sessions.filter(s=>s.experiment?.id===selectedExperiment).length}</strong></div><div class="stat"><span class="label">SUBMITTED SOLUTIONS</span><strong>${state.submissions.filter(s=>s.experiment?.id===selectedExperiment).length}</strong></div><div class="stat"><span class="label">COMPLETED REPORTS</span><strong>${reports.filter(r=>r.status==='complete').length}</strong></div></div>${r?`<div class="panel"><div class="row"><h2>${esc(r.name)}</h2><span class="pill">${esc(r.status)}</span><select id="report-select" aria-label="Saved report">${opts(reports,r.id)}</select></div><p class="muted">${esc(r.submissions[0].scenario.name)} · ${esc(r.submissions[0].batch)} · ${r.pairs.filter(p=>p.scores).length} complete pairs · ${r.pairs.reduce((n,p)=>n+p.orders.length,0)} Jev calls saved</p>${r.error?`<p>${esc(r.error)}</p>`:''}${['failed','interrupted'].includes(r.status)?'<button id="resume" class="primary">Resume unfinished comparisons</button>':''}${r.status!=='complete'?'<p class="muted">Results are incomplete. Final rankings appear when all required comparisons finish.</p>':''}</div>${humanResults(r,label)}${r.status==='complete'?Object.entries(r.rankings).map(([v,rows])=>`<div class="panel"><div class="label">JEV · WITHIN TEST</div><h2>${esc(r.submissions.find(s=>s.view.id===v).view.name)}</h2>${table(rows)}</div>`).join('')+`<div class="panel"><div class="label">JEV · ACROSS TEST WINNERS</div>${r.cross_ranking.some(x=>x.comparisons)?table(r.cross_ranking):'<p class="muted">Include at least two complete tests to compare their winners.</p>'}</div>`:''}<div class="panel"><h2>Comparison record</h2>${r.pairs.map(p=>`<details><summary>${esc(label(p.ids[0]))} ↔ ${esc(label(p.ids[1]))} · ${p.stage} · ${p.scores?'complete':p.orders.length+'/2 calls'}</summary>${p.scores?`<p class="muted">Reversed-order difference: ${(p.order_gap*100).toFixed(1)} percentage points.</p>`:''}<pre>${esc(JSON.stringify(p,null,2))}</pre></details>`).join('')||'<p class="muted">Waiting for the first comparison.</p>'}</div>`:'<div class="panel empty"><h2>Your first report starts with a conversation.</h2><p>Collect one response for each style, then use Analyze.</p></div>'}<footer>Scores average Jev’s pairwise preferences, with 50% as the neutral reference. They are not confidence intervals or proof of prompting effectiveness. Human effort, learning, solution length, and session order can affect outcomes. Repeat matched batches and vary collection order.</footer>`;
 bindStudyPicker();
 on('report-select',()=>{reportId=$('report-select').value;dashboard();},'change');on('resume',async()=>{await api('reports/'+r.id+'/resume',{});await refresh();dashboard();});
}
setInterval(async()=>{if((page==='dashboard'||(page==='runner'&&!judging))&&state?.reports.some(r=>r.status==='running')){try{await refresh();render();}catch(e){notice(e.message);}}},3000);
refresh().then(render).catch(e=>notice(e.message));
