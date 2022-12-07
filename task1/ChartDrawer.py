
import matplotlib
import matplotlib.pyplot as plt
import csv
import math


with open('results1.txt', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=';')    
    fields = next(csvreader)
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot(float(row[0]),float(row[x]), "o", color="blue",markersize = 2)
            sum += float(row[x])
        sum /= 50
        plt.plot(float(row[0]),sum,"o",color="red")

plt.plot([50,5000],[12,12],color="lime",linewidth=3)
plt.show()

with open('results2.txt', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=';')    
    fields = next(csvreader)
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot(float(row[0]),float(row[x]), "o", color="blue",markersize = 2)
            sum += float(row[x])
        sum /= 50
        plt.plot(float(row[0]),sum,"o",color="red")

plt.plot([50,5000],[2,2],color="lime",linewidth=3)

plt.show()
with open('results3.txt', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=';')    
    fields = next(csvreader)
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot(float(row[0]),float(row[x]), "o", color="blue",markersize = 2)
            sum += float(row[x])
        sum /= 50
        plt.plot(float(row[0]),sum,"o",color="red")

plt.plot([50,5000],[0.2,0.2],color="lime",linewidth=3)
plt.show()

with open('piResults.txt', 'r', ) as csvfile :
    csvreader = csv.reader(csvfile,delimiter=';')    
    fields = next(csvreader)
    for row in csvreader:
        sum = 0
        for x in range (1,51,1):
            plt.plot(float(row[0]),float(row[x]), "o", color="blue",markersize = 2)
            sum += float(row[x])
        sum /= 50
        plt.plot(float(row[0]),sum,"o",color="red")

plt.plot([50,5000],[math.pi,math.pi],color="lime",linewidth=3)
plt.show()

