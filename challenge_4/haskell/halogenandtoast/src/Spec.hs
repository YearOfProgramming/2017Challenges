module Spec where

import Test.Hspec
import Challenge

main :: IO ()
main = hspec $ do
  describe "Chalenge.invert" $ do
    it "returns Empty when Empty" $ do
      invert Empty `shouldBe` (Empty :: Tree Int)

    it "returns the root node when it is the only node" $ do
      let example = Node 1 Empty Empty
      invert example `shouldBe` example

    it "swaps the branches" $ do
      let example = Node 1 (Node 2 Empty Empty) (Node 3 Empty Empty)
      let expected = Node 1 (Node 3 Empty Empty) (Node 2 Empty Empty)
      invert example `shouldBe` expected

    it "swaps the branches recursively" $ do
      let example = Node 1 (Node 2 (Node 3 Empty (Node 4 Empty Empty)) Empty) (Node 5 (Node 6 Empty (Node 7 Empty Empty)) Empty)
      let expected = Node 1 (Node 5 Empty (Node 6 (Node 7 Empty Empty) Empty)) (Node 2 Empty (Node 3 (Node 4 Empty Empty) Empty))
      invert example `shouldBe` expected
