from collections import OrderedDict
import random
class Last(OrderedDict):
    def __init__(self,capacity):
        super(Last,self).__init__()
        self._capacity = capacity
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self)-containsKey >=self._capacity:
            last =self.popitem(last =False)
            print 'remove',last
        if containsKey:
            del self[Key]
            print 'set:',(key,value)
        else:
            print 'add',(key,value)
        OrderedDict.__setitem__(self,key,value)
if __name__ == '__main__':
    L=Last(random.randint(1,3))
    L.__setitem__('a',1)
    print L
