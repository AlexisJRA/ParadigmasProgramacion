notasLista :: [Float] -> [String] 
notasLista [] = []
notasLista (x:xs) | x < 5     = "SS" : notasLista xs
                  | x < 7     = "AP" : notasLista xs
                  | x < 9     = "NT" : notasLista xs
                  | x < 10    = "SB" : notasLista xs
                  | otherwise = "MH" : notasLista xs

main = print(notasLista [5, 10, 6, 7])