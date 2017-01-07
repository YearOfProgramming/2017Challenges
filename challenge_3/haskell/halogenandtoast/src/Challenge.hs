module Challenge where

import Data.Ord ( Down(..) )
import Data.List ( sortOn )
import Data.Maybe ( fromMaybe )
import Data.Hashable ( Hashable )
import Data.HashMap.Strict ( HashMap(..)
                           , empty
                           , alter
                           , toList
                           )

counts :: (Eq a, Hashable a) => [a] -> HashMap a Int
counts = flip counts' empty
  where
    upsert = Just . (+ 1) . fromMaybe 0
    counts' [] = id
    counts' (x:xs) = counts' xs . alter upsert x

findMajority :: (Eq a, Hashable a) => [a] -> a
findMajority = fst . head . sortDescending . toList . counts
  where
    sortDescending = sortOn (Down . snd)
