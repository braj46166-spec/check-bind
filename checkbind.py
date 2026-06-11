from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/bindinfo")
def bindinfo(access_token: str):
    url = "https://100067.connect.garena.com/game/account_security/bind:get_bind_info"

    headers = {
        "User-Agent": "GarenaMSDK/4.0.39 (M2007J22C; Android 10; en; US;)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip"
    }

    params = {
        "app_id": "100067",
        "access_token": access_token
    }

    r = requests.get(url, headers=headers, params=params)

    try:
        data = r.json()
    except:
        data = {"response": r.text}

    return {
        "developer": "XNITE FF DEVELOPER",
        "status": "success",
        "result": data
    }