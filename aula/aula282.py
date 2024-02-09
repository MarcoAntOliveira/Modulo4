import os
caminho = os.path .join('/home/users', 'desktop', 'curso', 'arquivo.txt')
diretorio , arquivo =os.path.split(caminho)
print(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo)