from itertools import permutations
import tools
import collections

def pretty(chunkView):
    n = len(chunkView[0])
    print('', end=' ')
    for i in chunkView[0]:
        print(i, end=' ')
    print()
    for i in range(n):
        print(chunkView[3][-i], ' '*(n+1), chunkView[1][i])

    print('', end=' ')
    for i in chunkView[2][::-1]:
        print(i, end=' ')
    print()
    print()


N = 4

basicRow = list(range(1, N + 1))
rowPerms = permutations(basicRow)
rowPerms = list(map(list, rowPerms))

def rowsBelow(citySoFar):
    if len(citySoFar) >= N:
        yield citySoFar
    else:
        for i in rowPerms:
            c = citySoFar[:]
            c.append(i)

            fail = False
            for j in range(len(c[0])):
                col = tools.extractColumn(c, j)
                if len(col) != len(set(col)):
                    fail = True

            if not fail:
                for newCity in rowsBelow(c):
                    yield newCity

cnt = collections.Counter()
cityGen = rowsBelow([])
for city in cityGen:
    view = tools.listViews(city)
    viewChunks = [tuple(view[i:i+4]) for i in range(0, len(view), 4)]
    hViewChunks = viewChunks[::-1]
    vViewChunks = [l[::-1] for l in viewChunks]
    allChunks = []
    for i in range(4):
        allChunks.append(viewChunks[:i] + viewChunks[i:])
        allChunks.append(hViewChunks[:i] + hViewChunks[i:])
        allChunks.append(vViewChunks[:i] + vViewChunks[i:])
    minView = min(allChunks)
    minView = tuple(minView)
    cnt[minView] += 1

#for view, c in cnt.items():
    #if c == 1:
        #pretty(view)

print(cnt.most_common())
