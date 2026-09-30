import json
import os

triagem = input("O que você está sentindo? ")
idade = int(input("Quantos anos você tem? "))
genero = input("Você é homem ou mulher? ").lower()

gravida = False

if genero == "mulher":
    resposta = input("Você está grávida? (sim/não) ").lower()
    if resposta == "sim":
        gravida = True

prioridade = 1

# Sintomas muito graves
if triagem.lower() in ["dor no peito", "falta de ar", "desmaio"]:
    prioridade = 10

# Sintomas graves
elif triagem.lower() in ["febre alta", "fratura", "dor intensa"]:
    prioridade = 8

# Sintomas moderados
elif triagem.lower() in ["febre", "enjoo", "dor de cabeça"]:
    prioridade = 5

# Sintomas leves
elif triagem.lower() in ["coriza", "espirro", "gripe"]:
    prioridade = 3

# Ajustes
if idade >= 65:
    prioridade += 1

if idade <= 5:
    prioridade += 1

if gravida:
    prioridade += 1

if prioridade > 10:
    prioridade = 10


pacientesFila = "pacientes.json"

# Se o arquivo existir, carrega os pacientes
if os.path.exists(pacientesFila):
    with open(pacientesFila, "r", encoding="utf-8") as arquivo:
        fila = json.load(arquivo)
else:
    fila = []

# Adiciona o novo paciente à fila
fila.append(pacientesFila)

# Salva a fila atualizada
with open(pacientesFila, "w", encoding="utf-8") as arquivo:
    json.dump(fila, arquivo, ensure_ascii=False, indent=4)

print(f"\nPaciente adicionado à fila.")
print(f"Total de pacientes: {len(fila)}")

# Dicionário (vira JSON)
pacienteSentindo = {
    "sintoma": triagem,
    "idade": idade,
    "genero": genero,
    "gravida": gravida,
    "prioridade": prioridade
}

# Salva em JSON
with open("pacienteSentindo.json", "w", encoding="utf-8") as arquivo:
    json.dump(pacienteSentindo, arquivo, ensure_ascii=False, indent=4)

print("\n--- RESULTADO DA TRIAGEM ---")
print(f"Prioridade: {prioridade}/10")

if prioridade >= 9:
    print("URGÊNCIA MÁXIMA")
elif prioridade >= 7:
    print("URGENTE")
elif prioridade >= 4:
    print("MODERADO")
else:
    print("Vai pra casa seu **** vc ta bem imundo")

print("\nDados salvos em pacienteSentindo.json")

#Usuário digita sintomas
#       ↓
#Sistema calcula prioridade
#       ↓
#Cria um dicionário
#        ↓
#Converte para JSON
#        ↓
#Salva em paciente.json
#        ↓
#Mostra o resultado na tela
