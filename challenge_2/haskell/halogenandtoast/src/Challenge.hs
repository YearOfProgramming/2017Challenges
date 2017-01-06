module Challenge where

import Data.Maybe ( fromMaybe )
import Data.Hashable ( Hashable )
import Data.HashMap.Strict ( alter
                           , toList
                           , filterWithKey
                           , empty
                           , HashMap(..)
                           )

counts :: (Eq a, Hashable a) => [a] -> HashMap a Int
counts = flip counts' empty
  where
    upsert = Just . (+ 1) . fromMaybe 0
    counts' [] = id
    counts' (x:xs) = counts' xs . alter upsert x

solve :: (Eq a, Hashable a) => [a] -> a
solve = fst . head . toList . filter . counts
  where
    filter = filterWithKey (const (== 1))
