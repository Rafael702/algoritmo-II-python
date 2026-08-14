### Exercício ###
# Considere uma entidade Funcionário, que possui
# nome, data de admissão e salário. Implemente sua
# classe, definindo também alguns métodos para
# manipulação dos atributos.
# Em seguida, considere a entidade Gerente, que
# também é um funcionário. Além dos atributos de
# funcionário, um gerente também contém um
# bônus, que é uma porcentagem adicional aplicada
# no seu salário.
# Implemente a classe Gerente como uma extensão
# de Funcionário.

class funcionario():
    def __init__(self, nome, dtAdmissao,salario):
        self.nome = nome
        self.dtAdmissao = dtAdmissao
        self.salario = salario
    
    def __repr__(self):
        return '(' + 'Nome:' + str(self.nome) + ',Data de Admissao:' + str(self.dtAdmissao) + ',Salario:R$' + str(self.salario) + ')'

f = funcionario("John", "23/05/2001", 1500)
print(f)

class gerente(funcionario):
    def bonus(self):
        self.salario += self.salario * 0.2

g = gerente("Bensom", "01/01/1990", 4500)
print(g)
g.bonus()
print(g)

class seguranca(funcionario):
    pass

s = seguranca("Aroldo", "25/11/1985", 2600)
print(s)