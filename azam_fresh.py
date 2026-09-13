# AZAM TV DASHBOARD - Fresh Start 100%
admin_html = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Azam TV Style - ALE TV Admin</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#050a14;color:#fff;font-family:'Segoe UI',sans-serif;display:flex;min-height:100vh}
.sidebar{width:230px;background:linear-gradient(180deg,#001a4d,#000c24);padding:18px;border-right:2px solid #ff6600;position:fixed;height:100vh;overflow-y:auto}
.sidebar h2{color:#ff6600;font-size:20px;font-weight:900;letter-spacing:1px}
.sidebar h2 span{color:#fff;display:block;font-size:10px;letter-spacing:3px;opacity:.7}
.menu{margin-top:30px}
.menu-item{padding:12px 14px;border-radius:10px;margin-bottom:6px;cursor:pointer;font-size:13px;display:flex;gap:10px;align-items:center;opacity:.7}
.menu-item.active{background:#ff6600;color:#fff;opacity:1;font-weight:800}
.main{margin-left:230px;flex:1;padding:20px;background:#070d1c}
.topbar{display:flex;justify-content:space-between;align-items:center;background:#0a1430;padding:14px 18px;border-radius:14px;border-left:4px solid #ff6600;margin-bottom:20px}
.card{background:linear-gradient(145deg,#0e1d40,#0a1430);border:1px solid #1a2d60;border-radius:16px;padding:18px;margin-bottom:16px}
.stat-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.stat{background:#101f45;border-radius:14px;padding:14px;text-align:center;border-top:2px solid #ff6600}
.stat b{font-size:22px;color:#ff6600;display:block}
.stat span{font-size:10px;opacity:.6}
input,select{background:#0a1430;border:1px solid #234080;border-radius:30px;padding:14px 16px;color:#fff;width:100%;outline:none;margin-bottom:10px}
.btn-azam{background:linear-gradient(90deg,#ff6600,#ff8800);color:#fff;border:0;padding:14px;border-radius:30px;font-weight:900;width:100%;cursor:pointer;box-shadow:0 4px 15px rgba(255,102,0,.3)}
.btn-live{background:#00ff88;color:#000;border:0;padding:7px 14px;border-radius:20px;font-weight:800;font-size:11px;cursor:pointer}
.btn-del{background:#ff2244;color:#fff;border:0;padding:7px 12px;border-radius:20px;font-size:11px;cursor:pointer}
.playlist-item{display:flex;justify-content:space-between;align-items:center;background:#0d1a38;padding:12px;border-radius:12px;margin-bottom:8px;border-left:3px solid transparent}
.playlist-item.now{border-left-color:#00ff88;background:#0e2a1a}
.live-badge{background:#ff0033;color:#fff;padding:3px 8px;border-radius:6px;font-size:8px;font-weight:900;animation:blink 1s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.5}}
@media(max-width:700px){.sidebar{width:100%;height:auto;position:relative}.main{margin-left:0}.stat-grid{grid-template-columns:1fr 1fr}}
</style></head>
<body>
<div class="sidebar">
<h2>AZAM<span>ALE TV KE LIVE</span></h2>
<div class="menu">
<div class="menu-item active">📺 Dashboard</div>
<div class="menu-item">🎬 Playlist Manager</div>
<div class="menu-item">🔴 Studio Live</div>
<div class="menu-item">💰 TILL 3624692</div>
</div>
<div style="margin-top:40px;padding:12px;background:#000a1e;border-radius:12px">
<div style="font-size:10px;opacity:.5">SYSTEM STATUS</div>
<div style="color:#00ff88;font-size:12px;margin-top:4px">● ONLINE - Azam Style</div>
<div style="font-size:9px;opacity:.4;margin-top:6px">Fresh install - No hidden videos</div>
</div>
</div>

<div class="main">
<div class="topbar">
<div><b style="font-size:18px">Admin Dashboard</b><div style="font-size:11px;opacity:.6">Azam TV Experience • ALE TV KE LIVE</div></div>
<a href="index.html" target="_blank" style="background:#ff6600;color:#fff;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;font-size:12px">📺 ONA TV</a>
</div>

<div class="stat-grid">
<div class="stat"><b id="totalV">0</b><span>JUMLA VIDEO</span></div>
<div class="stat"><b style="color:#00ff88" id="nowV">0</b><span>LIVE NOW</span></div>
<div class="stat"><b style="color:#fff" id="dataV">TINY</b><span>QUALITY</span></div>
</div>

<div class="card">
<div style="color:#ff6600;font-weight:900;font-size:12px;margin-bottom:12px">➕ WEKA VIDEO MPYA - YouTube</div>
<input id="vTitle" placeholder="Jina la video (mf: Habari za jioni)">
<input id="vUrl" placeholder="Weka YouTube link hapa https://youtube.com/watch?v=...">
<select id="vCat"><option>Habari</option><option>Michezo</option><option>Burudani</option><option>Dini</option><option>Live</option></select>
<button class="btn-azam" onclick="addVideo()">+ WEKA KWENYE PLAYLIST</button>
<div style="font-size:10px;opacity:.4;margin-top:8px;text-align:center">Inashika youtube.com na youtu.be - hakuna blob, hakuna kujificha!</div>
</div>

<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<div style="color:#fff;font-weight:900">🎬 Playlist Yangu</div>
<button onclick="clearAll()" style="background:transparent;color:#ff4444;border:1px solid #ff4444;padding:5px 10px;border-radius:15px;font-size:10px">Futa Zote</button>
</div>
<div id="plist"></div>
</div>

</div>

<script>
const KEY='azamtv_ale_final_2026';
let state={playlist:[]};
function getYtId(url){
 if(!url) return '';
 url=url.trim();
 if(url.includes('youtu.be/')) return url.split('youtu.be/')[1].split('?')[0].split('&')[0];
 try{ let u=new URL(url); if(u.searchParams.get('v')) return u.searchParams.get('v'); if(url.includes('/shorts/')) return url.split('/shorts/')[1].split('?')[0]; }catch(e){ let m=url.match(/v=([^&]+)/); if(m) return m[1]; }
 return '';
}
function load(){
 try{
  let s=localStorage.getItem(KEY);
  if(s) state=JSON.parse(s);
  // migrate old if any but fresh start preferred
 }catch(e){}
 render();
}
function save(){
 localStorage.setItem(KEY, JSON.stringify(state));
 // sync for TV
 let now = state.playlist.find(p=>p.status==='now') || state.playlist[0] || null;
 if(now) localStorage.setItem('aletv_live_now', JSON.stringify(now));
 else localStorage.removeItem('aletv_live_now');
 localStorage.setItem('aletv_state_v2', JSON.stringify(state));
}
function addVideo(){
 let t=document.getElementById('vTitle').value.trim();
 let u=document.getElementById('vUrl').value.trim();
 let cat=document.getElementById('vCat').value;
 if(!u){ alert('Weka YouTube link mkuu!'); return; }
 let id=getYtId(u);
 if(!id){ alert('Link si ya YouTube! Tumia https://www.youtube.com/watch?v=...'); return; }
 if(!t) t = cat + ' - ' + id;
 state.playlist.forEach(p=>p.status='next');
 let v={id:Date.now(),title:t,url:u,ytid:id,cat:cat,status:'now',added:new Date().toLocaleTimeString()};
 state.playlist.push(v);
 save(); render();
 document.getElementById('vTitle').value=''; document.getElementById('vUrl').value='';
}
function playNow(id){ state.playlist.forEach(p=>p.status = p.id===id? 'now' : 'next'); save(); render(); }
function removeOne(id){ state.playlist=state.playlist.filter(p=>p.id!==id); if(state.playlist.length &&!state.playlist.some(p=>p.status==='now')) state.playlist[0].status='now'; save(); render(); }
function clearAll(){ if(!confirm('Futa video ZOTE?')) return; state={playlist:[]}; localStorage.clear(); localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function render(){
 document.getElementById('totalV').innerText = state.playlist.length;
 document.getElementById('nowV').innerText = state.playlist.filter(p=>p.status==='now').length;
 let c=document.getElementById('plist');
 if(!state.playlist.length){ c.innerHTML='<div style="text-align:center;padding:20px;opacity:.4">Hakuna video - weka YouTube link juu</div>'; return; }
 c.innerHTML = state.playlist.map(v=>`
  <div class="playlist-item ${v.status==='now'?'now':''}">
   <div>
    <div style="font-weight:700;font-size:13px">${v.status==='now'?'<span class="live-badge">● LIVE</span> ':''}${v.title}</div>
    <div style="font-size:10px;opacity:.5;margin-top:3px">${v.cat} • ${v.ytid} • ${v.added||''} • ${v.status.toUpperCase()}</div>
   </div>
   <div style="display:flex;gap:6px">
    ${v.status!=='now'?`<button class="btn-live" onclick="playNow(${v.id})">LIVE</button>`:''}
    <button class="btn-del" onclick="removeOne(${v.id})">X</button>
   </div>
  </div>
 `).join('');
}
load();
</script></body></html>
"""

index_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ALE TV KE LIVE - Azam Style</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#050a14;color:#fff;font-family:'Segoe UI',sans-serif}
header{background:linear-gradient(90deg,#001a4d,#002a7a);padding:12px 16px;display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #ff6600;position:sticky;top:0;z-index:99}
header b{letter-spacing:1px}
header b span{color:#ff6600}
.badge{background:#ff0033;color:#fff;padding:4px 10px;border-radius:20px;font-size:10px;font-weight:900;animation:blink 1s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.6}}
#playerWrap{width:100%;aspect-ratio:16/9;background:#000;position:relative;overflow:hidden}
#playerWrap iframe{width:100%;height:100%;border:0;position:absolute;top:0;left:0}
#msg{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;color:#888}
.info{padding:16px;background:linear-gradient(180deg,#0a1430,#050a14)}
.title{font-size:18px;font-weight:900}
.meta{font-size:11px;opacity:.6;margin-top:4px}
.btn-join{background:linear-gradient(90deg,#ff6600,#ff8800);color:#fff;border:0;padding:14px;width:100%;border-radius:30px;font-weight:900;margin-top:14px}
</style></head><body>
<header><b>AZAM <span>ALE TV</span></b><span class="badge">● LIVE</span></header>
<div id="playerWrap"><div id="msg">📺 Hakuna matangazo<br><span style="font-size:11px">Subiri Admin awek e video</span></div><iframe id="yt" style="display:none" allowfullscreen allow="autoplay; encrypted-media; picture-in-picture"></iframe></div>
<div class="info"><div class="title" id="vTitle">Karibu ALE TV KE LIVE</div><div class="meta" id="vMeta">Azam TV Experience • Fresh System - Hakuna kujificha</div><button class="btn-join" onclick="location.reload()">🔄 Refresh TV</button></div>
<script>
const KEY='azamtv_ale_final_2026';
function getYtId(u){if(!u)return'';if(u.includes('youtu.be/'))return u.split('youtu.be/')[1].split('?')[0];try{return new URL(u).searchParams.get('v')||'';}catch{let m=u.match(/v=([^&]+)/);return m?m[1]:'';}}
function loadTV(){
 let cur=null; try{cur=JSON.parse(localStorage.getItem('aletv_live_now')||'null');}catch{}
 let st=null; try{st=JSON.parse(localStorage.getItem(KEY)||'null');}catch{}
 if(!cur && st && st.playlist) cur=st.playlist.find(p=>p.status==='now')||st.playlist[0];
 let msg=document.getElementById('msg'), yt=document.getElementById('yt');
 if(!cur ||!cur.url){ msg.style.display='block'; yt.style.display='none'; return; }
 let id=cur.ytid||getYtId(cur.url);
 document.getElementById('vTitle').innerText=cur.title;
 document.getElementById('vMeta').innerText='● LIVE NOW: '+cur.title+' • '+(cur.cat||'Live')+' • Quality: Data Saver (haikatiki)';
 msg.style.display='none'; yt.style.display='block';
 // Azam stable player - tiny quality + nocookie
 yt.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&playsinline=1&rel=0&modestbranding=1&vq=tiny&enablejsapi=1';
}
loadTV(); setInterval(loadTV,4000);
</script></body></html>
"""

open('admin.html','w',encoding='utf-8').write(admin_html)
open('index.html','w',encoding='utf-8').write(index_html)
open('clear_storage.html','w',encoding='utf-8').write('<script>localStorage.clear();alert("✅ FRESH START! Sasa fungua admin.html");location.href="admin.html";</script>')
print("✅ AZAM TV DASHBOARD MPYA IMEJENGWA!")
print("✅ Hakuna video ya zamani - kila kitu fresh!")
