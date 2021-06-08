import time
import math
from math import inf
import copy
import statistics
import matplotlib.pyplot as plt
#from plot import plot

class Point:
    def __init__(s, x, y):
        s.x_cor = x
        s.y_cor = y

    def distance_to(s, point):
        return math.sqrt((s.x_cor - point.x_cor)**2 + (s.y_cor - point.y_cor)**2)

def extract_data(data_file):
    d = set()
    p_cor = {}
    x_dir = {}
    i_index = []

    with open(data_file) as input_file:

        input_file.readline()
        num = 0
        current_x = inf
        i = 1

        for line in input_file:
            num += 1
            line = line.strip('\n')
            split_line = line.split(" ")
            print(split_line)
            x_coor = float(split_line[1])

            if current_x != x_coor:
                i = num
                i_index.append(i)
                x_dir[i] = []
                current_x = x_coor
            x_dir[i].append(num)
            p = Point(x_coor, float(split_line[2]))

            p_cor[num] = p
            d.add(num)
    return d, p_cor, x_dir, i_index

def find_min_tour(p_set, p_coord, x_dir, i_index):
    start_time = time.time()
    visited = [1, ]
    visited_set = set()
    visited_set.add(1)
    cities = len(p_set)
    m = 0.00000

    c = 1
    cp = 1
    dist = inf

    while len(visited_set) != cities:
        cities_left = cities - len(visited)
        print("{} cities left".format(str(cities_left)))

        for i in i_index:
            for point in x_dir[i]:
                if point == c or point in visited_set:
                    continue
                c_point = p_coord[c]
                other = p_coord[point]

                d = c_point.distance_to(other)

                if d < dist:
                    dist = d
                    cp = point
        visited.append(cp)
        visited_set.add(cp)
        c = cp
        m += dist
        dist = inf
    last_city = visited[len(visited) - 1]
    last_city_point = p_coord[last_city]
    first_city_point = p_coord[1]
    m += first_city_point.distance_to(last_city_point)
    end_time = time.time()
    print("visited", visited)
    print("Minimum tour length: " + str(m))
    print("Time taken: " + str(end_time-start_time))
    return m, end_time-start_time

def main():
    p_set, p_coord, x_dir, i_index = extract_data("Loc48.txt")
    find_min_tour(p_set, p_coord, x_dir, i_index)

if __name__ == "__main__":
    main()
