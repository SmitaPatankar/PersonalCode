"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
rows=5
stars = 1
spaces = 4
for i in range((rows*2)-1):
    for j in range(spaces):
        print(" ", end="")
    for j in range(stars):
        if j == stars - 1:
            print("*")
        else:
            print("*", end="")
    if i <rows-1:
        spaces -= 1
        stars += 2
    else:
        spaces += 1
        stars -= 2
