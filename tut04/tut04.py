import pandas as pd
def octant_longest_subsequence_count():
###Code

# from platform import python_version
# ver = python_version()

# 
# print("Correct Version Installed")
# 
#     
#creating dataframe as df and reading the excel file
    df =pd.read_excel('input_octant_longest_subsequence_with_range.xlsx')
    try:
        df1=df["U"].mean()#taking mean of each U,V,W column
        df2=df["V"].mean()
        df3=df["W"].mean()
    except:
        print("error getting while finding the mean\n")

    #printing average values in their respective column
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
    df["Count"]="" #creating the column count
    j=0
    while j<8:
        df.loc[j,"Count"]=list[j] #printing all the values of list in count column
        j+=1
    df["Longest subsequence length"]="" #creating the longest subsequence length column which stores count of longest subsequence
    df["count"]=" " #creating count array which stores count of longest subsequence
    count1=count2=count3=count4=count5=count6=count7=count8=0 #initializing longest subsequence length to zero
    c1=c2=c3=c4=c5=c6=c7=c8=0 #secondary variable which count the longest subsequence count
    #l_count represents the count of longest subsequence length
    l_count1=l_count2=l_count3=l_count4=l_count5=l_count6=l_count7=l_count8=0 
    try:
        for i in range (len(df)-1):
            curr_oct=df.loc[i,"Octant"] #storing current octant value
            next_oct=df.loc[i+1,"Octant"] #storing next octant value
            if curr_oct==next_oct:
                if curr_oct==1:
                    c1+=1
                elif curr_oct==-1:
                    c2+=1
                elif curr_oct==2:
                    c3+=1
                elif curr_oct==-2:
                    c4+=1
                elif curr_oct==3:
                    c5+=1
                elif curr_oct==-3:
                    c6+=1
                elif curr_oct==4:
                    c7+=1
                elif curr_oct==-4:
                    c8+=1
            else:
                if curr_oct==1:
                    c1+=1
                    if c1==count1:
                        l_count1+=1
                    elif c1>count1:
                        l_count1=1
                    count1=max(count1,c1)
                    c1=0
                elif curr_oct==-1:
                    c2+=1
                    if c2==count2:
                        l_count2+=1
                    elif c2>count2:
                        l_count2=1
                    count2=max(count2,c2)
                    c2=0
                elif curr_oct==2:
                    c3+=1
                    if c3==count3:
                        l_count3+=1
                    elif c3>count3:
                        l_count3=1
                    count3=max(count3,c3)
                    c3=0
                elif curr_oct==-2:
                    c4+=1
                    if c4==count4:
                        l_count4+=1
                    elif c4>count4:
                        l_count4=1
                    count4=max(count4,c4)
                    c4=0
                elif curr_oct==3:
                    c5+=1
                    if c5==count5:
                        l_count5+=1
                    elif c5>count5:
                        l_count5=1
                    count5=max(count5,c5)
                    c5=0
                elif curr_oct==-3:
                    c6+=1
                    if c6==count6:
                        l_count6+=1
                    elif c6>count6:
                        l_count6=1
                    count6=max(count6,c6)
                    c6=0
                elif curr_oct==4:
                    c7+=1
                    if c7==count7:
                        l_count7+=1
                    elif c7>count7:
                        l_count7=1
                    count7=max(count7,c7)
                    c7=0
                elif curr_oct==-4:
                    c8+=1
                    if c8==count8:
                        l_count8+=1
                    elif c8>count8:
                        l_count8=1
                    count8=max(count8,c8)
                    c8=0
    except:
        print("there is error in the loop\n")
    #locating the longest subsequence length of octant in its corresponding row
    df.loc[0,"Longest subsequence length"]=count1
    df.loc[1,"Longest subsequence length"]=count2
    df.loc[2,"Longest subsequence length"]=count3
    df.loc[3,"Longest subsequence length"]=count4
    df.loc[4,"Longest subsequence length"]=count5
    df.loc[5,"Longest subsequence length"]=count6
    df.loc[6,"Longest subsequence length"]=count7
    df.loc[7,"Longest subsequence length"]=count8  

    #locating count of longest subsequence length in the data in its corresponding row
    df.loc[0,"count"]= l_count1 
    df.loc[1,"count"]= l_count2
    df.loc[2,"count"]= l_count3
    df.loc[3,"count"]= l_count4
    df.loc[4,"count"]= l_count5
    df.loc[5,"count"]= l_count6
    df.loc[6,"count"]= l_count7
    df.loc[7,"count"]= l_count8
    df[' ']='  '
    df["Octant "]='  '  
    df["Longest subsequence length "]='  '
    df["Count "]='  '

    index=0
    row =0
    for i in list:
        count=0
        df.loc[row,"Octant "]=i
        df.loc[row,"Longest subsequence length "]=df.loc[index,"Longest subsequence length"]
        df.loc[row,"Count "]=df.loc[index,"count"]
        row+=1
        df.loc[row,"Octant "]='Time'
        df.loc[row,"Longest subsequence length "]='From'
        df.loc[row,"Count "]='To'
        row+=1
        for j in range (len(df)):
            if(df.loc[j,"Octant"]==i):
                count+=1
            else:
                if(count==df.loc[index,"Longest subsequence length"]):
                    df.loc[row,"Longest subsequence length "]=df.loc[j-df.loc[index,"Longest subsequence length"],"Time"]
                    df.loc[row,"Count "]=df.loc[j-1,"Time"]
                    row+=1
                    count=0
                else:
                    count=0
        index+=1
    df.to_excel('output_octant_longest_subsequence_with_range.xlsx',index=False) #printing output in excel file

octant_longest_subsequence_count()