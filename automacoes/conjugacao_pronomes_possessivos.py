from utils.salvar_txt import salvar_em_txt

def analisar_nome(nome):
    # Define se a nome é nasal, oral ou termina em k/t mudo
    if nome.endswith(('k', 't')):
        return "k_t"

    for c in nome:
        if c in 'nmãõẽũỹĩ':
            return "nasal"
    return "oral"

def aplicar_regras_nasalizacao(palavra, prefixo, adicionando_sufixo=False):
    # Aplica regras de nasalização apenas quando sufixos são adicionados
    if not prefixo or not palavra:
        return prefixo + palavra

    # Caso 1: Prefixo termina com consoante nasal (n, m, ng)
    if prefixo.endswith(('n', 'm', 'ng')):
        if palavra[0].lower() in 'aeiou':
            # Aqui entrariam regras específicas de assimilação nasal
            return prefixo + palavra

    # Caso 2: Palavra termina com consoante nasal
    if adicionando_sufixo and palavra.endswith(('n', 'm', 'ng')):
        base = palavra[:-1]  # Remove a consoante nasal final
        ultima_vogal = base[-1].lower() if base else ''

        # Aplica nasalização na vogal anterior à consoante nasal
        if ultima_vogal == 'a': base = base[:-1] + 'ã'
        elif ultima_vogal == 'o': base = base[:-1] + 'õ'
        elif ultima_vogal == 'e': base = base[:-1] + 'ẽ'
        elif ultima_vogal == 'u': base = base[:-1] + 'ũ'
        elif ultima_vogal == 'i': base = base[:-1] + 'ĩ'

        return prefixo + base

    # Caso 3: Prefixo termina com vogal e palavra começa com consoante nasal
    if prefixo[-1].lower() in 'aeiou' and palavra[0].lower() in 'nm':
        return prefixo + palavra

    return prefixo + palavra

def aplicar_regra_kt(palavra, sufixo=""):
    # Aplica a regra k_t apenas quando há sufixo
    # Sem sufixo: mantém k/t
    # Sufixo com vogal: k→g / t→r
    # Sufixo com consoante: k/t caem

    if not sufixo or not palavra.endswith(('k', 't')):
        return palavra + sufixo

    base = palavra[:-1]  # Remove o k/t final

    if sufixo[0].lower() in 'aeiouãõẽũỹĩ':
        # Sufixo começa com vogal: k→g / t→r
        if palavra.endswith('k'):
            return base + 'g' + sufixo
        elif palavra.endswith('t'):
            return base + 'r' + sufixo
    else:
        # Sufixo começa com consoante: k/t caem
        return base + sufixo

    return palavra + sufixo

def selecionar_prefixo_correto(tipo_nome, pessoa_chave):
    todos_prefixos = {
        "1ªp.s. (classe_1)": "e",
        "1ªp.s. (classe_2)": "ere",
        "2ªp.s. (oral_classe_1)": "de",
        "2ªp.s. (nasal_classe_1)": "ne",
        "2ªp.s. (oral_classe_2)": "dere",
        "2ªp.s. (nasal_classe_2)": "nere",
        "3ªp.s.": "o",
        "1ªp.p. (excl.)": "oro",
        "1ªp.p. (incl.)": "none",
        "2ªp.p.": "pe",
        "3ªp.p.": "o"
    }

    mapeamento_pessoas = {
        "1ªp.s.": ["1ªp.s. (classe_1)", "1ªp.s. (classe_2)"],
        "2ªp.s.": {
            "oral": ["2ªp.s. (oral_classe_1)", "2ªp.s. (oral_classe_2)"],
            "nasal": ["2ªp.s. (nasal_classe_1)", "2ªp.s. (nasal_classe_2)"],
            "k_t": ["2ªp.s. (oral_classe_1)", "2ªp.s. (oral_classe_2)"]
        },
        "3ªp.s.": ["3ªp.s."],
        "1ªp.p. (excl.)": ["1ªp.p. (excl.)"],
        "1ªp.p. (incl.)": ["1ªp.p. (incl.)"],
        "2ªp.p.": ["2ªp.p."],
        "3ªp.p.": ["3ªp.p."]
    }

    if pessoa_chave == "2ªp.s.":
        opcoes = mapeamento_pessoas["2ªp.s."].get(tipo_nome, ["2ªp.s. (oral_classe_1)"])
        return {opcao: todos_prefixos[opcao] for opcao in opcoes}
    elif pessoa_chave in mapeamento_pessoas:
        opcoes = mapeamento_pessoas[pessoa_chave]
        return {opcao: todos_prefixos[opcao] for opcao in opcoes}

    return {}

