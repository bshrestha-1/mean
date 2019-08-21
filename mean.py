#Mean calculating program
def mean(num_list):
    assert isinstance(num_list,list)
    if len(num_list) ==0:
        raise Expection("The algebraic mean of an empty list is undefined.") 
    else:
        return sum(num_list)/len(num_list)

