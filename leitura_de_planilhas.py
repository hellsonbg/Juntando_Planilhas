import os
from pathlib import Path
import pandas as pd


caminho= Path.cwd()
print(caminho)

planilha = pd.DataFrame(columns=['Loja','Vendedor','Valor da Venda'])#CRIANDO DATAFRAME PARA ARMAZENAR OS DADOS COLETADOS DAS PLANILHAS

for pasta in caminho.iterdir():
    if pasta.is_dir():
        os.chdir(pasta)
        caminho= Path.cwd()
        for pasta in caminho.iterdir():
            if pasta.is_dir():
                os.chdir(pasta)
                caminho= Path.cwd()
                for pasta in caminho.iterdir():
                    if pasta.is_dir():
                        os.chdir(pasta)
                        caminho= Path.cwd()
                        print(caminho)
                        for pasta in caminho.iterdir():
                            if pasta.is_dir():
                                os.chdir(pasta)
                                caminho= Path.cwd()
                                print(caminho)
                                for arquivo in caminho.iterdir():
                                    print(arquivo)
                                    venda = pd.read_excel(arquivo,engine='openpyxl') #LENDO CADA PLANILHA
                                    planilha = planilha.append(venda,ignore_index=True) #COLOCANDO
print(planilha)
vendas_total = planilha.groupby(by="Loja").sum()#MOSTRANDO VALORES DO DATAFRAME AGRUPADOS
del vendas_total['Vendedor']#TIRANDO A INFORMAÇÃO DOS VENDEDORES
print(vendas_total)
os.chdir('---------------')#<<<CAMINHO DO OUTPUT DO ARQUIVO AQUI
print(Path.cwd())
vendas_total.to_excel("Vendas por Loja.xlsx")#CRIANDO ARQUIVO EM EXCEL COM AS INFORMAÇÕES DO TOTAL DE VENDAS FILTRADO POR LOJA



                            