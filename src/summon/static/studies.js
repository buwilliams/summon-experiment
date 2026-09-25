let selectedExperiment=localStorage.getItem('summon-experiment');
let reviewer=activeUser||'';
let judging=null, activeBallot=null, judgmentSaving=false;

function scopeBatches(){return state.batches.filter(b=>b.experiment?.id===selectedExperiment&&sameUser(b.participant,activeUser));}
function scopeReports(){return state.reports.filter(r=>(r.experiment||r.submissions[0]?.experiment)?.id===selectedExperiment);}
async function startJudging(id){
 if(sending)return;
 sending=true;let result;
 try{result=await api(`reports/${id}/ballots`,{reviewer:activeUser});}finally{sending=false;}
 openReport('runner',id);judging=result;activeBallot=result.ballots.find(b=>b.status==='pending')?.id||result.ballots.at(-1)?.id;
 page='runner';render();
}
function judgingScreen(){
 const b=judging.ballots.find(b=>b.id===activeBallot);
 $('app').innerHTML=reportBreadcrumbs('runner',[['judging','Compare responses']])+title('Compare responses','Choose the recommendation you prefer, including its reasons.')+`<div class="panel"><div class="row"><strong>${esc(judging.reviewer)} · ${judging.completed} of ${judging.total} judgments saved</strong><button id="exit-judging">Back to report</button></div><progress value="${judging.completed}" max="${judging.total}"></progress><p class="muted">${b?.stage==='cross'?'Across-test comparison of Jev’s finalists.':'Two styles within the same test.'} Names, styles, and Jev scores stay hidden until you save your choice.</p></div>${b?`<details class="panel"><summary>Experiment: ${esc(b.scenario.name)}</summary><p class="scenario">${esc(b.scenario.text)}</p></details><div class="comparison-grid">${b.responses.map(x=>`<section class="panel"><h2>Response ${x.label}</h2><div class="markdown">${x.html}</div></section>`).join('')}</div>${b.status==='pending'?`<section class="panel judgment-actions"><details><summary>Add a reason (optional)</summary><label for="judgment-reason">Your reason</label><textarea id="judgment-reason"></textarea></details><div class="actions"><button data-vote="A" class="primary">Prefer Response A</button><button data-vote="tie">Tie / equally good</button><button data-vote="B" class="primary">Prefer Response B</button></div></section>`:`<section class="panel"><h2>Your preference: ${b.choice==='tie'?'Tie':'Response '+b.choice}</h2>${b.reason?`<p>${esc(b.reason)}</p>`:''}<h3>Jev’s judgment</h3><p>A: ${(b.jev.A*100).toFixed(1)}% · B: ${(b.jev.B*100).toFixed(1)}%</p><p class="muted">A: ${esc(b.identities.A)}<br>B: ${esc(b.identities.B)}</p><button id="next-judgment" class="primary">${judging.completed===judging.total?'View results':'Next comparison →'}</button></section>`}`:'<div class="panel">No response pairs in this report.</div>'}`;
 bindReportBreadcrumbs('runner');
 on('exit-judging',()=>{if(judgmentSaving)return;judging=null;render();});
 document.querySelectorAll('[data-vote]').forEach(button=>button.onclick=async()=>{if(judgmentSaving)return;judgmentSaving=true;sending=true;const buttons=document.querySelectorAll('[data-vote]');buttons.forEach(x=>x.disabled=true);try{const saved=await api(`ballots/${b.id}/vote`,{reviewer:judging.reviewer,choice:button.dataset.vote,reason:$('judgment-reason').value});judging.ballots[judging.ballots.findIndex(x=>x.id===b.id)]=saved;judging.completed++;await refresh();judgingScreen();}catch(e){notice(e.message);buttons.forEach(x=>x.disabled=false);}finally{judgmentSaving=false;sending=false;}});
 on('next-judgment',()=>{const next=judging.ballots.find(x=>x.status==='pending');if(next){activeBallot=next.id;judgingScreen();window.scrollTo({top:0});}else{const id=judging.report_id;judging=null;openReport('dashboard',id);}});
}

function humanResults(report,label){
 const h=report.human;
 if(!h?.votes)return '<section class="panel"><h2>Human judgments</h2><p>No human preferences saved yet. Use Analyze to compare anonymous responses.</p></section>';
 return `<section class="panel"><h2>Human judgments</h2><p>${h.votes} judgments from ${h.reviewers} reviewer(s) · ${h.judged_pairs} of ${h.total_pairs} pairs covered</p><p>${h.agreement} of ${h.votes} choices agree with Jev, counting a tie only when both judges tie.</p><p class="muted">Each human choice scores 1 for the preferred response and 0 for the other; a tie scores ½ each. These votes remain separate from Jev’s probabilities. Cross-test pairs use Jev’s finalists.</p><div class="table-scroll"><table><thead><tr><th>Comparison</th><th>Human preference for first response</th><th>Jev preference for first response</th><th>Votes</th></tr></thead><tbody>${h.pairs.map(p=>{const j=report.pairs.find(x=>x.key===p.key);return `<tr><td>${esc(label(p.ids[0]))} ↔ ${esc(label(p.ids[1]))}</td><td>${(p.scores[p.ids[0]]*100).toFixed(1)}%</td><td>${(j.scores[p.ids[0]]*100).toFixed(1)}%</td><td>${p.votes}</td></tr>`;}).join('')}</tbody></table></div><details><summary>Saved human judgments</summary>${h.records.map(b=>`<p><strong>${esc(b.reviewer)}</strong> · ${b.winner_id?esc(label(b.winner_id)):'Tie'} · ${esc(b.judged_at)}<br>${esc(b.reason)}</p>`).join('')}</details></section>`;
}
