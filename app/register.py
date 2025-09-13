from telegram import Update , ReplyKeyboardMarkup , KeyboardButton , ReplyKeyboardRemove
from telegram.ext import CallbackContext
from config import register_states
from database import LocalSession
from models import User
from app.menus import send_menu

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
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id, 
        text = "Ismingizni kiriting.! 🖊\n\n"\
            "Misol uchun: (Abdulla Abdullayev)",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardRemove()
    )
    
    return register_states.NAME
    
def set_name(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    name = update.message.text.title()
    
    context.user_data['name'] = name
    
    bot.send_message(
        chat_id = user.id,
        text = "Telefon raqamingizni yuboring!☎️",
        parse_mode = "markdown",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Yuborish! 📞" , request_contact=True)]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
    ))
    return register_states.CONTACT
    
def set_contact(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    contact = update.message.contact
    context.user_data['contact'] = contact.phone_number
    user_data = context.user_data
    
    bot.send_message(
        chat_id = user.id,
        text = "Ro'yhatdan o'tish uchun ma'lumotlaringizni tasdiqlang! 📃\n\n" \
            f"🔖 Ismim Familyangiz: {user_data['name']}\n"\
                f"📞 Telefon raqamingiz: {user_data['contact']}",
                parse_mode = "markdown",
                reply_markup = ReplyKeyboardMarkup(
                    keyboard=[
                        [KeyboardButton("Tasqiqlash! ✅") , KeyboardButton("Tahrirlash! ♻️")]
                    ],
                    one_time_keyboard=True,
                    resize_keyboard=True
                )
    )
    return register_states.CONFIRM

def save_user(update: Update , context: CallbackContext):
    bot = context.bot
    user_tg = update.effective_user
    user_data = context.user_data
    
    with LocalSession() as session:
        user = User(
            telegram_id = user_tg.id,
            name = user_data['name'],
            contact = user_data['contact']
        )
        session.add(user)
        session.commit()
        
    context.user_data.clear()
    bot.send_message(
        chat_id = user_tg.id,
        text = "Siz muvafaqqiyatli ro'yhatdan o'tdingiz! 👍🏻",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardRemove()
    )
    
    send_menu(update , context)