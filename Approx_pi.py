import random as rand

def pt_gen(n):
    num_crcl, num_sq = 0, 0
    for _ in range(n):
        x_coor = rand.uniform(0,1)
        y_coor = rand.uniform(0,1)
        if x_coor**2 + y_coor**2 < 1:
            num_crcl += 1
        num_sq += 1
    return 4 * num_crcl/num_sq
