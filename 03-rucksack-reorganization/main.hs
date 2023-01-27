import Data.List
import Data.Char

halve :: [a] -> ([a],[a])
halve = splitAt . (`div` 2) =<< length

getDuplicates :: String -> String
getDuplicates = (uncurry intersect) . halve

getSingleDuplicates :: [String] -> String
getSingleDuplicates xs = [ head s | s <- map getDuplicates xs, s /= [] ]

getTripleDuplicates :: [String] -> [String]
getTripleDuplicates [] = []
getTripleDuplicates [x] = []
getTripleDuplicates [x,y] = []
getTripleDuplicates (x:y:z:zs) = (tripleDup x y z):(getTripleDuplicates zs)
  where tripleDup x y z = intersect x (intersect y z)


getLetterScore:: Char -> Int
getLetterScore x
  | isUpper x = ord x - ord 'A' + 27
  | otherwise = ord x - ord 'a' + 1


-- main =  interact wordCount
--   where wordCount input = show $ sum $ map getLetterScore (getSingleDuplicates (lines input))

main = interact wordCount
  where wordCount input = show $ sum $ map getLetterScore  (concat (getTripleDuplicates (lines input)))

