from pprint import pprint
import requests

key = 'AIzaSyDmM8To4UYKBMEvfnmhY-EK8Yxpwoa3DWQ'

# string interpolation
search = input("검색어를 입력해 주세요 : ")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'

# 1. 검색어를 입력하면
# 2. 영상들을 검색 할 것
# 3. 그 영상들의 제목과 채널명

response = requests.get(url)
datas = response.json()

# 채널명, 영상
for data in datas['items'][:10] :
    print(data['snippet']['title'], end=' 채널명 : ')
    print(data['snippet']['channelTitle'])

