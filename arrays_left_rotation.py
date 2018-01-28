def main():
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(*answer, sep=' ')


def array_left_rotation(array, array_length, n):

    if array_length < 2:
        return array

    result = list()
    sliced_arr = array[0:n]
    shift_arr = array[n:array_length]

    result = shift_arr
    for i in range(n):
        result.append(sliced_arr[i])

    return result

if __name__ == '__main__':
    main()