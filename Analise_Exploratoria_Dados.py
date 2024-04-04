# Libs necessarias
import pandas as pd

# Lib graficas
import matplotlib.pyplot as plt
import seaborn as sns

#Leitura do excel
df = pd.read_csv("brazil_fire.csv", encoding="cp860")

df.columns = ['ano', 'estado', 'mes', 'numero', 'data']

df.head()

# Dicionário mapeando os meses para as estações do ano no Brasil
estacoes = {
    'Janeiro': 'Verão',
    'Fevereiro': 'Verão',
    'Março': 'Verão',
    'Abril': 'Outono',
    'Maio': 'Outono',
    'Junho': 'Outono',
    'Julho': 'Inverno',
    'Agosto': 'Inverno',
    'Setembro': 'Primavera',
    'Outubro': 'Primavera',
    'Novembro': 'Primavera',
    'Dezembro': 'Verão'
}

# Adicionando a coluna 'estacao' ao DataFrame com base nos meses
df['estacao'] = df['mes'].map(estacoes)

df.head()


#Quantidade de linhas e colunas
print("Número de Linhas:",df.shape[0])
print("Número de Colunas:",df.shape[1])
#Obtendo informações sobre nosso conjunto de dados, como tipos de dados de cada coluna e requisitos de memória
df.info()


#Removendo Duplicatas   
df.drop_duplicates(inplace=True)

print("Número de linhas pós remoção das duplicatas:",df.shape[0])
print("Número de colunas pós remoção das duplicatas:",df.shape[1])


#------------------------------------------------#
# Graficos --- Graficos - Graficos --- Graficos  #
#------------------------------------------------#

# Grafico 1

# Agrupando o DataFrame por mês e somando o número total de incêndios relatados em cada mês
# em seguida, ordenando os resultados em ordem descendente para identificar o mês com o maior número de incêndios
reg_incedios_mes = df.groupby('mes')['numero'].sum().sort_values(ascending=False)
reg_incedios_mes

# Plotando um gráfico de barras para visualizar o número de incêndios registrados em cada mês
reg_incedios_mes.plot(kind='bar')

# Adicionando rótulos aos eixos x e y
plt.ylabel('Incêndios Registrados')
plt.xlabel('Mês')
plt.title('Número de Incêndios Florestais Reportados por Mês')

# Adicionando uma grade ao gráfico
plt.grid(True)

# Exibindo o gráfico
plt.show()

#------------------------------------------------#

# Grafico 2

# Agrupando o DataFrame por ano e somando o número total de incêndios relatados em cada ano
# em seguida, ordenando os resultados em ordem descendente para identificar o mês com o maior número de incêndios
reg_incendios_ano=df.groupby('ano')['numero'].sum().sort_values(ascending=False)
reg_incendios_ano

# Plotando um gráfico de barras para visualizar o número de incêndios registrados em cada ano
reg_incendios_ano.plot(kind='bar')

# Adicionando rótulos aos eixos x e y
plt.ylabel('Incêndios Registrados')
plt.xlabel('Ano')
plt.title('Número de Incêndios Florestais Reportados por Ano')

# Adicionando uma grade ao gráfico
plt.grid(True)

# Exibindo o gráfico
plt.show()


#------------------------------------------------#

# Grafico 3

# Agrupando o DataFrame por ano e mês, e somando o número total de incêndios relatados em cada par (ano, mês)
# Em seguida, os resultados são ordenados em ordem descendente com base na soma do número de incêndios
reg_incendios_ano_mes = df.groupby(['ano', 'mes',])['numero'].sum().sort_values(ascending=False)

# reg_incendios_ano_mes contém os anos, meses e o número total de incêndios registrados em cada mês, ordenados do maior para o menor número de incêndios
reg_incendios_ano_mes

# Obtendo o índice correspondente ao maior número de incêndios
indice_maior_numero = reg_incendios_ano_mes.idxmax()

# Obtendo o ano e o mês correspondentes ao maior número de incêndios
ano_maior_numero, mes_maior_numero, = indice_maior_numero

# Imprimindo o ano, mês e o maior número de incêndios registrados em um determinado ano e mês
print("Ano do maior número de incêndios:", ano_maior_numero)
print("Mês do maior número de incêndios:", mes_maior_numero)
print("Maior número de incêndios:", reg_incendios_ano_mes.max())

# Plotando um gráfico de barras para visualizar o número total de incêndios registrados em cada ano e mês
# O método unstack() é utilizado para reorganizar os dados em um formato que facilite a plotagem do gráfico de barras
reg_incendios_ano_mes.unstack().plot(kind='bar')

# Adicionando rótulos aos eixos x e y
plt.ylabel('Incêndios Registrados')
plt.xlabel('Ano')
plt.title('Maiores Números de Casos de Incêndios Florestais Separado por Ano/Mês')

# Adicionando uma grade ao gráfico
plt.grid(True)

# Exibindo o gráfico
plt.show()
