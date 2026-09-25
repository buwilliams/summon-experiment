let selectedExperiment=localStorage.getItem('summon-experiment');
let reviewer=localStorage.getItem('summon-reviewer')||'Local participant';
let judging=null, activeBallot=null;

function studyPicker(){
 const experiments=state.catalog.experiments;
 const e=experiments.find(e=>e.id===selectedExperiment)||experiments[0];
 selectedExperiment=e.id;
 const h=state.catalog.hypotheses.find(h=>h.id===e.hypothesis_id);
 return `<div class="panel study-picker"><div class="row"><div><label for="scope-hypothesis">Hypothesis</label><select id="scope-hypothesis">${opts(state.catalog.hypotheses,h.id)}</select></div><div><label for="scope-experiment">Experiment</label><select id="scope-experiment">${opts(experiments.filter(x=>x.hypothesis_id===h.id),e.id)}</select></div></div><p class="muted">${esc(h.statement)}</p></div>`;
}
function scopeBatches(){return state.batches.filter(b=>b.experiment?.id===selectedExperiment);}
function scopeReports(){return state.reports.filter(r=>(r.experiment||r.submissions[0]?.experiment)?.id===selectedExperiment);}
function bindStudyPicker(){
 const change=id=>{selectedExperiment=id;localStorage.setItem('summon-experiment',id);selectedBatch=null;runnerBatch=null;current=null;reportId=null;judging=null;render();};
 on('scope-experiment',()=>change($('scope-experiment').value),'change');
 on('scope-hypothesis',()=>{const e=state.catalog.experiments.find(e=>e.hypothesis_id===$('scope-hypothesis').value);if(e)change(e.id);else notice('Add an experiment to this hypothesis in Hypotheses.');},'change');
}

function humanControls(runs){
 return `<section class="panel"><h2>Human judgments</h2><p>Choose the response you prefer before seeing Jev’s judgment. Only the selected LLM responses are compared.</p><label for="reviewer">Reviewer name</label><input id="reviewer" value="${esc(reviewer)}"><p class="muted">Use the same name to resume your judgments. Names identify local records; they are not accounts.</p>${runs.filter(r=>r.status==='complete').map(r=>`<div class="list-item"><strong>${esc(r.name)}</strong><p class="muted">${r.human?.judged_pairs||0} of ${r.pairs.length} pairs have human judgments</p><button data-judge="${r.id}">Judge responses →</button></div>`).join('')||'<p class="muted">Complete a batch report to start human judging.</p>'}</section>`;
}
function bindHumanControls(){
 on('reviewer',()=>{reviewer=$('reviewer').value;localStorage.setItem('summon-reviewer',reviewer);judging=null;},'input');
 document.querySelectorAll('[data-judge]').forEach(b=>b.onclick=()=>startJudging(b.dataset.judge).catch(e=>notice(e.message)));
}
async function startJudging(id){
 const result=await api(`reports/${id}/ballots`,{reviewer});
 judging=result;activeBallot=result.ballots.find(b=>b.status==='pending')?.id||result.ballots.at(-1)?.id;
 page='runner';render();
}
function judgingScreen(){
 const b=judging.ballots.find(b=>b.id===activeBallot);
 $('app').innerHTML=title('Compare responses','Choose the recommendation you prefer, including its reasons.')+`<div class="panel"><div class="row"><strong>${esc(judging.reviewer)} · ${judging.completed} of ${judging.total} judgments saved</strong><button id="exit-judging">Back to Analyze</button></div><progress value="${judging.completed}" max="${judging.total}"></progress><p class="muted">${b?.stage==='cross'?'Across-test comparison of Jev’s finalists.':'Two styles within the same test.'} Names, styles, and Jev scores stay hidden until you save your choice.</p></div>${b?`<section class="panel"><h2>${esc(b.scenario.name)}</h2><p class="scenario">${esc(b.scenario.text)}</p></section><div class="comparison-grid">${b.responses.map(x=>`<section class="panel"><h2>Response ${x.label}</h2><div class="markdown">${x.html}</div></section>`).join('')}</div>${b.status==='pending'?`<section class="panel judgment-actions"><label for="judgment-reason">Why do you prefer it? (optional)</label><textarea id="judgment-reason"></textarea><div class="actions"><button data-vote="A" class="primary">Prefer Response A</button><button data-vote="tie">Tie / equally good</button><button data-vote="B" class="primary">Prefer Response B</button></div></section>`:`<section class="panel"><h2>Your preference: ${b.choice==='tie'?'Tie':'Response '+b.choice}</h2>${b.reason?`<p>${esc(b.reason)}</p>`:''}<h3>Jev’s judgment</h3><p>A: ${(b.jev.A*100).toFixed(1)}% · B: ${(b.jev.B*100).toFixed(1)}%</p><p class="muted">A: ${esc(b.identities.A)}<br>B: ${esc(b.identities.B)}</p><button id="next-judgment" class="primary">${judging.completed===judging.total?'View results':'Next comparison →'}</button></section>`}`:'<div class="panel">No response pairs in this report.</div>'}`;
 on('exit-judging',()=>{judging=null;render();});
 document.querySelectorAll('[data-vote]').forEach(button=>button.onclick=async()=>{const buttons=document.querySelectorAll('[data-vote]');buttons.forEach(x=>x.disabled=true);try{const saved=await api(`ballots/${b.id}/vote`,{reviewer:judging.reviewer,choice:button.dataset.vote,reason:$('judgment-reason').value});judging.ballots[judging.ballots.findIndex(x=>x.id===b.id)]=saved;judging.completed++;await refresh();judgingScreen();}catch(e){notice(e.message);buttons.forEach(x=>x.disabled=false);}});
 on('next-judgment',()=>{const next=judging.ballots.find(x=>x.status==='pending');if(next){activeBallot=next.id;judgingScreen();window.scrollTo({top:0});}else{reportId=judging.report_id;judging=null;page='dashboard';render();}});
}

function humanResults(report,label){
 const h=report.human;
 if(!h?.votes)return '<section class="panel"><h2>Human judgments</h2><p>No human preferences saved yet. Use Analyze to compare anonymous responses.</p></section>';
 return `<section class="panel"><h2>Human judgments</h2><p>${h.votes} judgments from ${h.reviewers} reviewer(s) · ${h.judged_pairs} of ${h.total_pairs} pairs covered</p><p>${h.agreement} of ${h.votes} choices agree with Jev, counting a tie only when both judges tie.</p><p class="muted">Each human choice scores 1 for the preferred response and 0 for the other; a tie scores ½ each. These votes remain separate from Jev’s probabilities. Cross-test pairs use Jev’s finalists.</p><div class="table-scroll"><table><thead><tr><th>Comparison</th><th>Human preference for first response</th><th>Jev preference for first response</th><th>Votes</th></tr></thead><tbody>${h.pairs.map(p=>{const j=report.pairs.find(x=>x.key===p.key);return `<tr><td>${esc(label(p.ids[0]))} ↔ ${esc(label(p.ids[1]))}</td><td>${(p.scores[p.ids[0]]*100).toFixed(1)}%</td><td>${(j.scores[p.ids[0]]*100).toFixed(1)}%</td><td>${p.votes}</td></tr>`;}).join('')}</tbody></table></div><details><summary>Saved human judgments</summary>${h.records.map(b=>`<p><strong>${esc(b.reviewer)}</strong> · ${b.winner_id?esc(label(b.winner_id)):'Tie'} · ${esc(b.judged_at)}<br>${esc(b.reason)}</p>`).join('')}</details></section>`;
}
