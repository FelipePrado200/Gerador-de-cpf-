    ## Projeto *gerador de cpf* 
import random

for _ in range(100):
    nove_digitos =''
    for i in range(0,9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    print(digito_1)

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
    soma_1 = (resultado_digito_2 * 10) % 11
    soma_1 = soma_1 if soma_1 <= 9 else 0
    print(soma_1)

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{soma_1}'
    print(cpf_gerado_pelo_calculo)
