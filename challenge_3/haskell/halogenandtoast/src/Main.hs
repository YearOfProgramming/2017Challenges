module Main where

import System.Environment ( getArgs )
import Challenge ( findMajority )

main :: IO ()
main = getArgs >>= (putStrLn . findMajority)
