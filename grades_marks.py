from collections import Iterable
import argparse


class Mapper(dict):

    """A class that maps values in range [0,100] to grades S through F"""

    def __missing__(self, mark):
        """Maps all the input values to grades

        :mark - Marks in range [0,100]
        :returns: v - Grades 'S' through 'F'

        """

        for k, v in self.items():
            if isinstance(k, Iterable):
                lower, upper = k
                if lower <= mark < upper:
                    self[mark] = v
                    return v
        raise KeyError("{} out of range".format(mark))


def main(mark):

    grades_dist = {(0, 49): "F",
                   (50, 59): "D",
                   (60, 69): "C",
                   (70, 79): "B",
                   (80, 89): "A",
                   (90, 101): "S"}

    mapper = Mapper(grades_dist)
    print "Grade for the mark {mark} : {grade}".format(mark=mark,
                                                       grade=mapper[mark])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maps all the input " + \
                                     "values to grades')
    parser.add_argument('mark',
                        type=int,
                        help='Integer value in the range 0,100')
    args = parser.parse_args()
    main(args.mark)
