'''Módulo responsável pela validação e processamento dos arquivos pós seleção via interface gráfica.
Regra de negócio é imposta aqui.'''

import pdfplumber
import pandas as pd
import re


def extrair_texto_pdf(caminho_pdf):
    texto = ""

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            t = pagina.extract_text()
            if t:
                texto += t + "\n"


    texto = texto.replace("\n", " ")

    return texto



def extrair_ids(texto):
    padrao = r'\b\d{10}\b'
    return set(re.findall(padrao,texto))


def ler_planilha(caminho_excel):
    df = pd.read_excel(caminho_excel)

    ids = (
        df["codigo_da_operacao"]
        .astype(str)
        .str.replace(r'\D', '',regex=True)
    )

    if "codigo_da_operacao" not in df.columns:
        raise ValueError("Coluna 'codigo_da_operacao' não encontrada na planilha.")

    return set(ids)


