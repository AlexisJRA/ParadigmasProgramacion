mayorRectangulo :: (Int, Int) -> (Int, Int) -> (Int, Int)

mayorRectangulo (a, b) (c, d) | a*b >= c*d = (a,b)
                              | otherwise = (c,d)
