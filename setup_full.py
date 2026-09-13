import os

admin_html = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>ALE TV KE LIVE - ADMIN</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif} body{background:#050a05;color:#fff;padding:10px;padding-bottom:50px}
.header{display:flex;justify-content:space-between;align-items:center;padding:8px 2px;margin-bottom:10px}
.logo{display:flex;gap:8px;align-items:center}.logo-icon{width:36px;height:36px;background:linear-gradient(135deg,#00ff88,#00cc66);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px}
.logo h1{font-family:'Orbitron';font-size:18px;color:#00ff88;line-height:1}.logo h1 span{font-size:8px;color:#888;display:block;letter-spacing:1px}
.card{border:1px solid #1e3d1f;border-radius:14px;padding:14px 16px;margin-bottom:10px;background:linear-gradient(180deg,#0f1a0f,#0a120a)}
.card.green{border-color:#00ff88;box-shadow:0 0 20px rgba(0,255,136,.25)}.card.red{border-color:#ff0033;box-shadow:0 0 20px rgba(255,0,51,.2)}.card.yellow{border-color:#88aa00}
.amount{font-size:32px;font-weight:900;color:#c8ff00;font-family:'Orbitron'}.live-num{font-size:32px;font-weight:900;color:#ff0033;font-family:'Orbitron'}.join-num{font-size:26px;font-weight:900;color:#c8ff00;font-family:'Orbitron'}
.section-title{font-family:'Orbitron';font-size:12px;color:#c8ff00;margin:14px 0 4px}.section-sub{font-size:10px;opacity:.5;margin-bottom:10px}
.join-item{background:#0f1a0f;border:1px solid #1e3d1f;border-radius:12px;padding:10px 12px;margin-bottom:8px}
.join-top{display:flex;gap:10px;align-items:center}.av2{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:12px}
.av2.km{background:#3a5a4a;color:#8f8}.av2.jo{background:#5a5a2a;color:#ff8}
.nm{font-size:13px;font-weight:700}.loc{font-size:10px;opacity:.5}.pending{font-size:9px;background:#3a3a1a;color:#fc0;padding:2px 8px;border-radius:4px;margin-top:3px;display:inline-block;font-weight:700}
.actions{display:flex;gap:8px;margin-top:10px}.btn{flex:1;padding:10px;border-radius:20px;border:none;font-weight:800;font-size:12px;cursor:pointer}
.btn.accept{background:#00ff88;color:#003300}.btn.deny{background:#ff0033;color:#fff}
.pl-item{display:flex;gap:10px;align-items:center;background:#0a150a;border:1px solid #1a2a1a;border-radius:10px;padding:8px;margin-bottom:8px}
.pl-thumb{width:54px;height:36px;background:#1a2a1a;border-radius:6px;display:flex;align-items:center;justify-content:center}
.pl-info{flex:1}.pl-title{font-size:11px;font-weight:700}.pl-meta{font-size:8px;opacity:.5}
.badge-now{font-size:8px;background:#00ff88;color:#000;padding:3px 8px;border-radius:10px;font-weight:900}
.btn-small{font-size:9px;padding:5px 12px;border-radius:12px;border:none;font-weight:800}.btn-small.remove{background:#ff0033;color:#fff}.btn-small.live{background:#00ff88;color:#000}
.inputs input{width:100%;background:#0a150a;border:1px solid #1e3d1f;border-radius:20px;padding:10px 14px;margin-bottom:8px;color:#fff;font-size:12px}
.studio{border:2px solid #00ff88;border-radius:16px;padding:14px;margin-top:16px;background:#0f1f0f;text-align:center;box-shadow:0 0 25px rgba(0,255,136,.2)}
.btn-live{width:100%;background:#ff0033;color:#fff;border:none;padding:14px;border-radius:10px;font-family:'Orbitron';font-size:16px;font-weight:900;margin-top:8px;cursor:pointer}
.live-link-box{background:#000;border:1px dashed #00ff88;border-radius:10px;padding:10px;margin-top:10px;word-break:break-all;font-size:11px;color:#00ff88;display:none}
#toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#00ff88;color:#000;padding:10px 20px;border-radius:20px;font-weight:900;font-size:12px;display:none;z-index:999}
</style>
</head>
<body>
<div class="header"><div class="logo"><div class="logo-icon">📺</div><h1>ALE TV KE LIVE<span>KENYAN TV STATION • ADMIN PANEL</span></h1></div><div style="font-size:10px">● <span style="color:#00ff88">LIVE</span></div></div>
<div class="card green"><div style="font-size:10px;opacity:.7">🏦 TILL 3624692</div><div class="amount">KSh <span id="tillAmount">362,469.20</span></div><div style="font-size:10px;opacity:.6">Today +KSh 12,450 <span style="color:#00ff88">▲ +3.6%</span></div></div>
<div class="card red"><div style="font-size:10px;color:#ff0033">👁 LIVE VIEWERS</div><div class="live-num" id="liveViewers">1,284</div><div style="font-size:10px;opacity:.6">Peak: 1,532 • Studio: <span id="studioCount">0 in studio</span></div></div>
<div class="card yellow"><div style="font-size:10px;color:#c8ff00">👥 JOIN REQUESTS</div><div class="join-num" id="joinCount">5 Pending</div><div style="font-size:10px;opacity:.6">Click Accept to add to studio</div></div>
<div class="section-title">JOIN REQUESTS MANAGEMENT</div><div id="joinList"></div>
<div class="section-title">☰ PLAYLIST</div><div id="playlist"></div>
<div class="inputs"><input id="vTitle" placeholder="Video Title"><input id="vUrl" placeholder="YouTube link au video file URL"><input type="file" id="fileInput" accept="video/*" style="display:none"><button onclick="document.getElementById('fileInput').click()" style="width:100%;background:#1a2a1a;border:1px dashed #00ff88;padding:8px;border-radius:20px;color:#888;font-size:11px;margin-bottom:8px">📁 Chagua Video File Kwenye Simu</button></div>
<div class="studio"><div style="color:#ff0033;font-family:'Orbitron';font-size:12px">STUDIO STATUS</div><div id="studioStatus" style="color:#00ff88;font-size:11px;margin:5px 0">● Ready - No active live</div><div id="liveLinkBox" class="live-link-box"><div style="color:#fff;margin-bottom:5px">🔗 LINK YA LIVE (Tuma kwa watu):</div><div id="liveLink"></div><button onclick="copyLiveLink()" style="background:#00ff88;color:#000;border:none;padding:6px 12px;border-radius:10px;font-weight:800;margin-top:8px;font-size:11px">COPY LINK</button><button onclick="openLive()" style="background:#ff0033;color:#fff;border:none;padding:6px 12px;border-radius:10px;font-weight:800;margin-top:8px;font-size:11px;margin-left:5px">OPEN STUDIO</button></div>
<button class="btn-live" onclick="startLive()">🔴 INGIA LIVE STUDIO</button><div style="font-size:9px;opacity:.5;margin-top:8px">Studio ina-support watu 10 live kwa pamoja, camera + mic</div></div>
<div id="toast"></div>
<script>
let state=JSON.parse(localStorage.getItem('aletv_state_v2')||'null')||{joins:[{id:1,name:'Kevin Muriuki',loc:'Nairobi',time:'2 min ago',init:'KM',cls:'km'},{id:2,name:'John Otieno',loc:'Kisumu',time:'12 min ago',init:'JO',cls:'jo'},{id:3,name:'Aisha Hassan',loc:'Mombasa',time:'18 min ago',init:'AH',cls:'km'},{id:4,name:'Brian Kipchoge',loc:'Nakuru',time:'25 min ago',init:'BK',cls:'jo'},{id:5,name:'Faith Wanjiku',loc:'Thika',time:'30 min ago',init:'FW',cls:'km'}],playlist:[{id:1,title:'Morning Brief - 07:30',meta:'Uploaded 06:30',status:'now',thumb:'📰'},{id:2,title:'Sports News - Leo',meta:'05:12',status:'next',thumb:'⚽'},{id:3,title:'Music Mix - Weekend Vibes',meta:'12:45',status:'next',thumb:'🎵'}],liveRoom:null};
function save(){localStorage.setItem('aletv_state_v2',JSON.stringify(state));}
function toast(m){let t=document.getElementById('toast');t.innerText=m;t.style.display='block';setTimeout(()=>t.style.display='none',3000);}
function renderJoins(){let c=document.getElementById('joinList');c.innerHTML='';state.joins.slice(0,10).forEach(j=>{c.innerHTML+=`<div class=join-item><div class=join-top><div class="av2 ${j.cls}">${j.init}</div><div><div class=nm>${j.name}</div><div class=loc>${j.loc} • ${j.time}</div><div class=pending>Pending</div></div></div><div class=actions><button class="btn accept" onclick="acceptJoin(${j.id})">✔ Accept - Ingiza Studio</button><button class="btn deny" onclick="denyJoin(${j.id})">✕ Deny</button></div></div>`;});document.getElementById('joinCount').innerText=state.joins.length+' Pending';}
function acceptJoin(id){let j=state.joins.find(x=>x.id===id);state.joins=state.joins.filter(x=>x.id!==id);save();renderJoins();toast(j.name+' ameongezwa studio!');if(state.liveRoom){localStorage.setItem('aletv_new_guest',JSON.stringify(j));}}
function denyJoin(id){state.joins=state.joins.filter(x=>x.id!==id);save();renderJoins();toast('Denied');}
function renderPlaylist(){let c=document.getElementById('playlist');c.innerHTML='';state.playlist.forEach(v=>{let right=v.status==='now'?`<span class=badge-now>NOW PLAYING</span><button class="btn-small remove" onclick="removeVideo(${v.id})">Remove</button>`:`<span style="font-size:8px;opacity:.5">UP NEXT</span><button class="btn-small live" onclick="moveToLive(${v.id})">Move to Live</button>`;c.innerHTML+=`<div class=pl-item><div class=pl-thumb>${v.thumb}</div><div class=pl-info><div class=pl-title>${v.title}</div><div class=pl-meta>${v.meta}</div></div><div style="display:flex;flex-direction:column;gap:4px;align-items:flex-end">${right}</div></div>`;});}
function moveToLive(id){state.playlist.forEach(p=>{if(p.status==='now')p.status='next';});let v=state.playlist.find(p=>p.id===id);if(v){v.status='now';save();renderPlaylist();localStorage.setItem('aletv_live_now',JSON.stringify(v));toast('Now Live: '+v.title);}}
function removeVideo(id){state.playlist=state.playlist.filter(p=>p.id!==id);save();renderPlaylist();}
document.getElementById('fileInput').addEventListener('change',e=>{let f=e.target.files[0];if(!f)return;let url=URL.createObjectURL(f);let title=document.getElementById('vTitle').value||f.name;state.playlist.push({id:Date.now(),title:title,meta:'Just now • Local file',status:'next',thumb:'🎬',url:url});save();renderPlaylist();toast('Added: '+title);});
function startLive(){let room='aletvke-'+Math.random().toString(36).substring(2,8);state.liveRoom=room;save();localStorage.setItem('aletv_room',room);showLiveLink();toast('Studio imefunguliwa!');openLive();}
function showLiveLink(){if(!state.liveRoom)return;let box=document.getElementById('liveLinkBox');let linkEl=document.getElementById('liveLink');let base=window.location.origin+window.location.pathname.replace('admin.html','');let liveLink=base+'live.html?room='+state.liveRoom;let watchLink=base+'watch.html?room='+state.liveRoom;linkEl.innerHTML=`<div>Studio (we):<br>${liveLink}</div><div style=margin-top:8px;color:#c8ff00>Viewers link (tuma kwa watu):<br>${watchLink}</div>`;box.style.display='block';document.getElementById('studioStatus').innerText='● LIVE - Room: '+state.liveRoom;document.getElementById('studioCount').innerText=(state.joins.length?'0':'' )+' in studio';}
function copyLiveLink(){let base=window.location.origin+window.location.pathname.replace('admin.html','');let watchLink=base+'watch.html?room='+state.liveRoom;navigator.clipboard.writeText(watchLink);toast('Link ya viewers imecopy!');}
function openLive(){window.open('live.html?room='+state.liveRoom,'_blank');}
if(state.liveRoom)showLiveLink();
renderJoins();renderPlaylist();
</script>
</body>
</html>
"""

index_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ALE TV KE LIVE</title>
<style>body{margin:0;background:#000;color:#fff;font-family:sans-serif} header{background:#0f1a0f;padding:12px;display:flex;justify-content:space-between;border-bottom:1px solid #00ff8855} #player{aspect-ratio:16/9;background:#111;display:flex;align-items:center;justify-content:center;position:relative} video,iframe{width:100%;height:100%;border:none}.live-badge{position:absolute;top:10px;left:10px;background:#ff0033;color:#fff;padding:4px 10px;border-radius:5px;font-weight:900;font-size:12px;animation:blink 1s infinite} @keyframes blink{50%{opacity:.5}}.info{padding:15px}.btn-join{background:#00ff88;color:#000;border:none;padding:12px 20px;border-radius:20px;font-weight:900;width:100%;margin-top:10px}.chat{border-top:1px solid #1a2a1a;padding:10px;max-height:200px;overflow:auto}</style></head>
<body><header><b>ALE TV KE LIVE</b><span style="color:#00ff88">TILL 3624692</span></header>
<div id="player"><div id="msg">📺 Waiting for Admin LIVE - Karibu ALE TV</div><video id="v" controls autoplay style="display:none"></video><iframe id="yt" style="display:none" allowfullscreen></iframe><div id="liveBadge" class="live-badge" style="display:none">● LIVE</div></div>
<div class="info"><h2 id="title">Karibu ALE TV</h2><p id="desc" style="opacity:.6">Lipa 100 kwa TILL 3624692 uone live yote</p><div id="liveAction" style="display:none"><button class="btn-join" onclick="joinLive()">🔴 JOIN LIVE STUDIO - Ona Watu Live</button><div style="font-size:10px;opacity:.5;margin-top:6px;text-align:center">Watu <span id="viewerCnt">1,284</span> wanaangalia sasa</div></div><div style="margin-top:15px"><h4 style="color:#c8ff00">Now Playing</h4><div id="nowPlaying" style="font-size:12px;opacity:.7">Morning Brief - 07:30</div></div></div>
<div class="chat"><div style="font-size:11px;color:#00ff88">💬 LIVE CHAT</div><div id="chatBox" style="font-size:11px;margin-top:6px;opacity:.7">Admin: Karibuni sana ALE TV...</div></div>
<script>
function load(){let cur=null;let room=localStorage.getItem('aletv_room');try{cur=JSON.parse(localStorage.getItem('aletv_live_now'));}catch(e){}if(room){document.getElementById('liveAction').style.display='block';document.getElementById('liveBadge').style.display='block';document.getElementById('msg').innerHTML='🔴 LIVE INAENDELEA - Bonyeza JOIN kuona';}if(cur){document.getElementById('title').innerText=cur.title;document.getElementById('nowPlaying').innerText=cur.title;let v=document.getElementById('v'),yt=document.getElementById('yt');if(cur.url){document.getElementById('msg').style.display='none';if(cur.url.includes('youtu')){let id=cur.url.split('v=')[1]?.split('&')[0]||cur.url.split('/').pop().split('?')[0];yt.src='https://www.youtube.com/embed/'+id+'?autoplay=1';yt.style.display='block';}else{v.src=cur.url;v.style.display='block';v.play().catch(()=>{});}}}}
function joinLive(){let room=localStorage.getItem('aletv_room');if(room)window.location.href='watch.html?room='+room;else alert('Hakuna live sasa');}
load();setInterval(load,2000);
</script></body></html>
"""

live_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LIVE STUDIO - ALE TV</title>
<script src="https://meet.jit.si/external_api.js"></script>
<style>body{margin:0;background:#050a05;color:#fff;font-family:sans-serif;display:flex;flex-direction:column;height:100vh} header{background:#0f1a0f;padding:10px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #00ff8855} #jitsi{flex:1;background:#000}.controls{background:#0f1a0f;padding:10px;display:flex;gap:8px;flex-wrap:wrap}.ctrl{padding:8px 14px;border-radius:20px;border:1px solid #1e3d1f;background:#1a2a1a;color:#fff;font-size:12px}.ctrl.live{background:#ff0033;border-color:#ff0033}.link-bar{background:#000;padding:8px;font-size:11px;color:#00ff88;border-top:1px solid #1e3d1f;word-break:break-all}</style>
</head>
<body><header><div><b style="color:#00ff88;font-family:Orbitron">ALE TV STUDIO</b><div style="font-size:10px;opacity:.6" id="roomName">Room: --</div></div><div><button onclick="copyLink()" style="background:#00ff88;color:#000;border:none;padding:6px 12px;border-radius:10px;font-size:11px;font-weight:800">COPY VIEWER LINK</button> <button onclick="window.close()" style="background:#333;color:#fff;border:none;padding:6px 12px;border-radius:10px;font-size:11px">EXIT</button></div></header>
<div id="jitsi"></div>
<div class="link-bar" id="linkBar">Viewer link: </div>
<div class="controls"><button class="ctrl live" id="liveBtn">● LIVE</button><span style="font-size:11px;opacity:.6">Studio ina-support watu 10, mic + camera, viewers wanaweza join na link</span></div>
<script>
const urlParams=new URLSearchParams(window.location.search); let room=urlParams.get('room')||localStorage.getItem('aletv_room')||'aletvke-'+Math.random().toString(36).substring(2,6);
document.getElementById('roomName').innerText='Room: '+room;
let base=window.location.origin+window.location.pathname.replace('live.html',''); let viewerLink=base+'watch.html?room='+room;
document.getElementById('linkBar').innerText='🔗 Tuma hii kwa viewers: '+viewerLink;
function copyLink(){navigator.clipboard.writeText(viewerLink);alert('Link ya viewers imecopy: '+viewerLink);}
const domain='meet.jit.si'; const options={roomName:room,width:'100%',height:'100%',parentNode:document.querySelector('#jitsi'),configOverwrite:{startWithAudioMuted:false,startWithVideoMuted:false,prejoinPageEnabled:false},interfaceConfigOverwrite:{SHOW_JITSI_WATERMARK:false,SHOW_WATERMARK_FOR_GUESTS:false},userInfo:{displayName:'ALE TV Admin'}};
const api=new JitsiMeetExternalAPI(domain,options);
api.addEventListener('participantJoined',()=>{let c=api.getNumberOfParticipants();document.getElementById('liveBtn').innerText='● LIVE - '+c+' in studio';});
api.addEventListener('participantLeft',()=>{let c=api.getNumberOfParticipants();document.getElementById('liveBtn').innerText='● LIVE - '+c+' in studio';});
</script></body></html>
"""

watch_html = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Watch Live - ALE TV</title>
<script src="https://meet.jit.si/external_api.js"></script>
<style>body{margin:0;background:#000;color:#fff;font-family:sans-serif;display:flex;flex-direction:column;height:100vh} header{background:#0f1a0f;padding:12px;display:flex;justify-content:space-between;border-bottom:1px solid #ff0033} #jitsi{flex:1}.info-bar{background:#0f1a0f;padding:10px;text-align:center;font-size:12px}.btn{background:#ff0033;color:#fff;border:none;padding:10px 20px;border-radius:20px;font-weight:800;margin-top:8px}</style>
</head>
<body><header><b>ALE TV KE LIVE</b><span style="color:#ff0033">● LIVE</span></header><div id="jitsi"></div><div class="info-bar"><div>Unaangalia Live Studio ya ALE TV</div><div style="opacity:.5;font-size:10px">TILL 3624692 - Lipa 100</div><button class="btn" onclick="location.href='index.html'">RUDI KWA TV</button></div>
<script>
const params=new URLSearchParams(window.location.search); let room=params.get('room')||localStorage.getItem('aletv_room')||'aletvke-demo';
const domain='meet.jit.si'; const options={roomName:room,width:'100%',height:'100%',parentNode:document.querySelector('#jitsi'),configOverwrite:{startWithAudioMuted:true,startWithVideoMuted:true,prejoinPageEnabled:true},interfaceConfigOverwrite:{SHOW_JITSI_WATERMARK:false},userInfo:{displayName:'Viewer '+Math.floor(Math.random()*1000)}};
const api=new JitsiMeetExternalAPI(domain,options);
</script></body></html>
"""

open('admin.html','w',encoding='utf-8').write(admin_html)
open('index.html','w',encoding='utf-8').write(index_html)
open('live.html','w',encoding='utf-8').write(live_html)
open('watch.html','w',encoding='utf-8').write(watch_html)
print("✅ KILA KITU KIKO TAYARI: admin.html, index.html, live.html, watch.html")
