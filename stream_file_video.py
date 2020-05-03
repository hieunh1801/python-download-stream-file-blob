import requests
import m3u8

# inspect network and find file m3u8
# link film http://animeme.cliphub.net/movie/-ten-cau-la-gi-your-name-kimi-no-na-wa_vTjvxA5D.html
url = "https://sgp.dgo.clhcdn.net/ghls/clhgfs/5keC7wQP/vTjvxA5D-720.mp4/index-v1-a1.m3u8?v=1537462647"
r = requests.get(url)
print(r.text)
m3u8_master = m3u8.load(r.text)
print(m3u8.data)