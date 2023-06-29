sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def tup(tup_list):
    return tup_list[-1]
s=sorted(sample_list,key=tup)
print(s)

#output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
