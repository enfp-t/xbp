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

if 15 <= temperature < 20:
     print(f"気温:", {temperature},"°Cです。１５度から２０度の範囲です。")
     # 15~20度の範囲の場合、指定の画像Aを表示
     image_url = "URL_TO_IMAGE_A"
elif 20 <= temperature < 25:
     print(f"気温:", {temperature},"°Cです。２０度から２５度の範囲です。")
     # 20~25度の範囲の場合、指定の画像Bを表示
     image_url = "URL_TO_IMAGE_B"


# else:

#     print("気温情報を取得できませんでした。APIキーや場所を確認してください。")

 
 

 