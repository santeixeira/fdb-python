from database import *
from insercao import *
from transacoes import *

criar_tabelas()

opcao1 = input("Deseja inserir as embarcações? (S/N): ")
if opcao1.lower() == 's':
    inserir_embarcacao((1, 'Navio 1', 'Cargueiro'))
    inserir_embarcacao((2, 'Navio 2', 'Passageiro'))
    inserir_embarcacao((3, 'Navio 3', 'Petroleiro'))
    inserir_embarcacao((4, 'Navio 4', 'Cargueiro'))

opcao2 = input("Deseja inserir os tripulantes? (S/N): ")
if opcao2.lower() == 's':
    inserir_tripulante((1, 'Tripulante1', '1990-01-15', 'Oficial de Convés', 1))
    inserir_tripulante((2, 'Tripulante2', '1992-03-20', 'Engenheiro', 1))
    inserir_tripulante((3, 'Tripulante3', '1988-11-05', 'Comissário de Bordo', 2))
    inserir_tripulante((4, 'Tripulante4', '1995-06-30', 'Oficial de Convés', 3))
    inserir_tripulante((5, 'Tripulante5', '1991-07-10', 'Capitão', 4))
    inserir_tripulante((6, 'Tripulante6', '1994-09-25', 'Engenheiro', 4))

opcao3 = input("Deseja inserir os empregados? (S/N): ")
if opcao3.lower() == 's':
    inserir_empregados((1, 'Employee1', '1985-05-12', 'Manutenção'))
    inserir_empregados((2, 'Employee2', '1993-02-28', 'Segurança'))
    inserir_empregados((3, 'Employee3', '1987-09-18', 'Logística'))
    inserir_empregados((4, 'Employee4', '1990-12-05', 'Limpeza'))
    inserir_empregados((5, 'Employee5', '2001-08-30', 'Manutenção'))

opcao4 = input("Deseja inserir as movimentações? (S/N): ")
if opcao4.lower() == 's':
    inserir_movimentacoes((1, '2023-09-01', 'Carga', 1))
    inserir_movimentacoes((2, '2023-09-02', 'Embarque de Passageiros', 2))
    inserir_movimentacoes((3, '2023-10-03', 'Abastecimento', 3))
    inserir_movimentacoes((4, '2023-10-05', 'Descarga', 1))
    inserir_movimentacoes((5, '2023-10-05', 'Manutenção', 4))

opcao5 = input("Deseja atribuir empregado a movimentação? (S/N): ")
if opcao5.lower() == 's':
    atribuir_empregado_movimentacao((1, 1))
    atribuir_empregado_movimentacao((1, 3))
    atribuir_empregado_movimentacao((2, 2))
    atribuir_empregado_movimentacao((3, 1))
    atribuir_empregado_movimentacao((3, 4))
    atribuir_empregado_movimentacao((4, 1))
    atribuir_empregado_movimentacao((4, 3))
    atribuir_empregado_movimentacao((5, 1))

opcao6 = input("Deseja inserir nova movimentação? (S/N): ")
if opcao6.lower() == 's':
    inserir_nova_movimentacao((6, '2023-10-05', 'Manutenção', 1))

opcao7 = input("Deseja inserir empregado em nova movimentação? (S/N): ")
if opcao7.lower() == 's':
    inserir_nova_movimentacao_empregado((6, 1))

opcao8 = input("Deseja retornar quantidade de movimentações envolvendo cargueiros? (S/N): ")
if opcao8.lower() == 's':
    retornar_quantidade_movimentacoes_cargueiro()