# Write your code here
def median(ns):
    sorted_list = sorted(ns)
    idx = len(sorted_list)//2
    if len(sorted_list) % 2 != 0:
        return sorted_list[idx]
    else:
        return (sorted_list[idx] + sorted_list[idx - 1])/2