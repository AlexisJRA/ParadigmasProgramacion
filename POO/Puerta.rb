require "./Ventana"
class Puerta
    def iniatilize
        ventana=Ventana.new
        ventana.class
        @abierta="Cerrada"
        puts "Puerta Cerrada"
    end

    def abrir 
        @abierta = "Abierta"
        puts "Puerta Abierta"
    end

    def cerrar
        @abierta = "Cerrada"
        puts "Puerta Cerrada"
    end

    def cerarventana
        @ventana.cerrar
    end

    def abrirventana
        @ventana.abrir
    end

end
