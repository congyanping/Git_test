import functools
def myfunc(a,b=2):
    print 'called mfunc with:',(a,b)
    return
def show_details(name,f,is_partial=False):
    print '%s:' % name
    print 'object:',f
    if not is_partial:
        print '__name__:',f.__name__
    if is_partial:
        print 'func:',f.func
        print 'args:',f.args
        print 'keywords:',f.keywords
    return
show_details('myfunc',myfunc)
myfunc('a',3)
print
p1=functools.partial(myfunc,b=4)
print "p1",p1
show_details('partial with named default', p1 ,True)
p1('passing a')
p1('override b',b=5)
print


p2=functools.partial(myfunc,'default a',b=99)
show_details('partial with default',p2,True)
p2()
p2(b='override b')
print 
p1(1)

