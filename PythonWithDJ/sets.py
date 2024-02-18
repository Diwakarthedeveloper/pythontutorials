s = set() #this is emplty set
# l = [1, 2, 3, 4]
# S_from_list = set(l) 
# print(S_from_list)
# print(type(S_from_list))

s.add(1)
s.add(2)
s.union({1,2,})
s.union({1,2,3})
print(s)

s1 = s.intersection({1,2,3})
print(max(s))
s.remove(2)
print(max(s))
s2= {4,6}
print(s.isdisjoint(s2))