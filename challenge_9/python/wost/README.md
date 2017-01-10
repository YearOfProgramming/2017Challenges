# Challenge 8
Author: William Østensen (wOstensen)
## How to use:
Create a new LinkedList.

The LinkedList keeps track of the head (`self._root`), its current Node (`self._current`) and its lenght (`self._length`).

Add values using `add([value])`, either empty: creating an empty object; or with a value
creating a Node with a value.

Go to the next value using `next([node])`, where `node` either is a Node or is None. Then it checks whether or not the given node has a `next` value equal to None, or not. This function is also used recursively with `deep_copy`.

The function `deep_copy` creates a new instance of LinkedList in the class, adds the "parent" class' `root`'s val to this LinkedList. Then it saves your current position in another variable, sets your current position to the root node and starts traversing down into which Nodes exists in the first LinkedList and adds their value to the new LinkedList. This eliminates any chance
of the values in the new LinkedList instance being merely a reference to the elements in the old instance, because this creates entirely new Node objects, but with the same values.
At the end, your position is set to the position you had before you started the deep scan.

## Known Issues:
None so far.
