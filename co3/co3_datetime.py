import datetime
t=datetime.time(22,56,44)
print(t)
print("hour",t.hour)
print("minute",t.minute)
print("second",t.second)
print("microsecond",t.microsecond)


import datetime
t=datetime.time(22,56,44)  #time class
print(t)
print("Hour :",t.hour)
print("Minute :",t.minute)
print("Second :",t.second)
print("Microsecond :",t.microsecond)
print("......................................\n")
d=datetime.date.today()
print(d)
print("Year",d.year)
print("Month",d.month)
print("Day",d.day)
print("......................................\n")
d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2)
print(td)
d2=d1+td
print(d2)
print("......................................\n")
dt=datetime.datetime.combine(d,t)
print(dt)
