from ast import Try
import pandas as pd #importing pandas
from openpyxl import load_workbook
import math

def octant_transition_count(mod=5000):
###Code

# from platform import python_version
# ver = python_version()

# 
# print("Correct Version Installed")
# 
#     
#creating dataframe as df
    df =pd.read_excel('input_octant_transition_identify.xlsx')
    try:
        df1=df["U"].mean()
        df2=df["V"].mean()
        df3=df["W"].mean()
    except:
        print("error getting while finding the mean\n")

    #printing average values
    df.loc[0,"U Avg"]=df1
    df.loc[0,"V Avg"]=df2
    df.loc[0,"W Avg"]=df3

    try:
        df["U'=U- U Avg"]=df["U"]-df1
        df["V'=V- V Avg"]=df["V"]-df2
        df["W'=W- W Avg"]=df["W"]-df3
    except:
        print("error while finding difference\n")

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
        try:
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
        except:
            print("Getting error in finding the octant\n")
    
    df["Octant"]=oct #copying oct values to octant column
    df["  "]="" #intiliazing a empty column
    df.loc[1,"  "]="User Input" #asigning string to 1st row of empty column
    df[' ']='' #creating octant id column
    df.loc[0,' ']="Overall Count" #printing "Overall Count" to 0th row of "Octant ID" column
    df["1"]=''
    try:
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
    except:
        print("getting error while printing overall count\n")

    df.loc[1,' ']="mod {}".format(mod) #printing mod value in 1st row of "Octant ID" column
    n=math.ceil(len(df)/mod) #calculating number of intervals
    
    i=0 # i is the index which is traversing in row in excel file
    try:
        while i<n:
            a=i*mod #lower value of interval
            b=((i+1)*mod)-1 #maximum value of interval
            if b>len(df):
                b=len(df)-1
            df.loc[i+2,' ']="{}-{}".format(a,b) #printing intervals
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
            i+=1
        i+=2
    except:
        print("getting error while printing octant count for the interval")
    #from here we will count transition count
    df.loc[i+2,' ']="Overall Transition Count"
    i+=3
    df.loc[i,' ']="Count"
    df.loc[i+1,"  "]="From"

    ## MAKING MATRIX FOR OVERALL COUNT
    #Assigning octants in a row
    df.loc[i,"1"]=1
    df.loc[i,"-1"]=-1
    df.loc[i,"2"]=2
    df.loc[i,"-2"]=-2
    df.loc[i,"3"]=3
    df.loc[i,"-3"]=-3
    df.loc[i,"4"]=4
    df.loc[i,"-4"]=-4
    i+=1
    #defignign row of overall matrix
    df.loc[i,' ']=1
    df.loc[i+1,' ']=-1
    df.loc[i+2,' ']=2
    df.loc[i+3,' ']=-2
    df.loc[i+4,' ']=3
    df.loc[i+5,' ']=-3
    df.loc[i+6,' ']=4
    df.loc[i+7,' ']=-4
    k=1 #initializing the row from 1
    list1= [1,-1,2,-2,3,-3,4,-4]
    for l in list1:
        for j in range (8):
            df.loc[j+i,str(l)]=0 #assigning 0 to each value of matrix
    try:
        while k<len(df): #loop for counting the transition 
            prev=df.loc[k-1,"Octant"] #storing the previous octant value
            curr=str(df.loc[k,"Octant"]) ##storing the current octant value
            #checking the transition values and increament the corresponding transition
            if prev==1:
                df.loc[i,curr]+=1
            elif prev==-1:
                df.loc[i+1,curr]+=1
            elif prev==2:
                df.loc[i+2,curr]+=1
            elif prev==-2:
                df.loc[i+3,curr]+=1
            elif prev==3:
                df.loc[i+4,curr]+=1
            elif prev==-3:
                df.loc[i+5,curr]+=1
            elif prev==4:
                df.loc[i+6,curr]+=1
            elif prev==-4:
                df.loc[i+7,curr]+=1
            k+=1    
    
        i=i+11
    except:
        print("there is error in counting the overall transition")
    c=0 #initiliazing the no. of interval from zero 
    while c<n:
        a=c*mod #lower value of interval
        b=((c+1)*mod) #upper bound
        if b>len(df):
            b=len(df)
        df.loc[i,' ']="Mod Transition Count"
        i+=1
        df.loc[i,' ']="{}-{}".format(a,b-1) #printing intervals
        df.loc[i,"1"]="To"
        i+=1
        df.loc[i,' ']="Count"
        df.loc[i+1,"  "]="From"
        #Assigning octants in a column of matrix
        df.loc[i,"1"]=1
        df.loc[i,"-1"]=-1
        df.loc[i,"2"]=2
        df.loc[i,"-2"]=-2
        df.loc[i,"3"]=3
        df.loc[i,"-3"]=-3
        df.loc[i,"4"]=4
        df.loc[i,"-4"]=-4
        i+=1
        #Assigning octants in a row of matrix
        df.loc[i,' ']=1
        df.loc[i+1,' ']=-1
        df.loc[i+2,' ']=2
        df.loc[i+3,' ']=-2
        df.loc[i+4,' ']=3
        df.loc[i+5,' ']=-3
        df.loc[i+6,' ']=4
        df.loc[i+7,' ']=-4
        
        
        list1= [1,-1,2,-2,3,-3,4,-4]
        for l in list1:
            for j in range (8):
                df.loc[j+i,str(l)]=0
        j=a
        if b==len(df):
            b=b-1
        while j<b: #loop for calculating transition for each interval (a-b)
            prev=df.loc[j,"Octant"] #previous value of octant 
            curr=str(df.loc[j+1,"Octant"]) #current value of octant

            #now checking the condition how the transition goes
            if prev==1:
                df.loc[i,curr]+=1
            elif prev==-1:
                df.loc[i+1,curr]+=1
            elif prev==2:
                df.loc[i+2,curr]+=1
            elif prev==-2:
                df.loc[i+3,curr]+=1
            elif prev==3:
                df.loc[i+4,curr]+=1
            elif prev==-3:
                df.loc[i+5,curr]+=1
            elif prev==4:
                df.loc[i+6,curr]+=1
            elif prev==-4:
                df.loc[i+7,curr]+=1
            j+=1    
        i=i+11
            
        
            
        c+=1

    df.to_excel('output_octant_transition_identify.xlsx',index=False) #printing output in excel file
mod=5000
octant_transition_count(mod)