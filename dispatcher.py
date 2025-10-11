from config import config , register_states , booking_station_states
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , ConversationHandler, CallbackQueryHandler
from app.commands import start , stop , send_group_link
from app.helps import help , bot_error , order_error
from app.check_user import check_register
from app.register import get_name , set_name , set_contact , save_user
from database import engine , Base
from app.menus import send_menu
from app.date import send_date , handle_confirmation , handle_date_selection , handle_payment, handle_time_selection , back_to_date , back_to_time , cancel
from app.profile import profile
from Guest.menu import send_guest_menu
from Guest.stadium_order import order
#from app.booking import handle_date , handle_time , handle_confirm

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
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tganman! ✅"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Mehmoh sifatidan foydalanish! 🥷🏻"), send_guest_menu))
    
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
    
    #booking_station_handler = ConversationHandler(
    #    entry_points=[MessageHandler(Filters.text("Stadion buyurtma qilish 📌") , send_date)],
    #    states={
    #        booking_station_states.DATE: [],
    #        booking_station_states.TIME: [],
    #        booking_station_states.CONFIRM: [],
    #        booking_station_states.PAYMENT: []
    #    },
    #    fallbacks=[]
    #)
    #dispatcher.add_handler(booking_station_handler)
    
    # MessageHandler 
    
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni davom ettirish! ↩️") , send_menu))
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni tugatish! 🛑") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Yordam 👮🏻‍♂️") , help))
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni tugatish ❌") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Bot gruhiga qo'shilish! 💡"), send_group_link))
    dispatcher.add_handler(MessageHandler(Filters.text("Profilim 👤"), profile))
    dispatcher.add_handler(MessageHandler(Filters.text("Bot kamchiliklari! 👾"), bot_error))
    dispatcher.add_handler(MessageHandler(Filters.text("Buyurtmada muammolar! 🥡"), order_error))
    dispatcher.add_handler(MessageHandler(Filters.text("Boshqa muammo 🚧"), bot_error))
    
    # MessageHandler = Guest
    dispatcher.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tish! 🪪"), check_register))
    dispatcher.add_handler(MessageHandler(Filters.text("Stadion buyurtmasi 📌"), order))
    
    booking_station_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.text("Stadion buyurtma qilish 📌"), send_date)
    ],
    states={
        booking_station_states.DATE: [
            CallbackQueryHandler(handle_date_selection, pattern="^date:"),
            CallbackQueryHandler(cancel, pattern="^cancel$")
        ],
        booking_station_states.TIME: [
            CallbackQueryHandler(handle_time_selection, pattern="^time:"),
            CallbackQueryHandler(back_to_date, pattern="^back_to_date$"),
            CallbackQueryHandler(cancel, pattern="^cancel$")
        ],
        booking_station_states.CONFIRM: [
            CallbackQueryHandler(handle_confirmation, pattern="^confirm_yes$"),
            CallbackQueryHandler(back_to_time, pattern="^back_to_time$"),
            CallbackQueryHandler(cancel, pattern="^cancel$")
        ],
        booking_station_states.PAYMENT: [
            CallbackQueryHandler(handle_payment, pattern="^pay_"),
            CallbackQueryHandler(cancel, pattern="^cancel$")
        ]
    },
    fallbacks=[
        CallbackQueryHandler(cancel, pattern="^cancel$"),
        MessageHandler(Filters.text("❌ Bekor qilish"), cancel)
    ],
    per_message=False ) # Warning ni yo'qotish uchun
    dispatcher.add_handler(booking_station_handler)
    
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__":
    main()