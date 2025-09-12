from config import BOT_TOKEN
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
from app.start import start
from app.check_user import check_register
from database import engine , Base

Base.metadata.create_all(engine)

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    # CommandHandlers
    dispatcher.add_handler(CommandHandler("start" , start ))
    
    # MessageHandler = Start
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturda ro'yhatdan o'tish! 🪪") , check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Mehmoh sifatidan foydalanish! 🥷🏻") , ))
    
    # MessageHandler = Register
    dispatcher.add_handler(MessageHandler(Filters.text("📝 Ro'yhatdan o'tishni boshlash..!") , ))
    
    # MessageHandler = Guest
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()