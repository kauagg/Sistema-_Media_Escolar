""" @Dev_KauaGB, Kauã Gomes Barbosa Pereira."""""

def calcular_media(notas):
    return sum(notas) / len(notas)

def obter_notas():

    notas = []
    while len(notas) < 4:
        try:
            nota = float(input(f"Digite a nota {len(notas) + 1} (máximo 10): "))
            if nota < 0 or nota > 10:
                print("Error: A nota deve Ser de 0 a 10!")
            else:
                notas.append(nota)
        except ValueError:
            print("Erro: Digito Invalido, Retornando Perguntas.")
    return notas

def main():
    usuario = input("Descrimine a Identificação do Aluno Por Completo: ")
    notas = obter_notas()
    
    media = calcular_media(notas)
    
    resultado = f"Usuário: {usuario}\nNotas: {notas}\nMédia: {media:.2f}"
    
    # Escrevendo o resultado em um arquivo de texto
    with open("Sistema_Notas_Aula/resultado_final.txt", "w") as arquivo:
        arquivo.write(resultado)

    print("Resultados salvos em resultado.txt")

# Executando o programa
if __name__ == "__main__":
    main()
