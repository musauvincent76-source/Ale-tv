# Mfumo FINAL - hutumia key mpya kabisa, hazijifichi tena!
open('admin.html','w',encoding='utf-8').write("""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin FINAL</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:sans-serif;padding:10px}.card{background:#0a1a0a;border:1px solid #1a3a1a;border-radius:18px;padding:14px;margin-bottom:12px}input{background:#111;border:1px solid #2a2a2a;border-radius:24px;padding:14px;color:#fff;width:100%;margin-bottom:8px}.btn{background:#c8ff00;color:#000;border:0;padding:15px;border-radius:24px;font-weight:900;width:100%}.item{background:#111;border:1px solid #222;border-radius:12px;padding:10px;margin-top:8px;display:flex;justify-content:space-between}</style></head><body>
<div class="card"><b style="color:#00ff88">ALE TV - FINAL FIX</b><div style="font-size:10px;opacity:.5">Key mpya: aletv_FINAL - hakuna kujificha!</div></div>
<div class="card"><input id="t" placeholder="Jina la video"><input id="u" placeholder="YouTube link"><button class="btn" onclick="add()">+ Weka (FINAL)</button></div>
<div id="list" class="card"></div>
<div class="card" style="text-align:center"><a href="index.html" target="_blank" style="color:#00ff88;font-weight:900;text-decoration:none">📺 ONA TV</a> | <a href="clear_storage.html" style="color:#ff4444;font-size:11px">Futa zote za zamani</a></div>
<script>
let KEY='aletv_FINAL_V3';
let state={playlist:[]};
function getYtId(url){if(!url)return'';if(url.includes('youtu.be/'))return url.split('youtu.be/')[1].split('?')[0];try{let u=new URL(url);return u.searchParams.get('v')||'';}catch{let m=url.match(/v=([^&]+)/);return m?m[1]:'';}}
function load(){try{let s=localStorage.getItem(KEY);if(s)state=JSON.parse(s);}catch{}render();}
function save(){localStorage.setItem(KEY,JSON.stringify(state));localStorage.setItem('aletv_live_now',JSON.stringify(state.playlist.find(p=>p.status==='now')||state.playlist[0]||''));}
function add(){let title=document.getElementById('t').value||'Video';let url=document.getElementById('u').value;if(!url)return alert('Weka link');let id=getYtId(url);if(!id)return alert('Si YouTube!');state.playlist.forEach(p=>p.status='next');let v={id:Date.now(),title,url,ytid:id,status:'now'};state.playlist.push(v);save();render();document.getElementById('t').value='';document.getElementById('u').value='';}
function play(id){state.playlist.forEach(p=>p.status=p.id===id?'now':'next');save();render();}
function del(id){state.playlist=state.playlist.filter(p=>p.id!==id);if(state.playlist.length)state.playlist[0].status='now';save();render();}
function render(){let c=document.getElementById('list');if(!state.playlist.length){c.innerHTML='Hakuna video';return;}c.innerHTML=state.playlist.map(v=>`<div class="item"><div><b>${v.title}</b><div style="font-size:10px;opacity:.5">${v.ytid} - ${v.status}</div></div><div><button onclick="play(${v.id})" style="background:#00ff88;border:0;padding:5px 10px;border-radius:8px">Live</button><button onclick="del(${v.id})" style="background:#f33;border:0;padding:5px 10px;border-radius:8px;margin-left:4px">X</button></div></div>`).join('');}
load();
</script></body></html>""")
open('index.html','w',encoding='utf-8').write("""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ALE TV FINAL</title><style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:sans-serif}header{padding:12px;background:#0a1a0a;display:flex;justify-content:space-between}#wrap{width:100%;aspect-ratio:16/9;background:#000;position:relative}iframe{width:100%;height:100%;border:0;position:absolute;top:0;left:0}</style></head><body>
<header><b>ALE TV KE LIVE</b><span style="color:#0f8;font-size:10px">FINAL - NO HIDDEN</span></header>
<div id="wrap"><div id="msg" style="padding:40px;text-align:center;color:#888">Hakuna video - weka Admin</div><iframe id="yt" style="display:none" allowfullscreen allow="autoplay"></iframe></div>
<div style="padding:15px"><h3 id="tt">Karibu</h3><div id="st" style="font-size:11px;opacity:.6">Final System</div></div>
<script>
function getYtId(u){if(!u)return'';if(u.includes('youtu.be/'))return u.split('youtu.be/')[1].split('?')[0];try{return new URL(u).searchParams.get('v')||'';}catch{let m=u.match(/v=([^&]+)/);return m?m[1]:'';}}
function loadTV(){let KEY='aletv_FINAL_V3';let cur=null;try{cur=JSON.parse(localStorage.getItem('aletv_live_now')||'null');}catch{}let st=null;try{st=JSON.parse(localStorage.getItem(KEY)||'null');}catch{}if((!cur||!cur.ytid)&&st&&st.playlist)cur=st.playlist.find(p=>p.status==='now')||st.playlist[0];let msg=document.getElementById('msg'),yt=document.getElementById('yt');if(!cur||!cur.url){msg.style.display='block';yt.style.display='none';return;}let id=cur.ytid||getYtId(cur.url);document.getElementById('tt').innerText=cur.title;document.getElementById('st').innerText='NOW PLAYING: '+cur.title;msg.style.display='none';yt.style.display='block';yt.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&playsinline=1&rel=0&vq=tiny';}
loadTV();setInterval(loadTV,3000);
</script></body></html>""")
print("✅ FINAL FIX tayari! Key mpya - hakuna video iliyojificha tena!")
