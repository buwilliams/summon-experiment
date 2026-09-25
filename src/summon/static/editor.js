function editablePicker(hostId,label,items,selected,choose,rename,add){
 const host=$(hostId);if(!host)return;
 const inputId=hostId+'-name',listId=hostId+'-options';let active=0;
 host.innerHTML=`<label for="${inputId}">${label}</label><div class="editable-picker"><div class="editable-field"><input id="${inputId}" role="combobox" aria-expanded="false" aria-controls="${listId}" aria-label="${label}" value="${esc(selected?.name)}"><button class="picker-toggle" aria-label="Choose ${label.toLowerCase()}" aria-expanded="false"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="m4 6 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div><button class="add-record" aria-label="Add ${label.toLowerCase()}">+</button><div id="${listId}" class="picker-options" role="listbox" hidden></div></div>`;
 const input=$(inputId),list=$(listId),toggle=host.querySelector('.picker-toggle');
 const close=()=>{list.hidden=true;input.setAttribute('aria-expanded','false');toggle.setAttribute('aria-expanded','false');input.removeAttribute('aria-activedescendant');};
 const options=()=>{list.innerHTML=items.map((x,i)=>`<div id="${listId}-${i}" role="option" aria-selected="${x.id===selected.id}" class="picker-option ${i===active?'highlighted':''}" data-index="${i}">${esc(x.name)}</div>`).join('');};
 const open=()=>{active=items.findIndex(x=>x.id===selected.id);options();list.hidden=false;input.setAttribute('aria-expanded','true');toggle.setAttribute('aria-expanded','true');input.focus();};
 input.oninput=()=>{if(input.value.trim()){selected.name=input.value.trim();rename();}close();};
 input.onblur=()=>{input.value=selected.name;};
 toggle.onclick=()=>list.hidden?open():close();
 list.onmousedown=e=>e.preventDefault();
 list.onclick=e=>{const option=e.target.closest('[data-index]');if(option)choose(items[Number(option.dataset.index)]);};
 input.onkeydown=e=>{if(e.key==='Escape'||e.key==='Tab')close();else if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();if(list.hidden)open();else active=(active+(e.key==='ArrowDown'?1:-1)+items.length)%items.length;options();input.setAttribute('aria-activedescendant',`${listId}-${active}`);$(listId+'-'+active)?.scrollIntoView({block:'nearest'});}else if(e.key==='Enter'){e.preventDefault();if(!list.hidden&&items[active])choose(items[active]);close();}};
 host.onfocusout=e=>{if(!host.contains(e.relatedTarget))close();};
 host.querySelector('.add-record').onclick=add;
}

