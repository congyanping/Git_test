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
    time.sleep(i)
print "hello"
a=1
b=2
c=3
d=4
print a,b,c,d
