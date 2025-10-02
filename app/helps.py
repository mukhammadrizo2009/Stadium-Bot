from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def help(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Muammo turlarini tanlang! 🚨",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Bot kamchiliklari! 👾") , KeyboardButton("Buyurtmada muammolar! 🥡") , KeyboardButton("Boshqa muammo 🚧")],
                [KeyboardButton("Bot haqida ! ♟")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def bot_error(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Muammoni bu yerga yuborishingiz mumkin! 🔖\n\
        https://t.me/+_9C4KN-TlOA3Mjc6 ",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                    [KeyboardButton("Dasturni davom ettirish! ↩️"),KeyboardButton("Dasturni tugatish! 🛑")]
                ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def order_error(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id , 
        text = "Buyurtma bo'yicha muammo! \n\
ADMIN🌐: @stadium_bot_admin ",
            reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                    [KeyboardButton("Dasturni davom ettirish! ↩️"),
                        KeyboardButton("Dasturni tugatish! 🛑")]
                ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )