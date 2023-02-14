#14/02/2023
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gasolina_df = pd.read_csv("gasolina.csv") # lendo o arquivo csv em um dataframe.
gasolina_df.head(2)

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço Gasolina por dia', xlabel='Ano', ylabel='Preço Gasolina');
  import matplotlib.pyplot as plt