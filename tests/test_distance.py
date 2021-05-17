from mlproject.distance import haversine

def test_distance_type():
    assert type(haversine(48.865070, 2.380009, 49.865070, 3.380009))== type(32.23)
