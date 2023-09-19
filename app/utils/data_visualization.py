import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def limpar_converter_coluna(coluna):
    if coluna.dtype == 'object':
        return coluna.str.replace('.', '').str.replace(',', '.').astype(float)
    return coluna

def visualizar_top_10_venda_liquida(df):
    df['Venda Líquida'] = limpar_converter_coluna(df['Venda Líquida'])
    top_10_marcas = df.sort_values(by='Venda Líquida', ascending=False).head(10)
    plt.figure(figsize=(12,8))
    top_10_marcas.plot(x='Grupo', y='Venda Líquida', kind='bar', legend=False, color='blue')
    plt.title('Top 10 Venda Líquida por Marca')
    plt.ylabel('Venda Líquida')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualizar_top_10_custo_liquido(df):
    df['Custo Líquido'] = limpar_converter_coluna(df['Custo Líquido'])
    top_10_custo = df.sort_values(by='Custo Líquido', ascending=False).head(10)
    plt.figure(figsize=(12,8))
    top_10_custo.plot(x='Grupo', y='Custo Líquido', kind='bar', legend=False, color='green')
    plt.title('Top 10 Custo Líquido por Marca')
    plt.ylabel('Custo Líquido')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualizar_top_10_impostos(df):
    df['Impostos'] = limpar_converter_coluna(df['Impostos'])
    top_10_impostos = df.sort_values(by='Impostos', ascending=False).head(10)
    plt.figure(figsize=(12,8))
    top_10_impostos.plot(x='Grupo', y='Impostos', kind='bar', legend=False, color='red')
    plt.title('Top 10 Impostos por Marca')
    plt.ylabel('Impostos')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualizar_top_10_rentabilidade(df):
    df['Rentabilidade'] = limpar_converter_coluna(df['Rentabilidade'])
    top_10_rentabilidade = df.sort_values(by='Rentabilidade', ascending=False).head(10)
    plt.figure(figsize=(12,8))
    top_10_rentabilidade.plot(x='Grupo', y='Rentabilidade', kind='bar', legend=False, color='purple')
    plt.title('Top 10 Rentabilidade por Marca')
    plt.ylabel('Rentabilidade')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualizar_top_10_desconto(df):
    df['% Desc.'] = limpar_converter_coluna(df['% Desc.'])
    top_10_desconto = df.sort_values(by='% Desc.', ascending=False).head(10)
    plt.figure(figsize=(12,8))
    top_10_desconto.plot(x='Grupo', y='% Desc.', kind='bar', legend=False, color='orange')
    plt.title('Top 10 Percentual de Desconto por Marca')
    plt.ylabel('% Desc.')
    plt.xlabel('Marca')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analise_por_marca(df, marca):
    marca_df = df[df['Grupo'] == marca]
    venda_liquida = marca_df['Venda Líquida'].sum()
    custo_liquido = marca_df['Custo Líquido'].sum()
    impostos = marca_df['Impostos'].sum()
    rentabilidade = marca_df['Rentabilidade'].sum()
    ticket_medio = venda_liquida / marca_df['Qt Vda'].sum() if marca_df['Qt Vda'].sum() != 0 else 0

    print(f"\nAnálise para a marca: {marca}")
    print(f"Venda Líquida: {venda_liquida:.2f}")
    print(f"Custo Líquido: {custo_liquido:.2f}")
    print(f"Impostos: {impostos:.2f}")
    print(f"Rentabilidade: {rentabilidade:.2f}")
    print(f"Ticket Médio: {ticket_medio:.2f}")

def analise_top_10_marcas(df):
    top_10_marcas = df.groupby('Grupo')['Venda Líquida'].sum().nlargest(10).index
    for marca in top_10_marcas:
        analise_por_marca(df, marca)

if __name__ == "__main__":
    # Carregue seu DataFrame aqui, por exemplo:
    # df = pd.read_csv('seu_arquivo.csv')

    # Chame as funções de visualização e análise aqui, por exemplo:
    # visualizar_top_10_venda_liquida(df)
    # visualizar_top_10_custo_liquido(df)
    # ...
    # analise_top_10_marcas(df)
    pass
