module Main where

import System.Environment(getArgs)
import Data.List(reverse)

main :: IO ()
main = do
  args <- getArgs
  case args of
    (x:_) -> putStrLn $ reverse x
    _ -> putStrLn "Usage: runhaskell Main.hs STRING"
