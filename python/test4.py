・：＠import http.client

conn = http.client.HTTPSConnection("navitime-congestion-prediction.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "fcfd81ef59msh40554f0afa5a1e2p13957ajsnec0e34d1c324",
    'x-rapidapi-host': "navitime-congestion-prediction.p.rapidapi.com"
}

conn.request("GET", "/transport_node?word=%E6%9D%B1%E4%BA%AC&offset=0&limit=10&datum=wgs84&coord_unit=degree", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))