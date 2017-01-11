module Spec where

import Test.Hspec
import Challenge ( missingNumber )

main :: IO ()
main = hspec $ do
  describe "Challenge.missingNumber" $ do
    it "should return the missing number" $ do
      missingNumber [2, 3, 1] `shouldBe` 0
      missingNumber [2, 3, 0] `shouldBe` 1
      missingNumber [0, 3, 1] `shouldBe` 2
      missingNumber [1, 2, 0] `shouldBe` 3
