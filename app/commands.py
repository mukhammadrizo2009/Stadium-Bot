from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , ReplyKeyboardRemove
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
    
def stop(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Dasturda qayta ko'rishguncha! 👋",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardRemove()
    )
    
def help(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Yordam uchun ADMINGA murojat qiling! \n\n"\
            f"Admin: @mirzayeoff 🌐",
            reply_markup = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("Dasturni davom ettirish! ↩️") , KeyboardButton("Dasturni tugatish! 🛑")]
                ], 
                resize_keyboard=True,
                one_time_keyboard=True
            )
    )