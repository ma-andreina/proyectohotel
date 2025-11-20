import traceback

# Logger
from utils.Logger import Logger

user = str(input("Ingresa tu usuario: "))
password = str(input("Ingresa tu contraseña: "))
result = ""


#FUNCIÓN PARA VERIFICAR SI EL USUARIO Y LA CONTRASEÑA SON CORRECTOS

def incorretUser(userValue = "Luis", passwordValue = "123"):
    try:
        if user == userValue and password == passwordValue: result = "Usuario y contraseña correctos"
            
        Logger.add_to_log("info", "La respuesta es: {}".format(result))
    except Exception as ex:
        
        result = "Usuario o contraseña incorrecto"
        Logger.add_to_log("error", "La respuesta es: {}".format(result))
        print(result)


#incorretUser()







#FUNCIÓN PARA IDENTIFICAR SI LA CONTRASEÑA TIENE MAS DE 6 DIGITOS

def passwordLeng():
    try:
        if len(password) >= 6:
            result = "Contraseña mayor a 6 digitos"

            
        Logger.add_to_log("info", "La respuesta es: {}".format(result))

    except Exception as ex:
        result = "Contraseña menor a 6 digitos"
        print(result)
        Logger.add_to_log("warn", "La respuesta es: {}".format(result))



#passwordLeng()






# FUNCIÓN PARA INDENTIFICAR SI LA CONTRASEÑA CONTIENE LESTRAS MAYUSCULAS

def upperCharacter():
    try:
        x = any(c.isupper() for c in password)
        if x == True: 

            result = "Contiene mayuscula"
            
        Logger.add_to_log("info", "La respuesta es: {}".format(result))
    except Exception as ex:
        result = "No contiene mayusculas"
        Logger.add_to_log("error", "La respuesta es: {}".format(result))
        print("La contraseña debe contener una letra mayuscula")


upperCharacter()










