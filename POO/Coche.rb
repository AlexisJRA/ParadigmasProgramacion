
require "./Motor"
require "./Rueda"
require "./Puerta"

class Coche
    rueda1=Rueda.new()
    rueda1.class
    rueda2=Rueda.new()
    rueda2.class
    rueda3=Rueda.new()
    rueda3.class
    rueda4=Rueda.new()
    rueda4.class
    motor=Motor.new()
    motor.class
    puerta1=Puerta.new()
    puerta1.class
    puerta2=Puerta.new()
    puerta2.class
    puts "Coche creado"
  
    puts "inflando ruedas"
    puts "-1-"    
    rueda1.inflar
    puts "-2-"    
    rueda2.inflar
    puts "-3-"    
    rueda3.inflar
    puts "-4-"    
    rueda4.inflar
    
    puts "abriendo puertas"
    puts "-1-"
    puerta1.abrir
    puts "-2-"    
    puerta2.abrir

    puts "encendiendo motor"
    motor.arrancamotor
    
    puts "apagarmotor"
    motor.apagamotor

    puts "cerrando puertas"
    puts "-1-"
    puerta1.cerrar
    puts "-2-"    
    puerta2.cerrar

end

    

