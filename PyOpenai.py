import creds as config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from pyai import ai


TOKEN = config.conf['token_id']


async def start_commmand(update, context):
    await update.message.reply_text('Benvenuto, chiedimi quello che vuoi.')


async def all(update, context):
    testo = update.message.text
    x = ai(testo)

    await update.message.reply_text(x, parse_mode="Markdown")


if __name__ == '__main__':
    print('Starting a bot....')
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(MessageHandler(
        filters.BaseFilter(""), all))

    # Run bot
    application.run_polling(1.0)
