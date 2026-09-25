let activeUser=sessionStorage.getItem('summon-user')||'',choosingUser=false;
const normalizeName=name=>String(name||'').trim().replace(/\s+/g,' ');
const sameUser=(a,b)=>normalizeName(a).toLowerCase()===normalizeName(b).toLowerCase();
function updateIdentity(){
 const button=$('switch-user');button.hidden=!activeUser;button.textContent=activeUser+' · Switch user';
 button.onclick=async()=>{if(sending||judgmentSaving||dataWorking){notice('Wait for the current action to finish before switching users.');return;}await flushEditorSaves();choosingUser=true;dataLoading++;notice('');identityScreen();};
}
function identityScreen(){
 updateIdentity();conversationDockObserver?.disconnect();
 const names=new Map();
 for(const name of [...state.batches.map(b=>b.participant),...state.reports.flatMap(r=>(r.human?.records||[]).map(b=>b.reviewer))]){
  const cleaned=normalizeName(name);if(cleaned&&cleaned!=='Local participant')names.set(cleaned.toLowerCase(),cleaned);
 }
 $('app').innerHTML=`<section class="focused-flow identity-screen">${title(choosingUser?'Switch user':'Welcome to Summon','What name should we save your work under?')}<form id="user-form" class="panel"><label for="user-name">Your name</label><input id="user-name" name="name" autocomplete="name" maxlength="100" required value=""><div class="actions"><button class="primary" type="submit">Continue →</button>${activeUser?'<button id="cancel-user" type="button">Cancel</button>':''}</div><p class="muted">No password. Names identify contributions in this shared workspace.</p></form>${names.size?`<div class="drill-items">${[...names.values()].sort().map(name=>`<button class="drill-item" data-user="${esc(name)}"><span>${esc(name)}</span><span aria-hidden="true">→</span></button>`).join('')}</div>`:''}</section>`;
 function select(name){
  const normalized=normalizeName(name);if(!normalized||normalized.length>100){notice('Enter a name between 1 and 100 characters.');return;}
  activeUser=names.get(normalized.toLowerCase())||normalized;sessionStorage.setItem('summon-user',activeUser);reviewer=activeUser;choosingUser=false;
  current=null;selectedBatch=null;collectDepth='overview';collectHypothesis=null;judging=null;activeBallot=null;
  reportFlows.runner={depth:'overview'};reportFlows.dashboard={depth:'overview'};
  cleanupPreview=null;dataDepth='overview';dataLoading++;page='chat';notice('');render();
 }
 $('user-form').onsubmit=e=>{e.preventDefault();select($('user-name').value);};
 document.querySelectorAll('[data-user]').forEach(b=>b.onclick=()=>select(b.dataset.user));
 on('cancel-user',()=>{choosingUser=false;render();});$('user-name').focus();
}
