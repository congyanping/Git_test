import contextlib
@contextlib.contextmanager
def make_context(name):
    print 'entering:',name
    yield name
    print 'exiting :',name
with contextlib.nested(make_context('A'),
        make_context('B')) as (A,B):
    print 'inside with statement:',A,B
print 'it is really good for this'
class Door(object):
    def __init__(self):
        print '__init__()'
    def close(self):
        print 'close()'
print 'Normal Eeample:'
with contextlib.closing(Door()) as door:
    print 'inside with statement'
print '\nError handing example'
try:
    with contextlib.closing(Door()) as door:
        print 'raising from inside with statement'
        raise RuntimeError('error messagge')
except Exception,err:
    print 'hand an error',err

#when sleeping the clock is not changed
import time
for i in range(6,1,-1):
    print '%s %0.2f %0.2f' %(time.ctime(),
            time.time(),
            time.clock())
    print 'Sleeping',i
    #time.sleep(i)
print "hello"

print '#'*40
import time
def show_struct(s):
    print 'tm_year',s.tm_year
    print 'tm_mon',s.tm_mon
    print 'tm_mday',s.tm_mday
    print 'tm_hour',s.tm_hour
    print 'tm_min',s.tm_min
    print 'tm_sec',s.tm_sec
    print 'tm_wday',s.tm_wday
    print 'tm_yday',s.tm_yday
    print 'tm_isdst',s.tm_isdst

print 'gmtime'
show_struct(time.gmtime())
print '\nlocaltime'
show_struct(time.localtime())
print '\nmktime',time.mktime(time.localtime())
print '%d years ago' % int(time.mktime(time.localtime())/3600/24/365)

print '#'*40
import os
def show_zone_info():
    print 'TZ',os.environ.get('TZ','(not set)')
    print 'tzname',time.tzname
    print 'Zone: %d (%d)' %(time.timezone,
            (time.timezone/3600))
    print 'DST',time.daylight
    print 'Time',time.ctime()
    print
print 'Default'
show_zone_info()
ZONES = ['GMT',
        'Europe/Ameterdam',
        ]
for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print zone,':'
    show_zone_info()

print '#'*40
#datatime module
import datetime
t = datetime.time(1,2,3)
print t
print t.hour,t.minute,t.second,t.microsecond,t.tzinfo
print datetime.time.min
print datetime.time.max
print datetime.time.resolution
today = datetime.date.today()
print today
print 'ctime',today.ctime()
tt = today.timetuple()
print 'tuple : tm_year -',tt.tm_year
print 'tt',tt

print '#'*40
#733114 day total 2018 year
o = 734103
print 'fromordinal(o)',datetime.date.fromordinal(o)
print 'fromtimestamp(time.time())',datetime.date.fromtimestamp(time.time())
print 'Earlist data',datetime.date.min
print 'latest data',datetime.date.max
print 'Resolution is',datetime.date.resolution
d1 = datetime.date(2015,5,17)
print 'd1 is today' , d1
d2=d1.replace(year= 2019)
print 'd2 is two years later', d2
print '#'*40
print "datetime add minus multiply divide"
today = datetime.datetime.today()
print 'Today:',today
one_day =datetime.timedelta(days=1)
print 'one_day',one_day
yesterday = today -one_day
print 'yesterday',yesterday
print 'tomorrow',today +one_day



print '#'*40
print 'datetime.time()',datetime.time(12,55,0)
print 'time.time()',time.ctime()
print datetime.date.today()
print 'utc time',datetime.datetime.utcnow()
print 'now time',datetime.datetime.now()
print "getattr(d=datetime.datetime.now(),'year')=",getattr(datetime.datetime.now(),'year')


print '#'*40
t=datetime.time(1,2,3)
d=datetime.date.today()
dt=datetime.datetime.combine(d,t)
print 't is equal',t
print 'd is equal',d
print 'datetime.combine(d,t) is equal',dt
a=1
b=2
c=3
d=4
print a,b,c,d
