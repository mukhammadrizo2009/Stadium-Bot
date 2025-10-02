from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackContext

def send_guest_menu(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Sahifalar ro'yhati! 📝",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Stadion buyurtmasi 📌") , KeyboardButton("Ro'yhatdan o'tish! 🪪")],
                [KeyboardButton("Bot gruhiga qo'shilish! 💡") , KeyboardButton("Dasturni tugatish ❌")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )