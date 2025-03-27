# Lista de códigos fornecidos
codigos = [
#seus codigos separadaos por virgula exemplo: 1,2,3,4,5,6
]

# Caminho do arquivo onde os inserts serão salvos
arquivo = "inserts.txt"

# Gerando os inserts
with open(arquivo, "w") as f:
    for codigo in codigos:
        insert = f"INSERT INTO sua_Tabela VALUES (colunas, {codigo});\n"
        f.write(insert)

print(f"Inserts gerados e salvos em {arquivo}")
