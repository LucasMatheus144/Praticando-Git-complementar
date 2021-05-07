dados = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome,[nota1 , nota2],media])
    esc = str(input('Deseja continuar: ')).strip().upper()[0]
    if esc in 'N':
        break
print('='*40)
for u,n in enumerate(dados):
    print(f'{u:<4}{n[0]:<10}{n[2]:>8.1f}')
print('='*40)
while True:
    op = int(input('Mostrar nota de qual aluno[999 para encerrar]: '))
    if op == 999:
        break
    else:
        if op <= len(dados):
            print(f'O(a) aluno(a) {dados[op][0]} tirou as notas {dados[op][1]}')
        else:
            print('O alunao nao foi adicionado no sistema')
print('--------------------FINALIZANDO--------------------')