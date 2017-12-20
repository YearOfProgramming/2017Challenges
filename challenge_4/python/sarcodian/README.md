So I took this out and after a nice long slack discussion, decided to put it back, 
since what I lacked most was documentation, which was causing a missunderstanding.

So, instead of building a Node class, and recursing my way down, I built each node in 
list notation using the format tree = [head, [left, [], []], [right, [], []]]

The empty lists are equvalent to None

If you want to add left.left, you simply add tree[1][1] = [left.left, [], []]
If you want to add left.right, you can add tree[1][2] = [left.right, [], []]
Same notation if you want to retrieve a node or branch.

TL:DR; I did not hard code a list and reverse it. You can build and manipulate the tree from
scratch and the reverse fuction will recurse down until the null values and flip them for you.