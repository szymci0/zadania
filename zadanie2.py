# Function for finding missing numbers in an n-element array of a numbers 1-n
def missing_elems(arr, number_of_elems):
    found = [ele for ele in range(number_of_elems + 1) if ele not in arr and ele != 0]
    return found


# Test on some input
if __name__ == "__main__":
    given_list = [2, 3, 7, 4, 9]
    n = 10
    print(missing_elems(given_list, n))
