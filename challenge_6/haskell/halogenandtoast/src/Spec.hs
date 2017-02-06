module Spec where

import Test.Hspec
import Challenge ( ranges )

main :: IO ()
main = hspec $ do
  describe "Challenge.ranges" $ do
    it "will return an empty list when no ranges exist" $ do
      ranges [] `shouldBe` ([] :: [String])

    it "will return a single range" $ do
      ranges [1, 2] `shouldBe` ["1->2"]

    it "will return multiple ranges" $ do
      ranges [1, 2, 3, 4, 5, 8, 9, 10] `shouldBe` ["1->5", "8->10"]

    it "will return multiple ranges ignoring numbers that are not part of a range" $ do
      ranges [1, 2, 3, 5, 8, 9, 10, 12] `shouldBe` ["1->3", "8->10"]
