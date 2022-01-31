#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import requests
import os

from flask import Flask, request
from telebot import types

class User:
    def __init__(self, name):
        self.id = None

bot_token = '5111881778:AAF7-JkmSzGSlg8Hu_9vRpwTJ6aCLaWialE'
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

# BOT - START
@bot.message_handler(commands=['start'])
def send_welcome(message):
    userID = message.from_user.id
    UserFirst = message.from_user.first_name
    btn1 = types.InlineKeyboardButton("🇵🇹 PORTUGAL", callback_data='grupo')
    btn2 = types.InlineKeyboardButton("🇧🇷 BRASIL", callback_data='informacao')
    markup = types.InlineKeyboardMarkup(row_width=2)            
    markup.add(btn1,btn2)
    bot.send_message(userID, "<b>✅ Bem-Vindo, {}</b>" .format(UserFirst) + "<b> ! ✅</b>", parse_mode="HTML")
    bot.send_message(userID, "🗣 <b>Olá !</b> Sou o Bot do grupo <b>GreenBookTips</b>, fui criado para facilitar a tua entrada no nosso Grupo VIP, segue todos os passos para poderes entrar no grupo e ganhar connosco !\n\n"
                             "🍀 <b>Grupo de Apostas Desportivas</b>, especializado em: ⚽️🎾🏀\n\n"
                             '👉 <b>Grupo:</b> <a href="https://t.me/joinchat/AAAAAFQ9n54109kt-txTXQ">GreenBookTips FREE</a>\n'
                             "❓ <b>Qualquer Dúvida:</b> @TipsGreenBook\n\n"
                             "👍 Caso estejas interessado em entrar no nosso grupo carrega em GRUPO VIP e escolhe o teu plano de subscrição !\n"
                             "❗️ <b>Se precisares de ajuda enquanto usas o Bot faz:</b> /help"
                             , reply_markup=markup, parse_mode="HTML")

# BOT - GRUPO
@bot.callback_query_handler(lambda q: q.data == 'grupo')
def grupo(message):
    btn1 = types.InlineKeyboardButton("Plano 1", callback_data='vip1')
    btn2 = types.InlineKeyboardButton("Plano 2", callback_data='vip2')
    btn3 = types.InlineKeyboardButton("Plano 3", callback_data='vip3')
    btn4 = types.InlineKeyboardButton("Plano 4", callback_data='vip4')
    markup = types.InlineKeyboardMarkup(row_width=4)            
    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.from_user.id, "👉 <b>Escolhe o teu Plano de Subscrição no nosso Grupo VIP:</b>\n\n"
                                           "🔺 <b>Plano 1</b> - 10€ / 1Mês\n"
                                           "🔺 <b>Plano 2</b> - 18€ / 2Meses\n"
                                           "🔺 <b>Plano 3</b> - 25€ / 3Meses\n"
                                           "🔺 <b>Plano 4</b> - 45€ / 6Meses\n"
                                           , reply_markup=markup, parse_mode="HTML")
    
