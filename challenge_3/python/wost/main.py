"""
Python 3.6:
  :: Counts all the instances of all the elements in a list.
  :: Returns all the instances that counts as more than half the list.
"""


def find_prim_in_list(a_list):
    a_dict = {}

    for char in a_list:
        if char not in a_dict.keys():
            a_dict[char] = 1
        else:
            a_dict[char] += 1

    for letter in a_dict.keys():
        # Doing // 1 is essentially to floor the number, I think.
        if a_dict[letter] > (len(a_dict) / 2) // 1:
            print(letter, end=" ")
    print()

    def main():
        # Returns 6, 7.
        find_prim_in_list([5, 4, 3, 4, 5, 6, 1, 3, 1, 7, 8, 8])
        # Returns b.
        find_prim_in_list(["a", "b", "c", "a", "c", "W", "W"])
        # Returns A, 5, r.
        find_prim_in_list(["A", "b", "d", "r", 4, 5, 4, "b", "d"])
        # Returns nothing.
        find_prim_in_list([])


if __name__ == "__main__":
    main()
