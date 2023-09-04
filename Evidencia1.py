import datetime
import re

notas = []
folios_contador=0

patron_fecha = r"^\d{1,2}-\d{2}-\d{4}$"

while True:
    
    print("\n1. Registrar una nota.\n2. Consultas y reportes.\n3. Cancelar una nota.\n4. Recuperar nota.\n5.salir\n")
    
    opcion=input("Ingrese una opción:\n")

    if opcion == "1":
        
        folios_contador += 1
        
        while True:
            
            cliente = input("Nombre del cliente: ")
            
            if cliente.strip() =="":
                print("El dato no puede omitirse.Intente denuevo.")
                continue
            else:
                break
            
        fecha_actual =datetime.datetime.now()
           
        while True:
            
            fecha_ingresada_str = input("Fecha de la nota (dd-mm-aaaa): ")
            
            if fecha_ingresada_str =="":
                print("El dato no puede omitirse.Intente denuevo.")
                continue
            
            if not re.match(patron_fecha, fecha_ingresada_str):
                print("Formato de fecha incorrecto. Debe ser dd-mm-aaaa")
                continue
            
            try:
                fecha_ingresada = datetime.datetime.strptime(fecha_ingresada_str, "%d-%m-%Y")
            except Exception:
                print("La fecha NO existe. Intente denuevo.")
                continue
            
            if fecha_ingresada>fecha_actual:
                print("No debe ser posterior a la fecha actual del sistema")
                continue
            else:
                break

        nota = {
            'folio': folios_contador,
            'fecha': fecha_ingresada,
            'cliente': cliente,
            'monto_a_pagar': 0.0,
            'detalle': [],
            'estado':True
            }
        
        while True:
            
            while True:
            
                nombre_servicio = input("Nombre del servicio: ")
                
                if nombre_servicio.strip()=="":
                    print("El dato no puede omitirse.Intente denuevo.")
                    continue
                break
                
            while True:
                
                costo_servicio = input("Costo del servicio: ")
                
                if costo_servicio.strip()=="":
                    print("El dato no puede omitirse.Intente denuevo.")
                    continue
                
                try:
                    costo_servicio = float(costo_servicio)
                except Exception:
                    print("Se ingreso un carácter no numérico ")
                    continue
                
                if costo_servicio<=0:
                    print("El costo debe ser mayor a 0 pesos")
                    continue
                else:
                    nota['detalle'].append((nombre_servicio, costo_servicio))
                    nota['monto_a_pagar'] += costo_servicio
                    break
                
            if input("¿Agregar otro servicio? (s/n):\n ").lower() != "s":
                break    
            
        notas.append(nota)
        print(f"Folio asignado: {folios_contador}\n")
        print(f"Nombre: {cliente}")
        print(f"Fecha: {fecha_ingresada.date()}\n")
        print("Detalles: ")
        for servicio,costo in nota['detalle']:
            print(f"servicio: {servicio}---->costo: {costo}")
        print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")
            
        

    elif opcion=="2":
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
                
                if nota['fecha']>=fecha_inicial and nota['fecha'] <= fecha_final and nota['estado']:
                    notas_en_periodo.append(nota)
                    
            if notas_en_periodo:
                print("\nNotas encontradas en el período:")
                print("-"*100)
                
                for nota in notas_en_periodo:
                    print(f"\nFolio: {nota['folio']}\t Cliente: {nota['cliente']}\t Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                    print(f"Monto: {nota['monto_a_pagar']:.2f}")
                    print("-"*100)
                else:
                    print("Fin de las notas")
            else:
                print("\nNo se encontraron notas en el período especificado.")
        elif consulta_opcion=="2":
            while True:
                
                folio_consulta = input("Ingrese el folio de la nota a consultar: ")
                
                if folio_consulta.strip()=="":
                    print("Dato no puede omitirse. Intente denuevo.")
                    continue
                
                try:
                    folio_consulta=int(folio_consulta)
                except Exception:
                    print("Carácter no valido. Solo dígitos numéricos")
                    continue
                else:
                    break
                
            nota_encontrada=[]
            
            for nota in notas:
                if nota['folio'] == folio_consulta and nota['estado']:
                    nota_encontrada.append(nota)
            
            if len(nota_encontrada)==0:
                print("No se encontro el número de folio.")
                continue
                
            for nota in nota_encontrada:        
                print("\nDetalles de la nota:")
                print(f"Folio: {nota['folio']}")
                print(f"Cliente: {nota['cliente']}")
                print(f"Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                print("Detalle:")
                
                for servicio, costo in nota['detalle']:
                    print(f"  Servicio: {servicio}---> Costo: {costo:.2f}")
                    
                print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")    
            else:
                print("-"*100)
        else:
            print("Opcion no valida")
    elif opcion=="3":
        
        while True:
            
            folio_cancelar = input("Ingrese el folio de la nota a cancelar:\t ")
            
            if folio_cancelar.strip()=="":
                print("Dato no puede omitirse. Intente denuevo.")
                continue
            
            try:
                folio_cancelar=int(folio_cancelar)
            except Exception:
                print("Carácter no valido. Solo dígitos numéricos")
                continue
            else:
                break

        for nota in notas:
            
            if nota['folio'] == folio_cancelar:
                if nota['estado']:
                    print("\nDetalles de la nota a cancelar:")
                    print(f"Folio: {nota['folio']}")
                    print(f"Cliente: {nota['cliente']}")
                    print(f"Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                    
                    print("Detalle:\t")
                    
                    for servicio, costo in nota['detalle']:
                        print(f"  Servicio: {servicio}, Costo: {costo:.2f}")
                    print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")
                
                    confirmacion = input("¿Confirmar la cancelación de esta nota? (s/n): ").lower()
                    
                    if confirmacion == "s":
                        nota['estado'] = False
                        print(f"\nNota con folio {folio_cancelar} ha sido cancelada.")
                    else:
                        print("\nNota no fue cancelada")
                else:
                    print("Esta nota se encuentra cancelada.\t")
        else:
            print("Nota no esta en el sistema.\t")       
    elif opcion=='4':
        
        notas_canceladas=[]
        
        for nota in notas:
                
            if nota['estado']==False:
                    
                print("\nDetalles de la nota a recuperar:")
                print(f"Folio: {nota['folio']}")
                print(f"Cliente: {nota['cliente']}")
                print(f"Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                print("-"*20)
                notas_canceladas.append(nota)
                
        cantidad_canceladas=len(notas_canceladas)
        
        if cantidad_canceladas==0:
            print('-'*20)
            print('\nNo hay notas Canceladas\n')
            print('-'*20)
            continue
        
        
                    
        pregunta_rescate = input("Desea recuperar alguna nota presentada?:(s/n)\t").lower()
        
        if pregunta_rescate== 's':
            
            while True: 
                
                folio_recuperar = input("Ingrese el folio de la nota a recuperar:\t ")
                
                if folio_recuperar.strip=="":
                    print("Este dato no se puede omitir. Intente denuevo\n")
                    continue
                
                try:
                    folio_recuperar=int(folio_recuperar)
                except Exception:
                    print("Se ingreso un caracter NO númerico. Intente nuevamente\n")
                    continue
                else:
                    break
                
            
            for nota in notas_canceladas:
                
                if nota['folio'] == folio_recuperar:
                    if nota['estado']==False:
                        print("\nDetalles de la nota a cancelar:")
                        print(f"Folio: {nota['folio']}")
                        print(f"Cliente: {nota['cliente']}")
                        print(f"Fecha: {nota['fecha'].strftime('%d-%m-%Y')}")
                        
                        print("Detalle:\t")
                        
                        for servicio, costo in nota['detalle']:
                            print(f"  Servicio: {servicio}, Costo: {costo:.2f}")
                        print(f"Monto total a pagar: {nota['monto_a_pagar']:.2f}")
                    
                        confirmacion = input("¿Confirmar la recuperación de esta nota? (s/n): ").lower()
                        if confirmacion == "s":
                            for nota in notas:
                                if nota['folio']==folio_recuperar:
                                    nota['estado'] = True
                            print(f"Nota con folio {folio_recuperar} ha sido recuperada.")
                        else:
                            print("Nota no se cancelo.")
                else:
                    print('Folio no encontrada')
            else:
                print("-"*20)
        else:
            print("\nNinguna nota fue recuperada.\n")
        
    elif opcion=='5':
        break
print("\nFin del programa\n")