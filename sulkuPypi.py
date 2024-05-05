import requests
import time

base_url = "https://moibe-sulku-docker.hf.space/"
userfile = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="
work = "picswap"


def getTokens(userfile):

    method = "getTokens/"

    api_url = base_url + method + userfile

    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def debitTokens(userfile, work):

    api_url = base_url + "debitTokens" + "/" + userfile + "/" + work

    print("Apiurl es: ", api_url)
    time.sleep(8)

    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

if __name__ == "__main__":
    getTokens(userfile)
    debitTokens(userfile, work)
    pass
