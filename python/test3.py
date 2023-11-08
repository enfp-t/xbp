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


if temperature < 15:
    print("15度未満です")
elif 15 <= temperature < 20:
    print("15度以上20度未満です") #←ここに画像ingのやつ入れる.pcに画像を分かるように名前を付けて保存し、pythonの中のimaesに入れ、貼る
elif 20 <= temperature < 25:
    print("20 度以上25度未満です") #←ここに画像ingのやつ入れる.pcに画像を分かるように名前を付けて保存し、pythonの中のimaesに入れ、貼る
elif 25 < temperature :
    print("25度以上です")
else:
    print("天気情報を取得できませんでした。")

