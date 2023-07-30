# Calendar

      import calendar
      The calendar module allows you to output calendars and provides additional useful functions for them.

# calendar.setfirstweekday(weekday)
    Sets the weekday (0 is Monday, 6 is Sunday) to start each week.
    The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY are provided for convenience.
    For example, to set the first weekday to Sunday:
    
    import calendar
    calendar.setfirstweekday(calendar.SUNDAY)

# calendar.firstweekday()
    Returns the current setting for the weekday to start each week.

# calendar.isleap(year)
    Returns True if year is a leap year, otherwise False.
  
    calendar.isleap(2020)
    -->True

# calendar.leapdays(y1, y2)
    Returns the number of leap years in the range from y1 to y2 (exclusive), where y1 and y2 are years.

   calendar.leapdays(2000,2024)
   ->6
   2000,2004,2008,2012,2016,2020

# calendar.weekday(year, month, day)
    Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

# calendar.weekheader(n)
    Return a header containing abbreviated weekday names. n specifies the width in characters for one weekday.

    mon tue wed thu fri sat sun

# calendar.monthrange(year, month)
    Returns weekday of first day of the month and number of days in month, for the specified year and month.

# calendar.monthcalendar(year, month)
    Returns a matrix representing a month’s calendar. Each row represents a week; days outside of the month a represented by zeros. Each week begins with Monday unless set by setfirstweekday().
