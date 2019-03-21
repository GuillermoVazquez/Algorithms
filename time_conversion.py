def stringManipulation(time):

    part = time[8:10]
    hour = int(time[:2])

    if(part == "AM" and hour == 12):
        hour = "00"
    elif(part == "PM" and hour == 12):
        hour = "12"
    elif(part == "PM" and part != "AM"):
        hour+=12

    hour = str(hour)
    if(len(hour) == 1):
        hour = "0" + hour
    result = hour + time[2:8]
    return result

if __name__ == '__main__':
    time = "06:40:03AM"
    stringManipulation(time)
