import re
import json
import sentiment_analysis
import aulasdml
from pathlib import Path

CONFIG_PATH = str(Path(__file__).parents[1]) + '/config/config.json'

def start(bot, update):
    if update.message.chat.type == 'private':
        update.message.reply_html('Olá, seja bem vindo!\nPara pedir ajuda: <b>/help</b>')

def help_bot(bot, update):
    update.message.reply_html('Help!')

def sentiment(bot, update):
    insensitive_sentiment = re.compile('/sentiment', re.IGNORECASE)
    user_msg = insensitive_sentiment.sub('', update.message.text)

    if len(user_msg) != 0: 
        prediction = sentiment_analysis.predict(user_msg)
        update.message.reply_html(prediction)
    else:
        update.message.reply_html('[INFO] Favor escrever algo para analisar, <b>Trouxa!</b>')

def sofrer(bot, update):
    user_msg = update.message.text

    if user_msg.lower() == '/hoje':
        msg = aulasdml.read()[0]
        update.message.reply_html(msg)
    else:
        with open(CONFIG_PATH) as config:
            config_json = json.loads(config.read())

        if update.message.from_user.id in config_json['admins']:
                insensitive_hoje = re.compile('/hoje ', re.IGNORECASE)
                user_msg = insensitive_hoje.sub('', update.message.text)
                aulasdml.create(user_msg)
                update.message.reply_html('[INFO] <b>Tristeza adicionada com sucesso!</b>')
        else:
            update.message.reply_html('[INFO] Você não é admin, <b>Trouxa!</b>')