def nasalizar_raiz(raiz):
    # Aplica nasalização na raiz se ela terminar com n, m, ng.
    # Remove a consoante nasal e nasaliza a vogal anterior.
    if raiz.endswith(('n', 'm', 'ng')):
        base = raiz[:-1] if not raiz.endswith('ng') else raiz[:-2]
        ultima_vogal = base[-1].lower() if base else ''

        if ultima_vogal == 'a':
            base = base[:-1] + 'ã'
        elif ultima_vogal == 'o':
            base = base[:-1] + 'õ'
        elif ultima_vogal == 'e':
            base = base[:-1] + 'ẽ'
        elif ultima_vogal == 'u':
            base = base[:-1] + 'ũ'
        elif ultima_vogal == 'i':
            base = base[:-1] + 'ĩ'
        return base
    return raiz

def gerar_coletivo(forma_possessiva):
    # Gera a forma coletiva aplicando regras k_t e nasalização
    # Encontra a raiz original (removendo os prefixos conhecidos)
    prefixos = ["e", "ere", "de", "ne", "dere", "nere", "o", "oro", "none", "pe"]
    raiz = forma_possessiva
    for prefixo in sorted(prefixos, key=len, reverse=True):
        if forma_possessiva.startswith(prefixo):
            raiz = forma_possessiva[len(prefixo):]
            break

    # Aplica nasalização na raiz se terminar com n, m, ng
    if raiz.endswith(('n', 'm', 'ng')):
        raiz_nasalizada = nasalizar_raiz(raiz)
        # Reconstroi a forma possessiva com a raiz nasalizada
        forma_nasalizada = forma_possessiva[:-len(raiz)] + raiz_nasalizada
        return forma_nasalizada + "kan"
    else:
        # Caso contrário, aplica a regra k_t normalmente
        return aplicar_regra_kt(forma_possessiva, "kan")

def gerar_possessivos(palavra, tipo_nome):
    resultado = {}

    pessoas = [
        "1ªp.s.", "2ªp.s.", "3ªp.s.",
        "1ªp.p. (excl.)", "1ªp.p. (incl.)",
        "2ªp.p.", "3ªp.p."
    ]

    for pessoa in pessoas:
        prefixos = selecionar_prefixo_correto(tipo_nome, pessoa)

        for nome_prefixo, prefixo in prefixos.items():
            # Para formas possessivas (sem sufixo), naõ aplica nasalização
            # Apenas junta prefixo + palavra mantendo as consoantes nasais
            forma_final = prefixo + palavra

            resultado[nome_prefixo] = forma_final

    return resultado

def formatar_saida_possessivos(palavra, possessivos):
    saida = f"\nPronomes Possessivos para: {palavra}\n"

    grupos = {
        "1ª Pessoa Singular": [],
        "2ª Pessoa Singular": [],
        "3ª Pessoa Singular": [],
        "1ª Pessoa Plural": [],
        "2ª Pessoa Plural": [],
        "3ª Pessoa Plural": []
    }

    for prefixo_nome, forma in possessivos.items():
        if "1ªp.s." in prefixo_nome:
            grupos["1ª Pessoa Singular"].append((prefixo_nome, forma))
        elif "2ªp.s." in prefixo_nome:
            grupos["2ª Pessoa Singular"].append((prefixo_nome, forma))
        elif "3ªp.s." in prefixo_nome:
            grupos["3ª Pessoa Singular"].append((prefixo_nome, forma))
        elif "1ªp.p." in prefixo_nome:
            grupos["1ª Pessoa Plural"].append((prefixo_nome, forma))
        elif "2ªp.p." in prefixo_nome:
            grupos["2ª Pessoa Plural"].append((prefixo_nome, forma))
        elif "3ªp.p." in prefixo_nome:
            grupos["3ª Pessoa Plural"].append((prefixo_nome, forma))

    for grupo, itens in grupos.items():
        if itens:
            saida += f"{grupo}:\n"
            formas_coletivo = []

            for prefixo_nome, forma in itens:
                saida += f"  {prefixo_nome}: {forma}\n"
                # Gera coletivo aplicando regra k_t para sufixo começando com consoante
                formas_coletivo.append(gerar_coletivo(forma))

            if formas_coletivo:
                saida += f"  Coletivo: {', '.join(formas_coletivo)}\n"

    return saida

def main():
    palavra = str(input("Digite a palavra: ")).strip()

    if not palavra:
        print("Palavra inválida!")
        return

    if palavra and palavra[0] == '-':
        palavra = palavra[1:]

    tipo_nome = analisar_nome(palavra)
    print(f"Tipo do nome: {tipo_nome}")

    possessivos = gerar_possessivos(palavra, tipo_nome)
    
    # Saída formatada
    texto_saida = formatar_saida_possessivos(palavra, possessivos)
    print(texto_saida)

    # Salvando saída em arquivo txt
    salvar_em_txt(texto_saida, "conjugacoes_pronomes_possessivos_zoe.txt")

if __name__ == "__main__": 
    main()