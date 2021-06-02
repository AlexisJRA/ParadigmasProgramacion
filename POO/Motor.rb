class  Motor
    def iniatilize
        @estado="Apagado"
        puts "Motor apagado"        
    end

    def arrancamotor
        puts "Motor encendido"
        @estado="Encendido"
    end

    def apagamotor
        puts "Motor apagado"
        @estado="Apagado"
    end

end        
