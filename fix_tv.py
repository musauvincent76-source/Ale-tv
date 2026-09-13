index = open('index.html','r',encoding='utf-8').read()

# REJESHA PLAYER ILI ISIKATIKE - CITIZEN TV STYLE
index = index.replace(
    '#player{aspect-ratio:16/9;background:#111;display:flex;align-items:center;justify-content:center;position:sticky;top:0;z-index:20}',
    '#player{width:100%;aspect-ratio:16/9;background:#000;display:flex;align-items:center;justify-content:center;position:sticky;top:46px;z-index:20;overflow:hidden}'
)

# REKEBISHA VIDEO / IFRAME IONEKANE VIZURI
index = index.replace(
    'video,iframe{width:100%;height:100%;border:none}',
    'video,iframe{width:100%;height:100%;border:none;position:absolute;top:0;left:0;object-fit:contain}'
)

# REJESHA MSG KATI
index = index.replace(
    '.live-badge{position:absolute;top:10px;left:10px;background:#ff0033;color:#fff;padding:4px 10px;border-radius:5px;font-weight:900;font-size:12px;animation:blink 1s infinite}',
    '.live-badge{position:absolute;top:10px;left:10px;background:#ff0033;color:#fff;padding:4px 10px;border-radius:5px;font-weight:900;font-size:12px;animation:blink 1s infinite;z-index:30} #msg{position:absolute;z-index:5;text-align:center;padding:20px}'
)

# ONDOA MAX-HEIGHT ILIYOKATA SCROLL
index = index.replace(
    '.info{padding:15px;overflow-y:auto;max-height:55vh} body{display:flex;flex-direction:column;height:100vh} header{position:sticky;top:0;z-index:21}',
    '.info{padding:15px} body{background:#000} header{position:sticky;top:0;z-index:21;background:#0f1a0f}'
)

open('index.html','w',encoding='utf-8').write(index)
print("✅ TV Fixed - video haikatiki tena")
