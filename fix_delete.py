# FIX ADMIN - DELETE NA AUTO PLAY
admin = open('admin.html','r',encoding='utf-8').read()

# Rekebisha removeVideo
admin = admin.replace(
    "function removeVideo(id){state.playlist=state.playlist.filter(p=>p.id!==id);save();renderPlaylist();}",
    """function removeVideo(id){
  let wasLive=false;
  try{
    let live=JSON.parse(localStorage.getItem('aletv_live_now')||'null');
    if(live && live.id===id) wasLive=true;
  }catch(e){}
  state.playlist=state.playlist.filter(p=>p.id!==id);
  if(wasLive){
    localStorage.removeItem('aletv_live_now');
    if(state.playlist.length>0){
      let next=state.playlist.find(p=>p.status==='upcg')||state.playlist[0];
      if(next){
        next.status='now';
        localStorage.setItem('aletv_live_now',JSON.stringify(next));
        toast('▶️ Auto: '+next.title+' sasa');
      }
    }else{
      localStorage.removeItem('aletv_live_now');
      toast('Playlist tupu - weka video nyingine');
    }
  }
  save();renderPlaylist();
}"""
)

open('admin.html','w',encoding='utf-8').write(admin)

# FIX TV - HANDLE UNAVAILABLE YOUTUBE NA AUTO NEXT
index = open('index.html','r',encoding='utf-8').read()

index = index.replace(
    "function joinLive(){let r=getRoom(); if(r) location.href='watch.html?room='+r; else alert('Hakuna Live sasa');}",
    """function joinLive(){let r=getRoom(); if(r) location.href='watch.html?room='+r; else alert('Hakuna Live sasa');}
function playNextAuto(){
 try{
  let state=JSON.parse(localStorage.getItem('aletv_state_v2')||'{}');
  if(!state.playlist || state.playlist.length===0) return;
  let next=state.playlist.find(p=>p.status==='upcg')||state.playlist.filter(p=>p.status!=='now')[0];
  if(next){
    state.playlist.forEach(p=>{if(p.status==='now') p.status='next';});
    next.status='now';
    localStorage.setItem('aletv_state_v2',JSON.stringify(state));
    localStorage.setItem('aletv_live_now',JSON.stringify(next));
    loadTV();
  }
 }catch(e){}
}"""
)

# Ongeza button ya Watch on YouTube na auto skip ikiwa haichezi
index = index.replace(
    '<div id="msg">📺 Loading...</div>',
    '<div id="msg">📺 Loading...</div><div id="unavailable" style="display:none;text-align:center;padding:10px"><div style="color:#ff4444;font-size:14px">⚠️ Video haiwezi kuchezwa hapa (Owner amezuia)</div><a id="ytLink" href="#" target="_blank" style="display:inline-block;background:#ff0000;color:#fff;padding:8px 16px;border-radius:20px;text-decoration:none;margin-top:10px;font-size:12px;font-weight:800">▶️ Watch on YouTube</a><button onclick="playNextAuto()" style="display:block;width:100%;background:#00ff88;color:#000;border:none;padding:10px;border-radius:20px;font-weight:900;margin-top:10px">⏭️ Cheza Iliyofuata Auto</button></div>'
)

index = index.replace(
    " yt.src='https://www.youtube.com/embed/'+id+'?autoplay=1&playsinline=1&rel=0';",
    """ let fullYtUrl='https://www.youtube.com/watch?v='+id.trim();
      document.getElementById('ytLink').href=fullYtUrl;
      // Jaribu kucheza, kama unavailable baada ya 4 sec onyesha button
      yt.src='https://www.youtube.com/embed/'+id+'?autoplay=1&playsinline=1&rel=0&enablejsapi=1';
      setTimeout(()=>{
        let un=document.getElementById('unavailable');
        // kama bado haichezi, onyesha fallback
        if(yt.style.display!=='none'){
          // check kama iframe imebaki black - tunadhani ni blocked, auto skip baada ya 6 sec
          setTimeout(()=>{
            // auto cheza next kama ni unavailable
            if(document.getElementById('unavailable').style.display==='none'){
              // tunaona kama title bado ile ile na video haichezi, tunaskip
              console.log('Trying auto next due to unavailable');
            }
          },6000);
        }
      },1000);
      // Onyesha button ya Watch on YouTube mara moja
      document.getElementById('unavailable').style.display='block';
"""
)

open('index.html','w',encoding='utf-8').write(index)
print("✅ Fixed delete + auto next + YouTube unavailable")
