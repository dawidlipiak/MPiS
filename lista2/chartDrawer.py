
import matplotlib
import matplotlib.pyplot as plt
import csv
import math
import numpy 


plt.figure(1)
BnAverage1 = []
BnAverage2 = []
with open('Bn_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',')    
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        BnAverage1.append(float(sum/int(row[0])))
        BnAverage2.append(float(sum/math.sqrt(int(row[0]))))
        plt.plot(int(row[0]),sum,"o",color="red")

plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$B_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ B_n$'))
plt.title(r'$B_n$'' - first collision moment')
plt.xlabel('number of pockets')
plt.ylabel('number of throws')
plt.legend(loc='best')

plt.figure(2)
UnAverage = [] 
with open('Un_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',')    
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        UnAverage.append(float(sum/int(row[0])))
        plt.plot(int(row[0]),sum,"o",color="red")

plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$U_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ U_n$'))
plt.title(r'$U_n$'' - number of empty pockets for n throws')
plt.xlabel('number of pockets')
plt.ylabel('number of throws')
plt.legend(loc='best')

plt.figure(3)
LnAverage1 = []
LnAverage2 = []
LnAverage3 = []
with open('Ln_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',') 
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        LnAverage1.append(float(sum/math.log(int(row[0]))))
        LnAverage2.append(float(float(sum*math.log(math.log(int(row[0]))))/math.log(int(row[0]))))
        LnAverage3.append(float(sum/math.log(math.log(int(row[0])))))
        plt.plot(int(row[0]),sum,"o",color="red")


plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$L_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ L_n$'))
plt.title(r'$L_n$'' - maximum number of balls in a pocket for n throws')
plt.xlabel('number of pockets')
plt.ylabel('number of balls')
plt.legend(loc='best')

plt.figure(4)
CnAverage1 = []
CnAverage2 = []
CnAverage3 = []
with open('Cn_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',')  
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        CnAverage1.append(float(sum/int(row[0])))
        CnAverage2.append(float(sum/float(int(row[0])*math.log(int(row[0])))))
        CnAverage3.append(float(sum/float(int(row[0])*int(row[0]))))
        plt.plot(int(row[0]),sum,"o",color="red")

plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$C_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ C_n$'))
plt.title(r'$C_n$'' - minimum number of throws for at least one ball in all pockets')
plt.xlabel('number of pockets')
plt.ylabel('number of throws')
plt.legend(loc='best')

plt.figure(5)
DnAverage1 = []
DnAverage2 = []
DnAverage3 = []
with open('Dn_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',')    
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        DnAverage1.append(float(sum/int(row[0])))
        DnAverage2.append(float(sum/float(int(row[0])*math.log(int(row[0])))))
        DnAverage3.append(float(sum/float(int(row[0])*int(row[0]))))
        plt.plot(int(row[0]),sum,"o",color="red")

plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$D_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ D_n$'))
plt.title(r'$D_n$'' - minimum number of throws for at least two balls in all pockets')
plt.xlabel('number of pockets')
plt.ylabel('number of throws')
plt.legend(loc='best')

plt.figure(6)
DnCnAverage1 = [] 
DnCnAverage2 = [] 
DnCnAverage3 = [] 
with open('Dn-Cn_results.csv', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=',')    
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot( int(row[0]),int(row[x]), "o", color="skyblue",markersize = 2)
            sum += int(row[x])
        sum /= 50
        DnCnAverage1.append(float(sum/int(row[0])))
        DnCnAverage2.append(float(sum/float(int(row[0])*math.log(int(row[0])))))
        DnCnAverage3.append(float(sum/float(int(row[0])*math.log(math.log(int(row[0]))))))
        plt.plot(int(row[0]),sum,"o",color="red")

plt.plot(int(row[0]),int(row[1]), "o", color="skyblue",markersize = 2, label=(r'$D_n-C_n$'))
plt.plot(int(row[0]),sum, "o", color="red",markersize = 2, label=(r'$Average\ D_n-C_n$'))
plt.title(r'$D_n-C_n$'' - number of throws for at least two balls in all pockets from a Cn moment')
plt.xlabel('number of pockets')
plt.ylabel('number of throws')
plt.legend(loc='best')

nArray = []
for i in range (1000, 101000, 1000):
    nArray.append(i)

plt.figure(7)
plt.title("Various charts of b(n)")
plt.plot(nArray[:],BnAverage1[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{b(n)}{n}$'))
plt.xlabel('number of pockets')
plt.plot(nArray[:],BnAverage2[:], '-o',color = "red", markersize = 1, linewidth = 2, label = (r'$\frac{b(n)}{\sqrt{n}}$'))
plt.legend(loc='best')

plt.figure(8)
plt.title(r'$Chart\ of\ \frac{u(n)}{n}$')
plt.plot(nArray[:],UnAverage[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{u(n)}{n}$'))
plt.xlabel('number of pockets')
plt.legend(loc='best')

plt.figure(9)
plt.title("Various charts of l(n)")
plt.plot(nArray[:],LnAverage1[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{l(n)}{\ln{n}}$'))
plt.plot(nArray[:],LnAverage2[:], '-o', color = "red", markersize = 1, linewidth = 2, label = (r'$\frac{l(n)}{(\ln{n})/\ln{\ln{n}}}$'))
plt.plot(nArray[:],LnAverage3[:], '-o', color = "orange", markersize = 1, linewidth = 2, label = (r'$\frac{l(n)}{\ln{\ln{n}}}$'))
plt.xlabel('number of pockets')
plt.legend(loc='best')

plt.figure(10)
plt.title("Various charts of c(n)")
plt.plot(nArray[:],CnAverage1[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{c(n)}{n}$'))
plt.plot(nArray[:],CnAverage2[:], '-o',color = "red", markersize = 1, linewidth = 2, label = (r'$\frac{c(n)}{n \ln{n}}}$'))
plt.plot(nArray[:],CnAverage3[:], '-o',color = "orange", markersize = 1, linewidth = 2, label = (r'$\frac{c(n)}{n^{2}}$'))
plt.xlabel('number of pockets')
plt.legend(loc='best')

plt.figure(11)
plt.title("Various charts of d(n)")
plt.plot(nArray[:],DnAverage1[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{d(n)}{n}$'))
plt.plot(nArray[:],DnAverage2[:], '-o', color = "red", markersize = 1, linewidth = 2, label = (r'$\frac{d(n)}{n \ln{n}}}$'))
plt.plot(nArray[:],DnAverage3[:], '-o', color = "orange", markersize = 1, linewidth = 2, label = (r'$\frac{d(n)}{n^{2}}$'))
plt.xlabel('number of pockets')
plt.legend(loc='best')

plt.figure(12)
plt.title("Various charts of d(n)-c(n)")
plt.plot(nArray[:],DnCnAverage1[:], '-o', markersize = 1, linewidth = 2, label = (r'$\frac{d(n)-c(n)}{n}$'))
plt.plot(nArray[:],DnCnAverage2[:], '-o', color = "red", markersize = 1, linewidth = 2, label = (r'$\frac{d(n)-c(n)}{n \ln{n}}}$'))
plt.plot(nArray[:],DnCnAverage3[:], '-o', color = "orange", markersize = 1, linewidth = 2, label = (r'$\frac{d(n)-c(n)}{n \ln{\ln{n}}}$'))
plt.xlabel('number of pockets')
plt.legend(loc='best')

plt.show()