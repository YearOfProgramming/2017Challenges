module Spec where

import Test.Hspec
import Challenge

main :: IO ()
main = hspec $ do
  describe "Challenge.findTheDifference" $ do
    it "returns Nothing when no difference" $ do
      findTheDifference "a" "a" `shouldBe` Nothing

    it "returns the differing char" $ do
      findTheDifference "abcd" "adecb" `shouldBe` Just 'e'

    it "returns the differing char when the char shows up multiple times" $ do
      findTheDifference "abcde" "adecbb" `shouldBe` Just 'b'
