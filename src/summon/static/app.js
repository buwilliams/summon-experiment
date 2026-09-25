let conversationDockObserver;
let state, page='chat', current=null, sending=false, selectedBatch=localStorage.getItem('summon-batch');
const $=id=>document.getElementById(id);
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const opts=(items,value)=>items.map(x=>`<option value="${esc(x.id)}" ${x.id===value?'selected':''}>${esc(x.name)}</option>`).join('');
const title=(name,desc)=>`<h1>${name}</h1><p class="intro">${desc}</p>`;
const notice=text=>{$('notice').textContent=text;$('notice').hidden=!text;};
async function api(path,body,method='POST'){if(method!=='GET'&&path.startsWith('sessions/')){const record=state?.sessions.find(s=>s.id===path.split('/')[1]);if(record&&activeUser&&!sameUser(record.participant,activeUser))throw Error('Switch to '+record.participant+' to change this session.');}const r=await fetch('/api/'+path,{method,headers:{'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});const data=await r.json();if(!r.ok)throw Error(typeof data.detail==='string'?data.detail:JSON.stringify(data.detail));return data;}
async function refresh(){state=await api('state',undefined,'GET');
 const sessionIds=new Set(state.sessions.map(s=>s.id));
 Object.keys(localStorage).filter(k=>k.startsWith('summon-draft-')&&!sessionIds.has(k.slice('summon-draft-'.length))).forEach(k=>localStorage.removeItem(k));
 if(current&&!sessionIds.has(current))current=null;
 if(selectedBatch&&!state.batches.some(b=>b.id===selectedBatch)){selectedBatch=null;localStorage.removeItem('summon-batch');}
$('connection').textContent=state.connected?'● GPT-6 Astra · connected key':'API key required';}
function on(id,fn,event='click'){if($(id))$(id).addEventListener(event,async e=>{try{await fn(e);}catch(err){notice(err.message);}});}
function render(){if(!activeUser||choosingUser){identityScreen();return;}updateIdentity();document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('active',b.dataset.page===page));({chat,editor,runner,dashboard,dataManager})[page]();}
document.querySelectorAll('nav button').forEach(b=>b.onclick=async()=>{if(sending)return notice('Wait for the current response before switching screens.');await flushEditorSaves();page=b.dataset.page;notice('');render();});
async function beginInterview(){
 if(sending)return;
 sending=true;notice('Astra is preparing the first recommendation from the experiment, test, and style…');
 document.querySelectorAll('#next-interview,#new-batch,#batch-picker,[data-batch-session]').forEach(b=>b.disabled=true);
 try{if(!selectedBatch){const b=await api('batches?experiment_id='+encodeURIComponent(selectedExperiment)+'&participant='+encodeURIComponent(activeUser),{});selectedBatch=b.id;}const session=await api('interview/next'+(selectedBatch?'?batch_id='+encodeURIComponent(selectedBatch):''),{});current=session.complete?null:session.id;notice('');}
 finally{sending=false;await refresh();if(current){selectedBatch=state.batches.find(b=>b.session_ids.includes(current))?.id;localStorage.setItem('summon-batch',selectedBatch);}chat();}
}
function chat(){
 if(!activeUser||choosingUser){identityScreen();return;}
 if(collectDepth!=='conversation'){collectionScreen();return;}
 const batches=scopeBatches();
 const explicit=state.sessions.find(x=>x.id===current&&x.experiment?.id===selectedExperiment&&sameUser(x.participant,activeUser));
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
setInterval(async()=>{if(activeUser&&!choosingUser&&(page==='dashboard'||(page==='runner'&&!judging))&&!document.activeElement?.matches('input,textarea')&&state?.reports.some(r=>r.status==='running')){try{await refresh();render();}catch(e){notice(e.message);}}},3000);
refresh().then(render).catch(e=>notice(e.message));
