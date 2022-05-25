import classes
import datetime 

####### READING THE INPUT FILES #######


## READING THE INPUT FOR THE FESTIVAL ##

file = open(r"input_festival.txt","r")
file_festival = file.readlines()

# Number of days of the festival

D = file_festival[1]

days = []
job_types = set()
date = {'year':None, 'month':None, 'day':None}
l = 3
while l < len(file_festival)-1:
    l += 1 
    line = file_festival[l].split()
    date['year'] = int(line[0])
    date['month'] = int(line[1])
    date['day'] = int(line[2])
    jobs = []
    for j in range(l+1,len(file_festival)):
        line = file_festival[j].split()
        if "DAY" in line:
            break
        starting_time = datetime.datetime(date['year'],date['month'],date['day'],int(line[0]),int(line[1]))
        ending_time = datetime.datetime(date['year'],date['month'],date['day'],int(line[2]),int(line[3]))
        job_type = line[4]
        min_nb_volunteers = int(line[5])
        pref_nb_volunteers = int(line[6])
        jobs.append(classes.Job(classes.Time_slot(starting_time,ending_time),job_type,min_nb_volunteers,pref_nb_volunteers))
        job_types.add(job_type)
    days.append(classes.Day(datetime.date(date['year'],date['month'],date['day']), jobs))
    l = j

file.close()

## READING THE VOLUNTEERS INPUT ##

file_volunteers = open(r"input_volunteers.txt","r")
file_volunteers = file_volunteers.readlines()

V = file_volunteers[1]

volunteers = []

l = 3
while l < len(file_volunteers)-1:
    l += 1
    line = file_volunteers[l].split()
    id = line[0]
    print('New volunteer')
    print(l)
    print('id', id)
    #Read preferences
    preferences = {jt:0 for jt in job_types}
    for j in range(l+2,l+2+len(job_types)):
        line = file_volunteers[j].split()
        preferences[line[0]] = int(line[1])
    #Read availability
    availability = []
    l = j + 2
    while l < len(file_volunteers)-1:
        l += 1 
        line = file_volunteers[l].split()
        date['year'] = int(line[0])
        date['month'] = int(line[1])
        date['day'] = int(line[2])
        for k in range(l+1,len(file_volunteers)):
            line = file_volunteers[k].split()
            if "DAY" in line or 'ID' in line:
                break
            starting_time = datetime.datetime(date['year'],date['month'],date['day'],int(line[0]),int(line[1]))
            ending_time = datetime.datetime(date['year'],date['month'],date['day'],int(line[2]),int(line[3]))
            availability.append(classes.Time_slot(starting_time,ending_time))
        l = k
        if 'ID' in line:
            break

    volunteers.append(classes.Volunteer(id,preferences,availability))


