import sentiment_analysis

def start(bot, update):
    update.message.reply_text('Olá, seja bem vindo!\nPara pedir ajuda: /help')

def help_bot(bot, update):
    update.message.reply_text('Help!')

def sentiment(bot, update):
    msg = update.message.text
    prediction = sentiment_analysis.predict(msg)
    update.message.reply_text(prediction)

def sofrer(bot, update):
    update.message.reply_text('Aula no lab 17')