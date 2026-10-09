from automations.corpus_insert import (
    gerar_arquivo_de_revisao,
    carregar_entradas_revisadas,
    converter_para_dados_json,
    inserir_no_banco
)
# “” ã ẽ ĩ õ ũ ỹ ë ï
SOURCE = ( 
    "Entrada em zo'é"
)

#

TARGET = ( 
    "Saída em português"
)

#   

def main():
    print("\n[1] Gerando arquivo de revisão.")
    gerar_arquivo_de_revisao(SOURCE, TARGET)

    input("\n[2] Edite o arquivo JSON e pressione ENTER para continuar.")

    print("\n[3] Carregando entradas revisadas.")
    entradas = carregar_entradas_revisadas()

    print("\n[4] Pré-visualização final:")
    for i, e in enumerate(entradas, 1):
        print(f"{i}. {e['source']} → {e['target']} ({e['speaker']})")

    confirmar = input("\nDeseja inserir no banco? (s/n): ").lower()

    if confirmar == "s":
        dados_json = converter_para_dados_json(entradas)
        inserir_no_banco(dados_json)
    else:
        print("[X] Inserção cancelada!")
        

if __name__ == "__main__":
    main()
