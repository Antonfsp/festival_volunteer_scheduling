
from functools import cached_property
from datetime import date, datetime

# Class for the festival

class Festival(): 

    def __init__(self,days,nb_volunteers,volunteers, jobs):
        self.nb_volunteers = nb_volunteers
        self.days = days
        self.volunteers = volunteers
        self.jobs = jobs

    @cached_property
    def job_types(self):
        return set([j.type for j in self.jobs])
    

# Class for the day

class Day():

    def __init__(self,date,jobs):
        self.date = date
        self.jobs = jobs


# Class for the jobs

class Job():

    def __init__(self,time_slot,type, min_nb_volunteers,pref_nb_volunteers):
        self.type = type
        self.time_slot = time_slot
        self.min_nb_volunteers = min_nb_volunteers
        self.pref_nb_volunteers = pref_nb_volunteers
        self.assigned_volunteers = []

    def job_day(self):
        return self.time_slot.day

    def job_duration(self):
        return (self.time_slot.ending_time-self.time_slot.starting_time).total_seconds()/3600

    def is_min_volunteers(self):
        return self.min_nb_volunteers <= len(self.assigned_volunteers)

    def is_pref_volunteers(self):
        return self.pref_nb_volunteers <= len(self.assigned_volunteers)

    def assign_volunteers(self, volunteer):
        self.assigned_volunteers.append(volunteer)
    
    def reject_volunteers(self,volunteer):
        self.assigned_volunteers.remove(volunteer)



# Class for the volunteers

class Volunteer():

    def __init__(self,id,job_preferences,availability):
        self.id = id
        self.availability = availability
        self.job_preferences = job_preferences
        self.jobs_assigned = []

    def add_time_slot_available(self,time_slot):
        self.availability.append(time_slot)



# Class time_slot

class Time_slot():
    
    def __init__(self,starting_time,ending_time):
        self.starting_time = starting_time
        self.ending_time = ending_time




