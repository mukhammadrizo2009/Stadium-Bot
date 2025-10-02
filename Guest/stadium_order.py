from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackContext

def order(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Buyurtma qilish uchun avval ro'yhatdan o'ting! 📍",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Ro'yhatdan o'tish! 🪪") , KeyboardButton("Dasturni tugatish ❌") ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )