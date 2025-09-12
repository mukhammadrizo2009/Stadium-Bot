from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , ReplyKeyboardRemove
from telegram.ext import CallbackContext

def register_message(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Ro'yhatdan o'tishga xush kelibsiz! 🎯",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("📝 Ro'yhatdan o'tishni boshlash..!")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def get_name(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id, 
        text = "Ismingizni kiriting.! 🖊\n\n"\
            "Misol uchun: (Abdulla Abdullayev)",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardRemove()
    )