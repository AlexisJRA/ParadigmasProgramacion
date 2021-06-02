cuadrado :: Float -> Float
cuadrado n = n^2

modulo :: [Float] -> Float
modulo xs = sqrt (sum (map cuadrado xs))