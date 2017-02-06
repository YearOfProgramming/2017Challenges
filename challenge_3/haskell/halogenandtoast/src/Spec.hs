module Spec where

import Test.Hspec
import Challenge
import Data.HashMap.Strict as HashMap (lookup)

main :: IO ()
main = hspec $ do
  describe "Challenge.findMajority" $ do
    it "finds the element that occurs the most" $ do
      findMajority ([1, 1, 2, 3] :: [Int]) `shouldBe` 1

  describe "Challenge.counts" $ do
    it "returns the counts for each value" $ do
      let values = counts ([1, 2, 2, 3, 1] :: [Int])
      HashMap.lookup 1 values `shouldBe` Just 2
      HashMap.lookup 2 values `shouldBe` Just 2
      HashMap.lookup 3 values `shouldBe` Just 1
      HashMap.lookup 4 values `shouldBe` Nothing
