aplicarDescuento :: Double -> Double -> Double

aplicarDescuento precio desc = precio - precio * desc / 100

aplicarIva :: Double -> Double -> Double

aplicarIva precio iva = precio + precio*iva/100

precioCanasta :: String -> [Double] -> Double -> Double

precioCanasta "IVA" canasta iva = aplicarIva (sum canasta) iva 

precioCanasta "Desc" canasta desc = aplicarDescuento (sum canasta) desc

