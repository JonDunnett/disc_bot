from random import shuffle
def merge_sort(L):
    # PRE : L is a list  containing real numbers
    # POST: L sorted from low to high
    len_of_L = len(L)
    if len_of_L == 1:
		return L
    else:
        mid_list = len_of_L // 2
        first_half = merge_sort(L[:mid_list])
        second_half = merge_sort(L[mid_list:])
    	return merge_halves(first_half,second_half)

def merge_halves(first_half, second_half):
    i,j = 0,0
    i_bound = len(first_half)
    j_bound = len(second_half)
    new_list = []
    while (i<i_bound and j<j_bound ):
        if first_half[i] < second_half[j]:
            new_list = new_list + [first_half[i]]
            i+=1
        else:
            new_list = new_list + [second_half[j]]
            j+=1
    if (i < i_bound):
        new_list = new_list + first_half[i:]
    else:
        new_list = new_list + second_half[j:]

    return new_list

def main():

	L = [0.01,0.0001,99.999,-1.43]
	print ("Pre-sort  L: ", L)
	L = merge_sort(L)
	print ("Post-sort L: ", L)


if __name__ == '__main__':
	main()
