module Challenge where

import Data.List ( find )
import Data.Char ( ord
                 , chr
                 )
import Control.Lens ( (%~)
                    , element
                    )

toAlphaNum :: Char -> Int
toAlphaNum = subtract (ord 'a') . ord

fromAlphaNum :: Int -> Char
fromAlphaNum = chr . (+ ord 'a')

trackCharacters :: [Int] -> [Char] -> [Int]
trackCharacters acc [] = acc
trackCharacters acc (x:xs) = trackCharacters (updateAlpha acc) xs
  where
    updateAlpha = (element (toAlphaNum x) %~ succ)

findTheDifference :: String -> String -> Maybe Char
findTheDifference s t =  fromAlphaNum . fst <$> findOddIndex counts
  where
    counts = flip trackCharacters t $ trackCharacters zeroes s
    findOddIndex = find (odd . snd) . zip [0..]
    zeroes = take 26 (repeat 0)
