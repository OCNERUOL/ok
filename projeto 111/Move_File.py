import os
import shutil

pasta_inicial = r'C:\Users\Casa\OneDrive\Área de Trabalho\projeto 111\Arquivos_Documentos\pasta inicial'

pasta_final = r'C:\Users\Casa\OneDrive\Área de Trabalho\projeto 111\Arquivos_Documentos\pasta final'

lista_de_arquivos = os.listdir(pasta_inicial)
print(lista_de_arquivos)



for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivo)

    if extensao == '':
        continue
    if extensao in ['.png', '.jpg', '.jfif']:
        pasta1 = pasta_inicial + '/' + arquivo
        pasta2 = pasta_final + '/' + arquivo
        
        print("movendo " + arquivo + ' ... ')
        shutil.move(pasta1, pasta2)
