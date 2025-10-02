from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext
from sqlalchemy.orm import Session
from dependencies import get_db 
from models import User

def profile(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    telegram_id = update.message.from_user.id
    
    db: Session = next(get_db())
    
    try:
        user = db.query(User).filter(User.telegram_id == telegram_id).first()
        
        if user:
            name = user.name if user.name else "Kiritilmagan"
            contact = user.contact if user.contact else "Kiritilmagan"
            
            profile_text = (
                "👤 <b>Sizning profilingiz:</b>\n\n"
                f"📝 Ism: {name}\n"
                f"📱 Telefon: {contact}"
            )
            update.message.reply_text(profile_text, parse_mode='HTML')
           
            update.message.reply_text(
            "Yana biror amal bajarasizmi?",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("Dasturni davom ettirish! ↩️"),
                        KeyboardButton("Dasturni tugatish! 🛑")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))
    
        else:
            update.message.reply_text(
                "❌ Sizning ma'lumotlaringiz topilmadi."
            )
    finally:
        db.close()