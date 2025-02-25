import requests
from datetime import date, timedelta

import os
from dotenv import load_dotenv  # 📌 .env 파일 로드하는 라이브러리

load_dotenv()
# ✅ .env에서 TOKEN 가져오기
TOKEN = os.getenv("MOVIE_TOKEN")

# 어제 날짜 계산 (오늘 날짜에서 하루 빼기)
yesterday = date.today() - timedelta(days=1)
formatted_date = yesterday.strftime("%Y%m%d")

# API 요청 URL
url = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
params = {
    "key": TOKEN,  # 본인의 API 키 입력
    "targetDt": formatted_date  # 어제 날짜 사용
}
def movie():
    str=""
    # API 요청 및 JSON 데이터 가져오기
    response = requests.get(url, params=params)
    data = response.json()
    
    print("어제 상영된 영화 랭킹 순위입니다.")
    # rnum, rank, movieNm 필드만 출력
    for movie in data["boxOfficeResult"]["dailyBoxOfficeList"]:
        rank = movie["rank"]
        movieNm = movie["movieNm"]
        # print(f"랭킹 {rank}등은 [{movieNm}] 입니다.")
        sent=f'랭킹 {rank}등은 [{movieNm}] 입니다.\n'
        str += sent
    return str
