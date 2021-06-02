maxTres :: Int -> Int -> Int -> Int
maxTres x y z = max x (max y z)
main = print(maxTres 6 2 4)