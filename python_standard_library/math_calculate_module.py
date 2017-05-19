import decimal
import pprint 
context = decimal.getcontext()
print 'Emax = ',context.Emax
print 'Emin = ',context.Emin
print 'capitals =',context.capitals
print 'prec =',context.prec
print 'rounding =',context.rounding
print 'flags =',pprint.pprint(context.flags)
print 'traps =',pprint.pprint(context.traps)


d = decimal.Decimal('0.123456')
for i in range(4):
    decimal.getcontext().prec = i
    print i,':',d,d*1


#fractions module
print '#'*20 +'fraction module'+'#'*20
import fractions
for n,d in [(1,2),(2,4),(3,6)]:
    f = fractions.Fraction(n,d)
    print '%s/%s = %s' %(n,d,f)

for s in ['0.5','1.3','2.0']:
    f = fractions.Fraction(s)
    print '%s = %s'%(s,f)
for v in [0.1,0.5,1.5,2.0]:
    print '%s = %s' %(v,fractions.Fraction.from_float(v))
    print type(v)
for v in [decimal.Decimal('0.1'),
        decimal.Decimal('0.5'),
        decimal.Decimal('1.5'),
        decimal.Decimal('2.0')]:
    print '%s = %s'%(v,fractions.Fraction.from_decimal(v))

f1=fractions.Fraction(1,2)
f2=fractions.Fraction(3,4)
print 'f1+f2 = ',f1+f2
print 'f1-f2 = ',f1-f2
print 'f1/f2 = ',f1/f2
print 'f1*f2 = ',f1*f2

import math
print 'Pi',math.pi
f_pi = fractions.Fraction(str(math.pi))
print 'No limit =',f_pi
for i in [1,6,11,60,70,90,100]:
    limited = f_pi.limit_denominator(i)
    print '{0:8} = {1}'.format(i,limited)

#random
print '#'*20+'random module'+'#'*20
import random 
for i in xrange(5):
    print '%04.3f'% random.random()
print
for i in xrange(5):
    print '%04.3f'%random.uniform(1,100)
print

#simulate rolling the dice
import itertools
outcomes = {'heads':0,
        'tailes':0}
sides=outcomes.keys()
for i in range(6):
    outcomes[random.choice(sides)]+=1
print 'Heads :',outcomes['tailes']
print 'Tailes :',outcomes['heads']


