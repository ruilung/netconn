import time
import sys
import psutil
import socket

def netlisten():
# get listen port and listen program  and return it as a list
    proc_names = {}
    for p in psutil.process_iter():
        try:
            proc_names[p.pid] = p.exe() #full path and program name
        except psutil.AccessDenied:
            proc_names[p.pid] = p.name () #only program name, windows system process will hit this
            pass
        except psutil.Error:
            pass
    netlist=[]
    for c in psutil.net_connections(kind='inet4'): #only receive ipv4 info
        if c.status=='LISTEN':
            netlist.append([  ":"+str(c.laddr[1]), proc_names.get(c.pid, '?')])
    return netlist

def netestablish():
    estblist=[]
    for c in psutil.net_connections(kind='inet4'):
        if c.status <> 'LISTEN' and c.raddr:
            estblist.append([  ":"+str(c.laddr[1]), c.raddr[0] ])
    return estblist


if __name__ == '__main__':
    if len(sys.argv) > 1:
        t=int(sys.argv[1])
    else:
        #t=60
        t=1

    if len(sys.argv) > 2:
        c=int(sys.argv[2])
    else:
        #c=1440
        c=10

    if len(sys.argv) > 3:
        filename=(sys.argv[3])
    else:
        filename="netconn_"+time.strftime("%Y%m%d_%H%M%S", time.gmtime())+"_i"+str(t)+"_c"+str(c)+".log"



    nlist= netlisten()
    timelist=[]
    ndict={}

    f=open(filename,"w")
    print "listen port, program name\n--------------------------"
    f.write("listen port, program name\n--------------------------\n")
    for nl in nlist:
        listen=",".join(nl)
        print listen
        f.write(listen+"\n")


    print "\nstart\n------\n* collect listen and establish info.\n* interval is %d.\n* countdown is %d\n* or press ctrl+c to break...\n" %(t,c)
    while c>0:
        c-=1
        t1=int(time.time())
        try:
          time.sleep(t)
        except KeyboardInterrupt:
          print "avg execute is %d\n" %(sum(timelist)/len(timelist))
          break

        elist=netestablish()
        for el in elist:
            for nl in nlist:
                if nl[0] == el[0]:
                    key= nl[0]+","+nl[1]+","+el[1]
                    ndict[key]=ndict.get(key,0)+1
        t2=int(time.time())
        if len(timelist) >= 10:
          timelist.pop(0)
        timelist.append(t2-t1)
        print 'countdown is %d'%(c)


    astr="\nListen   Program_name                                           RemoteAddr  Count\n--------------------------------------------------------------------------------\n"
    print astr
    f.write(astr)
    for nd in ndict:
        nddata=nd+","+str(ndict[nd])
        #print nddata
        alist=nddata.split(',')
        port=alist[0]
        prog=alist[1]
        raddr=alist[2]
        rcount=alist[3]
        s= "%-8s %-54s %-12s %-4s" %(port,prog,raddr,rcount)
        print s
        f.write(s+"\n")



    f.close()
