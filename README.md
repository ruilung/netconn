# netconn
collect network establish info
1. Get list of listening port
2. wait for an interval(default is 60 seconds) and collect remote address who connect to listen port.
3. check countdown to 0(default is 1440 times). if not go back to step2.
4. display collect info and write it to file. filename pattern is netconn_date_time_ix_cx.log
5. press ctrl+c to break waiting time. and write the result to file just like step 4.

# requirement
* [python](https://www.python.org/)
* [psutils](https://pypi.python.org/pypi/psutil)

# parameter
default
python netconn.py  or netconn.exe (win32)
> equal python netconn.py 60 1440 netconn_date_time_i60_c1440.log
> wait 60 seconds, collect connection info 1440 times, write to netconn_date_time_i60_c1440.log

quick result
python netconn.py 1 10
> wait 1 second, collect connection 10 times


