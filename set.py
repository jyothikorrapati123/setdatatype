#implicit
a={1,2,3,4}
print(a)
a={'a','b','c'}
print(a)
#explicit
a=set(('a','b','c'))
print(type(a))
#datatype/variable annotation
a:set={'a','b','c'}
print(type(a))
#created
#add
a={'a','b','c'}
a.add('d')
print(a)
#update
a={'a','b','c'}
a.update('e')
print(a)
#delete
a={'a','b','c'}
a.remove('c')
print(a)

#discard
a={'a','b','c'}
a.discard('d')
print(a)
#pop
a={'a','b','c'}
a.pop()
print(a)
#some other methods of set
#union
a={'a','b','c'}
b={'c','d','e'}
print(a.union(b))
#intersection
a={'a','b','c'}
b={'c','d','b'}
print(a.intersection(b))
#intersection update
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)
#isdisjoint
a:set={'a','c'}
b:set={'b'}
print(a.isdisjoint(b))
#difference
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.difference(b))
#symmetric difference
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.symmetric_difference(b))
#symmetric differnce update
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)
#is subset
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.issubset(b))

a:set={'b','c'}
b:set={'b','c','d'}
print(a.issubset(b))

#issuperset
a:set={'a','b','c'}
b:set={'b','c','d'}
print(a.issuperset(b))

a:set={'b','c'}
b:set={'b','b','c'}
print(a.issuperset(b))


