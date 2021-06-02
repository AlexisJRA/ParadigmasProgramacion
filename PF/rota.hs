rota :: Int -> [Int] -> [Int]

rota n xs = drop n xs ++ take n xs 

main = print(rota 1 [3, 2, 5, 7], rota 2 [3, 2, 5, 7], rota 3 [3, 2, 5, 7])