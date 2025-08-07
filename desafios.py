# Exercícios
## Inteiros (int)
#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

try:
    numero_1 :int = int(input("Digite o primeiro número inteiro: "))   
    numero_2 :int = int(input("Digite o segundo número inteiro: ")) 
    resultado :int = numero_1 + numero_2
    print(f"O resultado da soma é: {resultado}")

except ValueError:
    print("Por favor, digite um número inteiro, não são aceitos outros valores nessa solução.")


# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
try:

    valor_usuario : int= int(input("Olá, usuário! Digite aqui um valor: "))
    resultado_divisao = valor_usuario % 5
    print(f"O resto dessa divisao por 5 é: {resultado_divisao}") 

except ValueError as e:
    print(e)   

# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    numero_multiplicacao_1 = int(input("Insira aqui o primeiro valor inteiro para a multiplicação: "))
    numero_multiplicacao_2 = float(input("Insira aqui um número real para a multiplicação: "))

    resultado_multiplicacao : float = float(numero_multiplicacao_1*numero_multiplicacao_2)

    print(f"O resultado da multiplicação é: {resultado_multiplicacao}")

except ValueError:
    print("Por favor digite um número válido!")    


# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    divisao_inteiro_1 = int(input("Insira aqui o primeiro valor inteiro para a divisão: "))
    divisao_inteiro_2 = int(input("Insira aqui uo segundo valor para a a divisão: "))

    resultado_duvisao_inteira : int = int(divisao_inteiro_1 // divisao_inteiro_1)

    print(f"O resultado da divisão inteira é: {resultado_duvisao_inteira}")

except ValueError:
    print("Por favor digite um número inteiro!")    


# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
try:
    valor_quadrado = float(input("Insira aqui o valor que deseja descobrir seu quadrado: "))

    resutado_quadrado : float = float(valor_quadrado**2)

    print(f"O quadrado de {valor_quadrado} é: {resutado_quadrado}")

except ValueError:
    print("Por favor digite um valor válido! Apenas são aceitos números") 



# Escreva um programa que receba dois números flutuantes e realize sua adição.

valor_soma_float = float(input("Digite aqui o primeiro valor da soma: "))

valor_soma_float2 = float(input("Digite aqui o primeiro valor da soma: "))

resultad_soma_float = valor_soma_float + valor_soma_float2 

print(f"A soma entre {valor_soma_float} e {valor_soma_float2} é {resultad_soma_float}")

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

resultado_media_float = float(resultad_soma_float/2)

print(f"A média entre {valor_soma_float} e {valor_soma_float2} é {resultado_media_float}")


# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
try:
    print("Olá, vamos realizar o cálculo da potência dos valores desejados!")
    base = float(input("Insira aqui o valor da base desejada: "))
    expoente = float(input("Insira aqui o valor do expoente: "))

    potencia : float = float(base**expoente)

    print(f"O resultado da potência é: {potencia}")

except ValueError:
    print("Por favor digite um número válido!")

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
try: 
    temperatura_em_celsius = float(input("Digite aqui a temperatura ep graus celsius: "))
    fahrenheit = (temperatura_em_celsius * 9/5) + 32
    print(f"{temperatura_em_celsius}°C é igual a {fahrenheit}°F")
except ValueError as erro :
    print (erro)

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

try: 
    raio = float(input("Digite aqui o raio do cículo:"))
    area = 3.14159 * raio ** 2

    print(f"A área do círculo é: {area}")

except ValueError as erro :
    print (erro)


# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Digite aqui um texto: ")
texto_upper = texto.upper()
print(texto_upper)
# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
texto_strip = texto.strip()
# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
usuario = input("Digite aqui seu nome: ")
texto_lw = usuario.lower()

print(texto_lw)
# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
try:
    data_dd_mm_aaa = input("Digite aqui a data no formato dd/mm/aaa: ")
    dia,mes,ano = data_dd_mm_aaa.split("/") 
    print(f"O dia é {dia}, o mês é {mes} e o ano é {ano}")

except ValueError:
    print("Digite no formato válido")
    
# Escreva um programa que concatene duas strings fornecidas pelo usuário.

txt_1 = input("Digite a primeira parte do texto: ")
txt_2 = input("Digite a segunda parte do texto: ")

texto_concatenado = txt_1 + txt_1
print("Texto concatenado:", texto_concatenado)

# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valboll_1 = True
valboll_2 = False
resultado_and = valboll_1 and valboll_1
print("Resultado do AND lógico:", resultado_and)

# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado_or = valboll_1 or valboll_1
print("Resultado do or lógico:", resultado_or)
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado_not = not valboll_1
print("Resultado do NOT lógico:", resultado_not)
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = 5
numero2 = "5"

resultado_igualdade = (numero1 == numero2)
print("Resultado da igualdade:", resultado_igualdade)

# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

resultado_diferenca = (numero1 != numero2)
print("Resultado da diferença:", resultado_diferenca)

### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Olá, tudo bem? Insira aqui o seu nome: ").strip()

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
        exit()

    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
        exit()
        
    # Verifica se há caracteres especiais no nome
    elif any(not caracter.isalnum() for caracter in nome):
        raise ValueError("Não são aceitos caracteres especiais no nome de usuário, por favor insira um valor válido.")
        exit()
   
    else:
        print("Nome válido:", nome)

except ValueError as e:
   
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_input = input(f"{nome}, digite aqui o seu salário: ").strip()

    # Verifica se o salário está vazio
    if  len(salario_input) == 0:
        raise ValueError("O salário não pode estar vazio, insira um valor válido.")
        exit()
    
    # Verifica se há caracteres especiais no salario
    elif any(not caracter.isalnum() for caracter in salario_input):
        raise ValueError("Não são aceitos caracteres especiais (#,$,%,@ e etc), por favor insira um valor válido e maior do que 0.")
        exit()
    salario = float(salario_input)

    if salario <= 0:
        raise ValueError("O salário precisa ser maior do que Zero, insira um valor válido.")
        exit()    
       
    else:
        print(f"Valor válido, {nome}, seu salário é de R$ {salario}")

except ValueError as e: 
    print(e)
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante - Vamos tomar como premissa um bonus de até 5 salários e com um valor mínimo de 1 salário.

try:
    bonus_input = input(f"{nome}, digite aqui o seu bônus: ").strip()

    # Verifica se o salário está vazio
    if  len(bonus_input) == 0:
        raise ValueError("O bônus não pode estar vazio, insira um valor válido.")
        exit()
    # Verifica se há caracteres especiais no bonus
   
    elif any(not caracter_bonus.isalnum() for caracter_bonus in bonus_input):
        raise ValueError("Não são aceitos caracteres especiais (#,$,%,@ e etc), por favor insira um valor válido.")
        exit()
    bonus = float(bonus_input)

    if bonus < 1:
        raise ValueError("O bônus precisa ser maior do que 1, insira um valor válido.")
        exit()
    elif bonus > 6:
        raise ValueError ("O seu bonus não pode ser maior do que 6, por favor insira um valor válido.")    
       
 # 4) Calcule o valor do bônus final      
    else:
        constante_bonus = int(1000)
        valor_recebido = round(float(constante_bonus + salario*bonus),2)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
        print(f"{nome}, com o seu salário de R$ {salario} e multiplicador de bonus de {bonus}, o seu bônus anual será de R$ {valor_recebido}, parabéns!")

except ValueError as e: 
    print(e)
    exit()

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


preco = float(10)
quantidade = float(24)

if (preco < 0) or (quantidade < 0):
    print('Preço ou quantidade são negativos! Verificar a qualidade dos dados.')
else:
    print("Dados válidos.")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

try: 
    temperatura_em_celsius = float(input("Digite aqui a temperatura em graus celsius: "))
        
    if temperatura_em_celsius < 18:
        print("Baixa")
    elif temperatura_em_celsius >=18 and temperatura_em_celsius <=26:
        print("Normal")
    else: print ("Alta")

except ValueError as erro :
    print (erro)


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

lista_de_logs = [{'timestamp': '2021-06-23 12:00:00', 'level': 'FATAL', 'message': 'Falha na rede'},
                 {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
                 {'timestamp': '2021-06-23 22:00:00', 'level': 'MEDIUM', 'message': 'Falha no update'},
                 {'timestamp': '2021-06-23 08:00:00', 'level': 'LOW', 'message': 'Falha no geteway'},
                 {'timestamp': '2021-06-23 00:20:00', 'level': 'ERROR', 'message': 'Falha na conexão'}]

valores_criterio_fatal = {'FATAL','ERROR'}

for log in lista_de_logs:
    if log['level'] in valores_criterio_fatal :
        print(log)
    else:
        pass


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


users_lista = []  # Lista que armazenará os dicionários

for i in range(3):  # Loop para 3 usuários
   
    try:
        print(f"\nCadastro do usuário {i+1}:")
        
        # Validação do nome
        nome = input("Nome: ").strip()
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        
        # Validação da idade
        idade = int(input("Idade: ").strip())
        if not (18 <= idade <= 65):
            raise ValueError("Idade deve estar entre 18 e 65 anos.")
        
        # Validação do email 
        email = input("Email: ").strip()
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email inválido.")
        
        # Adiciona à lista apenas se todas as validações passarem
        users_lista.append({
            "nome": nome,
            "idade": idade,
            "email": email
        })
        
    except ValueError as err:
        print(f"Erro: {err}")
        print("Por favor, repita os dados deste usuário.\n")
        continue  # Volta ao início do loop para o mesmo usuário

# Exibe a lista completa
print("\nUsuários cadastrados:")
for usuario in users_lista:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

lista_de_transacoes = [
    {'id_transacao': 'A3F5B2C8D1', 'valor': 12000, 'hora': 2},
    {'id_transacao': '4E7F209C6B', 'valor': 112000, 'hora': 17},
    {'id_transacao': '1B8D3E5F0A', 'valor': 100, 'hora': 21},
    {'id_transacao': '9C2D4A7E1F', 'valor': 12020, 'hora': 20},
    {'id_transacao': '5F0B3D8E2C', 'valor': 1200, 'hora': 22}]

limite_valor = 10000
horarios = range(9,19)

for transacao in lista_de_transacoes:
    if transacao['valor'] >limite_valor or (transacao['hora'] not in horarios):
        print(f"Transação {transacao['id_transacao']} suspeita, verificar")
    else :
        pass

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)


frase = "Olá, teste, estes são dados para o teste é uma frase de teste do jornada de dados"

caracteres_especiais = ',.!?:;"(){}[]<>@#$%^&*_~´`=+/-\\|'

frase_limpa = ''.join([char if char not in caracteres_especiais else ' ' for char in frase]).upper()

frase_splitada = frase_limpa.split()
contagem_palavras = {}

for palavra in frase_splitada:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(frase_splitada)
print(contagem_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [123, 222, 330, 4450, 5880]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

lista_de_users = [
    {'user': 'Roberto', 'grant_level': 'ADMIN', 'Último acesso em': '2021-06-23 10:00:00'},
    {'user': 'Julia', 'grant_level': None, 'Último acesso em': None},
    {'user': 'Carlos', 'grant_level': 'USER', 'Último acesso em': '2023-01-15 14:30:00'},
    {'user': 'Maria', 'grant_level': None, 'Último acesso em': None},
    {'user': 'José', 'grant_level': None, 'Último acesso em': None}
]

users_lista_erros = [] 

for usuario in lista_de_users:
    if usuario['grant_level'] is None or usuario['Último acesso em'] is None:
        users_lista_erros.append({
            "nome": usuario['user'],
            "problema": "Dados incompletos"
        })
        print(f"{usuario['user']} com dados corrompidos, por favor verificar o motivo do Bug!")
    else:
        pass  # Usuários válidos são ignorados

print("\nLista completa de usuários com problemas:")
print(users_lista_erros)

