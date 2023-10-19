a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["alekhya","mani","triveni"])
print(a.union(b))

#intersection
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["sumathi","mani","triveni"])

print(a.intersection(b))

#isdisjoint
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["alekhya","mani","triveni"])
print(a.isdisjoint(b))

a=frozenset(["sumathi"])
b=frozenset(["sumathi"])
print(a.isdisjoint(b))

#issubset
a = frozenset(["venky", "sumathi", "sagar"])
b = frozenset(["venky", "mani", "triveni"])
print(a.issubset(b))

a=frozenset(["sumathi"])
b=frozenset(["sumathi","sweety","sanju"])
print(a.issubset(b))

#issuperset
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["alekhya","mani","triveni"])
print(a.issuperset(b))

a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["sumathi"])
print(a.issuperset(b))

#diffrence
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["sumathi","mani","triveni"])
print(a.difference(b))


#symmetric_difference
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["alekhya","mani","triveni"])
print(a.symmetric_difference(b))

#copy
a=frozenset(["venky","sumathi","sagar"])
b=frozenset(["alekhya","mani","triveni"])
c1=a.copy()
c2=b.copy()
print(c1)
print(c2)


