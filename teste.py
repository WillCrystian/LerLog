def ler_arquivo(caminho_arquivo, numero_agv):
    
    lt_info = []
    nova_tarefa = f'[AgvNr:{numero_agv}] : Encontrado tarefa:'
    
    logs = open(caminho_arquivo, 'r')
    
    for log in logs:
        if nova_tarefa in log:
            lista_reduzida = []
            lista_reduzida.append(log.split()[1].split(',')[0])
            lista_reduzida.append(log.split()[8].split(':')[1])
            lista_reduzida.append(':'+log.split()[9].split(':')[1])
            lt_info.append(lista_reduzida)
    logs.close()
    
    return lt_info
   
def organizar_dados(lt_info):
    tag_descarga = 0
    lt_escrever = []
    
    while len(lt_info) > 0:
        lt_final = []
        if len(lt_final) < 6:

            if len(lt_final) == 0 and len(lt_info) > 0:
                if ':UNLOAD' in lt_info[0][2] and len(lt_info) > 0:
                    lt_info.remove(lt_info[0]) # remover linha
                elif ':NONE' in lt_info[0][2] and len(lt_info) > 0:
                    lt_final.append(lt_info[0][1]) # adicionar tag
                    lt_info.remove(lt_info[0]) # remover linha
                elif ':LOAD' in lt_info[0][2] and len(lt_final) == 0 and len(lt_info) > 0:
                    lt_final.append(tag_descarga)
                    lt_final.append(lt_info[0][0]) # adicionar horario
                    lt_final.append(lt_info[0][1]) # adicionar tag
                    lt_info.remove(lt_info[0])

            if len(lt_final) == 1 and len(lt_info) > 0:
                if ':LOAD' in lt_info[0][2]:
                    lt_final.append(lt_info[0][0]) # adicionar horario
                    lt_final.append(lt_info[0][1]) # adicionar tag
                    lt_info.remove(lt_info[0])

            if len(lt_final) == 3 and len(lt_info) > 0:
                if ':UNLOAD' in lt_info[0][2]:
                    lt_final.append(lt_info[0][0]) # adicionar horario
                    lt_final.append(lt_info[0][1]) # adicionar tag
                    lt_info.remove(lt_info[0])

            if len(lt_final) == 5 and len(lt_info) > 0:
                if ':NONE' in lt_info[0][2]:
                    lt_final.append(lt_info[0][0]) # adicionar horario

                elif ':LOAD' in lt_info[0][2]:
                    lt_final.append(lt_info[0][0]) # adicionar horario

        if len(lt_final) > 3:
            tag_descarga = lt_final[4]
        else:
            tag_descarga = 0

        if len(lt_final) == 6:
            lt_escrever.append(lt_final)
    
    return lt_escrever

def escrever_arquivo(arquivo, lista_dados):
    import xlsxwriter
    
    workbook = xlsxwriter.Workbook(arquivo)
    worksheet = workbook.add_worksheet()
    
    row = 0
    
    for linha in lista_dados:
        for index, coluna in enumerate(linha):
            worksheet.write(row, index, coluna)
     
        row += 1
    workbook.close()
    
    return print('Arquivo escrito com sucesso!')