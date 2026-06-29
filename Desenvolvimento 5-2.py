from datetime import datetime

# 1. Recebe o nome completo do usuário (texto puro)
nome = input("Digite seu nome: ")

# 2. Loop de validação (continua perguntando até que o valor seja correto)
while True:
    try:
        # Recebe a data de nascimento completa
        data_input = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        
        # Converte o texto para um objeto de data real do Python
        data_objeto = datetime.strptime(data_input, "%d/%m/%Y")
        
        # Extrai o ano para validação
        ano_nas = data_objeto.year
        
        # Valida se o ano está dentro do intervalo estipulado (1922-2021)
        if 1922 <= ano_nas <= 2021:
            break  # Ano válido! Sai do loop e segue o programa
        else:
            print("Erro: O ano de nascimento deve estar entre 1922 e 2021. Tente novamente.\n")
            
    except ValueError:
        # Trata o erro caso o usuário digite letras, mude o formato ou insira datas inexistentes
        print("Erro: Entrada inválida! Por favor, digite uma data válida no formato DD/MM/AAAA.\n")

# 3. Lógica de cálculo da idade baseada no ano de 2022
# Cria uma data de referência travada no último dia do ano de 2022 (ou você pode usar a data de hoje)
# Para fins didáticos de "completou ou completará", vamos simular que estamos em 30/06/2022
data_referencia_2022 = datetime(2022, 6, 30)

# Descobre o dia do aniversário da pessoa no ano de 2022
aniversario_2022 = data_objeto.replace(year=2022)

# Calcula a idade que ela faz no ano de 2022
idade_2022 = 2022 - ano_nas

# Verifica se a data do aniversário já passou ou não em relação à nossa referência de 2022
if aniversario_2022 <= data_referencia_2022:
    mensagem_idade = f"completou {idade_2022} anos"
else:
    mensagem_idade = f"completará {idade_2022} anos"

# 4. Exibição dos resultados conforme solicitado
print("-" * 40)
print(f"Nome do Usuário: {nome}")
print(f"No ano de 2022, você {mensagem_idade}.")
print("-" * 40)