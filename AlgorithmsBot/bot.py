import telebot
import random
import time
import functions
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
import math
import os

token = ''
bot = telebot.TeleBot(token)

global d
d = dict()

@bot.message_handler(commands=['start'])
def send_welcome(m):
    markup = telebot.types.InlineKeyboardMarkup()

    Lab2= telebot.types.InlineKeyboardButton(text='Laboratory work 2', callback_data="lab2")
    Lab3= telebot.types.InlineKeyboardButton(text='Laboratory work 3', callback_data="lab3")
    Lab4= telebot.types.InlineKeyboardButton(text='Laboratory work 4', callback_data="lab4")
    Lab5= telebot.types.InlineKeyboardButton(text='Laboratory work 5', callback_data="lab5")
    markup.add(Lab2)
    markup.add(Lab3)
    markup.add(Lab4)
    markup.add(Lab5)
    bot.send_message(m.chat.id, "Select the number of laboratory work", reply_markup = markup)

@bot.callback_query_handler(func=lambda call:True)
def inlin(call):
    global d

    if call.data == 'lab2':
        d[call.message.chat.id] = "lab2"
        markup = telebot.types.InlineKeyboardMarkup()
        num= telebot.types.InlineKeyboardButton(text='Enter length of array for generation', callback_data="num2")
        array2 = telebot.types.InlineKeyboardButton(text='Enter array', callback_data="array2")
        file= telebot.types.InlineKeyboardButton(text='Input file', callback_data="file2")
        image= telebot.types.InlineKeyboardButton(text='Create graphic', callback_data="image2")

        markup.add(num)
        markup.add(array2)
        markup.add(file)
        markup.add(image)

        bot.send_message(chat_id=call.message.chat.id, text="Choose:", reply_markup = markup)

    elif call.data == "num2":
        bot.send_message(chat_id=call.message.chat.id, text="Input number")
        d[call.message.chat.id] = "num2"

    elif call.data == "array2":
        bot.send_message(chat_id=call.message.chat.id, text="Input array")
        d[call.message.chat.id] = "array2"

    elif call.data == "file2":
        bot.send_message(chat_id=call.message.chat.id, text="Input file")
        d[call.message.chat.id] = "file2"

    elif call.data == "image2":
        functions.lab2_graph()
        photo="GraphicAmo2.png"
        bot.send_photo(chat_id=call.message.chat.id, photo=open(photo, 'rb'))

    elif call.data == 'lab3':
        markup = telebot.types.InlineKeyboardMarkup()
        i = telebot.types.InlineKeyboardButton(text='Interpolation', callback_data="i3")
        a = telebot.types.InlineKeyboardButton(text='Accuracy', callback_data="n3")

        markup.add(i)
        markup.add(a)

        bot.send_message(chat_id=call.message.chat.id, text="Choose:", reply_markup = markup)

    elif call.data == 'i3':
        d[call.message.chat.id] = "i3"
        bot.send_message(chat_id=call.message.chat.id, text="Enter the number of dots:")

    elif call.data == 'n3':
        try:
            rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
            rcParams['font.fantasy'] = 'Times New Roman'
            facecolor = 'k'
            rcParams['figure.edgecolor'] = facecolor
            rcParams['figure.facecolor'] = facecolor
            rcParams['axes.facecolor'] = facecolor
            rcParams['grid.color'] = 'w'
            rcParams['xtick.color'] = 'w'
            rcParams['ytick.color'] = 'w'
            rcParams['axes.labelcolor'] = 'w'

            fig = plt.figure()

            l=0.1
            x = np.arange(0, 4.0001, l)
            lagranz=[]

            for i in range(2,20):
                ylagran=functions.lagrange(x,i)
                lagranz.append(ylagran)
            print(lagranz)
            print(len(lagranz))

            default=[]

            ydef=np.sin(x)**3 + 3*(np.cos(x)**2)
            print(ydef)
            for i in range(len(lagranz)):
                default.append(ydef-lagranz[i])
            print(default)
            result=[]
            for i in default:
                result.append(sum(i)/len(i))

            print(result)
            x=np.arange(2, 20, 1)
            y=result
            plt.plot(x,y, color = "red")
            plt.grid(True)
            fig.savefig('GraphicAmo3Accuracy.png', format='png', facecolor='k')
            plt.close()
            photo='GraphicAmo3Accuracy.png'
            bot.send_message(chat_id=call.message.chat.id, text="Graphic accuracy")
            bot.send_photo(chat_id=call.message.chat.id, photo=open(photo, 'rb'))

        except:
             bot.send_message(chat_id=call.message.chat.id, text="Something went wrong")

    elif call.data == "lab4":
        markup = telebot.types.InlineKeyboardMarkup()
        result= telebot.types.InlineKeyboardButton(text='Input diapason', callback_data="result4")
        graph= telebot.types.InlineKeyboardButton(text='Create graphic', callback_data="graph4")
        markup.add(graph)
        markup.add(result)
        bot.send_message(chat_id=call.message.chat.id, text="Choose:", reply_markup = markup)

    elif call.data == 'result4':
        d[call.message.chat.id] = "result4"
        bot.send_message(chat_id=call.message.chat.id, text="Enter diapason and accuracy")

    elif call.data == 'graph4':
        functions.lab4_graph()
        photo="GraphicAmo4.png"
        bot.send_photo(chat_id=call.message.chat.id, photo=open(photo, 'rb'))

    elif call.data == 'lab5':
        markup = telebot.types.InlineKeyboardMarkup()
        cmatrix= telebot.types.InlineKeyboardButton(text='Variant matrix', callback_data="complete5")
        imatrix= telebot.types.InlineKeyboardButton(text='Input matrix', callback_data="input5")
        markup.add(cmatrix)
        markup.add(imatrix)
        bot.send_message(chat_id=call.message.chat.id, text="Choose:", reply_markup = markup)

    elif call.data == "complete5":
        var = [[4,2,-1,1], [5,3,-2,2], [3,2,-3,0]]
        complete = functions.Lab5(var,1.5,0.0001)

        bot.send_message(chat_id=call.message.chat.id, text="Matrix\n"+str(var[0][0:3])+"="+str(var[0][3])+"\n"
                         +str(var[1][0:3])+ " = " +str(var[1][3])+"\n"
                         +str(var[2][0:3])+ " = " +str(var[2][3])+"\n")

        bot.send_message(chat_id=call.message.chat.id, text="Result\n"+
                                                            "X1 = "+str(complete[0])+
                                                            "\nX2 = "+str(complete[1])+
                                                            "\nX3 = "+str(complete[2])+'.')

    elif call.data == "input5":
        d[call.message.chat.id] = "input5"
        bot.send_message(chat_id=call.message.chat.id, text="Enter the matrix:")


