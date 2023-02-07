def convertFaToCelcius(F):
    return (5*(F-32))/9
F=float(input("enter the temperature in fahreinheit\n"))
temp= convertFaToCelcius(F)

print(F,"F is :",temp,"Celcius")
