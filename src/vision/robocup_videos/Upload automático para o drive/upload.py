from setup import AuthDrive
from googleapiclient.http import MediaFileUpload
import os
import time
from tkinter import messagebox

AuthDrive()
inicial = time.time()

#variável criada para chamar os objetos da classe AuthDrive, de "setup.py", e utilizar seus métodos
authdrive=AuthDrive()

#Função que fará o upload, recebe o nome do arquivo armazenado no sistema e o caminho de sua pasta raiz
def upload_file(filename,path):
    folder_id = '1xJBiyK02XLJhP8korsy0_qpBwCikY22Q' #ID da pasta no Drive. Ex.: https://drive.google.com/drive/u/0/folders/*1INUiysLGmC1tw2sL-PWOsy3yRjctlV_x* <- Esse final aqui
    
    #A variável media contém os dados do arquivo a ser transferido do sistema para o Drive
    media = MediaFileUpload(f"{path}{filename}")

    #Retorna um dicionário de arquivos no Drive que tem nome igual e estão na mesma pasta que queremos fazer o upload 
    response = authdrive.service.files().list(
                                        q=f"name='{filename}' and parents='{folder_id}'",
                                        spaces='drive',
                                        fields='nextPageToken, files(id, name)',
                                        pageToken=None).execute()
    #print(response)

    #Se não existe cópia do arquivo na pasta
    if len(response['files']) == 0: 
        #Cria nova variável que contém as informações do arquivo para referências do Drive
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        #Cria um novo arquivo na pasta, usando a variavel file_metadata como parâmetro 
        file = authdrive.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"Um novo arquivo foi criado {filename}")
        

    #Se existe cópia do arquivo na pasta do Drive. IMPORTANTE: Usar apenas se houver arquivo modificado mas com mesmo nome
    #else:
     #   for file in response.get('files', []):
           # #Faz o update do arquivo na pasta, usando a variavel file.get('id') como parametro 
      #      update_file = authdrive.service.files().update(
       #         fileId=file.get('id'),
        #        media_body=media, #passa um media_body atualizado por media
         #       ).execute()
          #  print(f"Arquivo atualizado {filename}")
            


def main():
    #Diretório onde estão os arquivos para upload
    path='C://Users//Vinicius//Desktop//EDROM//Visão//Teste_Drive//arquivos//'
    files = os.listdir(path)
    qtde=0
    #Nesse for é possível também filtrar os arquivos que serão enviados ao Drive, como desejar
    for item in files:
        upload_file(item,path)
        qtde+=1
    final = time.time()
    messagebox.showinfo("Upload",f"O upload de {qtde} arquivos foi concluido em {(final-inicial)/60} minutos")
if __name__ == '__main__':
    main()

