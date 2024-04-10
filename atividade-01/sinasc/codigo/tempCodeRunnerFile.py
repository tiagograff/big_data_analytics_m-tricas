
# # banco ##

# # conexão com o banco
# con = banco.getConexao()
# # cursor
# cursor = con.cursor(prepared=True)
# # comando sql para inserir dados na tabela
# sql = 'INSERT INTO dnrs2022 (codestab, descestab, dtnasc, horanasc, sexo) VALUES (?,?,?,?,?)'
# # inserir valores
# for index, row in df.iterrows():
#     values = (row['CODESTAB'], row['DESCESTAB'],
#               row['DTNASC'], row['HORANASC'], row['SEXO'])
#     cursor.execute(sql, values)
# # commitar
# con.commit()
# # confirmação
# print(cursor.rowcount)
# # fechar conexão
# con.close()
