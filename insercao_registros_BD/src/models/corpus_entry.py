from utils.dates import data_hoje

def criar_entrada_json(
    source,
    target,
    unit_type="Palavra",
    notes="",
    semantic_conditioner="Ego masculino + Ego feminino",
    topic="Artesanato",
    speaker="Não consta"
):
    return {
        "source": source,
        "target": target,
        "unit_type": unit_type,
        "status": "Não revisado",
        "metadata": {
            "translator": "Leo",
            "semantic_conditioner": semantic_conditioner,
            "speaker": speaker,
            "genre": "Gestão política e territorial",
            "topic": topic,
            "origin": "Tese do Leo",
            "trust_level": "Alta",
            "collection_date": "",
            "registration_date": data_hoje(),
            "spelling_date": "2013",
            "pronunciation": "",
            "notes": notes
        }
    }