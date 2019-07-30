def calculateView(skyscrapersList):
    count = 0
    tallest = 0
    for i in skyscrapersList:
        if isinstance(i, int) and tallest < i:
            count += 1
            tallest = i

    return count

def cyclicEquiv(u, v):
    # 2019-07-29, https://stackoverflow.com/questions/31000591/check-if-a-list-is-a-rotation-of-another-list-that-works-with-duplicates
    n = len(u)
    if n != len(v):
        return False

    i = j = 0
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

def citiesEqual(city1, city2):
    view1 = listViews(city1)
    view1 = [view1[i:i+4] for i in range(0, len(view1), 4)]
    view2 = listViews(city2)
    view2 = [view2[i:i+4] for i in range(0, len(view2), 4)]
    return cyclicEquiv(view1, view2) or cyclicEquiv(view1, view2[::-1])

def listViews(city):
    views = []

    #Down the left
    for line in city:
        view = calculateView(line)
        views.append(view)

    #Across the bottom
    for i in range(len(city[0])):
        line = extractColumn(city, i)
        revLine = line[::-1]
        view = calculateView(revLine)
        views.append(view)

    #Up the right
    for line in city[::-1]:
        revLine = line[::-1]
        view = calculateView(revLine)
        views.append(view)

    #Back across the top
    for i in range(len(city[0]) - 1, -1, -1):
        line = extractColumn(city, i)
        view = calculateView(line)
        views.append(view)

    return views

def extractColumn(city, col):
    line = []
    for i in city:
        line.append(i[col])

    return line
