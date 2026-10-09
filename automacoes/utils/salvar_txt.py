import os

def salvar_em_txt(texto, nome_arquivo):
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    pasta_pai = os.path.dirname(pasta_script)

    caminho_arquivo = os.path.join(pasta_pai, nome_arquivo)

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto)
        arquivo.write("_"*60 + "\n")

    print(f"✓ Conjugação salva em {caminho_arquivo}")