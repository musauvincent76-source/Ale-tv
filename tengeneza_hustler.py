idx=open('index.html','w',encoding='utf-8')
idx.write("""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ALE TV - Hustler Mode</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:sans-serif}header{background:#0f1a0f;padding:12px 15px;display:flex;justify-content:space-between;position:sticky;top:0;z-index:50}#playerWrap{position:relative;width:100%;aspect-ratio:16/9;background:#000;overflow:hidden}#player iframe{width:100%;height:100%;border:0;position:absolute;top:0;left:0}.info{padding:15px;background:#0a0a0a}.badge{font-size:9px;background:#00ff88;color:#000;padding:4px 8px;border-radius:10px;font-weight:900}</style></head><body>
<header><b>ALE TV KE LIVE</b><span class="badge">HUSTLER MODE - DATA SAVER</span></header>
<div id="playerWrap"><div id="msg" style="color:#888;text-align:center;padding:60px 20px;font-size:14px">📺 Bado hamjaweka video<br><span style="font-size:11px;opacity:.6">Nenda Admin weka YouTube</span></div><iframe id="yt" style="display:none" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
<div class="info"><h3 id="title">Karibu ALE TV</h3><div id="status" style="font-size:11px;opacity:.6;margin-top:6px">Inasubiri video...</div>
<div style="margin-top:12px;display:flex;gap:8px"><button onclick="setQuality('small')" style="background:#222;color:#fff;border:1px solid #333;padding:8px 12px;border-radius:20px;font-size:10px">📱 DATA SAVER</button><button onclick="setQuality('medium')" style="background:#222;color:#fff;border:1px solid #333;padding:8px 12px;border-radius:20px;font-size:10px">🎥 HD</button></div>
</div>
<script>
let currentQ='small';
function setQuality(q){currentQ=q;localStorage.setItem('aletv_q',q);loadTV();alert(q=='small'?'✅ Data Saver ON - Haitakata tena!':'✅ HD ON');}
function getYtId(url){if(!url)return'';url=url.trim();if(url.includes('youtu.be/'))return url.split('youtu.be/')[1].split('?')[0].split('&')[0];try{let u=new URL(url);if(u.searchParams.get('v'))return u.searchParams.get('v');}catch(e){let m=url.match(/v=([^&]+)/);if(m)return m[1];}return'';}
function loadTV(){
 let q=localStorage.getItem('aletv_q')||'small';
 let cur=null;try{cur=JSON.parse(localStorage.getItem('aletv_live_now')||'null')}catch{}
 let state=null;try{state=JSON.parse(localStorage.getItem('aletv_state_v2')||'null')}catch{}
 if(!cur&&state&&state.playlist&&state.playlist.length>0)cur=state.playlist.find(p=>p.status==='now')||state.playlist[0];
 let msg=document.getElementById('msg'),yt=document.getElementById('yt');
 if(!cur){msg.style.display='block';yt.style.display='none';return;}
 document.getElementById('title').innerText=cur.title;
 document.getElementById('status').innerText='● LIVE - Mode: '+(q=='small'?'Data Saver (haikatiki)':'HD');
 let id=cur.ytid||getYtId(cur.url);
 if(!id){msg.innerHTML='⚠️ Link sio sahihi';msg.style.display='block';yt.style.display='none';return;}
 msg.style.display='none';
 // HUSTLER MODE: vq=small/tiny inapunguza data 80% - haikatiki!
 let vq=q=='small'?'tiny':'hd720';
 yt.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&playsinline=1&rel=0&modestbranding=1&vq='+vq+'&enablejsapi=1&origin='+location.origin;
 yt.style.display='block';
}
loadTV();setInterval(loadTV,4000);
document.addEventListener('visibilitychange',()=>{if(!document.hidden) loadTV();});
</script></body></html>""")
print("✅ HUSTLER MODE tayari - haikatiki tena hata na bundles za 20 bob!")
