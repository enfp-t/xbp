import requests

city = input("都市を教えてください。")
API_KEY = "02c25dd9f56a16b6187f18e83731704d"  # あなたのAPI Keyを入力。

api = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={API_KEY}"

response = requests.get(api)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    print(f"{city}の現在の気温は{temperature}°Cです。")
else:
    print("天気情報を取得できませんでした。")

#気温と画像を結び付けたいときはifでくくる　


if temperature>=20:
    print("20度以上です") #←ここに画像ingのやつ入れる.pcに画像を分かるように名前を付けて保存し、pythonの中のimaesに入れ、貼る
else:
    print("20度未満です")

