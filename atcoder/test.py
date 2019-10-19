import itertools

tmp = [ [ [1,2], [3,4] ], [ [5,6] , [7,8] ], [ [9,10] , [11,12] ] ]
tmp

a=list(map(list,zip(*tmp)))
for i in a:
    p=list(itertools.chain.from_iterable(i))
    print(p)


for row in tmp:
    a=list(map(list,zip(*tmp)))
    print(a)
