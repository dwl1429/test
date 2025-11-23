def hasonemom(a):
    return(len(mother_list[a]) == 1)
def hasonechd(a):
    return(len(children_list[a]) == 1)



T = int(input())
rlist = []
inpi = 0

for i in range(T):
    inp = (input()).split(' ')
    nodeN , edgeN = (tuple(list(map(int, inp))))
    inp = (input()).split(' ')
    Time_list = [0]
    for i in inp:
        Time_list.append(int(i))
    children_list = []
    mother_list = []
    for i2 in range(nodeN+1):
        children_list.append(set())
        mother_list.append(set())
    for i3 in range(edgeN):
        inp = (input()).split(' ')
        children_list[int(inp[1])].add(int(inp[0]))
        mother_list[int(inp[0])].add(int(inp[1]))
    for i2 in range(nodeN):
        i2+= 1
        if children_list[i2] == set():
            children_list[i2] = set([0])
            mother_list[0].add(i2)
    inp = (input())
    inpi += 3+edgeN
    lastW = int(inp)j
    Max_time = Time_list[lastW]
    done = False
    while not done:
        k = 0
        for i2 in range(nodeN):
            i2 += 1
            if i2 != lastW and Time_list[i2] != -1:
                if len(mother_list[i2]) == 0:
                    for i3 in children_list[i2]:
                        mother_list[i3].discard(i2)
                    Time_list[i2] = -1
                    children_list[i2] = set()
                    mother_list[i2] = set()
                    k += 1
                elif hasonemom(i2):
                    if hasonechd(i2):
                        a = tuple(children_list[i2])[0]
                        b = tuple(mother_list[i2])[0]
                        if hasonechd(b) and hasonemom(a):
                            children_list[b] = set([a])
                            mother_list[a] = set([b])
                            Time_list[b] += Time_list[i2]
                            Time_list[i2] = -1
                            children_list[i2] = set()
                            mother_list[i2] = set()
                            k += 1
                        elif not hasonechd(b) and not hasonemom(a):
                            d = []
                            for i3 in children_list[b]:
                                if i3 != i2 and i3 != lastW:
                                    if len(children_list[i3]) == 1:
                                        d.append(tuple(children_list[i3])[0])
                            if a in d:
                                    i3 = tuple(mother_list[a])[0]
                                    n=0
                                    while i3 == lastW:
                                        i3 = tuple(mother_list[a])[n]
                                        n+=1
                                    i4 = tuple(mother_list[a])[0]
                                    n=0
                                    while i4 == lastW or i4 == i3:
                                        i4 = tuple(mother_list[a])[n]
                                        n+=1
                                    if Time_list[i3] > Time_list[i4]:
                                        Time_list[i4] = -1
                                        children_list[b].discard(i4)
                                        mother_list[a].discard(i4)
                                        children_list[i4] = set([0])
                                        mother_list[i4] = set()
                                        k += 1
                                    else:
                                        Time_list[i3] = -1
                                        children_list[b].discard(i3)
                                        mother_list[a].discard(i3)
                                        children_list[i3] = set([0])
                                        mother_list[i3] = set()
                                        k += 1
                        elif hasonechd(b) and hasonemom(b):
                            children_list[b].add(a)
                            mother_list[a].add(b)
                            children_list[b].discard(i2)
                            mother_list[a].discard(i2)
                            Time_list[b] += Time_list[i2]
                            Time_list[i2] = -1
                            children_list[i2] = set()
                            mother_list[i2] = set()
                            k += 1
                else:
                    acl = set()
                    aml = set()
                    for i5 in mother_list[i2]:
                        acl.add(i5)
                        for i6 in mother_list[i5]:
                            aml.add(i6)
                    for i7 in aml:
                        if i7 in mother_list[i2]:
                            mother_list[i2].discard(i7)
                            children_list[i7].discard(i2)
                            k += 1
                    

        if hasonechd(lastW):
            lc = tuple(children_list[lastW])[0]
            if lc == 0:
                done = True
                break
        if k == 0:
            done = True
            break
    if hasonechd(lastW):
        lc = tuple(children_list[lastW])[0]
        if lc == 0:
            Max_time = Time_list[lastW]
        else:
            if hasonechd(lc):
                Max_time = Time_list[lastW] + Time_list[lc]
            else:
                Max_time = -1
    else:
        Max_time = -1
    rlist.append(Max_time)

for r in rlist:
    print(r)