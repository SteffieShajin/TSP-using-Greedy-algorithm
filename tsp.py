import matplotlib.pyplot as plt
import math
import copy
import statistics


class Point:
    def __init__(s, x, y):
        s.x_cor = x
        s.y_cor = y

    def distance_to(s, point):
        return math.sqrt((s.x_cor - point.x_cor)**2 + (s.y_cor - point.y_cor)**2)


def extract_data(data_file):

    d = set()
    p_cor = {}

    with open(data_file) as input_file:
        input_file.readline()
        line_count = 0
        for line in input_file:
            line_count += 1
            line = line.strip('\n')
            split_line = line.split(" ")
            print(split_line)
            p = Point(float(split_line[0]), float(split_line[1]))
            p_cor[line_count] = p
            d.add(line_count)

    point_dist = {}
    for point in d:
        for other_point in d:
            if point == other_point:
                pass
            point_dist[frozenset([point, other_point])] \
                = p_cor[point].distance_to(p_cor[other_point])
    return d, p_cor, point_dist

def plot_points(points_map):

    x_val = [point.x_cor for key, point in points_map.items()]
    print(x_val)
    y_val = [point.y_cor for key, point in points_map.items()]
    print(y_val)
    fig, ax = plt.subplots()
    ax.plot(x_val, y_val, 'ro')
    for x in range(1, len(x_val) + 1):
        ax.annotate(str(), (x_val[x - 1], y_val[x - 1]))
    plt.show()

def main():

    d, p_cor, point_dist = extract_data('Loc48.txt')
    plot_points(p_cor)

if __name__ == "__main__":
    main()
