from tkinter import Tk, messagebox
from src.reader.reader import selecionar_arquivos
from src.processor.validator import extrair_texto_pdf, extrair_ids, ler_planilha
from src.report.report_generator import gerar_relatorio, selecionar_saida



def main():
    root = Tk()
    root.withdraw()

    try:
        pdf_path = selecionar_arquivos(
            "Selecione o termo (PDF)",
            [("Arquivos PDF", "*.pdf")]
        )

        if not pdf_path:
            return
        
        excel_path = selecionar_arquivos(
            "Selecione a Planilha",
            [("Arquivos Excel", "*.xlsx")]
        )

        if not excel_path:
            return
        
        saida = selecionar_saida()

        if not saida:
            return

        texto = extrair_texto_pdf(pdf_path)

        ids_pdf = extrair_ids(texto)
        ids_planilha = ler_planilha(excel_path)

        gerar_relatorio(ids_pdf, ids_planilha, saida)

        messagebox.showinfo("Sucesso", "Auditoria concluída!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    main()