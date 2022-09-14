
import csv
from sqlite3 import Time
import pandas as pd 
import math
def octact_identification(mod=5000):
   
    df=pd.read_csv(r'C:\Users\DELL\Documents\GitHub\2001CE55_2022\tut01\octant_input.csv') 

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

    df.loc[1,"Octant ID"]="mod {}".format(mod)
    n=math.ceil(len(df)/mod)
    
    i=0
    while i<n:
        l=i*mod
        u=((i+1)*mod)-1
        if u>len(df):
            u=len(df)-1
        df.loc[i+2,"Octant ID"]="{}-{}".format(l,u)
        i+=1
    
    df["1"]=''
    df.loc[0,"1"]=count1
    df["-1"]=''
    df.loc[0,"-1"]=count5
    df["2"]=''
    df.loc[0,"2"]=count2
    df["-2"]=''
    df.loc[0,"-2"]=count6
    df["3"]=''
    df.loc[0,"3"]=count3
    df["-3"]=''
    df.loc[0,"-3"]=count7
    df["4"]=''
    df.loc[0,"4"]=count4
    df["-4"]=''
    df.loc[0,"-4"]=count8
    

    


    print (df["Octant ID"].head(10))
    
mod=5000
octact_identification(mod)