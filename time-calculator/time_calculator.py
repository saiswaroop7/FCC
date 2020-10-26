def add_time(start, duration, *args):
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ftime = ""
    day = ""
    d = str(*args)
    for i in range(len(days)):
      if(days[i].lower() == d.lower()):
        break
    beginh = start.split(" ")
    hh = beginh[0].split(":")
    dur = duration.split(":")
    meridian = beginh[1]
    finh = int(hh[0]) + int(dur[0])
    dcount = 0
    while (finh >= 12):
      if(meridian == "PM"):
          finh = finh - 12
          dcount = dcount + 1
          i = (i + 1) % len(days)
          d = days[i]
          meridian = "AM"
      else:
          finh = finh - 12
          meridian = "PM"
    if ((int(hh[1]) + int(dur[1])) >= 60):
      finh = finh + 1
      if (finh >= 11):
        finh = finh % 12
        i = (i + 1) % len(days)
        d = days[i]
        if(meridian == "PM"):
          dcount = dcount + 1
          meridian = "AM"
        else:
          i = (i + 1) % len(days)
          d = days[i]
          meridian = "PM"
    if(finh == 00):
      finh = 12
    elif(finh > 12):
      finh = finh % 12
    finm = (int(hh[1]) + int(dur[1])) % 60
    if (dcount == 1):
        day = " (next day)"
        if (len(args) == 1):
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + ", " + d + day
        else:
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + day
    elif (dcount == 0):
        if (len(args) == 1):
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + ", " + d
        else:
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + day
    elif (dcount > 1):
        day = " (" + str(dcount) + " days later)"
        if (len(args) == 1):
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + ", " + d + day
        else:
            ftime = str(finh) + ":" + "{:02d}".format(finm) + " " + meridian + day

    return ftime