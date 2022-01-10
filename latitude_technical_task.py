def function(lst):
    l = len(lst)
    a = []
    for i in range(l):
        if 0 in lst:
            lst.remove(0)
            a.append(0)
    lst.extend(a)
    print((lst))


num_list1 = [12,0,16,0,0,0,20,70]
num_list2 = [90,0,20,0,0,80,10,0]

function(num_list1)
function(num_list2)