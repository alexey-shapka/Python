import telebot
import time
import funcsql
from telebot import types

token = ''
bot = telebot.TeleBot(token)
global num

global d
d = dict()

global doc
#doc=dict()
cart=[]
cart1={}
data=funcsql.table("Врачи")
data_name=[]
for i in range(len(data)):
    data_name.append(data[i][1])
print(data_name)
@bot.message_handler(commands=['start'])
def send_welcome(m):
    markup = telebot.types.InlineKeyboardMarkup()
    idmember= bot.get_chat(m.chat.id)
    Lab2= telebot.types.InlineKeyboardButton(text='Doctor`s', callback_data="name")
    cart= telebot.types.InlineKeyboardButton(text='Cart', callback_data="cart")
    members = telebot.types.InlineKeyboardButton(text='Members', callback_data="members")
    markup.add(Lab2)
    markup.add(cart)
    #markup.add(members)
    bot.send_message(m.chat.id, "Select", reply_markup = markup)
    print(idmember)
    print(cart)

@bot.message_handler(commands=['dict'])
def send_welcome(m):
    print(cart1)
@bot.callback_query_handler(func=lambda call:True)
def inlin(call):
    global d
    global doc
    global cart
    global num
    if call.data == 'name':
            d[call.message.chat.id] = "name"
            markup = telebot.types.InlineKeyboardMarkup()
            for i in range(len(data)):
                n = telebot.types.InlineKeyboardButton(text=data[i][1], callback_data=data[i][1])
                markup.add(n)
            bot.send_message(chat_id=call.message.chat.id,text= "Doctor`s", reply_markup = markup)


    elif call.data in data_name:
        for i in range(len(data_name)):
            if data_name[i]==call.data:
                print(data[i])
                doc = data[i]
                markup = telebot.types.InlineKeyboardMarkup()
                add= telebot.types.InlineKeyboardButton(text='add to cart', callback_data="add to cart")
                markup.add(add)
                bot.send_message(chat_id=call.message.chat.id, text="Id Врача: "+str(data[i][0])+
                                                                    "\nФИО: "+str(data[i][1])+
                                                                    "\nДолжность: "+str(data[i][2])+
                                                                    "\n№ кабинета: "+str(data[i][3])+
                                                                    "\nВремя приема: "+str(data[i][4])+
                                                                    "\nВид услуг: "+str(data[i][5]), reply_markup = markup)

    elif call.data == 'add to cart':
        cart.append(doc)
        value=str(cart1.get(call.message.chat.id))

        print(value)
        #cart[call.data.id]=doc
        new=value.replace("None","")+str(doc)
        cart1[call.message.chat.id]=new

        print(cart)
        print(doc)
        bot.send_message(chat_id=call.message.chat.id, text="Doc "+doc[1]+" added to cart!")
        #d[call.message.chat.id] = "lower"
    elif call.data ==  'cart':
        markup = telebot.types.InlineKeyboardMarkup()
        remove= telebot.types.InlineKeyboardButton(text='clear cart', callback_data="remove")
        markup.add(remove)
        bot.send_message(chat_id=call.message.chat.id, text=str(cart1.get(call.message.chat.id)),reply_markup=markup)


        """if len(cart)==0:
            bot.send_message(chat_id=call.message.chat.id, text="Your cart is empty.")
        else:
            bot.send_message(chat_id=call.message.chat.id, text=str(cart), reply_markup = markup)"""

    elif call.data == 'remove':
        cart.clear()
        cart1.clear()
        bot.send_message(chat_id=call.message.chat.id, text="Your cart cleared.")

    elif call.data == 'members':

        num = bot.get_chat_members_count(chat_id=call.message.chat.id)
        bot.send_message(chat_id=call.message.chat.id, text=str(num))

@bot.message_handler(func=lambda message: True,content_types=['text'])
def handmes(message):
    global d
    if d.get(message.chat.id) == "name":
        #bot.send_message(message.chat.id, text=str(data))
        print(data)
    elif d.get(message.chat.id) == "lower":
        print(data)
        #bot.send_message(message.chat.id, text=message.text.lower())

if __name__ == '__main__':
     bot.polling(none_stop=True)

