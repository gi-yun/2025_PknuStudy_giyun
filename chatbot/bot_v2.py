from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Application, CommandHandler, MessageHandler, InlineQueryHandler, filters, CallbackContext
import random
import uuid
import talk_kgy as tk
import gemini as ge
import movie as mv
import melon as ml

import os
from dotenv import load_dotenv  # 📌 .env 파일 로드하는 라이브러리

load_dotenv()
# ✅ .env에서 TELEGRAM_BOT_TOKEN 가져오기
TOKEN = os.getenv("TELEGRAM_TOKEN")

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

    # ✅ gemini를 이용한 gpt
    if "gpt" in user_text:
        res = ge.aiai(user_text.replace("gpt ", ""))
        await context.bot.send_message(chat_id=chat_id, text=res)
    # ✅ 한국영화진흥원에서 영화 랭킹뽑기
    elif "영화정보" in user_text:
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

# ✅ 봇 실행 설정
def main():
    app = Application.builder().token(TOKEN).build()

    # 🔹 명령어 핸들러 추가
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("fortune", get_fortune))  # ✅ 랜덤 운세 기능 추가

    # 🔹 응답 핸들러 추가 (일반 키워드 감지)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    # 🔹 인라인 모드 핸들러 추가
    app.add_handler(InlineQueryHandler(inline_query))

    print("기봇이 실행 중입니다... 모니터링 중...")
    app.run_polling()

# ✅ 실행 (메인 함수)
if __name__ == "__main__":
    main()