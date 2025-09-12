from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def start(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "✋ Assalomu Alaykum...! \n\n" \
            "📍 Bu yerda Futbol maydonini buyurtma qilishingiz mumkin! 🏟",
            parse_mode = "markdown",
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("Dasturda ro'yhatdan o'tish! 🪪") , KeyboardButton("Mehmoh sifatidan foydalanish! 🥷🏻")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
    )