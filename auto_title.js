// ALE TV - Auto Jina Citizen Style
async function getYTInfo(url){
  try{
    let id=url.match(/(?:v=|youtu\.be\/|shorts\/)([^&\?\/\s]+)/)?.[1];
    if(!id) return null;
    // Jaribu noembed + YouTube oembed
    let r=await fetch('https://noembed.com/embed?url=https://www.youtube.com/watch?v='+id);
    let j=await r.json();
    return j.title||null;
  }catch{return null;}
}
function findTitleInput(){
  return document.querySelector('#title, #songTitle, #videoTitle, input[placeholder*=jina i], input[placeholder*=Jina], input[placeholder*=title i], input[placeholder*=Title], input[placeholder*=wimbo]');
}
function findUrlInput(){
  return document.querySelector('input[placeholder*=youtube i], input[placeholder*=YouTube], input[placeholder*=link i], input[placeholder*=Link], #youtubeUrl, #ytUrl, #url');
}
function setup(){
  let urlIn=findUrlInput();
  let titleIn=findTitleInput();
  if(!urlIn ||!titleIn || urlIn.dataset.done) return;
  urlIn.dataset.done=1;
  console.log('ALE Auto-Title active');
  const doFetch=async()=>{
    if(!urlIn.value) return;
    titleIn.placeholder='Inatafuta jina...';
    let t=await getYTInfo(urlIn.value);
    if(t){
      titleIn.value=t;
      titleIn.dispatchEvent(new Event('input',{bubbles:true}));
      titleIn.dispatchEvent(new Event('change',{bubbles:true}));
      // Hifadhi haraka kwenye playlist
      titleIn.style.border='2px solid #00ff00';
      setTimeout(()=>titleIn.style.border='',1000);
    }else{
      titleIn.placeholder='Jina la wimbo';
    }
  };
  urlIn.addEventListener('paste',()=>setTimeout(doFetch,700));
  urlIn.addEventListener('change',doFetch);
  urlIn.addEventListener('blur',doFetch);
}
setInterval(setup,1000);
setup();
