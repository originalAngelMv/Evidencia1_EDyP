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
    
    elif opcion == "2":
        print("1. Consultar por período.\n2. Consultar por folio.")
        consulta_opcion = input("Ingrese una opción de consulta:\n")
        
        if consulta_opcion == "1":
            
            fecha_inicial_str = input("Fecha inicial (dd-mm-aaaa): ")
            fecha_final_str = input("Fecha final (dd-mm-aaaa): ")
            fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%d-%m-%Y")
            fecha_final = datetime.datetime.strptime(fecha_final_str, "%d-%m-%Y")
            
            notas_en_periodo = []
            
            for nota in notas:
                if nota['fecha']>=fecha_inicial and nota['fecha']<= fecha_final and nota['estado']:
                    notas_en_periodo.append(nota)
                    
            if notas_en_periodo:
                
                print('\nNotas encontradas en el período:')
                print("-"*50)
                
                for nota in notas_en_periodo:
                    
                    print(f"Folio: {nota['folio']}\t Cliente: {nota['cliente']}\t Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                    for servicio,costo in nota['detalle']:
                        print(f' Servicio: {servicio}-----> Costo: {costo:.2f}')
                    print(f'Monto: {nota["monto_a_pagar"]:.2f}')
                    print("-"*50)
                else:
                    print('Fin de las notas')
            else:
                print('\nNo se encontraron notas en el período especificado')
                
        elif opcion == "2":
            pass
                
                 
            
                
    
            
            
        
        