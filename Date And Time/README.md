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
          Returns a matrix representing a month’s calendar.
          Each row represents a week; days outside of the month a represented by zeros.
          Each week begins with Monday unless set by setfirstweekday().


# Datetime

           import datetime

# Print current time
           x = datetime.datetime.now()
           print(x)

# The strftime() Method
            The datetime object has a method for formatting date objects into readable strings.
            The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

            x = datetime.datetime(2018, 6, 1)
            print(x.strftime("%B"))

            o/p-> June

            Directive	  Description	                                               Example
            %a	        Weekday, short version	                                    Wed	
            %A	        Weekday, full version	                                          Wednesday	
            %w	        Weekday as a number 0-6, 0 is Sunday	                        3	
            %d	        Day of month 01-31	                                          31	
            %b	        Month name, short version	                                    Dec	
            %B	        Month name, full version	                                    December	
            %m	        Month as a number 01-12	                                    12	
            %y	        Year, short version, without century	                        18	
            %Y	        Year, full version	                                          2018	
            %H	        Hour 00-23	                                                17	
            %I	        Hour 00-12	                                                05	
            %p	        AM/PM	                                                      PM	
            %M	        Minute 00-59	                                                41	
            %S	        Second 00-59	                                                08	
            %f	        Microsecond 000000-999999	                                    548513	
            %z	        UTC offset	                                                +0100	
            %Z	        Timezone	                                                      CST	
            %j	        Day number of year 001-366	                                    365	
            %U	        Week number of year, Sunday as the first day of week, 00-53	52	
            %W	        Week number of year, Monday as the first day of week, 00-53	52	
            %c	        Local version of date and time	                              Mon Dec 31 17:41:00 2018	
            %C	        Century	                                                      20	
            %x	        Local version of date	12/31/18	
            %X	        Local version of time	17:41:00	
            %%	        A % character	                                                %	
            %G	        ISO 8601 year	                                                2018	
            %u	        ISO 8601 weekday (1-7)	                                    1	
            %V	        ISO 8601 weeknumber (01-53)

# Strptime() method
            strptime() is another method available in DateTime which is used to format the time stamp which is in string format to date-time object.

            Syntax: datetime.strptime(time_data, format_data)


