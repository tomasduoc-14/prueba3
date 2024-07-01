while True:
    try:
        menu = int(input(""""Que opciones desea?: 
        1.Registrar vehiculos
        2.Listar todos los vehiculos registrados
        3.Imprimir orden en reparacion
        4.Salir del programa:
        """))
        
        if menu == 1:
            imppuesto = 8
            Marca = input("Ingrese marca del vehiculo:")
            año_fabricacion = input("Ingrese año del vehiculo:")
            Kilometraje = input("Ingrese su kilometraje:")
            costo_reparacion = int(input("Ingrese costo de reparacion:"))
            impuesto = costo_reparacion * 0.8
            total_a_pagar = impuesto
            matriz = print(f"""
            Total a pagar:{total_a_pagar}
            La marca es:{Marca}
            año fabricacion:{año_fabricacion}
            kilometraje:{Kilometraje}""")

            break
    except:
            input("Ingreso mal los datos,enter para salir")
            

            if menu ==2:
                print(f"Vehiculos registrados{matriz}")
                print(f"Marca {Marca}")
                print(f"año fabricacion {año_fabricacion}")
                print(f"Kilometraje {Kilometraje}")
                print(f"Costo de reparacion {costo_reparacion}")
                print(f"impuesto {impuesto}")
                print(f"total a pagar {total_a_pagar}")
                break
            if menu ==3:
                print(f"Vehiculos en reparacion{Marca}")
            if menu ==4:
                print("Gracias por usar el programa")
                input("desea volver a intentarlo: s/n")
                break
            