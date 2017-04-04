class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,data):
        self._birth = data
    @property
    def age(self):
        return 2017 - self._birth
p =Student()
p.birth = 1992
print "my birth is",p.birth ,"so my age is",p.age
