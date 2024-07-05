# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    #list to store all the race times.
    Rhines_race_times = []
    
    #defining a get_time method to construct rhines times.
    def get_time():
        ...
    
    #condition to append rhines times to a list we'll return.
    for item in races.splitlines():
        if 'Jennifer Rhines' in item:
            Rhines_race_times.append(item)

    return Rhines_race_times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    
    pass
