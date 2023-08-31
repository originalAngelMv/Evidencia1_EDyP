import datetime

notas = []
folios_contador = 0
while True:
    print("1. Registrar una nota.\n2. Consultas y reportes.\n3. Cancelar una nota.\n4. Recuperar nota.\n5. Salir")
    
    opcion = input("Ingrese una opción:\n")
    
    if opcion == "1":
        
        folios_contador += 1
        
        cliente = input("Nombre del cliente:\n")
        
        fecha_ingresada_str = input("Fecha de la nota (dd-mm-aaaa):\n")
        fecha_ingresada = datetime.datetime.strftime(fecha_ingresada_str, "%d-%m-%Y")
        
        nota = {
            "folio": folios_contador,
            "fecha": fecha_ingresada,
            "cliente": cliente,
            "monto_a_pagar": 0.0,
            "detalle": [],
            "estado": True
        }
        
        while True:
            
            nombre_servicio = input("Nombre del servicio: ")
            costo_servicio = input("Costo del servicio: ")
            costo_servicio = float(costo_servicio)
            
            if input("¿Agregar otro servicio? (s/n): ").lower() != "s":
                break
            
        notas.append(nota)
        print(f"Folio asignado: {folios_contador}")
    
            
            
        
        