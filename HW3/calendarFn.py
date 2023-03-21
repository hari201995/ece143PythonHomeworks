import calendar as cal

def number_of_days(year,month):
    ''' Returns the number of days in a month
    :year param: Input
    :month param: Input
    :days param  : Output
    '''
    assert type(year)== int and year >0, 'wrong year'
    assert type(month) == int and month in range(1,12), 'Wrong Month'
    days = cal.monthrange(year, month)
    return days[1]

def number_of_leap_years(year1,year2):
     ''' Returns the number of leap years between 2 years
     :year1,year2 param: 2 input years
     :output param: Number of leap years
     '''
     assert type(year1) is int and type(year2) is int,'wrong inputs'
     assert year1>0 and year2 >0,'wrong years'
     return cal.leapdays(year1,year2)

def get_day_of_week(year,month,day):
    ''' Gives the day pertaining to a particular day
    :year param: input
    :month param: input
    :day param:
    '''
    assert type(day)==int and type(month)==int and type(year)==int,'wrong data type'
    assert day>0 and month>0 and year>0,'wrong inputs'
    return cal.day_name[cal.weekday(year, month, day)]
