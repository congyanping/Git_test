import os
#join path
import os.path
for parts in [('one','two','three'),('/','one','two'),('/one','/two','/three')]:
    print parts,':',os.path.join(*parts)

import pprint
def visit(arg,dirname,names):
    print dirname,arg
    for name in names:
        subname = os.path.join(dirname,name)
        if os.path.isdir(subname):
            print 'name %s'%name
        else:
            print 'name1 %s'%name
    print
if not os.path.exists('example'):
    pass

print '*'*20 +'glob module'+'*'*20
#glob module
import glob
for name in glob.glob('dir/*'):
    print name
for name in glob.glob('dir/file?.txt'):#? match one element
    print name
for name in glob.glob('dir/*[0-9].*'):
    print name

from shutil import *
#from command import *
print 'BRFORE'
#print getoutput('ls -rlast /tmp/example')
#copytree('../sutil','/tmp/example')

#pickle module
try:
    import cPickle as pickle
except:
    import pickle
data = [{'a':'A','b':'B','c':'C'}]
print 'Data:'
print data
import pprint 
pprint.pprint(data)
data_string = pickle.dumps(data)
print 'Pickle:%r'% data_string
data_1 = pickle.loads(data_string)
print 'load pickle data to normal\n',data_1
print 'data_1 == data is ',data_1 == data

from StringIO import StringIO
class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        self.name_backwards = name[::-1]
        return
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))
out_s = StringIO()
for o in data:
    print "'WRITING' : %s (%s)" % (o.name,o.name_backwards)
    pickle.dump(o,out_s)
    out_s.flush()
print 'out_s',out_s
in_s = StringIO(out_s.getvalue())
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ : %s (%s)'%(o.name,o.name_backwards)

import pickle
class Node(object):
    def __init__(self,name):
        self.name =name
        self.conections = []
    def add_edge(self,node):
        self.conections.append(node)
    def __iter__(self):
        return iter(self.conections)
def preorder_traversal(root,seen=None,parent=None):
    if seen is None:
        seen =set()
    yield (parent,root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        for parent,child in preorder_traversal(node,seen,root):
            yield (parent,child)
            #print 'parent.child',(parent,child)
def show_edges(root):
    for parent,child in preorder_traversal(root):
        if not parent:
            continue
        print '%5s -> %2s (%s)' %(parent.name,child.name,id(child))
root = Node('root')
a=Node('a')
b=Node('b')
c=Node('c')

root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)

print 'ariginal graph'
show_edges(root)
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print 'reloaded graph'
show_edges(reloaded)


