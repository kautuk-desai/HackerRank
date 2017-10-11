def main():
    a = input().strip()
    b = input().strip()

    print(number_needed(a, b))


def number_needed(a, b):
    sort_a = sorted(a)
    sort_b = sorted(b)
    a_len = len(sort_a)
    b_len = len(sort_b)

    if a_len < 1:
        return b_len
    elif b_len < 1:
        return a_len
    else:
        num_needed = 0
        while a_len > 0 or b_len > 0:
            if a_len == 0:
                num_needed += b_len
                return num_needed

            if b_len == 0:
                num_needed += a_len
                return num_needed

            if sort_a[0] < sort_b[0]:
                num_needed += 1
                del sort_a[0]
                a_len = len(sort_a)
            elif sort_a[0] > sort_b[0]:
                num_needed += 1
                del sort_b[0]
                b_len = len(sort_b)
            else:
                del sort_a[0]
                a_len = len(sort_a)
                del sort_b[0]
                b_len = len(sort_b)

        return num_needed

if __name__ == '__main__':
    main()