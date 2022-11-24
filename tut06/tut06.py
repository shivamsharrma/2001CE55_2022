from datetime import datetime
start_time = datetime.now()
import os
import pandas #importing pandas


def sortDates(datesList): # sorting the dates
    year_month_date = datesList.split('/') # Splitting the dates to find out date month and year
    return year_month_date[2], year_month_date[1], year_month_date[0] 

def attendance_report(): 
    attendance = pandas.read_csv('input_attendance.csv') # Reading the attendace file
    students_registered = pandas.read_csv('input_registered_students.csv') # Reading registered students file 
    attendance['Attendance'] = attendance['Attendance'].str.upper()   
    attendance = attendance.sort_values('Timestamp', ascending=True, ignore_index=True)
    l_1 = len(attendance)
    l_2 = len(students_registered)
    
    students = {'Attendance': []} # store students who are pressent
    stud_info = {'Roll': [], 'Name': []} # store data of student
    lec_date = [] # will Store all the lecture dates
    absent_stud = {'Timestamp': [], 'Attendance': []} # Finding students that are not in attendance list
    
    start_time = '14:00:00'
    end_time = '15:00:00' 

    previous_date = '0'
    for i in range(l_1): # loop for checking monday and thursday
        datetime_str = attendance.at[i, 'Timestamp'].strip() 
        current_date = datetime_str[:10] 
        datetime_object = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S') 
        day = datetime_object.strftime('%A') 
        if((day == 'Monday') | (day == 'Thursday')): 
            if(current_date != previous_date):
                lec_date.append(current_date)
                previous_date = current_date
    lec_date.sort(key=sortDates) #sorting the lec_date array

    for i in range(l_2): # Finds all the students name and roll 
        stud_roll = str(students_registered.at[i, 'Roll No'].strip()).upper()
        stud_name = str(students_registered.at[i, 'Name'].strip()).upper()
        students['Attendance'].append(f'{stud_roll} {stud_name}')

    l_2 = l_2 - 1        
    while(l_2 != 0): #this loop finds the stuents are absent in the class
        if(students['Attendance'][l_2] not in attendance['Attendance'].values): 
            absent_stud['Attendance'].append(students['Attendance'][l_2])
            absent_stud['Timestamp'].append('')
        l_2 -= 1

    absent_stud = pandas.DataFrame(absent_stud)
    attendance = pandas.concat([attendance, absent_stud], ignore_index=True)  
        
    
    individual_report = {'Roll': [], 'Name': [], 'Total attendance count': [], 'Real': [], 'Duplicate': [], 'Invalid': [], 'Absent': []} #  store the individual data of students

    for date in lec_date: 
        stud_info[f'{date}'] = []

    stud_info['Total lecture taken'] = [] 
    stud_info['Actual attendance count'] = []
    stud_info['Fake attendance count'] = []
    stud_info['Absent attendance count'] = []
    stud_info['% Attendance'] =  []

    attendance = attendance.sort_values(['Attendance','Timestamp'], ascending=[True,True], ignore_index=True) 
    while (i<l_1): 
        datetime_str = attendance.at[i, 'Timestamp'].strip() 
        time = datetime_str[11:]
        
        try:
            datetime_obj = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S') # Converting datetime str to datetime object with the specified format
            day = datetime_obj.strftime('%A') # Gives the weekday
        except:
            pass 
        
        date = datetime_str[:10]
        user = str((attendance.at[i, 'Attendance'])).strip() 
        roll =  user[0:8]
        name = user[9:]
        flag = False 
        j = i 

        if((roll in students_registered['Roll No'].values) & (name in students_registered['Name'].values)): 
            if((roll not in stud_info['Roll']) & (name not in stud_info['Name'])): 
                #appending in the main file
                stud_info['Name'].append(name) 
                stud_info['Roll'].append(roll)
                stud_info['Total lecture taken'].append(len(lec_date))
                stud_info['Actual attendance count'].append(0)
                stud_info['Fake attendance count'].append(0)
                stud_info['Absent attendance count'].append(0)
                stud_info['% Attendance'].append(0.00)
                #appending in individual report file
                individual_report['Name'].append(name)
                individual_report['Roll'].append(roll)
                individual_report['Total attendance count'].append([0]*len(lec_date))
                individual_report['Real'].append([0]*len(lec_date))
                individual_report['Duplicate'].append([0]*len(lec_date))
                individual_report['Invalid'].append([0]*len(lec_date))
                individual_report['Absent'].append([1]*len(lec_date))
                KAL=0
                for i in range (81):
                    KAL=KAL+1
                for dates in lec_date: 
                    stud_info[f'{dates}'].append('A')
            if((roll in stud_info['Roll']) & (name in stud_info['Name'])): 
                index = stud_info['Roll'].index(roll) 
                index2 = individual_report['Roll'].index(roll)
                if((time <= start_time) | (time >= end_time)): 
                    stud_info['Fake attendance count'][index] += 1 
                    if KAL==81:
                        try: # For mondays and thursdays
                            date_index = lec_date.index(date) 
                            individual_report['Invalid'][index2][date_index] += 1 
                            individual_report['Total attendance count'][index2][date_index] += 1 
                            individual_report['Absent'][index2][date_index] = 1 - individual_report['Real'][index2][date_index] 
                        except:
                            pass
                else: 
                    if((day == 'Monday') | (day == 'Thursday')): 
                        date_index = lec_date.index(date) 
                        if((time >= start_time) & (time <= end_time)): 
                            individual_report['Total attendance count'][index2][date_index] += 1 
                            if(individual_report['Real'][index2][date_index] == 0): 
                                individual_report['Real'][index2][date_index] = 1
                                individual_report['Absent'][index2][date_index] = 1 - individual_report['Real'][index2][date_index] 
                            else:
                                individual_report['Duplicate'][index2][date_index] += 1 # Adds to duplicate if attendnace is done more than once in lecture hours
                            stud_info[f'{date}'][index] = 'P' # Appends present for that particular date for the particular individual in consolidated report if present found
                            stud_info['Actual attendance count'][index] += 1 # Similarly, updates actual attendance count
                            if(i != l_1-1): # If the row being checked is not last row, checks for consecutive attendance
                                next_attendance_at = attendance.at[i+1, 'Timestamp'].strip() # Extracts next row's datetime
                                if(next_attendance_at == datetime_str): # Implies that there are more than one attendance on a particular day
                                    flag = True # Checks for duplicate attendnaces
                                    number=KAL+3
                                    while(flag == True): # Checks till unique attendance is not found
                                        current_date = attendance.at[j,'Timestamp'].strip() 
                                        next_date = attendance.at[j+1,'Timestamp'].strip() 
                                        current_user = str(attendance.at[j, 'Attendance']).strip()
                                        next_user = str(attendance.at[j+1, 'Attendance']).strip()
                                        current_name = current_user[9:].upper()
                                        next_name = next_user[9:].upper()
                                        current_roll = current_user[0:8].upper()
                                        next_roll = next_user[0:8].upper()
                                        if((current_name == next_name) & (current_roll == next_roll) & (current_date == next_date)): # If the same person has done his attendance more than once on same day
                                            individual_report['Duplicate'][index2][date_index] += 1
                                            individual_report['Total attendance count'][index2][date_index] += 1
                                            j += 1
                                            KAL=number
                                        else:
                                            flag = False

                    individual_report['Absent'][index2][date_index] = 1 - individual_report['Real'][index2][date_index] # Updates the absent count in individual report

                stud_info['Absent attendance count'][index] = len(lec_date) - stud_info['Actual attendance count'][index] # Updates the absent count in consolidated report
                percentage = stud_info['Actual attendance count'][index]/len(lec_date) * 100 # Finds the % attendance
                stud_info['% Attendance'][index] = round(percentage, 2) # Rounds off the % to 2 decimal digits
        i = j 
        i += 1

    individual_data = {'Date': [], 'Name': [], 'Roll': []} # Dictionary for individual dataframe
    for date in lec_date: # Appends the lecture date(name and roll default values as emtpy string which will later get replaced. This is done to make dictionary of uniform dimension so that it can be converted to dataframe later)
        individual_data['Date'].append(date)
        individual_data['Name'].append('')
        individual_data['Roll'].append('')

    for i in range(len(individual_report['Roll'])): # Loops overs students in individual report
        individual_data['Name'][0] = individual_report['Name'][i] # Replaces the first element of Name by Name of student being looped over
        individual_data['Roll'][0] = individual_report['Roll'][i]# Replaces the first element of Roll by Roll of student being looped over
        individual_data['Total attendance count'] = individual_report['Total attendance count'][i] # Total attendance count, real, duplicate, invalid and absent of that particular student being added/replaced in dataframe
        individual_data['Real'] = individual_report['Real'][i] 
        individual_data['Duplicate'] = individual_report['Duplicate'][i]
        individual_data['Invalid'] = individual_report['Invalid'][i]
        individual_data['Absent'] = individual_report['Absent'][i]

        individual_df = pandas.DataFrame(individual_data) # Converting the individual report dictionary to dataframe
        individual_df.to_excel(f"output/{individual_data['Roll'][0]}.xlsx", index=False) # Outputs the file in excel format for that particular roll no.

        
    consolidated_data = pandas.DataFrame(stud_info) # Converting consolidated report to dataframe
    consolidated_data.to_excel('output/attendance_report_consolidated.xlsx', index=False) # Outputs the file in excel format

from platform import python_version
ver = python_version()






attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
