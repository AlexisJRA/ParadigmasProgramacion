funcionBooleanaPar :: Integer -> Bool
funcionBooleanaPar valor | mod valor 2 == 0 = True
                         | mod valor 2 == 1 = False

listaBooleanos :: [Integer] -> [Bool]
listaBooleanos xs = map funcionBooleanaPar xs