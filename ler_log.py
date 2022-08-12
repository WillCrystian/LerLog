import xlsxwriter

############ fazer leitura do arquivo e filtar #############
workbook = xlsxwriter.Workbook('./tabela_tempo.xlsx')
worksheet = workbook.add_worksheet()

numero_agv = 3
row = 0

for agv in range(numero_agv):
    logs = open('./TrafficWarden.txt', 'r')
    nova_tarefa = f'[AgvNr:{agv+1}] : Encontrado tarefa:'

    tag_descarga = 0
    lt_info = []
    lt_escrever = []

    #1  '09:45:55,058' ,8    TARGET_POSITION:802, 9 TARGET_ACTION:NONE

    #percorrer linha por linha e pegar informaçoes necessárias
    for log in logs:
        if nova_tarefa in log:
            lista_reduzida = []
            lista_reduzida.append(log.split()[1].split(',')[0])
            lista_reduzida.append(log.split()[8].split(':')[1])
            lista_reduzida.append(':'+log.split()[9].split(':')[1])
            lt_info.append(lista_reduzida)
    logs.close()

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

    ###### escrever arquivo ########
    column = 0
    worksheet.write(row, column, f'LGV{agv+1}')
    row += 1
    for a,b,c,d,e,f in lt_escrever:

        worksheet.write(row, column, a)
        worksheet.write(row, column +1, b)
        worksheet.write(row, column +2, c)
        worksheet.write(row, column +3, d)
        worksheet.write(row, column +4, e)
        worksheet.write(row, column +5, f)
        row += 1
workbook.close()