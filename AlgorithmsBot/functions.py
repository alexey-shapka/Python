from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def time_funk(l):
    time_list=[]
    for i in l:
            start_time = time.time()
            mergeSort(i)
            time.sleep(0.000001)
            end_time = (time.time()-start_time-0.000001)
            time_list.append(end_time)
    return time_list

def lab2_graph():
    try:
        a=[]
        lenlist=[20,100,200,300,400,500,600,800,900,1000]
        for i in lenlist:
            l=[random.randint(1,100) for k in range(i)]
            a.append(l)
        print(a)

        time_list = time_funk(a)
        print(time_list)
        print(a)

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

        koef_all=[]
        for i in range(len(lenlist)):
            koef_all.append(time_list[i]/(math.log(lenlist[i])*lenlist[i]))
        koef = sum(koef_all)/len(koef_all)
        print(koef)

        koef_new=[]
        for i in range(len(lenlist)):
            koef_new.append(lenlist[i]*koef_all[i])
        print(koef_new)

        y = np.log(lenlist)*lenlist*koef

        fig = plt.figure()
        plt.plot(lenlist, y,'w')
        plt.plot(lenlist, time_list, 'r')

        plt.xlim(lenlist[0], lenlist[-1])
        plt.ylim(np.min(y), np.max(y))

        plt.xlabel(u'Length', fontsize=15)
        plt.ylabel(u'Time', fontsize=15)
        plt.grid(True, color='w')

        fig.savefig('GraphicAmo2.png', format='png', facecolor='k')

        plt.close()

    except: print("Error")

def xlisty(r,sin):
    x=[i*0.4 for i in range(r)]
    y=[]
    if sin == 'sin':
        for i in x:
            y.append(math.sin(i))
    else:
        for i in x:
            y.append((math.sin(i))**3+ 3*(math.cos(i))**2)
    return(x,y)

def lagrange(d,n):
    x,y = xlisty(n,'no')
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1
            else:
                p1=p1*(d-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z

def newton(d,n):
    x,y = xlisty(n,'no')
    l=y[0]
    p=1
    for k in range(1,n):
        p=p*(d-x[k-1])
        for i in range(n-k):
            y[i]=(y[i+1]-y[i])/(x[i+k]-x[i])
        l = l + p*y[0]
    return l

def lagrange_sin(d,n):
                        x,y = xlisty(n,'sin')
                        z=0
                        for j in range(len(y)):
                            p1=1; p2=1
                            for i in range(len(x)):
                                if i==j:
                                    p1=p1*1; p2=p2*1
                                else:
                                    p1=p1*(d-x[i])
                                    p2=p2*(x[j]-x[i])
                            z=z+y[j]*p1/p2
                        return z

#1.8*x**2-sin(10x)=0
def fl4(x):
    return 1.8*(x**2)-math.sin(10*x)

def fl4_1(x):
    return 3.6*x - 10*math.cos(10*x)

def fl4_2(x):
    return 3.6+100*math.sin(10*x)

def lab4_alg(a,b,e):
    if fl4(a)*fl4(b)<0:
        k=0
        while math.fabs(b-a)>e:
            if fl4_1((b+a)/2)*fl4_2((b+a)/2)<0:
                z=a
                a=b
                b=z
            a = a-(fl4(a)*(b-a))/(fl4(b)-fl4(a))
            b = b- fl4(b)/fl4_1(b)
            k=k+1
        x = (b+a)/2
        return x

def lab4_graph():
    lag = 0.00001
    x = np.arange(-0.75, 0.75, lag)
    y = -np.sin(10*x)+1.8*(x**2)

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

    fig4 = plt.figure()

    plt.scatter(-0.5667, 0, color="white", marker="x")
    plt.scatter(-0.334, 0, color="white", marker="x")
    plt.scatter(0, 0, color="white", marker="x")
    plt.scatter(0.298, 0, color="white", marker="x")

    plt.plot(x, y, 'r')
    plt.xlabel(u'X', fontsize=15)
    plt.ylabel(u'Y', fontsize=15)
    plt.grid(True)

    fig4.savefig('GraphicAmo4.png', format='png', facecolor='k')

    plt.close()

def chunkIt(seq, num):
                                avg = len(seq) / float(num)
                                out = []
                                last = 0.0
                                while last < len(seq):
                                    out.append(seq[int(last):int(last + avg)])
                                    last += avg
                                return out

def Lab5(m, w, eps, max_iteration=100, x0=None):
  n  = len(m)
  x0 = [0] * n
  x1 = x0[:]

  for __ in range(max_iteration):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
      x1[i] = w*(m[i][n]+s)/m[i][i] + (1-w)*x0[i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1
    x0 = x1[:]
  raise ValueError('Solution does not converge')
