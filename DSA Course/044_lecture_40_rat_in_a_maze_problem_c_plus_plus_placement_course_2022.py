# program: recursion: rat in a maze - https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
# maze matrix with 0s and 1s
# 1 means open, 2 means blocked
#
# find way out from 0,0 to 3,3
#
# can move left, right, up, down
#
#       0       1   2   3
# -----------------------
# 0   | -->1    0   0   0
# 1   | 1       1   0   1
# 2   | 1       1   0   0
# 3   | 0       1   1   1-->
#
# 0,0-->
#     1,0-->
#         1,1-->
#             2,1-->
#                 3,1-->
#                     3,2-->
#                         3,3
#         2,0-->
#             2,1-->
#                 3,1-->
#                     3,2-->
#                         3,3
#
# DRDDRR OR DDRDRR
#
# provide all solutions
#
# logic:
# check if down is within array, it is unblocked and not visited
# else check for right, up, down one by one
# collect path along the way and mark visited as True
# while returning mark unvisited i.e. backtracking
"""
def is_safe(x,y,visited,m,n):
    if x >= 0 and x < n and y >= 0 and y < n and visited[x][y] == 0 and m[x][y] == 1:
        return True
    else:
        return False
def solve(x,y,path,paths,visited,m,n):
    if x == n-1 and y == n-1:
        print(f"REACHED---------------------------------------------------------------------------------------------------")
        paths.append(path.copy())
        print(f"{x},{y} - {path} - {paths} - {visited}")
    else:
        visited[x][y] = 1
        # down
        new_x = x + 1
        new_y = y
        if is_safe(new_x,new_y,visited,m,n):
            path.append("D")
            print(f"{x},{y} - {path} - {paths} - {visited}")
            solve(new_x,new_y,path,paths,visited,m,n)
            path.pop()
            print(f"{x},{y} - {path} - {paths} - {visited}")
        # left
        new_x = x
        new_y = y - 1
        if is_safe(new_x,new_y,visited,m,n):
            path.append("L")
            print(f"{x},{y} - {path} - {paths} - {visited}")
            solve(new_x,new_y,path,paths,visited,m,n)
            path.pop()
            print(f"{x},{y} - {path} - {paths} - {visited}")
        # right
        new_x = x
        new_y = y + 1
        if is_safe(new_x,new_y,visited,m,n):
            path.append("R")
            print(f"{x},{y} - {path} - {paths} - {visited}")
            solve(new_x,new_y,path,paths,visited,m,n)
            path.pop()
            print(f"{x},{y} - {path} - {paths} - {visited}")
        # up
        new_x = x - 1
        new_y = y
        if is_safe(new_x,new_y,visited,m,n):
            path.append("U")
            print(f"{x},{y} - {path} - {paths} - {visited}")
            solve(new_x,new_y,path,paths,visited,m,n)
            path.pop()
            print(f"{x},{y} - {path} - {paths} - {visited}")
        visited[x][y] = 0
def find_path(m, n):
    x = 0
    y = 0
    path = []
    paths = []
    visited = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        visited.append(row)
    solve(x, y, path, paths, visited, m, n)
    paths = ["".join(path) for path in paths]
    return sorted(paths)
print()
print(find_path([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]], 4))
"""
