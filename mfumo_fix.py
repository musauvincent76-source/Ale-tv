import pathlib
# SOMA ADMIN ILIYO NA GRAPHICS YAKO - USIIGUSE, TUNAFIX LOGIC TU
code = pathlib.Path('admin.html').read_text(encoding='utf-8')

# TOA kabisa file input - ndio inaharibu mfumo
code = code.replace('addFile(this)', 'alert("Mkuu tumia YouTube link pekee - file ya simu inabomoa mfumo!")')

# Hakikisha save inafanya kazi 100% - NO BLOB
code = code.replace(
    "function addFile(inp){ if(!inp.files[0]) return; let f=inp.files[0]; let url=URL.createObjectURL(f); state.playlist.push({id:Date.now(),title:f.name,url:url,meta:'File',status:'next'}); save(); render(); }",
    "function addFile(inp){ alert('Usitumie file ya simu mkuu - tumia YouTube link tu ndio mfumo usikate!'); }"
)

# Ongeza cleanup ya blob zilizokufa
code = code.replace(
    "function load(){try{let s=localStorage.getItem('aletv_state_v2'); if(s) state=JSON.parse(s);}catch{} render();}",
    "function load(){try{let s=localStorage.getItem('aletv_state_v2'); if(s){state=JSON.parse(s); state.playlist=state.playlist.filter(v=>!v.url.startsWith('blob:'));}}catch{} render();}"
)

pathlib.Path('admin.html').write_text(code, encoding='utf-8')
print("✅ MFUMO IMEFIXIWA - hakuna tena blob, hakuna kujikata!")