let editorSelection={},editorDepth='overview';
function editor(){
 const edits=automaticEdit('catalog',state.catalog,'catalog','PUT',validCatalogDraft),c=edits.data;
 let h=c.hypotheses.find(x=>x.id===editorSelection.hypothesis)||c.hypotheses[0];
 let e=c.experiments.find(x=>x.id===(editorSelection.experiment||selectedExperiment)&&x.hypothesis_id===h.id)||c.experiments.find(x=>x.hypothesis_id===h.id);
 let v=c.views.find(x=>x.id===editorSelection.view&&e?.view_ids.includes(x.id))||c.views.find(x=>e?.view_ids.includes(x.id))||c.views[0];
 let st=v.styles.find(x=>x.id===editorSelection.style)||v.styles[0];
 function changed(){edits.changed();}
 function renamed(){changed();const names={hypothesis:h.name,experiment:e?.name,view:v.name,style:st.name};document.querySelectorAll('[data-level]').forEach(b=>{if(names[b.dataset.level])b.textContent=names[b.dataset.level];});}
 function chooseExperiment(item){e=item;v=c.views.find(x=>e.view_ids.includes(x.id))||c.views[0];st=v.styles[0];editorDepth='experiment';draw();}
 function enter(level,id){editorDepth=level;if(level==='hypothesis'){h=c.hypotheses.find(x=>x.id===id);e=c.experiments.find(x=>x.hypothesis_id===h.id);}if(level==='experiment'){chooseExperiment(c.experiments.find(x=>x.id===id));return;}if(level==='view'){v=c.views.find(x=>x.id===id);st=v.styles[0];}if(level==='style')st=v.styles.find(x=>x.id===id);draw();window.scrollTo({top:0});}
 function add(level){editorDepth=level;
  if(level==='hypothesis'){h={id:crypto.randomUUID(),name:'New hypothesis',statement:''};c.hypotheses.push(h);e=null;}
  if(level==='experiment'){e={id:crypto.randomUUID(),hypothesis_id:h.id,name:'New experiment',text:'',view_ids:c.views.map(x=>x.id)};c.experiments.push(e);}
  if(level==='view'){v={id:crypto.randomUUID(),name:'New test',styles:v.styles.map(x=>({...structuredClone(x),id:crypto.randomUUID()}))};c.views.push(v);e.view_ids.push(v.id);st=v.styles[0];}
  if(level==='style'){st={id:crypto.randomUUID(),name:'New style',opening:'{{EXPERIMENT}}\n\nRespond with only the recommendation and supporting rationale, in two paragraphs or fewer.'};v.styles.push(st);}
  changed();draw();const field=$(level+'-picker-name');field?.focus();field?.select();
 }
 function nextSection(label,level,items,detail){return `<section class="drill-next"><div class="drill-section-heading"><h2>${label}</h2><button class="add-record" data-new="${level}" aria-label="Add ${level==='view'?'test':level}">+</button></div><div class="drill-items">${items.map(x=>`<button class="drill-item" data-enter="${level}" data-id="${x.id}"><span><strong>${esc(x.name)}</strong>${detail?`<small>${esc(detail(x))}</small>`:''}</span><span aria-hidden="true">→</span></button>`).join('')||'<p class="muted">None yet. Use + to add one.</p>'}</div></section>`;}
 function draw(){
  if(!e&&['experiment','view','style'].includes(editorDepth))editorDepth='hypothesis';
  editorSelection={hypothesis:h.id,experiment:e?.id,view:v.id,style:st.id};if(e){selectedExperiment=e.id;localStorage.setItem('summon-experiment',e.id);}
  const order=['overview','hypothesis','experiment','view','style'];
  const path=[['overview','Hypotheses'],['hypothesis',h.name],['experiment',e?.name],['view',v.name],['style',st.name]].slice(0,order.indexOf(editorDepth)+1);
  const descriptions={overview:'Choose a hypothesis to work on.',hypothesis:'Define the claim, then choose an experiment to test it.',experiment:'Edit the experiment, then choose a test for its prompts.',view:'Choose the prompting style for this experiment and test.',style:'Edit the opening for this experiment, test, and style.'};
  let content='';
  if(editorDepth==='overview')content=nextSection('Your hypotheses','hypothesis',c.hypotheses,x=>`${c.experiments.filter(e=>e.hypothesis_id===x.id).length} experiments`);
  if(editorDepth==='hypothesis')content=`<div id="hypothesis-picker"></div><label for="hypothesis-statement">Statement to test</label><textarea id="hypothesis-statement" rows="3">${esc(h.statement)}</textarea>${nextSection('Experiments in this hypothesis','experiment',c.experiments.filter(x=>x.hypothesis_id===h.id),x=>`${x.view_ids.length} ${x.view_ids.length===1?'test':'tests'}`)}`;
  if(editorDepth==='experiment')content=`<div id="experiment-picker"></div><label for="experiment-body">Experiment</label><textarea id="experiment-body" rows="7">${esc(e.text)}</textarea><details class="experiment-scope"><summary>Manage tests and hypothesis</summary><div class="scope-options">${c.views.map(x=>`<label class="check"><input type="checkbox" data-scope-view="${x.id}" ${e.view_ids.includes(x.id)?'checked':''}>${esc(x.name)}</label>`).join('')}</div><label for="experiment-parent">Belongs to hypothesis</label><select id="experiment-parent">${opts(c.hypotheses,h.id)}</select></details>${nextSection('Tests for this experiment','view',c.views.filter(x=>e.view_ids.includes(x.id)),x=>`${x.styles.length} styles`)}`;
  if(editorDepth==='view')content=`<div id="view-picker"></div><p class="muted">Editing prompts for <strong>${esc(e.name)}</strong>. Test and style names are shared across experiments.</p>${nextSection('Styles in this test','style',v.styles)}`;
  if(editorDepth==='style')content=`<div id="style-picker"></div><label for="style-opening">Opening prompt</label><textarea id="style-opening" rows="12">${esc(st.openings?.[e.id]??st.opening)}</textarea><p class="muted">{{EXPERIMENT}} inserts the experiment text.</p><details class="scenario-reference"><summary>Read experiment: ${esc(e.name)}</summary><p>${esc(e.text)}</p></details>`;
  $('app').innerHTML=`<section class="experiment-editor drill-editor"><div class="editor-heading"><div><h1>Hypotheses</h1><p class="intro">${descriptions[editorDepth]}</p></div><span id="editor-save-state" class="muted" role="status" aria-live="polite">${esc(edits.status)}</span></div><nav class="editor-breadcrumbs" aria-label="Editing hierarchy">${path.map(([level,name],i)=>`${i?'<span aria-hidden="true">›</span>':''}<button data-level="${level}" ${level===editorDepth?'aria-current="page"':''}>${esc(name)}</button>`).join('')}</nav><section class="panel drill-content">${content}</section>${editorDepth!=='overview'?'<p class="muted editor-history-note">Type in the dropdown to rename; use its arrow to switch or + to add. Changes apply to new batches.</p>':''}${editorDepth==='overview'?submissionEditor():''}</section>`;
  document.querySelectorAll('[data-enter]').forEach(b=>b.onclick=()=>enter(b.dataset.enter,b.dataset.id));
  document.querySelectorAll('[data-new]').forEach(b=>b.onclick=()=>add(b.dataset.new));
  document.querySelectorAll('[data-level]').forEach(b=>b.onclick=()=>{editorDepth=b.dataset.level;draw();window.scrollTo({top:0});});
  editablePicker('hypothesis-picker','Hypothesis',c.hypotheses,h,x=>enter('hypothesis',x.id),renamed,()=>add('hypothesis'));
  editablePicker('experiment-picker','Experiment',c.experiments.filter(x=>x.hypothesis_id===h.id),e,chooseExperiment,renamed,()=>add('experiment'));
  editablePicker('view-picker','Test',c.views.filter(x=>e?.view_ids.includes(x.id)),v,x=>enter('view',x.id),renamed,()=>add('view'));
  editablePicker('style-picker','Style',v.styles,st,x=>enter('style',x.id),renamed,()=>add('style'));
  on('hypothesis-statement',()=>{h.statement=$('hypothesis-statement').value;changed();},'input');
  on('experiment-body',()=>{e.text=$('experiment-body').value;changed();},'input');
  on('experiment-parent',()=>{e.hypothesis_id=$('experiment-parent').value;h=c.hypotheses.find(x=>x.id===e.hypothesis_id);changed();draw();},'change');
  on('style-opening',()=>{st.openings??={};st.openings[e.id]=$('style-opening').value;changed();},'input');
  document.querySelectorAll('[data-scope-view]').forEach(x=>x.onchange=()=>{e.view_ids=[...document.querySelectorAll('[data-scope-view]:checked')].map(x=>x.dataset.scopeView);changed();draw();document.querySelector('.experiment-scope').open=true;});
  for(const s of state.submissions){const edit=submissionEdit(s);on('notes-'+s.id,()=>{edit.data.notes=$('notes-'+s.id).value;edit.changed();},'input');on('include-'+s.id,()=>{edit.data.included=$('include-'+s.id).checked;edit.changed();},'change');}
  document.querySelectorAll('[data-transcript]').forEach(b=>b.onclick=async()=>{await flushEditorSaves();current=b.dataset.transcript;selectedExperiment=state.sessions.find(s=>s.id===current)?.experiment?.id||selectedExperiment;collectDepth='conversation';page='chat';render();});
 }
 draw();
}
function submissionEditor(){return `<details class="panel editor-submissions"><summary>Submissions <span class="badge">${state.submissions.length}</span></summary>${state.submissions.map(s=>{const edit=submissionEdit(s);return `<div class="list-item"><strong>${esc(s.scenario.name)} · ${esc(s.view.name)} · ${esc(s.style.name)}</strong><p class="muted">${esc(s.batch)} / ${esc(s.participant)}</p><details><summary>Read submitted solution</summary><pre>${esc(s.text)}</pre></details><label for="notes-${s.id}">Research notes</label><textarea id="notes-${s.id}">${esc(edit.data.notes)}</textarea><label class="check"><input type="checkbox" id="include-${s.id}" ${edit.data.included?'checked':''}>Include in future reports</label><span id="save-status-submission-${s.id}" class="muted" role="status">${esc(edit.status)}</span><button data-transcript="${s.session}">Open transcript ↗</button></div>`;}).join('')||'<p class="muted">No submitted responses yet.</p>'}</details>`;}
