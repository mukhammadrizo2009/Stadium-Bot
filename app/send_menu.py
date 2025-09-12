from telegram import Update
from telegram.ext import CallbackContext

def user_already_register(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Siz ro'yhatdan o'tgan ekansiz! 💡\n\n"\
            "📃 Sahifalardan birini tanlashingiz mumkin! ",
        parse_mode = "markdown",
    )