# 구글 제미나이 AI
from google import genai
import os
from dotenv import load_dotenv  # 📌 .env 파일 로드하는 라이브러리
load_dotenv()
# ✅ .env에서 TOKEN 가져오기
TOKEN = os.getenv("GOOGLE_GEMINI")

def aiai(text):
    client = genai.Client(api_key=TOKEN)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text+ "; 단 400자 이내 그리고 서술형으로 친절히 알려줘."
    )
    answer = response.text
    print(answer)
    return answer
aiai("pandas에 대해서 궁금해")

if __name__=="__main__":
    aiai("gpt에대해 설명해")