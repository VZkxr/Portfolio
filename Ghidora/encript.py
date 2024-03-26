import re
import pyperclip

enc_v_s = ["oneQ", "oneq", "zeroW", "zerow", "oneE", "onee", 
         "zeroR", "zeror", "oneT", "onet", "zeroY", "zeroy",
         "oneU", "oneu", "zeroI", "zeroi", "oneS", "ones",
         "zeroP", "zerop", "oneA", "onea", "zeroS", "zeros",
         "oneD", "oned", "zeroF", "zerof", "oneG", "oneg",
         "zeroH", "zeroh", "oneJ", "onej", "oneK", "onek",
         "zeroL", "zerol", "oneR", "oner", "zeroZ", "zeroz",
         "oneX", "onex", "zeroC", "zeroc", "oneV", "onev",
         "zeroB", "zerob", "oneN", "onen", "zeroM", "zerom",
         "oneW", "onew", "zeroQ", "zeroq", "oneY", "oney",
         "zeroE", "zeroe", "oneI", "onei", "zeroT", "zerot",
         "oneP", "onep", "zeroU", "zerou", "oneF", "onef",
         "zeroA", "zeroa", "oneH", "oneh", "zeroD", "zerod",
         "oneL", "onel", "zeroG", "zerog", "oneZ", "onez"]

lett_v = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g",
          "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n",
          "Ñ", "ñ", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
          "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", " ", ",", 
          ".", ":", ";", "_", "á", "é", "í", "ó", "ú", "@", "(", ")", "¿", "?",
          "¡", "!", "$", "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Dictionary
dic_v = {lett_v:enc_v_s for (lett_v, enc_v_s) in zip(lett_v, enc_v_s)}

# Features
def enc_m(message):
    lista_m = []
    result = ""
    for letra in message:
        lista_m.append(letra)
    for letra in lista_m:
        if letra in dic_v:
            result += dic_v[letra]
    return result

def dec_m(encm):
    key_found = []
    pattern = r'(zero|one)([a-zA-Z])'
    matches = re.findall(pattern, encm)
    lista = [match[0] + match[1] for match in matches]
    for encript in lista:
        for key, value in dic_v.items():
            if encript == value:
                key_found.append(key)
    result = ''.join(key_found)
    return result

def copiar_texto(texto):
    pyperclip.copy(texto)

def pegar_texto():
    return pyperclip.paste()