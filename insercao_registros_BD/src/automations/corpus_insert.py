import json
from pathlib import Path

from services.text_to_corpus import processar_texto_para_entradas
from models.corpus_entry import criar_entrada_json
from database.mongo_client import db
from config.settings import COLLECTION_NAME


DATA_PATH = Path("data/revisao_entradas.json")


def gerar_arquivo_de_revisao(source, target):
    entradas = processar_texto_para_entradas(source, target)

    DATA_PATH.parent.mkdir(exist_ok=True)

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(entradas, f, indent=2, ensure_ascii=False)

    print(f"✔ Arquivo de revisão gerado em: {DATA_PATH}")


def carregar_entradas_revisadas():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Arquivo de revisão não encontrado.")

    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def converter_para_dados_json(entradas):
    dados_json = []

    for e in entradas:
        dados_json.append(criar_entrada_json(
            source=e["source"],
            target=e["target"],
            unit_type=e.get("unit_type", "Frase"),
            notes=e.get("notes_base", ""),
            speaker=e.get("speaker", "Não consta")
        ))

    return dados_json


def inserir_no_banco(dados_json):
    collection = db[COLLECTION_NAME]
    collection.insert_many(dados_json)
    print(f"[SUCCESS] {len(dados_json)} registros inseridos no MongoDB.")
