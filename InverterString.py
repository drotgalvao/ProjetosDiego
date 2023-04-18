# Função para inverter os caracteres de uma string
def inverter_string(string):
    # Converter a string em uma lista de caracteres
    caracteres = list(string)
    # Obter o tamanho da lista de caracteres
    tamanho = len(caracteres)
    # Realizar a troca dos caracteres de posição
    for i in range(tamanho // 2):
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]
    # Converter a lista de caracteres de volta para uma string
    string_invertida = ''.join(caracteres)
    return string_invertida

# Exemplo de uso da função
string = "Target Sistemas"
string_invertida = inverter_string(string)
print("String original:", string)
print("String invertida:", string_invertida)
