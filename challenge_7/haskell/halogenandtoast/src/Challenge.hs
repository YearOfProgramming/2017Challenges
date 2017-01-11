module Challenge where

missingNumber :: [Int] -> Int
missingNumber xs = triangleNumber (length xs) - sum xs
  where
    triangleNumber x = (x * (x + 1)) `div` 2
