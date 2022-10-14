
import csv
from sqlite3 import Time
import pandas as pd #importing pandas
import math #importing math
def octact_identification(mod=5000):
   #code to read input csv file and store that in dataframe
    df=pd.read_excel('octant_input.xlsx') 

    #takingh mean of each 'U','V','W' column
    df1=df["U"].mean()
    df2=df["V"].mean()
    df3=df["W"].mean()

    #printing average values
    df.loc[0,"U Avg"]=df1
    df.loc[0,"V Avg"]=df2
    df.loc[0,"W Avg"]=df3

    
    df["U'=U- U Avg"]=df["U"]-df1
    df["V'=V- V Avg"]=df["V"]-df2
    df["W'=W- W Avg"]=df["W"]-df3

    oct=[] #creating empty array
    #initializing count of every octant is zero
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0

    
    #initializing loop 
    for row in range(len(df)):
        x=df.loc[row,"U'=U- U Avg"] #calculating difference between 'U' and 'U Avg'
        y=df.loc[row,"V'=V- V Avg"] #calculating difference between 'V' and 'V Avg'
        z=df.loc[row,"W'=W- W Avg"] #calculating difference between 'W' and 'W Avg'
        #checking in which octant the value lies and appending according value to oct array
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
    
    df["Octant"]=oct #copying oct values to octant column
    df["Octant"]=df["Octant"].shift(-1)
    df[" "]="" #intiliazing a empty column
    df.loc[1," "]="User Input" #asigning string to 1st row of empty column
    df["Octant ID"]='' #creating octant id column
    df.loc[0,"Octant ID"]="Overall Count" #printing "Overall Count" to 0th row of "Octant ID" column
    df["1"]=''
    df.loc[0,"1"]=count1 #printing overall count of 1
    df["-1"]=''
    df.loc[0,"-1"]=count5 #printing overall count of -1
    df["2"]=''
    df.loc[0,"2"]=count2 #printing overall count of 2
    df["-2"]=''
    df.loc[0,"-2"]=count6 #printing overall count of -2
    df["3"]=''
    df.loc[0,"3"]=count3 #printing overall count of 3
    df["-3"]=''
    df.loc[0,"-3"]=count7 #printing overall count of -3
    df["4"]=''
    df.loc[0,"4"]=count4 #printing overall count of 4
    df["-4"]=''
    df.loc[0,"-4"]=count8 #printing overall count of -4
    
    array=[count1,count2,count3,count4,count5,count6,count7,count8,]
    array.sort(reverse=True)
    df[1]=df[-1]=df[2]=df[-2]=df[3]=df[-3]=df[4]=df[-4]=" "
    # df.loc[0,1]="Rank 1"
    # df.loc[0,-1]="Rank 2"
    # df.loc[0,2]="Rank 3"
    # df.loc[0,-2]="Rank 4"
    # df.loc[0,3]="Rank 4"
    # df.loc[0,-3]="Rank 6"
    # df.loc[0,4]="Rank 7"
    # df.loc[0,-4]="Rank 8"
    rank=0
    for i in array:
        if(i==df.loc[0,"1"]):
            df.loc[0,1]=rank+1
        elif(i==df.loc[0,"-1"]):
            df.loc[0,-1]=rank+1
        elif(i==df.loc[0,"2"]):
            df.loc[0,2]=rank+1
        elif(i==df.loc[0,"-2"]):
            df.loc[0,-2]=rank+1
        elif(i==df.loc[0,"3"]):
            df.loc[0,3]=rank+1
        elif(i==df.loc[0,"-3"]):
            df.loc[0,-3]=rank+1
        elif(i==df.loc[0,"4"]):
            df.loc[0,4]=rank+1
        elif(i==df.loc[0,"-4"]):
            df.loc[0,-4]=rank+1
        rank+=1
        


    df.loc[1,"Octant ID"]="mod {}".format(mod) #printing mod value in 1st row of "Octant ID" column
    n=math.ceil(len(df)/mod) #calculating number of intervals
    df["Rank1 Octant ID"]=""
    i=0
    while i<n:
        a=i*mod #lower value of interval
        b=((i+1)*mod)-1 #maximum value of interval
        if b>len(df):
            b=len(df)-1
        df.loc[i+2,"Octant ID"]="{}-{}".format(a,b) #printing intervals
        j=a 
        
        #initializing count of each octant to zero in the particular interval
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        c6=0
        c7=0
        c8=0
        while j<=b:
            
            #counting the number of octants in the particular interval
            if df.loc[j,"Octant"]==1:
                c1+=1
            elif df.loc[j,"Octant"]==2:
                c2+=1
            elif df.loc[j,"Octant"]==3:
                c3+=1
            elif df.loc[j,"Octant"]==4:
                c4+=1
            elif df.loc[j,"Octant"]==-1:
                c5+=1
            elif df.loc[j,"Octant"]==-2:
                c6+=1
            elif df.loc[j,"Octant"]==-3:
                c7+=1
            elif df.loc[j,"Octant"]==-4:
                c8+=1
            j+=1
        
        #printing the count of each octants
        df.loc[i+2,"1"]=c1
        df.loc[i+2,"-1"]=c5
        df.loc[i+2,"2"]=c2
        df.loc[i+2,"-2"]=c6
        df.loc[i+2,"3"]=c3
        df.loc[i+2,"-3"]=c7
        df.loc[i+2,"4"]=c4
        df.loc[i+2,"-4"]=c8
        rank=0
        array=[c1,c2,c3,c4,c5,c6,c7,c8]
        array.sort(reverse=True)
        for element in array:
            if(element==df.loc[i+2,"1"]):
                df.loc[i+2,1]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=1
            elif(element==df.loc[i+2,"-1"]):
                df.loc[i+2,-1]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=-1
            elif(element==df.loc[i+2,"2"]):
                df.loc[i+2,2]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=2
            elif(element==df.loc[i+2,"-2"]):
                df.loc[i+2,-2]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=-2
            elif(element==df.loc[i+2,"3"]):
                df.loc[i+2,3]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=3
            elif(element==df.loc[i+2,"-3"]):
                df.loc[i+2,-3]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=-3
            elif(element==df.loc[i+2,"4"]):
                df.loc[i+2,4]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=4
            elif(element==df.loc[i+2,"-4"]):
                df.loc[i+2,-4]=rank+1
                if(rank==0):df.loc[i+2,"Rank1 Octant ID"]=-4
            rank+=1

        i+=1
    
    
    

    


    
    df.to_excel('octant_output_ranking_excel.xlsx',index=False)
    
mod=5000
octact_identification(mod)