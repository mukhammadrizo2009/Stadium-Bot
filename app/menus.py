import datetime
from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackContext

def send_menu(update: Update , context: CallbackContext): 
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Sahifalar ro'yhati! 📝",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Stadion buyurtma qilish 📌") , KeyboardButton("Profilim 👤")],
                [KeyboardButton("Yordam 👮🏻‍♂️") , KeyboardButton("Dasturni tugatish ❌")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def send_date(update: Update , context: CallbackContext):
    months = {
        "January": "Yanvar",
        "February": "Fevral",
        "March": "Mart",
        "April": "Aprel",
        "May": "May",
        "June": "Iyun",
        "July": "Iyul",
        "August": "Avgust",
        "September": "Sentyabr",
        "October": "Oktyabr",
        "November": "Noyabr",
        "December": "Dekabr"
    }
    date = datetime.date.today()
    keyboard = [
        [
            InlineKeyboardButton(
                f'📅 {date.day}-{months[date.strftime("%B")]}',
                callback_data=f"date: {date}"
            )
        ]
    ]
    
    for _ in range(6): 
        date += datetime.timedelta(days=1)
        keyboard.append(
            [
                InlineKeyboardButton(
                    f'📅 {date.day}-{months[date.strftime("%B")]}',
                    callback_data=f"date: {date}"
                )
            ]
        )
    update.message.reply_text(
        "Sanalardan birini tanlang!",
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
        
def user_already_register(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Siz ro'yhatdan o'tgan ekansiz! 💡\n\n"\
            "📃 Sahifalardan birini tanlashingiz mumkin! ",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Stadion buyurtma qilish 📌") , KeyboardButton("Profilim 👤")],
                [KeyboardButton("Yordam 👮🏻‍♂️") , KeyboardButton("Dasturni tugatish ❌")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )