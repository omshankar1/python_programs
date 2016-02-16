from itertools import permutations, combinations, tee, izip

# points_tuple has list of lat, lon
points_tuple = [("x1", "y1"),
                ("x2", "y2"),
                ("x3", "y3"),
                ("x4", "y4"),
                ("x5", "y5"),
                ("x6", "y6")]


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def all_paths(points_tuple):
    "All pairs of points from the given list points_tuple"
    for index, pair in enumerate(permutations(points_tuple, 2)):
        print "{index} : {point1} ==> {point2}".format(index=index+1,
                                                       point1=pair[0],
                                                       point2=pair[1])


def sequencer(points_tuple):
    "Pair of points in the given sequence to construct a path"
    for pt1, pt2 in pairwise(points_tuple):
        print "{point1} ==> {point2}".format(point1=pt1, point2=pt2)

if __name__ == "__main__":
    all_paths(points_tuple)
    sequencer(points_tuple)