@bot.callback_query_handler(lambda q: q.data == 'vip1')
def vip1(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    btn1 = types.InlineKeyboardButton("Multibanco", callback_data='mb')
    btn2 = types.InlineKeyboardButton("Neteller", callback_data='nt')
    btn3 = types.InlineKeyboardButton("PayPal", callback_data='pp')
    markup = types.InlineKeyboardMarkup(row_width=3)            
    markup.add(btn1,btn2,btn3)
    bot.send_message(userID, "▶️ Escolheste o <b>Plano de Subscrição 1</b>\n\n"
                             "📣 <b>Benefícios do Grupo VIP:</b>\n"
                             "🔺 Apostas Diárias\n"
                             "🔺 Apostas Live\n"
                             "🔺 Apostas Pré-Live\n"
                             "🔺 Challenges || Raspadinhas\n\n"
                             "<b>Total:</b> 10€ - 1 Mês\n\n"
                             "👉 <b>Escolhe o Método de pagamento para efetuares o pagamento:</b>",reply_markup=markup, parse_mode="HTML")
    bot.send_message("375387984", "<b>==========\n  ENTRADA \n ==========\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>1Mes | 10€</b>",parse_mode="HTML")

@bot.callback_query_handler(lambda q: q.data == 'vip2')
def vip2(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    btn1 = types.InlineKeyboardButton("Multibanco", callback_data='mb')
    btn2 = types.InlineKeyboardButton("Neteller", callback_data='nt')
    btn3 = types.InlineKeyboardButton("PayPal", callback_data='pp')
    markup = types.InlineKeyboardMarkup(row_width=3)            
    markup.add(btn1,btn2,btn3)
    bot.send_message(userID, "▶️ Escolheste o <b>Plano de Subscrição 2</b>\n\n"
                             "📣 <b>Benefícios do Grupo VIP:</b>\n"
                             "🔺 Apostas Diárias\n"
                             "🔺 Apostas Live\n"
                             "🔺 Apostas Pré-Live\n"
                             "🔺 Challenges || Raspadinhas\n\n"
                             "<b>Total:</b> 18€ - 2 Meses\n\n"
                             "👉 <b>Escolhe o Método de pagamento para efetuares o pagamento:</b>",reply_markup=markup, parse_mode="HTML")
    bot.send_message("375387984","<b>==========\n  ENTRADA \n ==========\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>2Meses | 18€</b>",parse_mode="HTML")

@bot.callback_query_handler(lambda q: q.data == 'vip3')
def vip3(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    btn1 = types.InlineKeyboardButton("Multibanco", callback_data='mb')
    btn2 = types.InlineKeyboardButton("Neteller", callback_data='nt')
    btn3 = types.InlineKeyboardButton("PayPal", callback_data='pp')
    markup = types.InlineKeyboardMarkup(row_width=3)            
    markup.add(btn1,btn2,btn3)
    bot.send_message(userID, "▶️ Escolheste o <b>Plano de Subscrição 3</b>\n\n"
                             "📣 <b>Benefícios do Grupo VIP:</b>\n"
                             "🔺 Apostas Diárias\n"
                             "🔺 Apostas Live\n"
                             "🔺 Apostas Pré-Live\n"
                             "🔺 Challenges || Raspadinhas\n\n"
                             "<b>Total:</b> 25€ - 3 Meses\n\n"
                             "👉 <b>Escolhe o Método de pagamento para efetuares o pagamento:</b>",reply_markup=markup, parse_mode="HTML")
    bot.send_message("375387984","<b>==========\n  ENTRADA \n ==========\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>3Meses | 25€</b>",parse_mode="HTML")

@bot.callback_query_handler(lambda q: q.data == 'vip4')
def vip4(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    btn1 = types.InlineKeyboardButton("Multibanco", callback_data='mb')
    btn2 = types.InlineKeyboardButton("Neteller", callback_data='nt')
    btn3 = types.InlineKeyboardButton("PayPal", callback_data='pp')
    markup = types.InlineKeyboardMarkup(row_width=3)            
    markup.add(btn1,btn2,btn3)
    bot.send_message(userID,"▶️ Escolheste o <b>Plano de Subscrição 4</b>\n\n"
                             "📣 <b>Benefícios do Grupo VIP:</b>\n"
                             "🔺 Apostas Diárias\n"
                             "🔺 Apostas Live\n"
                             "🔺 Apostas Pré-Live\n"
                             "🔺 Challenges || Raspadinhas\n\n"
                             "<b>Total:</b> 45€ - 6 Meses\n\n"
                             "👉 <b>Escolhe o Método de pagamento para efetuares o pagamento:</b>",reply_markup=markup, parse_mode="HTML")
    bot.send_message("375387984","<b>==========\n  ENTRADA \n ==========\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>6Meses | 45€</b>",parse_mode="HTML")

# BOT - PAGAMENTO
@bot.callback_query_handler(lambda q: q.data == 'mb')
def mb(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    bot.send_message(userID, "▶️ Escolheste o <b>Método de Pagamento por Multibanco</b>\n\n"
                             "👉 <b>O teu Pedido esta agora ser processado...</b>\n\n"
                             "👇 Aguarda pela minha mensagem com os dados para efetuares o teu pagamento:\n"
                             ,parse_mode="HTML")
    bot.send_message("375387984","<b>=============\n  PAGAMENTO \n =============\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>Multibanco</b>",parse_mode="HTML")

@bot.callback_query_handler(lambda q: q.data == 'nt')
def nt(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    bot.send_message(userID, "▶️ Escolheste o <b>Método de Pagamento por Neteller</b>\n\n"
                             "👉 Agora faz o teu pagamento para o email: <b>fryzenn@gmail.com</b>\n\n"
                             "👇 Assim que fizeres o pagamento envia um <b>comprovativo de pagamento</b> para:\n"
                             "@TipsGreenBook"
                             ,parse_mode="HTML")
    bot.send_message("375387984","<b>=============\n  PAGAMENTO \n =============\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + u" || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>Neteller</b>",parse_mode="HTML")

@bot.callback_query_handler(lambda q: q.data == 'pp')
def pp(message):
    userID = message.from_user.id
    userNome = message.from_user.username
    UserFirst = message.from_user.first_name
    userLast = message.from_user.last_name
    bot.send_message(userID, "▶️ Escolheste o <b>Método de Pagamento por PayPal</b>\n\n"
                             "👉 Agora faz o teu pagamento para o email: <b>fryzenn1@gmail.com</b>\n\n"
                             "👇 Assim que fizeres o pagamento envia um <b>comprovativo de pagamento</b> para:\n"
                             "@TipsGreenBook"
                             ,parse_mode="HTML")
    bot.send_message("375387984","<b>=============\n  PAGAMENTO \n =============\n</b> -> <b>ID:</b> {}" .format(userID) + " || <b>Username:</b> @{}\n" .format(userNome) + 
                     "-> <b>First Name:</b> {}" .format(UserFirst) + " || <b>Last Name:</b> {}\n" .format(userLast) + 
                     "-> <b>PayPal</b>",parse_mode="HTML")

# BOT - INFORMACAO
@bot.callback_query_handler(lambda q: q.data == 'informacao')
def informacao(message):
    bot.send_message(message.from_user.id,"<b>GreenBookTips</b> - Aberto desde <b>24/08</b>\n\n"
                                          "🍀 <b>Grupo Free:</b>\n"
                                          "👉 <b>1º Mês(24/09) - +106€</b>\n"
                                          "️▶️ 1 Semana: <b>+38€ | 138€</b>\n"
                                          "️▶️ 2 Semana: <b>+72€ | 210€</b>\n"
                                          "️▶️ 3 Semana: <b>+32€ | 242€</b>\n"
                                          "▶️ 4 Semana: <b>-34€ | 208€</b>\n", parse_mode="HTML")

# BOT - MANAGEMENT
@bot.message_handler(commands=['managementsend'])
def management(message):
    msg = bot.reply_to(message, '👉 Insere o ID do User: ')
    bot.register_next_step_handler(msg, process_envio)

def process_envio(message):
    User.id = message.text
    msg = message.text
    if not msg.isdigit():
        bot.send_message(message.from_user.id, "👉 Inseriste um ID errado, faz /managementsend e tenta denovo")
        return
    msg = bot.reply_to(message, '👉 Que mensagem queres enviar para o ID: {}'.format(User.id))
    bot.register_next_step_handler(msg, process_send_final)

def process_send_final(message):
    bot.send_message(User.id, message.text)
    bot.send_message(message.from_user.id, "<b>MENSAGEM ENVIADA COM SUCESSO !!</b>", parse_mode='HTML')

# BOT - COMANDO ERROR
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    bot.send_message(message.from_user.id, "<b>⚠️ Oooops !</b>\n"
                                           "👉 Comando Inexistente, tenta: /help", parse_mode="HTML")

# BOT - FLASK|HEROKU
@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://greenbooktipsbot.herokuapp.com/' + bot_token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

bot.polling()