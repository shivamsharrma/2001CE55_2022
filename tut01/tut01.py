
import csv
from sqlite3 import Time
import pandas as pd

df=pd.read_csv(r'C:\Users\DELL\Documents\GitHub\CS384_2022\tut01\octant_input.csv')

df1=df["U"].mean()
df2=df["V"].mean()
df3=df["W"].mean()
df.loc[0,"U Avg"]=df1
df.loc[0,"V Avg"]=df2
df.loc[0,"W Avg"]=df3

df["U'=U- U Avg"]=df["U"]-df1
df["V'=V- V Avg"]=df["V"]-df2
df["W'=W- W Avg"]=df["W"]-df3

oct=[]
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0

for row in range(len(df)):
    x=df.loc[row,"U'=U- U Avg"]
    y=df.loc[row,"V'=V- V Avg"]
    z=df.loc[row,"W'=W- W Avg"]
    if x >= 0 and y >= 0 and z >= 0:
        oct.append(1)
        count1+=1
         
    elif x < 0 and y >= 0 and z >= 0:
        oct.append(2)
        count2+=1
         
    elif x < 0 and y < 0 and z >= 0:
        oct.append(3)
        count3+=1
         
    elif x >= 0 and y < 0 and z >= 0:
        oct.append(4)
        count4+=1
         
    elif x >= 0 and y >= 0 and z < 0:
        oct.append(-1)
        count5+=1
         
    elif x < 0 and y >= 0 and z < 0:
        oct.append(-2)
        count6+=1
         
    elif x < 0 and y < 0 and z < 0:
        oct.append(-3)
        count7+=1

    elif x >= 0 and y < 0 and z < 0:
        oct.append(-4)
        count8+=1

df["octant"]=oct
df[" "]=""
df.loc[1," "]="user input"
df["Octant ID"]=''
df.loc[0,"Octant ID"]="Overall Count"



print (df)
