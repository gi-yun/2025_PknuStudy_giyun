# ✅ cache_util.py - 캐시 저장 및 불러오기 유틸 모듈
import os
import json
from datetime import datetime

# ✅ 캐시 디렉토리 (우분투 기준으로 임시 설정)
CACHE_DIR = "/home/gy/chatbot/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# ✅ 캐시 파일 경로
CACHE_FILE = os.path.join(CACHE_DIR, "hanmirak_cache.json")

# ✅ 캐시 읽기 함수
def read_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

# ✅ 캐시 쓰기 함수
def write_cache(data):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ✅ 캐시 파일 경로 반환 함수 (사용자 디버깅용)
def get_cache_path():
    return CACHE_FILE
