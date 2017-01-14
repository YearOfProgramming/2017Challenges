module Challenge where

safeLast :: [a] -> Maybe a
safeLast [] = Nothing
safeLast xs = Just $ last xs

rangeStr :: Int -> Int -> String
rangeStr s e = show s ++ "->" ++ show e

endOfRange :: [Int] -> Maybe (Int, Int)
endOfRange [] = Nothing
endOfRange (x:xs) = safeLast matches
  where
    matches = takeWhile (\(i, y) -> x + i == y) (zip [1..] xs)

ranges :: [Int] -> [String]
ranges [] = []
ranges xs = ranges' xs []
  where
    ranges' [] = id
    ranges' ys@(h:t) = case endOfRange ys of
                            Just (i, z) -> ranges' (drop i t) . (++ [rangeStr h z])
                            Nothing -> ranges' t
