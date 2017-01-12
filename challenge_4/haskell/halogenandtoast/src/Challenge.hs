module Challenge where

data Tree a = Node a (Tree a) (Tree a) | Empty
            deriving (Show, Eq)

invert :: Tree a -> Tree a
invert Empty = Empty
invert (Node v l r) = Node v (invert r) (invert l)
