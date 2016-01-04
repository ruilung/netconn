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

# result
:445 to :80 are listen ports on my desktop
remote address 192.168.3.41 connect to my desktop 10 times in collect periods

<pre>
Listen   Program name
--------------------------
:445     System                                                
:5357    System                                                
:55491   ?                                                     
:3389    svchost.exe                                           
:49671   lsass.exe                                             
:51384   C:\Program Files\WindowsApps\Microsoft.Messaging_2.12.15004.0_x86__8wekyb3d8bbwe\SkypeHost.exe
:139     System                                                
:50037   sqlservr.exe                                          
:49667   svchost.exe                                           
:49665   svchost.exe                                           
:139     System                                                
:49685   services.exe                                          
:49666   spoolsv.exe                                           
:135     svchost.exe                                           
:80      C:\tools\nginx-1.8.0\nginx.exe                        
:49664   wininit.exe                                           
:38415   C:\Program Files (x86)\Skype\Phone\Skype.exe          
:23443   C:\Program Files\Ditto\Ditto.exe                      
:80      C:\tools\nginx-1.8.0\nginx.exe                        

Listen   Program name                                           RemoteAddr  Count
--------------------------------------------------------------------------------
:38415   C:\Program Files (x86)\Skype\Phone\Skype.exe           192.168.3.41  10  

</pre>
