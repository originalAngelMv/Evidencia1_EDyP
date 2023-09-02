import datetime
import re

notas = []
folios_contador = 0

patron_fecha = r"^\d{1,2}-\d{2}-\d{4}$"

while True:
    
    print("1. Registrar una nota.\n2. Consultas y reportes.\n3. Cancelar una nota.\n4. Recuperar nota.\n5. Salir")
    
    opcion = input("Ingrese una opción:\n")
    
    if opcion == "1":
        
        folios_contador += 1
        
        while True:
        
            cliente = input("Nombre del cliente:\n")
            
            if cliente.strip()=="":
                print("El dato no puede omitirse. Intente nuevamente")
                continue
            else:
                break
        
        fecha_actual = datetime.datetime.now()
        
        while True:
            
            fecha_ingresada_str = input("Fecha de la nota (dd-mm-aaaa):\n")
            
            if fecha_ingresada_str =="":
                print("El dato no puede omitirse. Intente nuevamente.")
                continue
            elif not re.match(patron_fecha,fecha_ingresada_str):
                print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa")
                continue
            
            
            try:
                fecha_ingresada = datetime.datetime.strftime(fecha_ingresada_str, "%d-%m-%Y")
            except Exception:
                print("La fecha NO existe. Intente nuevamente.")
                continue
            
            if fecha_ingresada>fecha_actual:
                print("No debe ser posterior a la fecha actual del sitema. Intente nuevamente.")
                continue
            else:
                break
        
        nota = {
            "folio": folios_contador,
            "fecha": fecha_ingresada,
            "cliente": cliente,
            "monto_a_pagar": 0.0,
            "detalle": [],
            "estado": True
        }
        
        while True:
            
            while True:
            
                nombre_servicio = input("Nombre del servicio: ")
                
                if nombre_servicio.strip()=="":
                    print("El dato no puede omitirse. Intente nuevamente.")
                    continue
                break
                
            while True:
                
                costo_servicio = input("Costo del servicio: ")
                
                if costo_servicio.strip()=="":
                    print("El dato no puede omitirse. Intente nuevamente.")
                    continue
                
                try:
                    costo_servicio = float(costo_servicio)
                except Exception:
                    print("Se ingreso un carácter no númerico ")
                    continue
                
                if costo_servicio<=0:
                    print("El costo debe ser mayor a 0 pesos. Intente nuevamente.")
                    continue
                else:
                    nota['detalle'].append((nombre_servicio,costo_servicio))
                    nota['monto_a_pagar'] += costo_servicio
                    break
            
            if input("¿Agregar otro servicio? (s/n): \n").lower() != "s":
                break
            
        notas.append(nota)
        print(f"\nFolio asignado: {folios_contador}\n")
        print(f"Nombre: {cliente}")
        print(f"Fecha: {fecha_ingresada.date()}\n")
        print("Detalles: ")
        for servicio,costo in nota['detalle']:
            print(f"servicio: {servicio}---->costo: {costo}")
        print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")
    
    
    
    elif opcion == "2":
        print("\n1. Consultar por período.\n2. Consultar por folio.")
        consulta_opcion = input("\nIngrese una opción de consulta:\n")
        
        if consulta_opcion == "1":
            
            while True:
                
                fecha_inicial_str = input("Fecha inicial (dd-mm-aaaa): ")
                
                if fecha_inicial_str =="":
                    print("El dato no puede omitirse.Intente denuevo.")
                    continue
                elif not re.match(patron_fecha, fecha_inicial_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa")
                    continue
                
                try:
                    fecha_inicial = datetime.datetime.strptime(fecha_inicial_str, "%d-%m-%Y")
                except Exception:
                    print("La fecha NO existe. Intente denuevo.")
                    continue
                else:
                    break
                
            while True:
                
                fecha_final_str = input("Fecha final (dd-mm-aaaa): ")
                
                if fecha_final_str =="":
                    print("El dato no puede omitirse.Intente denuevo.")
                    continue
                elif not re.match(patron_fecha, fecha_final_str):
                    print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa")
                    continue
                
                try:
                    fecha_final = datetime.datetime.strptime(fecha_final_str, "%d-%m-%Y")
                except Exception:
                    print("La fecha NO existe. Intente denuevo.")
                    continue
                else:
                    break

            notas_en_periodo = []
            
            for nota in notas:
                
                if nota['fecha']>=fecha_inicial and nota['fecha']<= fecha_final and nota['estado']:
                    notas_en_periodo.append(nota)
                    
            if notas_en_periodo:
                print('\nNotas encontradas en el período:')
                print("-"*100)
                
                for nota in notas_en_periodo:
                    print(f"Folio: {nota['folio']}\t Cliente: {nota['cliente']}\t Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                    print(f'Monto: {nota["monto_a_pagar"]:.2f}')
                    print("-"*100)
                else:
                    print('Fin de las notas')
            else:
                print('\nNo se encontraron notas en el período especificado')
        elif consulta_opcion == "2":
            pass
                
                 
            
                
    
            
            
        
        