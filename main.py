from telegram import Update
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.first_name}')

async def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if 'hello' in text:
        response = "hello"
    if 'tiktok' in text:
        arr = text.split('?')
        if len(arr) > 0:
            response = arr[0] + '/live'
    # Reply normal if the message is in private
    await update.message.reply_text(response)

app = Application.builder().token("5967167915:AAFYOZfs01Zga_yLbyqxEz3GdjRdztfTyVA").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_message))
app.run_polling()