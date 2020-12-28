def add_time(start, duration, day=''):
    [startTime, ending] = start.split(' ')
    [startH, startMin] = [int(x) for x in startTime.split(':')]
    [durationH, durationMin] = [int(x) for x in duration.split(':')]

    newMin = startMin + durationMin
    newH = 1 if newMin >= 60 else 0
    newMin = newMin - 60 if newMin >= 60 else newMin
    newMin = str(newMin).zfill(2) if newMin < 10 else newMin
    newH += startH + durationH

    days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    if day in days_of_the_week:
        day = (days_of_the_week.index(day) + round(newH / 24)) % 7
        day = days_of_the_week[day]

    daysAfter = ''
    if durationH >= 24 and durationMin:
        daysAfter = f'({round(newH / 24)} days later)'
    elif ending == 'PM' and (12 - startH) < durationH or (
            24 - startH) < durationH:
        daysAfter = '(next day)'

    if ((durationH % 12) + startH) >= 11:
        ending = 'PM' if ending == 'AM' else 'AM'

    newH = (newH % 12) or 12

    new_time = f'{newH}:{newMin} {ending}'
    if 'daysAfter' in locals():
        new_time += f'{day} {daysAfter}'

    return new_time
