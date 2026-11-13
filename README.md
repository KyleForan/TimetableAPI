# Interface for TUD timetables

## Introduction
This is an API that allows for simple use of TU Dublins timetable using fastAPI.  
  
## Features
`/rooms?name=<string>` Search for the ID of a specific room  
`/course?name=<string>` Search for the ID of a specific course  
`/timetable/<category>/<id>?group=<string>?day=<string>`:  
 - category is 'rooms' or 'course'
 - id is the string gotten from the other endpoints
 - group filters the response to a specific group or all (typically used in lecture bookings)
 - day filters for specific days of the week
  
## TODO list
./src/timetable/main.py:                        # TODO: User input  
./src/timetable/main.py:                        # TODO: Handle Null  
./src/timetable/main.py:                        # TODO: Handle API error  
./src/timetable/main.py:                        # TODO: better handling  
./src/timetable/main.py:                        # TODO: Handle API error  
./src/timetable/main.py:                        # TODO: Actual Output  
./src/timetable/utils/parsers.py:               # TODO: Handle multiple selections  
./src/timetable/utils/constants.py:             # TODO: Add other types  
./src/timetable/api.py:                         # TODO: FIX GROUP FILTERING  
