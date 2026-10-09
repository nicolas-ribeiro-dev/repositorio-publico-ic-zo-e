import re

def dividir_em_periodos(texto):
    periodos = []
    atual = ""

    aspas = {'"', '“', '”', '«', '»', '『', '』', '「', '」', '(', ')'}
    contador_aspas = 0

    for c in texto:
        atual += c

        if c in aspas:
            contador_aspas += 1

        # encerra período se:
        # - encontrou pontuação
        # - E o número de aspas no trecho é par (ou zero)
        if c in ".!?" and contador_aspas % 2 == 0:
            periodos.append(atual.strip())
            atual = ""
            contador_aspas = 0  # reset seguro

    if atual.strip():
        periodos.append(atual.strip())

    return periodos



def processar_capitalizacao(texto):
    return texto[0].lower() + texto[1:] if texto else texto


def extrair_citacoes(texto):
    return re.findall(r'["「』](.*?)["」』]', texto)


def identificar_speaker(periodo):
    if ':' in periodo:
        candidato = periodo.split(':')[0].strip()
        if 0 < len(candidato) < 30 and any(c.isalpha() for c in candidato):
            return candidato.capitalize()
    return None


def processar_texto_para_entradas(
    source,
    target,
    notes_base="Artesanato"
):
    periodos_source = dividir_em_periodos(source)
    periodos_target = dividir_em_periodos(target)

    if len(periodos_source) != len(periodos_target):
        print(
            f"ATENÇÃO: períodos diferentes "
            f"(source={len(periodos_source)}, target={len(periodos_target)})"
        )

    entradas = []
    speaker_atual = "Não consta"

    for ps, pt in zip(periodos_source, periodos_target):
        speaker = identificar_speaker(ps)
        if speaker:
            speaker_atual = speaker

        ps = processar_capitalizacao(ps)
        pt = processar_capitalizacao(pt)

        entradas.append({
            "source": ps,
            "target": pt,
            "unit_type": "Frase",
            "speaker": speaker_atual,
            "notes_base": notes_base
        })

    return entradas
