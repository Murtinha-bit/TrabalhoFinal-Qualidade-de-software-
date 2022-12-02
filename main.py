class Pessoa:
    #pedindo peso e altura
    def __init__(self, peso, altura, idade, sexo):
        self.peso = peso
        self.altura = altura
        self.imc = 0
        self.idade = idade
        self.sexo = sexo
    
    
    def calculaImc(self):
        imc = self.peso / (self.altura **2)
        if(imc < 20):
            print(f'IMC = {round(imc, 2)} - Abaixo do peso')
        elif(imc >= 20 and imc < 25):
            print(f'IMC = {round(imc, 2)} - Peso Normal')
        elif(imc >= 25 and imc < 30):
            print(f'IMC = {round(imc, 2)} - Sobre Peso')
        elif(imc >= 30 and imc < 40):
            print(f'IMC = {round(imc, 2)} - Obeso')
        elif(imc >= 40):
            print(f'IMC = {round(imc, 2)} - Obeso Mórbido')

    def calculaPesoIdeal(self):
        if self.idade < 3:
            print('Sua idade nao se enquadra na idade permitida para calcular o seu peso ideal')
        elif self.idade >= 3 and self.idade <= 10:
            pI = (self.idade * 2) + 9
        elif self.idade >= 18 and self.idade <= 64:
            if self.sexo == 'M':
                imcDesejado = 22
                pI = imcDesejado * (self.altura * self.altura)
            elif self.sexo == 'F':
                imcDesejado = 21
                pI = imcDesejado * (self.altura * self.altura)
        elif self.idade >= 65:
            if self.idade >= 65 and self.idade <= 69:
                if self.sexo == 'M':
                    imcDesejado = 24.3
                elif self.sexo == 'F':
                    imcDesejado = 26.5
            elif self.idade >= 70 and self.idade <= 74:
                if self.sexo == 'M':
                    imcDesejado = 25.1
                elif self.sexo == 'F':
                    imcDesejado = 26.3
            elif self.idade >= 75 and self.idade <= 79:
                if self.sexo == 'M':
                    imcDesejado = 23.9
                elif self.sexo == 'F':
                    imcDesejado = 26.1
            elif self.idade >= 80 and self.idade <= 84:
                if self.sexo == 'M':
                    imcDesejado = 23.7
                elif self.sexo == 'F':
                    imcDesejado = 25.5
            elif self.idade >= 85:
                if self.sexo == 'M':
                    imcDesejado = 23.1
                elif self.sexo == 'F':
                    imcDesejado = 23.6
            pI = imcDesejado * (self.altura * self.altura)
        print(f'Seu peso ideal é: {pI} \n')
            
            

class DailyEnergy:
    def __init__(self, peso, altura, idade, sexo):
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.sexo = sexo
        self.tmb = 0
        self.fa = 0
    
    

    def calculaTMB(self):
        if self.idade >= 10 and self.idade < 18:
            if self.sexo == 'M':
                self.tmb = 17.5 * self.peso + 651
            elif self.sexo == 'F':
                self.tmb = 12.2 * self.peso + 746
        elif self.idade >= 18 and self.idade < 30:
            if self.sexo == 'M':
                self.tmb = 15.3 * self.peso + 679
            elif self.sexo == 'F':
                self.tmb = 14.7 * self.peso + 496
        elif self.idade >= 30 and self.idade < 60:
            if self.sexo == 'M':
                self.tmb = 8.7 * self.peso + 879
            elif self.sexo == 'F':
                self.tmb = 8.7 * self.peso + 829
        elif self.idade >= 60:
            if self.sexo == 'M':
                self.tmb = 13.5 * self.peso + 487
            elif self.sexo == 'F':
                self.tmb = 10.5 * self.peso + 596
    

    def calculaFA(self):
        print('Digite o numero que a descricao mais combina com sua rotina: \n')
        print('1 - Fica a maior parte do tempo sentada e não pratica atividades físicas programadas. \n')
        print('2 - Dia-a-dia movimentado – dirige, cozinha, caminha até o ponto de ônibus, mas sem atividades físicas programadas \n OU dia-a-dia sedentário e exercícios físicos três vezes por semana, cerca de 30 minutos por dia. \n')
        print('3 - Dia-a-dia movimentado e atividades físicas três vezes por semana, cerca de 30 minutos por dia. \n')
        print('4 - De uma a duas horas e meia de atividades físicas diárias. \n')
        escolha = int(input('5 - Atividade física diária por mais de três horas.\n'))
        if escolha == 1:
            self.fa = 1.2
        elif escolha == 2:
            if self.sexo == 'M':
                self.fa = 1.4
            elif self.sexo == 'F':
                self.fa = 1.3
        elif escolha == 3:
            if self.sexo == 'M':
                self.fa = 1.5
            elif self.sexo == 'F':
                self.fa = 1.45
        elif escolha == 4:
            if self.sexo == 'M':
                self.fa = 1.6
            elif self.sexo == 'F':
                self.fa = 1.5
        elif escolha == 5:
            if self.sexo == 'M':
                self.fa = 1.8
            elif self.sexo == 'F':
                self.fa = 1.7

    def calculaEnergia(self):
        energia = self.tmb * self.fa
        print(f'Sua necessidade de energia diaria é {energia}')
        
    
    
        
        




print('Calcula IMC \n')
print('============')
peso = float(input('Peso: '))
altura = float(input('Altura: '))
idade = float(input('Idade: '))
sexo = input('Sexo (M/F): ')
pessoa = Pessoa(peso, altura, idade , sexo)
pessoa.calculaImc()
pessoa.calculaPesoIdeal()
energiaPessoa = DailyEnergy(peso, altura, idade , sexo)
energiaPessoa.calculaTMB()
energiaPessoa.calculaFA()
energiaPessoa.calculaEnergia()
