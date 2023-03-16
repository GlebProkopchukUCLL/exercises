# Write your code here
def coins(one, two, five, goal):
    x = 0
    for i in range (goal):
        x += five*i
        if goal == x:
            return True
        for j in range (goal):
            if x == goal:
                return True
            if goal == two*j:
                return True
            for k in range (goal):
                if goal == one*k:
                    return True