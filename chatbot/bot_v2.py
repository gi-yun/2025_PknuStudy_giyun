from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Application, CommandHandler, MessageHandler, InlineQueryHandler, filters, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler # 스케줄러
import random
import uuid
import asyncio #비동기
import time
# 추가 요소 import
import talk_kgy as tk
import gemini as ge
import movie as mv
import melon as ml
from hanmirak import update_cache  # 🔹 캐시 자동 생성을 위해 import
import hanmirak as hm


import os
from dotenv import load_dotenv  # 📌 .env 파일 로드하는 라이브러리

load_dotenv()
# ✅ .env에서 TELEGRAM_BOT_TOKEN 가져오기
TOKEN = os.getenv("TELEGRAM_TOKEN")

GROUP_CHAT_IDS = os.getenv("GROUP_CHAT_IDS", "") # defalt로 None 만들기
GROUP_CHAT_IDS = [int(chat_id.strip()) for chat_id in GROUP_CHAT_IDS.split(",") if chat_id.strip()]# 리스트로 만들고 공백과 정수형으로 변환


# TOKEN = ""

# ✅ 기본 응답 트리거
#흔적

# ✅ 랜덤 운세 카드 목록
#흔적


# ✅ 봇 시작 명령어
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("안녕하세요! 저는 기봇 입니다. 무엇을 도와드릴까요?")

# ✅ 사진 보내기
async def send_photo(update, context):
    photo_url = "https://i.namu.wiki/i/R0AhIJhNi8fkU2Al72pglkrT8QenAaCJd1as-d_iY6MC8nub1iI5VzIqzJlLa-1uzZm--TkB-KHFiT-P-t7bEg.webp"
    await update.message.reply_photo(photo=photo_url,caption="사진 이미지 불러왔어요~")

# ✅ 사용자 메시지 감지 및 응답 (키워드 자동 응답)
async def monitor_chat(update: Update, context: CallbackContext):
    user_text = update.message.text  # 감지된 메시지
    chat_id = update.message.chat_id  # 메시지가 온 채팅방 ID
    print(f"[DEBUG] 그룹방 ID: {update.message.chat_id}")

    # ✅ gemini를 이용한 gpt
    if "gpt" in user_text:
        res = ge.aiai(user_text.replace("gpt ", " "))
        await context.bot.send_message(chat_id=chat_id, text=res)
    # ✅ 한국영화진흥원에서 영화 랭킹뽑기
    elif "영화순위" in user_text:
        res = mv.movie()
        await context.bot.send_message(chat_id=chat_id, text=res)
    # ✅ 사진 가져오기
    elif "사진줘" in user_text:
        await send_photo(update,context)
    # ✅ 멜론 노래 순위
    elif "멜론순위" in user_text:
        res = ml.melon()
        await context.bot.send_message(chat_id=chat_id, text=res)
    #✅ 그외 특정언어 대답
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id=chat_id, text=res)
                break  # 한 개의 키워드에만 반응

# ✅ 운세 뽑기 기능 (명령어 방식)
async def get_fortune(update: Update, context: CallbackContext):
    card = random.choice(tk.FORTUNE_CARDS)  # 랜덤 카드 선택

    message = f"""
✨ 당신의 운세 카드 ✨
🎴 **{card['name']}** 🎴

📜 {card['description']}

✅ {card['positive']}
❌ {card['negative']}
    """

    await update.message.reply_text(message, parse_mode="Markdown")

# ✅ 인라인 쿼리 처리 (사용자가 @pkgy_bot 입력하면 실행)
async def inline_query(update: Update, context: CallbackContext):
    query = update.inline_query.query.lower().strip()  # 사용자가 입력한 검색어

    # 랜덤 운세 카드 선택
    card = random.choice(tk.FORTUNE_CARDS)

    result = InlineQueryResultArticle(
        id=str(uuid.uuid4()),  # 고유 ID 생성
        title="✨ 랜덤 운세 뽑기!",
        input_message_content=InputTextMessageContent(
            f"✨ 당신의 랜덤 운세 카드 ✨\n🎴 **{card['name']}** 🎴\n📜 {card['description']}\n✅ {card['positive']}\n❌ {card['negative']}"
        ),
        description=f"{card['name']} - {card['description']}",
    )

    # 결과 전송 (한 개만 보여줌 → 랜덤)
    await update.inline_query.answer([result], cache_time=1)

# ✅ 한미락 → 오늘 메뉴
async def get_hanmirak_today(update: Update, context: CallbackContext):
    start = time.time()  # ⏱ 전체 처리 시간 측정
    menu = hm.get_today_menu()
    await update.message.reply_text(menu)
    print(f"[DEBUG] get_today_menu() 전체 소요 시간: {time.time() - start:.4f}초")

# ✅ 한미락주간 → 주간 전체
async def get_hanmirak_weekly(update: Update, context: CallbackContext):
    start = time.time()  # ⏱ 전체 처리 시간 측정
    menu = hm.get_weekly_menu()
    await update.message.reply_text(menu)
    print(f"[DEBUG] get_today_menu() 전체 소요 시간: {time.time() - start:.4f}초")


# ✅ 12시 되면 메뉴 전송
def schedule_jobs(application):
    scheduler = BackgroundScheduler()
    scheduler.start()

    async def send_lunch():
        try:
            if GROUP_CHAT_IDS:
                menu = hm.get_today_menu()
                for chat_id in GROUP_CHAT_IDS:
                    await application.bot.send_message(chat_id=chat_id, text=menu)
                print("[INFO] ⏰ 스케줄 메시지 전송 완료")
            else:
                print("[WARN] GROUP_CHAT_IDS가 설정되지 않음")
        except Exception as e:
            print(f"[ERROR] 스케줄 메시지 전송 실패: {e}")

    def job():
        import asyncio
        asyncio.run(send_lunch())  # 🔥 핵심 비동기 처리

    scheduler.add_job(job, 'cron', hour=12, minute=00, misfire_grace_time=60)

# 테스트
async def testlunch(update: Update, context: CallbackContext):
    from hanmirak import get_today_menu
    menu = get_today_menu()
    for chat_id in GROUP_CHAT_IDS:
        try:
            await context.bot.send_message(chat_id=chat_id, text=menu)
            print(f"[INFO] 테스트 메시지 전송 성공: {chat_id}")
        except Exception as e:
            print(f"[WARN] 테스트 메시지 전송 실패: {chat_id} → {e}")







# ✅ 봇 실행 설정
def main():
    app = Application.builder().token(TOKEN).build()

    # ✅ 실행 시점에 캐시 초기화 (없으면 생성)
    try:
        result = update_cache()
        if result:
            print("✅ 한미락 캐시 초기화 완료")
        else:
            print("⚠️ 한미락 캐시 초기화 실패 (페이지 로딩 문제)")
    except Exception as e:
        print(f"❌ 한미락 캐시 초기화 중 오류 발생: {e}")

    # 🔹 명령어 핸들러 추가
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fortune", get_fortune))
    app.add_handler(CommandHandler("lunch", get_hanmirak_today))
    app.add_handler(CommandHandler("lunchweekly", get_hanmirak_weekly))
    app.add_handler(CommandHandler("testlunch", testlunch))

    # 🔹 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    # 🔹 인라인 핸들러 추가
    app.add_handler(InlineQueryHandler(inline_query))

    # 🔹 스케줄러 등록
    schedule_jobs(app)

    print("🤖 기봇이 실행 중입니다... 명령을 기다리는 중...")
    app.run_polling()

# ✅ 실행 (메인 함수)
if __name__ == "__main__":
    main()