@bot.message_handler(func=lambda message: True,content_types=['text'])
def handmes(message):
    global d
    if d.get(message.chat.id) == "num2":
        try:
            b = message.text
            print(b)
            number = int(b)
            print(number)
            list = [random.randint(1,100) for i in range(number)]
            if number<=10000000:
                bot.send_message(message.chat.id, "Please wait, your array is sorting...")
                not_sort = list.copy()
                start_time = time.time()
                functions.mergeSort(list)
                time.sleep(0.0000001)
                end_time = time.time()

                print(list)

                if number<=1000:
                    bot.send_message(message.chat.id, str(not_sort))
                    bot.send_message(message.chat.id, "Sorted list\n"+str(list))
                    bot.send_message(message.chat.id, "Time: "+str(end_time-start_time-0.0000001))

                else:
                    file = open("Result_lab2.txt", "w")
                    file.write("Sort list\n"+str(list)+"\nTime\n"+str(end_time-start_time-0.0000001))
                    file.close()
                    bot.send_document(message.chat.id, open("Result_lab2.txt",'rb'))
            else:
                approximatelytime = math.ceil(number/83334)

                bot.send_message(message.chat.id, "Please wait, your array is sorting...\n"
                                                              "Approximate time of sorting and sending: " + str(approximatelytime)+"sec.")
                start_time = time.time()
                functions.mergeSort(list)
                time.sleep(0.0000001)
                end_time = time.time()
                parts = math.ceil(number/10000000)

                print(parts)


                complete_list = functions.chunkIt(list, parts)

                for i in range(parts):
                    if i==0:
                        file = open("Result_lab2_part"+str(i+1)+".txt", "w")
                        file.write("Sort list\n"+str(complete_list[i]))
                        file.close()
                    elif i==parts-1:
                        file = open("Result_lab2_part"+str(i+1)+".txt", "w")
                        file.write(str(complete_list[i])+"\nTime: "+str(end_time-start_time-0.0000001))
                        file.close()
                    else:
                        file = open("Result_lab2_part"+str(i+1)+".txt", "w")
                        file.write(str(complete_list[i]))
                        file.close()
                for i in range(parts):
                    bot.send_document(message.chat.id, open("Result_lab2_part"+str(i+1)+".txt", 'rb'))

        except:
            bot.send_message(message.chat.id, "Something went wrong😔\nTry again.")

    elif d.get(message.chat.id) == 'array2':
        try:
            b = message.text
            strb = str(b)
            list=strb.split()
            intlist=[]
            for i in list:
                intlist.append(int(i))
            print(intlist)
            start_time = time.time()
            functions.mergeSort(intlist)
            time.sleep(0.0000001)
            end_time = time.time()-start_time
            bot.send_message(message.chat.id, str(intlist))
            bot.send_message(message.chat.id, "Time: "+str(end_time))

        except:
            bot.send_message(chat_id=message.chat.id, text="Incorrect array!")

    elif d.get(message.chat.id) == 'i3':
        try:
            dots = message.text
            dotsint = int(dots)

            rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
            rcParams['font.fantasy'] = 'Times New Roman'
            facecolor = 'k'
            rcParams['figure.edgecolor'] = facecolor
            rcParams['figure.facecolor'] = facecolor
            rcParams['axes.facecolor'] = facecolor
            rcParams['grid.color'] = 'w'
            rcParams['xtick.color'] = 'w'
            rcParams['ytick.color'] = 'w'
            rcParams['axes.labelcolor'] = 'w'

            fig = plt.figure()
            lag = 4/dotsint
            x_lag_new = np.arange(0, 4, lag)
            y_lag = functions.lagrange(x_lag_new,10)
            lag1=0.02
            x_def=np.arange(0,4,lag1)
            y_def = np.sin(x_def)**3 + 3*(np.cos(x_def)**2)

            plt.plot(x_lag_new,y_lag, color = "red")
            plt.plot(x_def, y_def,color = "white")

            plt.text(0.55, 2.8, r'Interpolation Lagrange - red line', fontsize=14, color="yellow")
            plt.grid(True)
            fig.savefig('GraphicAmo3lagrange.png', format='png', facecolor='k')
            plt.close()


            rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
            rcParams['font.fantasy'] = 'Times New Roman'
            facecolor = 'k'
            rcParams['figure.edgecolor'] = facecolor
            rcParams['figure.facecolor'] = facecolor
            rcParams['axes.facecolor'] = facecolor
            rcParams['grid.color'] = 'w'
            rcParams['xtick.color'] = 'w'
            rcParams['ytick.color'] = 'w'
            rcParams['axes.labelcolor'] = 'w'

            fig1 = plt.figure()
            y_new=functions.newton(x_lag_new,10)
            plt.plot(x_lag_new,y_new, color = "red")
            plt.plot(x_def, y_def,color = "white")

            plt.text(0.55, 2.8, r'Interpolation Newton - red line', fontsize=14, color="yellow")
            plt.grid(True)
            fig1.savefig('GraphicAmo3newton.png', format='png', facecolor='k')
            plt.close()

            rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
            rcParams['font.fantasy'] = 'Times New Roman'
            facecolor = 'k'
            rcParams['figure.edgecolor'] = facecolor
            rcParams['figure.facecolor'] = facecolor
            rcParams['axes.facecolor'] = facecolor
            rcParams['grid.color'] = 'w'
            rcParams['xtick.color'] = 'w'
            rcParams['ytick.color'] = 'w'
            rcParams['axes.labelcolor'] = 'w'

            fig2 = plt.figure()
            ydefsin = np.sin(x_def)
            ysin = functions.lagrange_sin(x_lag_new,10)
            plt.plot(x_lag_new,ysin, color = "red")
            plt.plot(x_def, ydefsin,color = "white")

            plt.text(0.55, -0.15, r'Interpolation sin(x) - red line', fontsize=14, color="yellow")
            plt.grid(True)
            fig2.savefig('GraphicAmo3sinLagrange.png', format='png', facecolor='k')
            plt.close()

            photo="GraphicAmo3lagrange.png"
            photo1='GraphicAmo3newton.png'
            photo2='GraphicAmo3sinLagrange.png'

            bot.send_message(chat_id=message.chat.id, text="Interpolations")
            bot.send_photo(chat_id=message.chat.id, photo=open(photo, 'rb'))
            bot.send_photo(chat_id=message.chat.id, photo=open(photo1, 'rb'))
            bot.send_photo(chat_id=message.chat.id, photo=open(photo2, 'rb'))

        except:
            bot.send_message(chat_id=message.chat.id, text="Incorrect input")

    elif d.get(message.chat.id) == 'result4':
        try:
            b = message.text
            strb=str(b)
            num = strb.split()
            bot.send_message(message.chat.id,"Result\n"+str(functions.lab4_alg(float(num[0]),float(num[1]),float(num[2]))))

        except:
            bot.send_message(message.chat.id, "Input numbers!")

    elif d.get(message.chat.id) == 'input5':
        try:
            b = message.text
            strb=str(b)
            arrstrb=strb.split()
            lstr=""
            for i in strb:
                if i =="\n":
                    break
                lstr+=i
            matrixlen = len((lstr.split()))-1
            intmat=[]
            for i in arrstrb:
                intmat.append(int(i))
            matrix = functions.chunkIt(intmat, matrixlen)
            a=[]
            b=[]
            for i in matrix:
                a.append(i[0:matrixlen])
                b.append(i[matrixlen])
            print(a)
            print(b)
            x=np.linalg.solve(a,b)
            xcomplete=[]
            for i in x:
                xcomplete.append(i)

            complete = functions.Lab5(matrix,1.25,0.001)
            print(xcomplete)
            bot.send_message(chat_id=message.chat.id, text="Matrix\n"+str(matrix[0:len(matrix)][0:(len(matrix[0])-1)]))
            bot.send_message(chat_id=message.chat.id, text="Result\n"+str(xcomplete))
            """ +" = "+str(matrix[0][len(matrix[0])-1])+"\n"
                         +str(matrix[1][0:(len(matrix[0])-1)])+ " = " +str(matrix[1][len(matrix[0])-1])+"\n"
                         +str(matrix[2][0:(len(matrix[0])-1)])+ " = " +str(matrix[2][len(matrix[0])-1])+"\n")
                                                            "X1 = "+str(complete[0])+
                                                            "\nX2 = "+str(complete[1])+
                                                            "\nX3 = "+str(complete[2])+'.')"""

        except:
            bot.send_message(chat_id=message.chat.id, text="Incorrect matrix")


