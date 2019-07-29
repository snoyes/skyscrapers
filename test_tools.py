import tools

def test_calc_view_plain():
    l = [4, 3, 5, 2, 1, 6, 7]
    assert tools.calculateView(l) == 4

def test_calc_view_some_none():
    l = [4, 3, None, 2, 1, None, 7]
    assert tools.calculateView(l) == 2

def test_calc_view_all_none():
    l = [None, None, None]
    assert tools.calculateView(l) == 0

def test_calc_view_empy():
    l = []
    assert tools.calculateView(l) == 0

def test_cyclic_equiv_true():
    l1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 3, 4]
    l2 = l1[:5] + l1[5:]
    assert tools.cyclicEquiv(l1, l2) == True

def test_cyclic_equiv_false():
    l1 = [1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 3, 4]
    l2 = l1[:5] + l1[4:]
    assert tools.cyclicEquiv(l1, l2) == False

def test_list_views():
    city = []
    city.append([3, 1, 4, 2])
    city.append([4, 3, 2, 1])
    city.append([2, 4, 1, 3])
    city.append([1, 2, 3, 4])

    correctView = [2, 1, 2, 4, 3, 2, 2, 1, 1, 2, 4, 2, 3, 1, 3, 2]

    assert tools.listViews(city) == correctView

def test_extract_column():
    city = []
    city.append([3, 1, 4, 2])
    city.append([4, 3, 2, 1])
    city.append([2, 4, 1, 3])
    city.append([1, 2, 3, 4])

    assert tools.extractColumn(city, 2) == [4, 2, 1, 3]

def test_reflection_equal():
    city1 = []
    city1.append([3, 1, 4, 2])
    city1.append([4, 3, 2, 1])
    city1.append([2, 4, 1, 3])
    city1.append([1, 2, 3, 4])

    city2 = city1[::-1]

    assert tools.citiesEqual(city1, city2) == True
