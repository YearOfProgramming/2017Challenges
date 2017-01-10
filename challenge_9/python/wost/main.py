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
    lst.root.random = lst.current.next
    lst2 = LinkedList()

    lst2 = lst.deep_copy()

    print(lst)
    print(lst2)


if __name__ == "__main__":
    main()
