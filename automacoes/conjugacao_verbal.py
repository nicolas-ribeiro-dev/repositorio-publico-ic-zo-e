from utils.salvar_txt import salvar_em_txt

def analisar_raiz(raiz):
    # Define se a raiz é nasal, oral ou termina em k/t mudo
    if raiz.endswith(('n', 'm', 'ng', 'ã', 'õ', 'ẽ', 'ũ', 'ỹ', 'ĩ')):
        return "nasal"
    elif raiz.endswith(('k', 't')):
        return "k_t"
    else:
        return "oral"

def gerar_presente_afirmativo(raiz):
    prefixos = {
        "1ªp.s.": "a",
        "2ªp.s.": "ere",
        "3ªp.s.": "o",
        "1ªp.p. (excl.)": "oro",
        "1ªp.p. (incl.)": "ja",
        "2ªp.p.": "pe",
        "3ªp.p.": "o"
    }
    return {pessoa: prefixo + raiz for pessoa, prefixo in prefixos.items()}

def gerar_presente_negativo(raiz, tipo_raiz):
    prefixos_neg = {
        "nasal": {
            "1ªp.s.": "na",
            "2ªp.s.": "nere",
            "3ªp.s.": "no",
            "1ªp.p. (excl.)": "noro",
            "1ªp.p. (incl.)": "naja",
            "2ªp.p.": "nepe",
            "3ªp.p.": "no"
        },
        "oral": {
            "1ªp.s.": "da",
            "2ªp.s.": "dere",
            "3ªp.s.": "do",
            "1ªp.p. (excl.)": "doro",
            "1ªp.p. (incl.)": "daja",
            "2ªp.p.": "depe",
            "3ªp.p.": "do"
        }
    }
    sufixo = "i" if not raiz[-1].lower() in "aeiouãõ" else "j"

    if tipo_raiz == "k_t":
        raiz_neg = raiz[:-1] + ("g" if raiz.endswith("k") else "r")
        return {pessoa: prefixo + raiz_neg + sufixo for pessoa, prefixo in prefixos_neg["oral"].items()}
    else:
        prefixos = prefixos_neg["nasal"] if tipo_raiz == "nasal" else prefixos_neg["oral"]
        return {pessoa: prefixo + raiz + sufixo for pessoa, prefixo in prefixos.items()}

def gerar_futuro(raiz, tipo_raiz, afirmativo=True):
    marcador = "potat" if afirmativo else "potari"
    conjugacoes = {}
    presente = gerar_presente_afirmativo(raiz) if afirmativo else gerar_presente_negativo(raiz, tipo_raiz)

    for pessoa, forma in presente.items():
        if not afirmativo and (forma.endswith('j') or forma.endswith('i')):
            forma = forma[:-1]

        # Removendo "k_t" quando seguido por consoante
        if tipo_raiz == "k_t":
            forma = forma[:-1]

        if forma.endswith(('n', 'm', 'ng')) and marcador[0].lower() not in 'aeiou':
            if forma.endswith('n'):
                base = forma[:-1]
                ultima_vogal = base[-1].lower()
                if ultima_vogal == 'a': base = base[:-1] + 'ã'
                elif ultima_vogal == 'o': base = base[:-1] + 'õ'
                elif ultima_vogal == 'e': base = base[:-1] + 'ẽ'
                elif ultima_vogal == 'u': base = base[:-1] + 'ũ'
                elif ultima_vogal == 'i': base = base[:-1] + 'ĩ'
                forma = base
            elif forma.endswith('m'):
                base = forma[:-1]
                ultima_vogal = base[-1].lower()
                if ultima_vogal == 'a': base = base[:-1] + 'ã'
                elif ultima_vogal == 'o': base = base[:-1] + 'õ'
                elif ultima_vogal == 'e': base = base[:-1] + 'ẽ'
                elif ultima_vogal == 'u': base = base[:-1] + 'ũ'
                elif ultima_vogal == 'i': base = base[:-1] + 'ĩ'
                forma = base
            elif forma.endswith('ng'):
                base = forma[:-2]
                ultima_vogal = base[-1].lower()
                if ultima_vogal == 'a': base = base[:-1] + 'ã'
                elif ultima_vogal == 'o': base = base[:-1] + 'õ'
                elif ultima_vogal == 'e': base = base[:-1] + 'ẽ'
                elif ultima_vogal == 'u': base = base[:-1] + 'ũ'
                elif ultima_vogal == 'i': base = base[:-1] + 'ĩ'
                forma = base

        conjugacoes[pessoa] = forma + marcador

    return conjugacoes

