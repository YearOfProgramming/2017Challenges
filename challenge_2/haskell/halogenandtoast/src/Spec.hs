module Spec where

import Test.Hspec
import Challenge
import Data.HashMap.Strict as HashMap (lookup)

main :: IO ()
main = hspec $ do
  describe "Challenge.solve" $ do
    it "returns the value appearing only once" $ do
      solve ["1", "2", "2", "3", "1"] `shouldBe` "3"

  describe "Challenge.counts" $ do
    it "returns the counts for each value" $ do
      let values = counts ["1", "2", "2", "3", "1"]
      HashMap.lookup "1" values `shouldBe` Just 2
      HashMap.lookup "2" values `shouldBe` Just 2
      HashMap.lookup "3" values `shouldBe` Just 1
      HashMap.lookup "4" values `shouldBe` Nothing
