from collections import Counter

def square_sort(input_list):
    output_list = []
    abs_counter = Counter([abs(i) for i in input_list])  # O(n)
    max_abs, min_abs = max(abs_counter.keys()), min(abs_counter.keys())  # O(n)

    for i in range(min_abs, max_abs+1):  # O(m), where m is unique ints, then...
        if i in abs_counter:
            for iters in range(abs_counter[i]): # O(m) -> O(n), for all ints now
                output_list.append(i**2)

    return output_list

