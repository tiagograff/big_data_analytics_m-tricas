import pandas as pd
import banco as banco
# arquivo csv
arquivo = "sinasc/csv/DNRS2022.csv"
# ler arquivo csv
df = pd.read_csv(arquivo)

# excluindo colunas
colunas_para_deletar = ["ORIGEM", "CODMUNNASC", "LOCNASC", "IDADEMAE", "ESTCIVMAE", "ESCMAE", "CODOCUPMAE", "QTDFILVIVO", "QTDFILMORT", "CODMUNRES", "GESTACAO", "GRAVIDEZ", "PARTO", "CONSULTAS", "DTNASC", "APGAR1", "APGAR5", "RACACOR", "PESO", "IDANOMAL", "DTCADASTRO", "CODANOMAL", "NUMEROLOTE", "VERSAOSIST", "DTRECEBIM", "DIFDATA", "DTRECORIGA", "NATURALMAE", "CODMUNNATU", "CODUFNATU",
                        "ESCMAE2010", "SERIESCMAE", "DTNASCMAE", "RACACORMAE", "QTDGESTANT", "QTDPARTNOR", "QTDPARTCES", "IDADEPAI", "DTULTMENST", "SEMAGESTAC", "TPMETESTIM", "CONSPRENAT", "MESPRENAT", "TPAPRESENT", "STTRABPART", "STCESPARTO", "TPNASCASSI", "TPFUNCRESP", "TPDOCRESP", "DTDECLARAC", "ESCMAEAGR1", "STDNEPIDEM", "STDNNOVA", "CODPAISRES", "TPROBSON", "PARIDADE", "KOTELCHUCK", "CONTADOR"]
df = df.drop(columns=colunas_para_deletar)
# saída
df = df.to_csv('sinasc/csv/dnrs_sem_colunas.csv', index=False)
df = pd.read_csv('sinasc/csv/dnrs_sem_colunas.csv')


df['CODESTAB'] = df['CODESTAB'].astype(float).astype(str)
df['HORANASC'] = df['HORANASC'].astype(float).astype(str)

# df = df.to_csv('sinasc/csv/dnrs_final.csv', index=False)

# banco ##

# conexão com o banco
con = banco.getConexao()
# cursor
cursor = con.cursor(prepared=True)
# comando sql para inserir dados na tabela
sql = 'INSERT INTO dnrs2022 (codestab, horanasc, sexo) VALUES (?,?,?)'
# inserir valores
for index, row in df.iterrows():
    values = (row['CODESTAB'], row['HORANASC'], row['SEXO'])
    cursor.execute(sql, values)
# commitar
con.commit()
# confirmação
print(cursor.rowcount)
# fechar conexão
con.close()
