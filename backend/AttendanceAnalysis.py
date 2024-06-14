import pandas as pd
import os

os.chdir("./backend")

#cleaning and formatting data, sorted by date
attendance_data = pd.DataFrame( pd.read_csv('AttendanceLog.csv') )
attendance_data['first'] = attendance_data['first'].str.upper()
attendance_data['last'] = attendance_data['last'].str.upper()
attendance_data['computingID'] = attendance_data['computingID'].str.lower()
attendance_data = attendance_data.drop_duplicates()
attendance_data.sort_values('date', inplace=True)
attendance_data.rename(columns={
    'first': 'First',
    'last': 'Last',
    'computingID': 'Computing ID',
    'date': 'Date'
}, inplace=True)


#number of meetings attended by each person
num_attended = attendance_data.groupby(['Computing ID', 'First', 'Last']).size().reset_index(name='Meetings')

#Number of attendees per meeting
attendance_by_meeting = attendance_data.groupby(['Date']).size().reset_index(name="Attended")

#Attendance sorted by person
attendance_by_person = attendance_data.sort_values(['First', 'Last', 'Computing ID'])
attendance_by_person = attendance_by_person[['First', 'Last', 'Computing ID', 'Date']]

print("LOG: SORTED BY DATE")
print(attendance_data)
print()

print("TOTAL ATTENDANCE BY PERSON")
print(num_attended)
print()

print("TOTAL ATTENDANCE PER MEETING")
print(attendance_by_meeting)
print()

print("LOG: SORTED BY PERSON")
print(attendance_by_person)
print()



