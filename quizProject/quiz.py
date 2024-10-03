nom = input("ingresar un nombrre: ")
dias = int(input("ingrese un dia: "))
salari =int(input("ingrese su respectivo salario: "))

prima= (salari*dias)/360
cesantias= (salari*dias)/360
intereesescesantias= (cesantias*12)/dias
vacasiones =(salari*dias)/720
liquidacion = prima+ cesantias+intereesescesantias+vacasiones
print(f"señor {nom } para los {dias} laborados y salario {salari},"
      f" su liquidacion se compone asi: prima ${prima} cesantias ${cesantias},"
      f" interesescesantias ${intereesescesantias},"
      f"vacaciones ${vacasiones}, liquidacion ${liquidacion}")