from LinkedList import LinkedList


def main():
    lst = LinkedList()
    lst.add(6)
    lst.add(5)
    lst.add(11)
    lst.add(3)
    lst.add(1)
    lst.add(7)
    lst.add(4)
    lst.add(5)
    lst.add(6)
    lst.add(10)
    lst.add(5)
    lst.add(8)
    lst2 = LinkedList()

    lst2 = lst.deep_copy()

    print(len(lst))
    print(len(lst2))
    print(lst.current.val)
    print(lst2.current.val)
    print(lst.current.val)

    print(lst.print_all(lst.root))
    print(lst2.print_all(lst2.root))


if __name__ == "__main__":
    main()
