mochila=["casco","sable de luz","mate","s","a","asd","asdasd"]
contador=0
def usar_la_fuerza(lista,contador):
    if (len(lista) == 1):
        return None
    else:
        if (lista[-1]=="sable de luz"):
            print("Se encontro el sable de luz en la mochila: ")
            print(f"La cantidad de objetos retirados fue {contador}")
            return lista
        else:
            contador+=1
            return usar_la_fuerza(lista[:-1],contador)
    

print(usar_la_fuerza(mochila,contador))