def gerar_preposicao_para(raiz, tipo_raiz, afirmativo=True):
    if afirmativo:
        prefixos = {
            "1ªp.s.": "ta",
            "2ªp.s.": "tere",
            "3ªp.s.": "to",
            "1ªp.p. (excl.)": "toro",
            "1ªp.p. (incl.)": "taja",
            "2ªp.p.": "tepe",
            "3ªp.p.": "to"
        }
        return {pessoa: prefixo + raiz for pessoa, prefixo in prefixos.items()}
    else:
        prefixos_neg_para = {
            "oral": {
                "1ªp.s.": "tada",
                "2ªp.s.": "terede",
                "3ªp.s.": "todo",
                "1ªp.p. (excl.)": "torodo",
                "1ªp.p. (incl.)": "tajada",
                "2ªp.p.": "tepede",
                "3ªp.p.": "todo"
            },
            "nasal": {
                "1ªp.s.": "tana",
                "2ªp.s.": "terene",
                "3ªp.s.": "tono",
                "1ªp.p. (excl.)": "torono",
                "1ªp.p. (incl.)": "tanaja",
                "2ªp.p.": "tepene",
                "3ªp.p.": "tono"
            }
        }

        sufixo = "j" if raiz[-1].lower() in "aeiouãõ" else "i"

        # Considerando o caso k_t separadamente
        if tipo_raiz == "k_t":
            # Modifica a raiz: k -> g, t -> r
            raiz_modificada = raiz[:-1] + ("g" if raiz.endswith("k") else "r")
            # Utilizando os prefixos orais
            prefixos = prefixos_neg_para["oral"]
            return {pessoa: prefixo + raiz_modificada + sufixo for pessoa, prefixo in prefixos.items()}
        else:
            prefixos = prefixos_neg_para["nasal"] if tipo_raiz == "nasal" else prefixos_neg_para["oral"]
            return {pessoa: prefixo + raiz + sufixo for pessoa, prefixo in prefixos.items()}

def gerar_imperativo(raiz, afirmativo=True):
    base = "e" + raiz if afirmativo else "name e" + raiz
    return {
        "2ªp.s.": base,
        "2ªp.p.": "epe" + raiz if afirmativo else "name epe" + raiz
    }

def formatar_saida(verbo, raiz, conjugacoes):
    saida = f"\n{verbo} = -{raiz}\n"
    modos = {
        "Afirmação no presente ou no passado": conjugacoes["presente_afirmativo"],
        "Negação no presente ou no passado": conjugacoes["presente_negativo"],
        "Afirmação no futuro": conjugacoes["futuro_afirmativo"],
        "Negação no futuro": conjugacoes["futuro_negativo"],
        'Afirmação com a preposição "para"': conjugacoes["preposicao_afirmativo"],
        'Negação com a preposição "para"': conjugacoes["preposicao_negativo"],
        "Afirmação no imperativo": conjugacoes["imperativo_afirmativo"],
        "Negação no imperativo": conjugacoes["imperativo_negativo"]
    }
    for modo, formas in modos.items():
        saida += f"\n{modo}\n"
        for pessoa, forma in formas.items():
            saida += f"{pessoa}: {forma}\n"
    return saida

def main(): 
    # Entrada do usuário
    raiz = str(input("Digite a raiz verbal: ")).strip()
    verbo = str(input("Digite o significado do verbo: ")).strip()

    if not raiz:
        print("Raiz inválida!")
        return

    if raiz[0] == '-':
        raiz = raiz[1:]

    tipo_raiz = analisar_raiz(raiz)

    # Gera todas as conjugações
    conjugacoes = {
        "presente_afirmativo": gerar_presente_afirmativo(raiz),
        "presente_negativo": gerar_presente_negativo(raiz, tipo_raiz),
        "futuro_afirmativo": gerar_futuro(raiz, tipo_raiz, afirmativo=True),
        "futuro_negativo": gerar_futuro(raiz, tipo_raiz, afirmativo=False),
        "preposicao_afirmativo": gerar_preposicao_para(raiz, tipo_raiz, afirmativo=True),
        "preposicao_negativo": gerar_preposicao_para(raiz, tipo_raiz, afirmativo=False),
        "imperativo_afirmativo": gerar_imperativo(raiz, afirmativo=True),
        "imperativo_negativo": gerar_imperativo(raiz, afirmativo=False)
    }

    # Saída formatada
    texto_saida = formatar_saida(verbo, raiz, conjugacoes)
    print(texto_saida)

    # Salvando saída em arquivo txt
    salvar_em_txt(texto_saida, "conjugacoes_verbais_zoe.txt")

if __name__ == "__main__":
    main()