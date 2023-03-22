from consultas.consulta01 import consulta01
from consultas.consulta02 import consulta02
from consultas.consulta03 import consulta03
from consultas.consulta04 import consulta04
from consultas.consulta05 import consulta05
from consultas.consulta06 import consulta06
from consultas.consulta07 import consulta07
from consultas.consulta08 import consulta08
from consultas.consulta09 import consulta09
from consultas.consulta10 import consulta10

opt = int(input("""
informe uma opção:
1 - selecionar todos as pessoas que tem mais de 18 anos;
2 - selecionar todas as colunas da cidade;
3 - selecionar a uf e quantas cidades tem em cada uf;
4 - selecionar a pessoa mais velha;
5 - selecionar qual a pessoa mais nova;
6 - selecionar o nome, endereco, telefone, celular, nome_cidade, nascimento das pessoas que moram no PR;
7 - selecionar as cidades possuem pessoas cadastradas e quantas pessoas em cada cidade;
8 - selecionar todas as pessoas ativas exibindo todas as colunas ordenando pelo telefone;
9 - selecionar todas as cidades que nao possuem pessoas;
10 - selecionar quais pessoas tem e-mail do hotmail.
"""))

match opt:
    case 1:
        consulta01()
    case 2:
        consulta02()
    case 3:
        consulta03()
    case 4:
        consulta04()
    case 5:
        consulta05()
    case 6:
        consulta06()
    case 7:
        consulta07()
    case 8:
        consulta08()
    case 9:
        consulta09()
    case 10:
        consulta10()