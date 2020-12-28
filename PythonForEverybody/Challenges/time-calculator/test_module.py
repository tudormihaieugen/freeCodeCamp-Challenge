def add_time(start, duration, day=''):
    # get info from arguments
    [startTime, endTime] = start.split(' ')
    [startH, startMin] = [int(x) for x in startTime.split(':')]
    [durationH, durationMin] = [int(x) for x in duration.split(':')]

    # start the timer
    newMin = startMin + durationMin
    newH = 1 if newMin >= 60 else 0
    newMin = newMin - 60 if newMin >= 60 else newMin
    newMin = str(newMin).zfill(2) if newMin < 10 else newMin
    newH += startH + durationH

    # validate the third argument
    new_time = f'{newH}:{newMin} {endTime}'
    newDays = round(newH / 24)
    week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if day in week:
        day = (week.index(day) + newDays) % 7
        day = week[day]
        new_time += f' {day},'

    # check for "days later" and "next day" cases
    daysAfter = ''
    if durationH >= 24 and durationMin:
        daysAfter = f'({newDays} days later)'
    elif endTime == 'PM' and (12 - startH) < durationH or (24 - startH) < durationH:
        daysAfter = '(next day)'
    new_time += f' {daysAfter}'

    return new_time
