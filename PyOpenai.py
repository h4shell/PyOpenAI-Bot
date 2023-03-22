import creds as config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from pyai import ai


TOKEN = config.conf['token_id']


async def start_commmand(update, context):
    await update.message.reply_text('**Benvenuto/a sono ChatGPT 3.5 Chiedimi quello che vuoi!!!**', parse_mode="Markdown")


async def all(update, context):
    testo = update.message.text
    x = ai(testo)

    parti = len(x)/4000
    parti = int(str(parti)[0])
    if parti <= 1:

        await update.message.reply_text(x, parse_mode="Markdown")
    elif parti > 1 and parti < 2:

        testo = {0: x[:4000], 1: x[4000:]}
        print(testo[0])
        await update.message.reply_text(testo[0], parse_mode="Markdown")
        await update.message.reply_text(testo[1], parse_mode="Markdown")
        pass
    elif parti > 2 and parti <= 3:

        testo = {0: x[:4000], 1: x[4000:8000], 2: x[8000:12000]}
        await update.message.reply_text(testo[0], parse_mode="Markdown")
        await update.message.reply_text(testo[1], parse_mode="Markdown")
        await update.message.reply_text(testo[2], parse_mode="Markdown")
    else:
        print("ERROR!! Risposta troppo lunga")

        # if len(x) < 4000:
        #     print(len(x))
        #     await update.message.reply_text(x, parse_mode="Markdown")
        # else:
        #     mex1 = x[:4095]
        #     mex2 = x[4095:]
        #     await update.message.reply_text(mex1, parse_mode="Markdown")
        #     await update.message.reply_text(mex2, parse_mode="Markdown")


if __name__ == '__main__':
    print('Starting a bot....')
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(CommandHandler('ai', start_commmand))
    application.add_handler(MessageHandler(
        filters.BaseFilter(""), all))

    # Run bot
    application.run_polling(1.0)