@bot.message_handler(content_types=['document'])
def docs(message):
    global d
    if d[message.chat.id] == "file2":
        #try:
            file = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file.file_path)
            name=message.document.file_name
            src = 'E:/KPI/Python/' + name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            result_file = open(name, "r")
            line = result_file.readlines()

            for i in line:
                if i == "\n" or i == " ":
                    line.remove(i)


            line_complete = [l.rstrip().split() for l in line]
            numbers=[]

            for i in line_complete:
                for j in i:
                    if j != " ":
                        numbers.append(int(j))
            print(numbers)
            not_sort = numbers.copy()
            start_time = time.time()
            functions.mergeSort(numbers)
            time.sleep(0.0000001)
            end_time = time.time()
            file_result = open(message.document.file_name, "w")
            file_result.write("Sort list\n"+str(numbers)+"\nTime\n"+str(end_time-start_time-0.0000001))
            file_result.close()
            bot.send_document(message.chat.id, open(message.document.file_name,'rb'))

            bot.send_message(message.chat.id, str(not_sort))
            bot.send_message(message.chat.id, "Sort list\n"+str(numbers))
            bot.send_message(message.chat.id, "Time: "+str(end_time-start_time-0.0000001))
            result_file.close()
            new_file.close()
            os.remove(src)
        #except(ValueError):
            #bot.send_message(chat_id=message.chat.id, text="Incorrect data in file!")

        #except:
            #bot.send_message(chat_id=message.chat.id, text="Incorrect format file!")

if __name__ == '__main__':
     bot.polling(none_stop=True)
