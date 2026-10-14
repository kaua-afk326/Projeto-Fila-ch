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

# Os sintomas são normalizados para permitir buscas por palavras-chave,
# inclusive quando o usuário digita mais de um sinal no mesmo campo.
sintoma_normalizado = " ".join(triagem.lower().split())

# Sintomas de maior risco: exigem atendimento immediado.
sintomas_muito_graves = (
    "dor no peito", "falta de ar", "desmaio", "paralise", "desmaio",
    "sangue no vomito", "vomito sangue", "vomito constante",
    "confusão", "desidratação", "temperatura muito alta",
    "dor intensa", "dor súbita", "cessação de respiração"
)

# Sintomas graves que precisam de avaliação urgente.
sintomas_graves = (
    "febre alta", "fratura", "lesão importante", "lesão no braço",
    "lesão na perna", "vomito", "diarréia", "dor de cabeça intensa",
    "dor forte", "sangue", "inchaço importante", "dor abdominal"
)

# Sintomas moderados.
sintomas_moderados = (
    "febre", "enjoo", "dor de cabeça", "coriza", "espirro", "gripe",
    "dor muscular", "dor de barriga", "cansaço", "tontura"
)

# Sintomas leves e sinais de acompanhamento.
sintomas_leves = (
    "mialgia", "dor de garganta", "nariz congestionado", "estômago ruim",
    "perda de apetite", "calor", "só roxo"
)

prioridade = 1

if any(sintoma in sintoma_normalizado for sintoma in sintomas_muito_graves):
    prioridade = 10
elif any(sintoma in sintoma_normalizado for sintoma in sintomas_graves):
    prioridade = 8
elif any(sintoma in sintoma_normalizado for sintoma in sintomas_moderados):
    prioridade = 5
elif any(sintoma in sintoma_normalizado for sintoma in sintomas_leves):
    prioridade = 3

# Ajustes adicionais de acordo com a idade e a condição gestacional.
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
