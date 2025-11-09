from telegram import (
    Update, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove
)
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters, 
    ConversationHandler, 
    CallbackContext
)
from datetime import datetime, timedelta

# --- Holatlar (States) ---
class booking_station_states:
    DATE, TIME, CONFIRM, PAYMENT = range(4)

# --- 1. START: Foydalanuvchi "Stadion buyurtma qilish 📌"ni bosganda ---
def send_date(update: Update, context: CallbackContext):
    user = update.message.from_user

    today = datetime.now()
    dates = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(4)]

    keyboard = [[d] for d in dates] + [["Bekor qilish ❌"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
        text=(
            f"📅 Stadionni qaysi sanaga bron qilmoqchisiz, {user.first_name}?\n\n"
            "Masalan: 2025-11-10"
        ),
        reply_markup=reply_markup
    )

    return booking_station_states.DATE


# --- 2. Sana tanlangandan keyin vaqtni so‘rash ---
def get_time(update: Update, context: CallbackContext):
    date_text = update.message.text

    if date_text == "Bekor qilish ❌":
        update.message.reply_text("❌ Buyurtma bekor qilindi.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    # Sanani saqlaymiz
    context.user_data["date"] = date_text

    times = [["09:00 - 10:00"], ["12:00 - 14:00"], ["15:00 - 17:00"], ["18:00 - 20:00"], ["Bekor qilish ❌"]]
    reply_markup = ReplyKeyboardMarkup(times, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
        text=f"⏰ {date_text} sanasiga qaysi vaqtda o‘ynamoqchisiz?",
        reply_markup=reply_markup
    )

    return booking_station_states.TIME


# --- 3. Vaqt tanlangandan keyin tasdiqlash ---
def confirm_booking(update: Update, context: CallbackContext):
    time_text = update.message.text

    if time_text == "Bekor qilish ❌":
        update.message.reply_text("❌ Buyurtma bekor qilindi.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    context.user_data["time"] = time_text

    date = context.user_data["date"]
    keyboard = [["Ha, tasdiqlayman ✅"], ["Yo‘q, bekor qilish ❌"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
        text=f"📋 Buyurtma ma’lumotlari:\n\n📅 Sana: {date}\n⏰ Vaqt: {time_text}\n\nTasdiqlaysizmi?",
        reply_markup=reply_markup
    )

    return booking_station_states.CONFIRM


# --- 4. Tasdiqlangandan keyin to‘lov jarayoni ---
def process_payment(update: Update, context: CallbackContext):
    text = update.message.text

    if "bekor" in text.lower():
        update.message.reply_text("❌ Buyurtma bekor qilindi.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

    date = context.user_data["date"]
    time = context.user_data["time"]

    # (Bu joyda to‘lov tizimi ulanadi, hozircha oddiy xabar)
    update.message.reply_text(
        text=(
            f"💸 Buyurtmangiz qabul qilindi!\n\n"
            f"📅 Sana: {date}\n⏰ Vaqt: {time}\n\n"
            "To‘lov joyida amalga oshiriladi.\n\nRahmat! 🙌"
        ),
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


# --- 5. Fallback (bekor qilish komandasi) ---
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("❌ Jarayon bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END