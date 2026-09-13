from http.server import BaseHTTPRequestHandler, HTTPServer
import json, time, os

class DarajaDemo(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type','text/html; charset=utf-8')
            self.end_headers()
            html = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ALE TV LIPA DEMO</title>
<style>body{background:#0a0f1e;color:#fff;font-family:sans-serif;padding:20px;text-align:center}.card{background:#111a33;padding:20px;border-radius:12px;max-width:400px;margin:20px auto}input{width:90%;padding:12px;border-radius:8px;border:0;margin:8px 0}button{background:#ff6600;color:#fff;padding:12px 20px;border:0;border-radius:8px;font-weight:800;cursor:pointer;width:100%}</style></head><body>
<h2>ALE TV KE - LIPA NA TILL 3624692 (DEMO)</h2>
<div class="card"><h3>Daraja Sandbox Demo</h3><p style="color:#888">Hii ni demo - hakuna pesa ya kweli</p>
<input id="phone" placeholder="Namba: 2547XXXXXXXX" value="254700000000"><input id="amount" placeholder="Amount" value="10"><button onclick="lipa()">LIPA SASA (STK Push Demo)</button><div id="status" style="margin-top:12px;color:#ffcc99"></div></div>
<div class="card"><small>TV itaonyesha: Asante John Demo - 10 bob kwa scroll</small><br><br><a href="/tv" style="color:#ff6600">Fungua TV</a></div>
<script>
async function lipa(){
 let p=document.getElementById('phone').value, a=document.getElementById('amount').value;
 document.getElementById('status').innerText='Tuma STK Push kwa '+p+'...';
 let r=await fetch('/pay',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,amount:a})});
 let j=await r.json();
 document.getElementById('status').innerText=j.msg;
 if(j.ok){
   localStorage.setItem('ale_last_pay',JSON.stringify({name:'John Demo',amount:a,time:Date.now()}));
 }
}
</script></body></html>
"""
            self.wfile.write(html.encode('utf-8'))
        elif self.path == '/tv':
            self.send_response(302); self.send_header('Location','/aletv/index.html' if os.path.exists('index.html') else '/'); self.end_headers()
        elif self.path == '/payments':
            self.send_response(200); self.send_header('Content-type','application/json'); self.end_headers()
            try:
                with open('payments.json','r') as f: self.wfile.write(f.read().encode())
            except: self.wfile.write(b'[]')

    def do_POST(self):
        if self.path == '/pay':
            length = int(self.headers.get('Content-Length',0))
            data = json.loads(self.rfile.read(length).decode())
            print(f"DEMO STK Push -> {data['phone']} Amount {data['amount']}")
            try:
                with open('payments.json','r') as f: pays=json.load(f)
            except: pays=[]
            pays.append({"phone":data['phone'],"amount":data['amount'],"name":"John Demo","time":time.time()})
            with open('payments.json','w') as f: json.dump(pays,f)
            with open('last_pay.json','w') as f: json.dump({"name":"John Demo","amount":data['amount']},f)
            self.send_response(200); self.send_header('Content-type','application/json'); self.end_headers()
            self.wfile.write(json.dumps({"ok":True,"msg":"STK Push imetumwa! Angalia simu (DEMO) - TV inaonyesha Asante!"}).encode())

print("Demo ina-run kwa http://localhost:8082/")
HTTPServer(('0.0.0.0',8082), DarajaDemo).serve_forever()
