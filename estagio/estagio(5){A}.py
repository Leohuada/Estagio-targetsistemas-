def inverter_string(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):  # Loop de trás para frente
        invertida += s[i]
    return invertida

# Exemplo de uso
string_original = "Exemplo de string"
string_invertida = inverter_string(string_original)
print(f"Original: {string_original}")
print(f"Invertida: {string_invertida}")