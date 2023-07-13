class Smartphone:
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def descricao(self):
        print(f'O smartphone {self.modelo} é da marca {self.marca}.')

    def ano_lancamento(self):
        print(f'O ano de lançamento do smartphone {self.modelo} da marca {self.marca} é {self.ano}.')

marca = input('Qual a marca do seu smartphone? ')
modelo = input('Qual o modelo do seu smartphone? ')
ano = int(input('Qual o ano de lançamento do seu smartphone? '))

smartphone = Smartphone(marca,modelo,ano)
smartphone.descricao()
smartphone.ano_lancamento()
print()


class Smartphone_capacidade(Smartphone):
    def __init__(self, marca, modelo, ano, capacidade):
        super().__init__(marca, modelo, ano)
        self.capacidade = capacidade


    def especificacao(self):
        print(f'O smartphone {self.modelo} da marca {self.marca} tem {self.capacidade} gb de capacidade.')


capacidade = int(input('Qual a capacidade do seu smartphone? '))

especificacao_smartphone = Smartphone_capacidade(marca,modelo,ano,capacidade)
especificacao_smartphone.especificacao()
print()



class Smartphone_saida(Smartphone):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)


    def sair_de_linha(self):
        periodo = int(input('Quantos anos esse modelo permanecerá em linha? '))
        self.ano += periodo
        print(f'O smartphone {self.modelo} da marca {self.marca} sairá de linha em {self.ano}.')



ano = Smartphone_saida(marca,modelo,ano)


ano.ano_lancamento()
ano.sair_de_linha()    
