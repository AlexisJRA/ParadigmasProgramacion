calculadora :: String -> Float -> Float
calculadora opcion n | opcion == "seno" = sin n 
                     | opcion == "coseno" = cos n
                     | opcion == "tangente" = tan n
                     | opcion == "exponencial" = n ** 2
                     | opcion == "logaritmo" = log n 