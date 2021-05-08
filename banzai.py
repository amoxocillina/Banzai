#!/usr/bin/env python3

import numpy as np
import random

n = 9
array = np.zeros((n, n), dtype=int)
r = 0
while r < n:
    while True:
        try:
            c = 0
            while c < n:
                liner = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                col = array[:, c]
                row = array[r, :]
                row_res = np.setdiff1d(liner, row)
                col_res = np.setdiff1d(liner, col)

                if r <= 2:
                    row_init = 0
                    row_end = 3
                elif r >= 3 and r <= 5:
                    row_init = 3
                    row_end = 6
                elif r >= 6:
                    row_init = 6
                    row_end = 9

                if c <= 2:
                    col_init = 0
                    col_end = 3
                elif c >= 3 and c <= 5:
                    col_init = 3
                    col_end = 6
                elif c >= 6:
                    col_init = 6
                    col_end = 9

                sub = array[row_init:row_end, col_init:col_end].flatten()
                cross = np.intersect1d(row_res, col_res)
                sector = np.setdiff1d(cross, sub)
                array[r, c] = np.random.choice(sector)
                c += 1
            break
        except Exception:
            array = np.delete(array, r, 0)
            array = np.delete(array, r-1, 0)
            array = np.insert(array, r, 0, axis=0)
            array = np.insert(array, r-1, 0, axis=0)
            r -= 1
            continue
    r += 1

print(array)
