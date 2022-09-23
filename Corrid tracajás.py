'''No Brasil há um pouco mais de 33 espécies de quelônios (tartarugas, jabutis e cágados). 
Na Amazônia há uma espécie de cágado de carapaça comumente conhecida como "tracajá", 
mas que é diferente das demais pois geralmente são mais velozes. 
Possui peso variando de 9 a 12kg. 
Pensando na diversão, surgiu um esporte que cresceu muito nos últimos anos em uma cidade do 
interior do Pará a chamada corrida de tracajás. 
Cada tracajá é classificado em um nível dependendo de sua velocidade:

Nível 1: Se a velocidade é menor que 10 km/h.

Nível 2: Se a velocidade é maior ou igual a 10 km/h e menor que 15 km/h.

Nível 3: Se a velocidade é maior ou igual a 15 km/h.

Sua tarefa é identificar qual nível de velocidade do tracajá mais veloz de um grupo de tracajás.

    Entrada:

    A entrada consiste de múltiplos casos de teste, e cada um consiste em várias linhas: 
    a primeira linha contém um inteiro L (1 ≤ L ≤ 50) representando o número de tracajás do grupo, 
    e as outras L linhas contêm inteiros Vi (1 ≤ Vi ≤ 25) representando as velocidades de cada tracajá do grupo. 
    
    Veja o exemplo:

    7

    5 
    2 
    2 
    6 
    7 
    8 
    12

    Saída

    Para cada caso de teste, imprima uma única linha indicando o nível de velocidade do tracajá mais veloz do grupo. 
    Para o exemplo anterior a saída seria:

    2

    Caso algum dos valores esteja fora dos intervalos estabelecidos, 
    uma mensagem de erro deve ser emitida indicando a linha em que o erro ocorreu: 
    Valor inválido na linha <l>. '''

vaux = []
i = niv = 0
quant = int(input("DIGITE A QUANTIDADE DE TRACAJÁS [ENTRE 1 E 50]: "))
while quant < 1 or quant > 50:
    quant = int(input("DIGITE A QUANTIDADE DE TRACAJÁS [ENTRE 1 E 50]: "))
while i < quant:
    veloc = float(input(f"LINHA {i+1} >>> DIGITE A VELOCIDADE DE CADA TRACAJÁ [ENTRE 1 E 25KM/H]: "))
    vaux.append(veloc)
    vaux.sort()
    maior_veloc = vaux[i]
    i += 1

    if 1 <= maior_veloc < 10:
        niv = 1
    elif 10 <= maior_veloc < 15:
        niv = 2
    elif 15 <= maior_veloc < 25:
        niv = 3
    else:
        print(f"VALOR INVÁLIDO NA LINHA {i+1}")
        break
print(f"\n\tO TRACAJÁ MAIS RÁPIDO TEM VELOCIDADE DE {maior_veloc} KM/H CORRESPONDENTE AO NÍVEL {niv}")