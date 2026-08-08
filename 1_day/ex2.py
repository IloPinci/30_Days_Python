#The euclidian distance between (2, 3) and (10, 8)

import math

coordinates = [2, 3, 10, 8]

print(math.sqrt(
    ((coordinates[0] - coordinates[2])**2) + 
    (coordinates[1] - coordinates[3])**2
    ))