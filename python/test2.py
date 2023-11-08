import requests
# ご自身のOpenWeatherMap APIキーを設定してください
# api_key = "YOUR_API_KEY"
# # 都市名や緯度経度を設定します（例: Tokyo,JP）
# location = "Tokyo,JP"
# OpenWeatherMap APIにリクエストを送信
url = "https://api.weatherapi.com/v1/current.json?key=9578d0e7dac54754bc470314233110&q=Tokyo&aqi=yes"
response = requests.get(url)
data = response.json()
place= data['location']['name']
temperature = data['current']['temp_c']
print(place, temperature,"度")

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']

if temperature < 15:
    print("15度未満です")
elif 15 <= temperature < 20:
    print("15度以上20度未満です") #←ここに画像ingのやつ入れる.pcに画像を分かるように名前を付けて保存し、pythonの中のimaesに入れ、貼る
elif 20 <= temperature < 25:
    print("20 度以上25度未満です") #←ここに画像ingのやつ入れる.pcに画像を分かるように名前を付けて保存し、pythonの中のimaesに入れ、貼る
elif 25 < temperature :
    print("25度以上です")
else:
    print("条件に該当しない範囲です。")


#     print("気温情報を取得できませんでした。APIキーや場所を確認してください。")

 
 

 