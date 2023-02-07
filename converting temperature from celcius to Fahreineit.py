def convertCelciusToFa(celcius):
    return ((celcius*9)/5) +32
celcius=float(input("enter the temperature in celcius"))
temp= convertCelciusToFa(celcius)

print(celcius,"celcius is :",temp,"F")
