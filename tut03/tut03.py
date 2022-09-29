#Help https://youtu.be/H37f_x4wAC0
import pandas as pd
import math
def octant_longest_subsequence_count():

###Code

# from platform import python_version
# ver = python_version()

# 
# print("Correct Version Installed")
# 
#     
#creating dataframe as df
    df =pd.read_excel('input_octant_longest_subsequence.xlsx')
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
    df["  "]="" #intiliazing a empty column\
    list=[1,-1,2,-2,3,-3,4,-4]
    df["Count"]=""
    j=0
    while j<8:
        df.loc[j,"Count"]=list[j]
        j+=1
    df["Longest subsequence length"]=""
    df["count"]=" "
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    c1=c2=c3=c4=c5=c6=c7=c8=0
    for i in range (len(df)-1):
        a=df.loc[i,"Octant"]
        b=df.loc[i+1,"Octant"]
        if a==b:
            if a==1:
                c1+=1
            elif a==-1:
                c2+=1
            elif a==2:
                c3+=1
            elif a==-2:
                c4+=1
            elif a==3:
                c5+=1
            elif a==-3:
                c6+=1
            elif a==4:
                c7+=1
            elif a==-4:
                c8+=1
        else:
            if a==1:
                c1+=1
                count1=max(count1,c1)
                c1=0
            elif a==-1:
                c2+=1
                count2=max(count2,c2)
                c2=0
            elif a==2:
                c3+=1
                count3=max(count3,c3)
                c3=0
            elif a==-2:
                c4+=1
                count4=max(count4,c4)
                c4=0
            elif a==3:
                c5+=1
                count5=max(count5,c5)
                c5=0
            elif a==-3:
                c6+=1
                count6=max(count6,c6)
                c6=0
            elif a==4:
                c7+=1
                count7=max(count7,c7)
                c7=0
            elif a==-4:
                c8+=1
                count8=max(count8,c8)
                c8=0

    df.loc[0,"Longest subsequence length"]=count1
    df.loc[1,"Longest subsequence length"]=count2
    df.loc[2,"Longest subsequence length"]=count3
    df.loc[3,"Longest subsequence length"]=count4
    df.loc[4,"Longest subsequence length"]=count5
    df.loc[5,"Longest subsequence length"]=count6
    df.loc[6,"Longest subsequence length"]=count7
    df.loc[7,"Longest subsequence length"]=count8       

    df.to_excel('output_octant_transition_identify.xlsx',index=False) #printing output in excel file

octant_longest_subsequence_count()