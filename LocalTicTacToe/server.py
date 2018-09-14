import socket
import random
import sqlconnect

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)

choices = []
dict={}


global player

def connectfunc(clients,nameclients):
    global dict
    print("Wait players")
    while len(clients)<2:
        conn, addr = sock.accept()
        conn.setblocking(1)
        data = str(conn.recv(1024).decode())
        logpas=data.split()

        if data == 'records':
            sqllog=sqlconnect.table("xo")
            st=''
            for i in range(len(sqllog)):
                if int(sqllog[i][3])==0:
                    winr = int(sqllog[i][2])/1*100
                    winr = '{:.2f}'.format(winr)
                else:
                    winr = int(sqllog[i][2])/int(sqllog[i][3])*100
                    winr = '{:.2f}'.format(winr)
                st+=" "+str(sqllog[i][0])+" "+str(sqllog[i][2]) + " " + winr
            conn.send(st.encode())

        elif "con" in data:
            sqllog=sqlconnect.table("xo")
            print("table: "+str(sqllog))
            print("datalog: "+str(logpas))
            count=0
            for i in range(len(sqllog)):
                if sqllog[i][0]==logpas[1]:
                    if sqllog[i][1]==logpas[2]:
                        print('connected:', addr)
                        if addr[0] not in clients:
                            clients.append(addr[0])
                            nameclients.append(logpas[1])
                        conn.send('go'.encode())
                        count+=1
                        pass

                    else:
                        conn.send("incorrect".encode())
                        count+=1
                        pass
                elif count == 0 and i+1 == len(sqllog):
                    sqlconnect.add(logpas[1], logpas[2])
                    print('connected:', addr)
                    if addr[0] not in clients:
                        clients.append(addr[0])
                        nameclients.append(logpas[1])
                    conn.send('create'.encode())


        if len(clients)!=2 or data == 'up':
            conn.send("wait".encode())
        conn.close()

    dict = create_dict(clients, nameclients)

def clean_and_create():
    global player
    choices.clear()
    for x in range (0, 9) :
        choices.append(str(x + 1))
    player=0

clean_and_create()


def create_dict(clients, nameclients):
    dict = {clients[0]:nameclients[0], clients[1]:nameclients[1]}
    return dict

clients=[]
nameclients=[]


connectfunc(clients,nameclients)
print(clients)
print(nameclients)
print("Dictionary: "+str(dict))
print('Players ready.')

random.shuffle(clients)
print("After shuffle clients: "+ str(clients))

turns=clients[0]

win=False

breaker = ''

while 2:
    conn, addr = sock.accept()
    data = str(conn.recv(1024).decode())

    if data == '':
            pass

    elif data == 'up':
        send= choices.copy()
        strsend=''
        for i in send:
            if i =='X':
                strsend+='1'
            elif i =='O':
                strsend+='2'
            else:
                strsend+='0'

        if len(nameclients)!=0:
            if dict.get(addr[0]) == nameclients[0]:
                strsend+= " " + str(len(clients))+ " " + nameclients[1]
            else:
                strsend+=" " + str(len(clients))+ " " + nameclients[0]
        else:
            strsend+=" " + str(len(clients))

        if breaker!=addr[0]:
            conn.send(strsend.encode())
        else:
            pass

        #if len(clients) == 0:
            #break

    elif data == 'exit':
        print('connected:', addr, "turn: ",turns, 'data: ', data)
        clients.clear()
        breaker=addr[0]
        print("exit: "+ str(clients))
        choices.clear()
        nameclients.clear()
        clean_and_create()
        print(clients)

        #connectfunc(clients, nameclients)


    elif data == 'records':
        sqllog=sqlconnect.table("xo")
        st=''
        for i in range(len(sqllog)):
            if int(sqllog[i][3])==0:
                winr = int(sqllog[i][2])/1*100
                winr = '{:.2f}'.format(winr)
            else:
                winr = int(sqllog[i][2])/int(sqllog[i][3])*100
                winr = '{:.2f}'.format(winr)
            st+=" "+str(sqllog[i][0])+" "+str(sqllog[i][2]) + " " + winr
        conn.send(st.encode())

    elif data == 'reset':
            print('connected:', addr, "turn: ",turns, 'data: ', data)
            print(choices)
            #res=addr[0]
            #while 1:
            clean_and_create()
            print(choices)
    else:
        if turns == addr[0]:
                print('connected:', addr, "turn: ",turns, 'data: ', data)
                turn=int(data)
                if choices[turn - 1] == 'X' or choices [turn-1] == 'O':
                    conn.send("error".encode())
                    print(choices)
                    continue

                pplayer=0
                win=False
                print(player)

                if player%2!=1:
                    choices[turn-1]='X'
                    if turns !=clients[1]:
                        turns=clients[1]
                    else:
                        turns = clients[0]
                    pplayer=1
                else:
                    choices[turn-1]='O'
                    if turns !=clients[1]:
                        turns=clients[1]
                    else:
                        turns = clients[0]
                    pplayer=2

                print(choices)
                for x in range (0, 3) :
                    y = x * 3
                    if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                        conn.send('win'.encode())
                        clean_and_create()
                        win=True
                        print(dict.get(addr[0]))

                        record = sqlconnect.getwins(dict.get(addr[0]))
                        record+=1
                        sqlconnect.updatewins(dict.get(addr[0]), record)

                        matchesfirstplayer = sqlconnect.getmatches(nameclients[0])
                        matchesfirstplayer+=1
                        sqlconnect.updatematches(nameclients[0], matchesfirstplayer)

                        matchessecondplayer = sqlconnect.getmatches(nameclients[1])
                        matchessecondplayer+=1
                        sqlconnect.updatematches(nameclients[1], matchesfirstplayer)

                        continue

                    if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
                        conn.send('win'.encode())
                        clean_and_create()
                        win=True
                        print(dict.get(addr[0]))

                        record = sqlconnect.getwins(dict.get(addr[0]))
                        record+=1
                        sqlconnect.updatewins(dict.get(addr[0]), record)

                        matchesfirstplayer = sqlconnect.getmatches(nameclients[0])
                        matchesfirstplayer+=1
                        sqlconnect.updatematches(nameclients[0], matchesfirstplayer)

                        matchessecondplayer = sqlconnect.getmatches(nameclients[1])
                        matchessecondplayer+=1
                        sqlconnect.updatematches(nameclients[1], matchesfirstplayer)

                        continue

                if((choices[0] == choices[4] and choices[0] == choices[8]) or (choices[2] == choices[4] and choices[4] == choices[6])) :
                    conn.send('win'.encode())
                    clean_and_create()
                    win=True
                    print(dict.get(addr[0]))

                    record = sqlconnect.getwins(dict.get(addr[0]))
                    record+=1
                    sqlconnect.updatewins(dict.get(addr[0]), record)

                    matchesfirstplayer = sqlconnect.getmatches(nameclients[0])
                    matchesfirstplayer+=1
                    sqlconnect.updatematches(nameclients[0], matchesfirstplayer)

                    matchessecondplayer = sqlconnect.getmatches(nameclients[1])
                    matchessecondplayer+=1
                    sqlconnect.updatematches(nameclients[1], matchesfirstplayer)

                    continue

                conn.send((str(pplayer)).encode())

                print(win)
                if win == True:
                    player+=0
                else:
                    player+=1
                win=False

        else:
            conn.send("Other".encode())
    conn.close()
