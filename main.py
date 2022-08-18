from teste import ler_arquivo, organizar_dados, escrever_arquivo

arquivo = './TrafficWarden.txt'
onde_escrever = './tabela_tempo.xlsx'
quantidade_agv = 3
lista_dados = []

for agv in range(quantidade_agv):
        
    arquivo_filtrado = ler_arquivo(arquivo, agv + 1)
    arquivo_organizado = organizar_dados(arquivo_filtrado)
    
print(escrever_arquivo(onde_escrever, lista_dados))
