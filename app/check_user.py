from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext
from database import LocalSession
from models import User
from app.menus import user_already_register
from app.register import register_message

def check_register(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    with LocalSession() as session:
        user = session.query(User).filter(User.telegram_id == user.id).first()
        
        if user:
            user_already_register(update , context)
            
        else:
            register_message(update , context)