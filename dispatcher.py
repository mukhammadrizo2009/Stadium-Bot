from config import config , register_states , booking_station_states
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , ConversationHandler
from app.commands import start , stop , help
from app.check_user import check_register
from app.register import get_name , set_name , set_contact , save_user
from database import engine , Base
from app.menus import send_date , send_menu

Base.metadata.create_all(engine)

def main() -> None:
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher
    
    # CommandHandlers
    dispatcher.add_handler(CommandHandler("start" , start ))
    dispatcher.add_handler(CommandHandler("stop" , stop))
    dispatcher.add_handler(CommandHandler("help" , help))
    
    # MessageHandler = Start
    
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturda ro'yhatdan o'tish! 🪪"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Mehmoh sifatidan foydalanish! 🥷🏻"), check_register))
    
    # Conversation Handler = Register
    
    register_conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text("📝 Ro'yhatdan o'tishni boshlash..!") , get_name)],
    states={
        register_states.NAME: [MessageHandler(Filters.text, set_name)],
        register_states.CONTACT: [MessageHandler(Filters.contact, set_contact)],
        register_states.CONFIRM: [
            MessageHandler(Filters.text("Tasqiqlash! ✅") , save_user),
            MessageHandler(Filters.text("Tahrirlash! ♻️") , get_name),
        ]
    },
    fallbacks = []
    )
    dispatcher.add_handler(register_conversation_handler)
    
    # Converstation Handler SEND DATE
    
    booking_station_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text("Stadion buyurtma qilish 📌") , send_date)],
        states={
            booking_station_states.DATE: [],
            booking_station_states.TIME: [],
            booking_station_states.CONFIRM: [],
            booking_station_states.PAYMENT: []
        },
        fallbacks=[]
    )
    dispatcher.add_handler(booking_station_handler)
    
    # MessageHandler 
    
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni davom ettirish! ↩️") , send_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni tugatish! 🛑") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Yordam 👮🏻‍♂️") , help))
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni tugatish ❌") , stop))
                        
    
    # MessageHandler = Guest
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()