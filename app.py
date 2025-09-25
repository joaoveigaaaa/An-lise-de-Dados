import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
regioes = ['Norte', 'Sul', 'Leste']
canais = ['Online', 'Loja Física']

np.random.seed(42)  # Para consistência

data = []
for dia in pd.date_range(start='2025-09-01', periods=7):
    for produto in produtos:
        for regiao in regioes:
            canal = np.random.choice(canais)
            quantidade = np.random.randint(5, 50)
            valor_total = quantidade * np.random.randint(50, 200)
            data.append([dia, produto, regiao, canal, quantidade, valor_total])

df = pd.DataFrame(data, columns=['Data', 'Produto', 'Região', 'Canal', 'Quantidade', 'Valor Total'])

# Resumos
vendas_produto = df.groupby('Produto')['Valor Total'].sum().reset_index()
vendas_regiao = df.groupby('Região')['Valor Total'].sum().reset_index()
vendas_canal = df.groupby('Canal')['Valor Total'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.bar(vendas_produto['Produto'], vendas_produto['Valor Total'], color='skyblue')
plt.title('Vendas Totais por Produto')
plt.ylabel('Valor Total (R$)')
plt.show()

plt.figure(figsize=(10,5))
plt.bar(vendas_regiao['Região'], vendas_regiao['Valor Total'], color='orange')
plt.title('Vendas Totais por Região')
plt.ylabel('Valor Total (R$)')
plt.show()

plt.figure(figsize=(10,5))
plt.bar(vendas_canal['Canal'], vendas_canal['Valor Total'], color='green')
plt.title('Vendas Totais por Canal')
plt.ylabel('Valor Total (R$)')
plt.show()

# Produto com menor e maior venda
produto_top = vendas_produto.loc[vendas_produto['Valor Total'].idxmax()]
produto_baixo = vendas_produto.loc[vendas_produto['Valor Total'].idxmin()]

# Região com menor e maior venda
regiao_top = vendas_regiao.loc[vendas_regiao['Valor Total'].idxmax()]
regiao_baixo = vendas_regiao.loc[vendas_regiao['Valor Total'].idxmin()]

# Canal com menor e maior venda
canal_top = vendas_canal.loc[vendas_canal['Valor Total'].idxmax()]
canal_baixo = vendas_canal.loc[vendas_canal['Valor Total'].idxmin()]

print("=== Insights Automáticos ===")
print(f"Produto com maior venda: {produto_top['Produto']} → R$ {produto_top['Valor Total']}")
print(f"Produto com menor venda: {produto_baixo['Produto']} → R$ {produto_baixo['Valor Total']}")
print(f"Região com maior venda: {regiao_top['Região']} → R$ {regiao_top['Valor Total']}")
print(f"Região com menor venda: {regiao_baixo['Região']} → R$ {regiao_baixo['Valor Total']}")
print(f"Canal com maior venda: {canal_top['Canal']} → R$ {canal_top['Valor Total']}")
print(f"Canal com menor venda: {canal_baixo['Canal']} → R$ {canal_baixo['Valor Total']}")
