# To get an output [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]

outer_loop = []
for outer_l in range(4):
    inner_loop = []
    for inner_l in range(4):
        inner_loop.append(outer_l*inner_l)   # generating a sequence of numbers and appending to inner loop
    outer_loop.append(inner_loop)  # the inner loop is appended to the outer loop

print(outer_loop)