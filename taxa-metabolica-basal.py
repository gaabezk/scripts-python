# Algoritmo para calcular a taxa metabólica basal (TMB) em kcal/dia
# baseado na fórmula de Harris-Benedict

# Informações do usuário
sexo = input("Qual é o seu sexo (M/F)? ")
peso = float(input("Qual é o seu peso em kg? "))
altura = float(input("Qual é a sua altura em cm? "))
idade = int(input("Qual é a sua idade em anos? "))
nivel_atividade = input("Qual é o seu nível de atividade física (sedentário, pouco ativo, moderado, muito ativo ou "
                        "extremamente ativo)? ")

# Fatores de atividade física
fatores_atividade = {
    "sedentário": 1.2,
    "pouco ativo": 1.375,
    "moderado": 1.55,
    "muito ativo": 1.725,
    "extremamente ativo": 1.9
}
fator_atividade = fatores_atividade[nivel_atividade]

# Fórmula de Harris-Benedict
if sexo == "M":
    tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
else:
    tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

tmb *= fator_atividade

# Mostrar resultado
print("Sua taxa metabólica basal é de aproximadamente", round(tmb), "calorias por dia.")

# Cálculo para emagrecer
perda_peso = float(input("Quantos quilos você deseja perder por semana? "))
deficit_calorico = perda_peso * 7700 / 7  # 7700 calorias correspondem a 1 kg de gordura corporal
calorias_para_emagrecer = tmb - deficit_calorico
print("Para perder", perda_peso, "kg de gordura corporal por semana, você precisaria ingerir cerca de",
      round(calorias_para_emagrecer), "calorias por dia.")