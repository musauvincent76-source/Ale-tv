admin = open('admin.html','r',encoding='utf-8').read()

# 1. ONGEZA BUTTON YA WEKA ONLINE NA AUTO TITLE
admin = admin.replace(
    '<div class="inputs"><input id="vTitle" placeholder="Video Title"><input id="vUrl" placeholder="YouTube link au video file URL">',
    '''<div class="inputs"><input id="vTitle" placeholder="Video Title - itajijaza auto ukiweka YouTube"><input id="vUrl" placeholder="YouTube link au video file URL" oninput="autoTitle(this.value)">
<button id="addBtn" onclick="addVideoOnline()" style="width:100%;background:#c8ff00;color:#000;border:none;padding:12px;border-radius:20px;font-weight:900;margin-bottom:10px">➕ Weka Online</button>'''
)

# Add functions
admin = admin.replace(
    "function moveToLive(id){",
    """
function addVideoOnline(){
 let title=document.getElementById('vTitle').value.trim();
 let url=document.getElementById('vUrl').value.trim();
 if(!url){toast('Weka YouTube link kwanza!');return;}
 if(!title){title='YouTube Video - '+url.split('/').pop().split('?')[0].substring(0,15);}
 state.playlist.push({id:Date.now(),title:title,meta:'YouTube • Just now',status:'next',thumb:'▶️',url:url});
 save();renderPlaylist();
 document.getElementById('vTitle').value='';document.getElementById('vUrl').value='';
 toast('✅ Imewekwa Online: '+title);
}
async function autoTitle(url){
 if(!url.includes('youtu')) return;
 try{
   let o='https://www.youtube.com/oembed?url='+encodeURIComponent(url)+'&format=json';
   let r=await fetch('https://api.allorigins.win/raw?url='+encodeURIComponent(o));
   let d=await r.json();
   if(d.title){document.getElementById('vTitle').value=d.title;}
 }catch(e){
   // fallback - jaza ID tu
   let id=url.split('v=')[1]?.split('&')[0]||url.split('/').pop().split('?')[0];
   if(id) document.getElementById('vTitle').value='YouTube: '+id;
 }
}
function toggleUpcg(id){
 let v=state.playlist.find(p=>p.id===id);
 if(!v) return;
 if(v.status==='upcg'){v.status='next'; toast('Toa kwenye Upcoming');}
 else {v.status='upcg'; toast('Weka Upcoming');}
 save();renderPlaylist();
}
function moveToLive(id){
"""
)

# 2. ONGEZA BUTTON YA UPCG KATIKA PLAYLIST
admin = admin.replace(
    "let right=v.status==='now'?`<span class=badge-now>NOW PLAYING</span><button class=\"btn-small remove\" onclick=\"removeVideo(${v.id})\">Remove</button>`:`<span style=\"font-size:8px;opacity:.5\">UP NEXT</span><button class=\"btn-small live\" onclick=\"moveToLive(${v.id})\">Move to Live</button>`;",
    """let isUpcg=v.status==='upcg';
let right=v.status==='now'?`<span class=badge-now>NOW PLAYING</span><button class="btn-small remove" onclick="removeVideo(${v.id})">Remove</button>`:
 isUpcg?`<span style="font-size:8px;background:#ffaa00;color:#000;padding:2px 6px;border-radius:6px;font-weight:800">UPCG</span><div style="display:flex;gap:4px"><button class="btn-small live" onclick="moveToLive(${v.id})" style="font-size:8px">Live</button><button class="btn-small" onclick="toggleUpcg(${v.id})" style="background:#555;color:#fff;font-size:8px">Toa</button></div>`:
 `<div style="display:flex;gap:4px;align-items:center"><span style="font-size:8px;opacity:.5">UP NEXT</span><button class="btn-small" onclick="toggleUpcg(${v.id})" style="background:#ffaa00;color:#000;font-size:8px;font-weight:900">upcg</button></div><div style="display:flex;gap:4px"><button class="btn-small live" onclick="moveToLive(${v.id})">Move to Live</button><button class="btn-small remove" onclick="removeVideo(${v.id})" style="font-size:8px;padding:4px 6px">X</button></div>`;"""
)

open('admin.html','w',encoding='utf-8').write(admin)

# FIX INDEX.HTML - CITIZEN TV STYLE
index = open('index.html','r',encoding='utf-8').read()
index = index.replace(
    "#player{aspect-ratio:16/9;background:#111;display:flex;align-items:center;justify-content:center;position:relative}",
    "#player{aspect-ratio:16/9;background:#111;display:flex;align-items:center;justify-content:center;position:sticky;top:0;z-index:20}"
)
index = index.replace(
    ".info{padding:15px}",
    ".info{padding:15px;overflow-y:auto;max-height:55vh} body{display:flex;flex-direction:column;height:100vh} header{position:sticky;top:0;z-index:21}"
)

open('index.html','w',encoding='utf-8').write(index)
print("✅ Fixed: Weka Online + auto title + upcg + Citizen TV scroll")
