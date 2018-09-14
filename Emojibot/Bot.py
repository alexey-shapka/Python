import telebot
import letters
import time
token = '497885659:AAENUo0GELAyDn0HB5El3x7CZ_0Afoj6U08'
bot = telebot.TeleBot(token)

bot.send_message(chat_id=192348836,text='123')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    sentence = []
    b = message.text
    a = b.replace(' ', '')
    sentence.append(a)
    if len(sentence[0]) < 3:
        bot.send_message(message.chat.id, "Друг, а ты походу долбоёб.\n"
                                          "Нужно ввести как минимум 3 символа (два последних задают отрисовку букв).")
    elif a:
        a = [a[0:len(a)-2]]
        symbols=[]
        for i in sentence[0]:
            symbols.append(i)

        print(symbols)

        print(sentence)
        if symbols[-1] == '️' and symbols[-3] == '️':
            s = [symbols[-2], symbols[-4]]
        elif symbols[-1] == '️':
            s = [symbols[-2], symbols[-3]]
        elif symbols[-2] == '️':
            s = [symbols[-1], symbols[-3]]
        elif (ord(symbols[-1])> 127461 and ord(symbols[-1])<127488) and  (ord(symbols[-3])> 127461 and ord(symbols[-3])<127488):
            s = [str(symbols[-2])+str(symbols[-1]), str(symbols[-4]+str(symbols[-3]))]
        elif (ord(symbols[-3])> 127461 and ord(symbols[-3])<127488):
            s = [symbols[-1], str(symbols[-3])+str(symbols[-2])]
        elif (ord(symbols[-2])> 127461 and ord(symbols[-2])<127488):
            s = [str(symbols[-2])+str(symbols[-1]),symbols[-3]]
        else:
            s = [symbols[-1] , symbols[-2]]
        print(s)
        print(a[0])

        complete_words = []

        exceptions = ['[', "'", '.', ',', '!', '№', ';', '%', ':', '?', '@', '$', '^', '*', '&', '(', ')', '_', '+', ']', '+', '"', " ",' ']
        for i in a[0]:
            if i in exceptions:
                i.replace(i, "")
            elif ord(i)>1039 and ord(i)<1106:
                complete_words.append(i.lower())
        print(complete_words)
        for i in complete_words:
            ret = alph.repl(i,s[0],s[1])
            bot.send_message(message.chat.id, ret)

if __name__ == '__main__':
     bot.polling(none_stop=True)
