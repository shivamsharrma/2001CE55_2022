
from datetime import datetime as dt
start_time = dt.now()
import os
import pandas as pd #importing pandas
import calendar

def attendance_report():
###Code
# if ver == "3.8.10":
    print("Correct Version Installed")
    df1=pd.read_csv('input_registered_students.csv')
    df2=pd.read_csv('input_attendance.csv')

    df2["Timestamp"]=pd.to_datetime(df2["Timestamp"] , format='%d-%b-')
    df2['Time']=pd.to_datetime(df2['Timestamp']).dt.time
    df2['date']=pd.to_datetime(df2['Timestamp']).dt.date
    df2['dayofweek']=df2['Timestamp'].dt.day_name()
    # print(df2) 
    
    df2['interval']={'class':['14:00:00','14:59:59']}
    df2['class']=pd.to_datetime(df2['interval']).dt.time
    start=dt.time(14,0,0)
    end=dt.time(14,59,59)
    df3=pd.read_csv('input_registered_students.csv')
    df3['total_lecture_taken']=df3['attendance_count_actual']=df3['attendance_count_fake']=''
    df3['attendance_count_absent']=df3['Percentage']=''
    df4=pd.read_csv('input_registered_students.csv')
    df4['Total count of attendance on that day']=''
    # print(df2.dtypes)
    print(df1.loc[0,"Roll No"]+" "+df1.loc[0,"Name"]=="2001CB02 ABHAY CHAHAR")
    for i in range (len(df1)):
        attendance_count=0
        attendance_count_fake=0
        duplicate_attendance=0
        
        for j in range (len(df2)):
            if(df2.loc[j,"Attendance"]==df1.loc[i,"Roll No"]+" "+df1.loc[i,"Name"]):
                if((df2.loc[j,'dayofweek']=="Monday" or df2.loc[j,'dayofweek']=="Thursday")and
                 df2.loc[j,'Time']>=start and df2.loc[j,'Time']<=end):
                    attendance_count+=1
                    
                    # while(j+1<len(df2) and df2.loc[j,'date']==df2.loc[j+1,'date']):
                    #     if( df2.loc[j+1,"Attendance"]==df1.loc[i,"Roll No"]+" "+df1.loc[i,"Name"]):
                    #         duplicate_attendance+=1
                    #     j+=1

                else:
                    attendance_count_fake+=1
              
        df3.loc[i,'attendance_count_actual']=attendance_count
        df3.loc[i,'attendance_count_fake']=attendance_count_fake
        df4.loc[i,'Total count of attendance on that day']=duplicate_attendance
    
    print(df2)
    df2.to_csv('output.csv',index=False)
            

attendance_report()




#This shall be the last lines of the code.
end_time = dt.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
