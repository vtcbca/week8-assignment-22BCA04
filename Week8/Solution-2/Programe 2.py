'''
Sales (sid, year, totalsales)

Create above table into a SQLite database with appropriate constraints. 

A. Insert at least 5-10 records into the sales table.<br> 
B. Export sales table data into sales.csv file.<br>
C. Write a python scripts that read the sales.<br>
D. csv file and plot a bar chart that shows totalsales of the year.<br>

Also decorate the chart with appropriate title, lables, colours etc.
'''
from sqlite3 import *
con=connect("c:\\sqlite3\\Sale_Data.db")
cur=con.cursor()
cur.execute("""create table if not exists Sale
            (
                S_id int,
                Year int,
                Total_Sales int
            )""")
print("Sale Table Created Successfully")

records=[]
for i in range(5):
    n=int(input("Enter Sales ID:"))
    year=int(input('Enter Year'))
    total_Sell=int(input('Enter Total Sell:'))
    data=[n,year,total_Sell]
    records.append(data)


#A. Insert at least 5-10 records into the sales table

cur.executemany("insert into Sale values(?,?,?)",records)
print('Insert Successfully')

con.commit()


#B. Export sales table data into sales.csv file.
#in sqlite3 terminl

'''
.output sales.csv<br>
.header on<br>
.mode csv<br>
select * from Sale;<br>
.quit<br>
'''

# C. Write a python scripts that read the sales.

from csv import *

file="c:\\sqlite3\\sales.csv"

with open(file,"r")as read_file:
    for row in reader(read_file):
        print(row)


# D. csv file and plot a bar chart that shows totalsales of the year.
# Also decorate the chart with appropriate title, lables, colours etc.

import matplotlib.pyplot as plt

from pandas import *

df=read_csv(file)
print(df)

y=df['Year']
t=df['Total_Sales']

# for Create a Bar Chart We USe bar() function
plt.bar(y,t,color="brown")
plt.legend("total sell",bbox_to_anchor=(1.0,1.05),facecolor="cyan",title="Legend")
plt.title("Total Sell of 5 Years")
plt.xticks(rotation=25)
plt.xlabel("Year")
plt.ylabel("Total Sell")

