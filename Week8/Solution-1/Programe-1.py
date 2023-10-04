'''
Records for 5 different products. 
(Prod_Name, Jan ,Feb, Mar, Apr , May, Jun )<br> 
Create Python script to perform following task.<br>
A. Read data in Dataframe. <br>
B. Add columns and calculate total_sell, average_sell.<br>
C. Plot Total sell and average sell together on line chart with proper Legends, titles and lables. <br>
D. Explain final dataframe to csv named sell_analysis.csv
'''

header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']

rows=[]
for i in range(12):
    n=int(input('Enter Product Id:'))
    name=input('Enter Product Name:')
    jan=int(input('Enter Jan Month Selling:'))
    feb=int(input('Enter Feb Month Selling:'))
    march=int(input('Enter March Month Selling:'))
    april=int(input('Enter April Month Selling:'))
    may=int(input('Enter May Month Selling:'))
    jun=int(input('Enter Jun Month Selling:'))
#   create a list 
    data=[n,name,jan,feb,march,april,may,jun]
    rows.append(data)
    
from csv import *

filename="c:\\sqlite3\\data.csv"
#create and write file
with open(filename,"w",newline="")as write_file:
    write=writer(write_file)
    write.writerow(header)
    write.writerows(rows)
    print('csv file created successfully')


#A. Read data in Dataframe.

from pandas import *

df=read_csv(filename)
print(df)

#B. Add columns and calculate total_sell, average_sell

df["Total_Sell"]=df["Jan"]+df["Feb"]+df["Mar"]+df["Apr"]+df["May"]+df["Jun"]
df["Average_sell"]=df["Total_Sell"]/6
print(df)

#C.Plot Total sell and average sell together on line chart with proper Legends, titles and lables

from matplotlib.pyplot import *
#for creating a line chart we can use plot() function

name=df["Prod_Name"]
t=df["Total_Sell"]
a=df["Average_sell"]

plot(name,t)
plot(name,a)
xticks(rotation=24)
#add title
title("Analysis Of Total And Average Sell")
#add xlabel
xlabel("Product Name")
#add ylabel
ylabel("Total Sell & Average Sell")
#legend
legend(['Total_Sell',"Average_Sell"],title="Data Information",facecolor="cyan",title_fontsize=14)

#D. Explain final dataframe to csv named sell_analysis.csv

df.to_csv("c:\\sqlite3\\sell_analysis.csv")
print("File Successfull create")

