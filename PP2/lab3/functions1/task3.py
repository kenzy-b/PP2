def solve(numheads, numlegs):
    for i in range(1, numheads + 1):  
        rabbits = numheads - i  
        if i * 2 + rabbits * 4 == numlegs: 
            return f"chickens {i}, rabbits {rabbits}"

print(solve(35, 94))