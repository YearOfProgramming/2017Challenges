import System.IO
import System.Environment

import Data.Function
import Control.Monad

import Data.Char
import Data.Word

import Data.ByteString (ByteString)
import qualified Data.ByteString as ByteString
import qualified Data.ByteString.Char8 as ByteString.Char8

import Data.Vector.Unboxed (Vector)
import qualified Data.Vector.Unboxed as Vector
import qualified Data.Vector.Unboxed.Mutable as MVector

lowercase_a :: (Num a) => a
lowercase_a = fromIntegral (ord 'a')
{-# SPECIALIZE lowercase_a :: Int   #-}
{-# SPECIALIZE lowercase_a :: Word8 #-}

unsafeCountLowercaseBytes :: ByteString -> Vector Int
unsafeCountLowercaseBytes s = Vector.create $ do
  r <- MVector.replicate 26 0
  forM_ (ByteString.unpack s) $ \c -> do
    let i = fromIntegral c - lowercase_a
    n <- MVector.unsafeRead r i
    MVector.unsafeWrite r i (n + 1)
  return r

unsafeByteStringDiff :: ByteString -> ByteString -> Maybe Word8
unsafeByteStringDiff s t =
  let sCount  = unsafeCountLowercaseBytes s
      tCount  = unsafeCountLowercaseBytes t
      stCount = Vector.zip sCount tCount
  in do i <- Vector.findIndex (uncurry (/=)) stCount
        return $ fromIntegral $ i + lowercase_a

main :: IO ()
main = do
  progName <- getProgName
  args     <- getArgs
  case args of
    [s, t] -> doMain progName s t
    _      -> usageError progName
  where
    doMain progName s t
      | not (all isAsciiLower s && all isAsciiLower t) = caseError progName
      | otherwise = let s' = ByteString.Char8.pack s
                        t' = ByteString.Char8.pack t
                        mc = unsafeByteStringDiff s' t'
                    in case mc of
                         Nothing -> charError progName
                         Just c  -> putStrLn [chr $ fromIntegral c]

    usageError progName =
      hPutStrLn stderr ("usage: " ++ progName ++ " STRING1 STRING2")

    caseError progName =
      hPutStrLn stderr (progName ++ ": arguments must be lowercase strings")

    charError progName =
      hPutStrLn stderr (progName ++ ": arguments contain the same characters")
