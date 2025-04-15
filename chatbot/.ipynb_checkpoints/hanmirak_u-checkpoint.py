# hanmirak_u.py 개선 버전
import os
import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ cache_util 모듈에서 캐시 함수 가져오기
from cache_util import read_cache, write_cache

# ====== 캐시 유효기간 설정 (월요일 기준 새로고침) ======
# def is_cache_expired():
#     today = datetime.datetime.today()
#     return today.weekday() == 0  # 월요일이면 True 반환

# ====== 한미락 테이블 HTML 가져오기 ======
def _fetch_hanmirak_table():
    options = Options()
    options.binary_location = "/home/gy/chatbot/chrome/chrome/chrome-linux64/chrome"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    prefs = {
        "profile.managed_default_content_settings.images": 2,
        "profile.managed_default_content_settings.fonts": 2,
        "profile.managed_default_content_settings.plugins": 2
    }
    options.add_experimental_option("prefs", prefs)

    service = Service("/home/gy/chatbot/chrome/chromedriver/chromedriver-linux64/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.pknu.ac.kr/main/399")

    try:
        wait = WebDriverWait(driver, 10)
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#subCont > table > tbody > tr:nth-child(1) > td.bdlTitle > a")))
        ActionChains(driver).move_to_element(link).click().perform()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.con03_sub_2_wrap")))
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for div in soup.select("div.con03_sub_2_wrap"):
            p = div.find("p")
            if p and "한미락" in p.text:
                print("[INFO] 한미락 테이블 찾음")
                return div.find("table", class_="con03_sub_2")
        print("[ERROR] '한미락' 테이블을 찾을 수 없습니다.")
        return None
    finally:
        driver.quit()

# ====== 캐시 업데이트 (전체 주간 식단) ======
def update_cache():
    table = _fetch_hanmirak_table()
    if not table:
        print("[ERROR] 크롤링 실패: 테이블이 존재하지 않음")
        return None

    cache = {}
    try:
        meal_row = table.select('tr')[2]
        tds = meal_row.select('td')[1:6]
        for idx, td in enumerate(tds):
            date = (datetime.datetime.today() + datetime.timedelta(days=(idx - datetime.datetime.today().weekday()))).strftime("%m월 %d일")
            meals = [p.get_text(strip=True) for p in td.select('p') if p.get_text(strip=True)]
            cache[f"{['월','화','수','목','금'][idx]}"] = f"{date} " + "\n" + "\n".join(f"• {m}" for m in meals) if meals else "• 식단 정보 없음"
        write_cache(cache)
        print("[INFO] 캐시 생성 완료")
        return cache
    except Exception as e:
        print(f"[데이터 처리 오류] {e}")
        return None

# ====== 오늘 식단 가져오기 ======
def get_today_menu(force=False):
    weekday = datetime.datetime.today().weekday()
    days = ['월','화','수','목','금']

    if weekday >= 5:
        return "😴 주말은 한미락 운영이 없습니다."

    cache = read_cache()
    if not cache or force:
        print("[INFO] 캐시 없음 또는 강제 재생성. 캐시 갱신 시작...")
        cache = update_cache()
        if not cache:
            print("[ERROR] 오늘 식단 정보를 불러올 수 없습니다. 캐시 생성 실패")
            return "⚠️ 오늘의 식단 정보를 불러오는 데 문제가 발생했습니다."

    print("[INFO] 오늘 식단 반환")
    return f"📅 오늘의 한미락 식단 ({cache[days[weekday]].splitlines()[0]})\n" + "\n".join(cache[days[weekday]].splitlines()[1:])

# ====== 이번 주 식단 가져오기 ======
def get_weekly_menu(force=False):
    days = ['월','화','수','목','금']
    cache = read_cache()
    if not cache or force:
        print("[INFO] 캐시 없음 또는 강제 재생성. 캐시 갱신 시작...")
        cache = update_cache()
        if not cache:
            print("[ERROR] 주간 식단 정보를 불러올 수 없습니다. 캐시 생성 실패")
            return "⚠️ 주간 식단 정보를 불러오는 데 문제가 발생했습니다."

    result = []
    for day in days:
        lines = cache.get(day, "• 식단 정보 없음").splitlines()
        if lines:
            header = f"📅 {day}요일 ({lines[0]})"
            result.append(header + "\n" + "\n".join(lines[1:]))
        else:
            result.append(f"📅 {day}요일\n• 식단 정보 없음")
    print("[INFO] 주간 식단 반환")
    return "\n\n".join(result)
