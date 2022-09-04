# Probabilidade de ter ladrão
    # V, F
l = [0.001, 0.999]
# Probabilidade de ter terremoto
    # V, F
t = [0.002, 0.998]
# João ligar e não ligar, e ter alarme
    # V, F
j = [0.90, 0.05]
# Maria ligar e não ligar, e ter alarme
      # V, F
m  = [0.70, 0.01]

# [ladrao, terremoto, V - Alarme, F - Alarme]
probAlarme = [
              [True, True, 0.950, 0.050],
              [True, False, 0.950, 0.050],
              [False, True, 0.290, 0.710],
              [False, False, 0.001, 0.999] 
            ]

print ("Digite 1 para SIM e 2 para NÃO.")
flagJoaoLiga = True if int(input("João ligou? \n1 - S \n2 - N\n-> ")) == 1 else False
flagMariaLiga = True if int(input("Maria ligou? \n1 - S \n2 - N\n-> ")) == 1 else False
flagLadrao = True if int(input("Tem ladrão? \n1 - S \n2 - N\n-> ")) == 1 else False
flagTerremoto = True if int(input("Tem terremoto? \n1 - S \n2 - N\n-> ")) == 1 else False
flagAlarme = True if int(input("O alarme tocou? \n1 - S \n2 - N\n-> ")) == 1 else False

probabilidade = 1.0

if (flagJoaoLiga): 
  probabilidade *= j[0]
else:
  probabilidade *= j[1]

if (flagMariaLiga): 
  probabilidade *= m[0]
else:
  probabilidade *= m[1]

if (flagLadrao): 
  probabilidade *= l[0]
else:
  probabilidade *= l[1]

if (flagTerremoto): 
  probabilidade *= t[0]
else:
  probabilidade *= t[1]



for linha in probAlarme:
  if (flagAlarme):
    if (linha[0] == flagLadrao and linha[1] == flagTerremoto):
      probabilidade *= linha[2]
  else: 
    if (linha[0] == flagLadrao and linha[1] == flagTerremoto):
      probabilidade *= linha[3]


print("A probabilidade é de "+ str(round(probabilidade,7)))

# A probabilidade de o alarme tocar sem ocorrência de ladrão, nem terremoto, mas com ligação de João e Maria = 0.00062

# P(j, m, a, ~l, ~t) = p(j|a) * p(m|a) * p(a | ~l ~t) * p (~l) * p(~t) 
# p(j|a) -> probabilidade de João ligar e ter alarme
# p(m|a) -> probabilidade de Maria ligar e ter alarme
# p(a | ~l ~t) -> probabilidade do alarme tocar e não ter ladrão e não ter terremoto 
# p(~l) -> probabilidade de não ter ladrão
# p(~t) -> probabilidade de não ter terremoto
