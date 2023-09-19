import pandas as pd
import os

ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_data(filepath):
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath, encoding='ISO-8859-1')
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)  # Removido o argumento encoding
    return df

def process_data(df):
    print(df.head())
    print(df.columns)

    colunas = [
        "Grupo", "Vlr Venda", "Vlr Dev.", "Venda Líquida", "Custo Líquido",
        "Impostos", "Rentabilidade", "% Desc.", "Qt Vda", "Ticket Médio", "Coluna Adicional"
    ]

    df.columns = colunas

    # Vamos adicionar a primeira linha de volta ao DataFrame, já que ela foi interpretada como cabeçalho
    df = pd.concat([pd.DataFrame([df.columns.tolist()], columns=colunas), df], ignore_index=True)

    print(df.head())
    return df

# Se você quiser testar o código diretamente, pode adicionar o seguinte:
if __name__ == "__main__":
    filepath = "seu_caminho_para_o_arquivo.csv_ou_.xlsx"
    data = load_data(filepath)
    process_data(data)
