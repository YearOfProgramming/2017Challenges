module Main where

import System.Environment (getArgs)
import Challenge (solve)

main :: IO ()
main = getArgs >>= (putStrLn . solve)
