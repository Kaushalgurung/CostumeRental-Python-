#getting live time and date from system using inbuilt function 
def getDateTime():
    import datetime
    datetime=datetime.datetime.now()
    #print("Date and Time: ",datetime)
    dt_string = datetime.strftime("%d %b %Y")
    return str(dt_string)
def getTime():
    import datetime
    datetime=datetime.datetime.now()
    #print("Date and Time: ",datetime)
    t_string = datetime.strftime("%H:%M:%S")
    return str(t_string)