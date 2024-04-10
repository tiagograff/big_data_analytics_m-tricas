import pandas as pd
import banco as banco
# arquivo csv
arquivo = "faculdade/big_data_analytics_metricas/atividade-01/sinasc/csv/DNRS2022.csv"
# ler arquivo csv
df = pd.read_csv(arquivo)

# excluindo colunas
colunas_para_deletar = ["ORIGEM", "CODMUNNASC", "LOCNASC", "IDADEMAE", "ESTCIVMAE", "ESCMAE", "CODOCUPMAE", "QTDFILVIVO", "QTDFILMORT", "CODMUNRES", "GESTACAO", "GRAVIDEZ", "PARTO", "CONSULTAS", "APGAR1", "APGAR5", "RACACOR", "PESO", "IDANOMAL", "DTCADASTRO", "CODANOMAL", "NUMEROLOTE", "VERSAOSIST", "DTRECEBIM", "DIFDATA", "DTRECORIGA", "NATURALMAE", "CODMUNNATU", "CODUFNATU",
                        "ESCMAE2010", "SERIESCMAE", "DTNASCMAE", "RACACORMAE", "QTDGESTANT", "QTDPARTNOR", "QTDPARTCES", "IDADEPAI", "DTULTMENST", "SEMAGESTAC", "TPMETESTIM", "CONSPRENAT", "MESPRENAT", "TPAPRESENT", "STTRABPART", "STCESPARTO", "TPNASCASSI", "TPFUNCRESP", "TPDOCRESP", "DTDECLARAC", "ESCMAEAGR1", "STDNEPIDEM", "STDNNOVA", "CODPAISRES", "TPROBSON", "PARIDADE", "KOTELCHUCK", "CONTADOR"]
df = df.drop(columns=colunas_para_deletar)

# transformando float em string
df['DTNASC'] = df['DTNASC'].astype(float).astype(str)
df['CODESTAB'] = pd.to_numeric(df['CODESTAB'])
df['HORANASC'] = df['HORANASC'].astype(float).astype(str)

# mapeando valores de sexo
# armazenando valores em um dicionário
sexo_map = {0: 'IGNORADO', 1: 'MASCULINO', 2: 'FEMININO'}
# sobrescreve cada valor através do map, que aplica o dicionário para cada linha da coluna sexo
df['SEXO'] = df['SEXO'].map(sexo_map)

# pegando arquivos auxiliares de tabulação
arquivo_nome_estab = "faculdade/big_data_analytics_metricas/atividade-01/sinasc/csv/CNESDN22.csv"
# lendo arquivo
df_nome = pd.read_csv(arquivo_nome_estab, encoding='latin1')
# transformando para númerico
df_nome['CODESTAB'] = pd.to_numeric(df_nome['CODESTAB'])
# integrando colunas CODESTAB em uma única com o nome resultante
df = df.merge(df_nome, on='CODESTAB', how='left')
df['DESCESTAB'] = df['DESCESTAB'].astype(str)
# banco ##

# conexão com o banco
con = banco.getConexao()
# cursor
cursor = con.cursor(prepared=True)
# comando sql para inserir dados na tabela
sql = 'INSERT INTO dnrs2022 (codestab, descestab, dtnasc, horanasc, sexo) VALUES (?,?,?,?,?)'
# inserir valores
for index, row in df.iterrows():
    values = (row['CODESTAB'], row['DESCESTAB'],
              row['DTNASC'], row['HORANASC'], row['SEXO'])
    cursor.execute(sql, values)
# commitar
con.commit()
# confirmação
print(cursor.rowcount)
# fechar conexão
con.close()
