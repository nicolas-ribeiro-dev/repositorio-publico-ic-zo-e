# Produção e organização de corpus paralelo digital da língua zo’é

Este repositório reúne os códigos desenvolvidos durante o projeto de Iniciação Científica _Produção e organização de corpus paralelo digital da língua indígena zo’é_. O trabalho tem como objetivo contribuir para a organização de dados linguísticos da língua zo’é e sua utilização em aplicações de Processamento de Linguagem Natural (PLN).

Os códigos abrangem a inserção e organização de registros linguísticos, a construção de um corpus paralelo zo’é–português, experimentos com um modelo de tradução automática do tipo _sequence-to-sequence_ (_seq2seq_) e scripts auxiliares para a geração de formas verbais e possessivas.

## 1. Requisitos
Para utilizar os códigos, são necessários:
* Python instalado;
* Jupyter Notebook ou JupyterLab para executar os arquivos `.ipynb`;
* As bibliotecas Python utilizadas por cada script ou notebook;
* MongoDB configurado, caso seja utilizada a etapa de inserção de registros no banco de dados.

Alguns scripts dependem de módulos auxiliares presentes na estrutura do projeto. Por isso, mantenha a organização original dos arquivos e diretórios ao executar os códigos.

## 2. Organização dos arquivos
Os principais arquivos do repositório são:
* `automacoes/conjugacao_verbal.py`: gera formas verbais a partir de uma raiz verbal em zo’é;
* `automacoes/conjugacao_verbal.py`: gera formas possessivas associadas a um substantivo em zo’é;
* `insercao_registros_BD/src/main.py`: coordena o processo de preparação, revisão e inserção de registros no banco de dados;
* `modelo_seq2seq/corpus.ipynb`: reúne o processamento dos dados e a construção do corpus paralelo;
* `modelo_seq2seq/zoe_model.ipynb`: contém os experimentos com o modelo de tradução automática seq2seq.

## 3. Como executar os códigos
### 3.1. Geração de formas verbais
O arquivo `automacoes/conjugacao_verbal.py` recebe uma raiz verbal em zo’é e seu significado em português. A partir desses dados, aplica as regras morfológicas implementadas para gerar diferentes formas verbais.

Para executar o programa, abra o terminal na pasta do projeto e utilize:

`python conjugacao_verbal.py`

Em seguida, informe os dados solicitados pelo programa:

A raiz verbal em zo’é;
O significado do verbo em português.

O programa apresenta as formas geradas no terminal e salva os resultados no arquivo `conjugacoes_verbais_zoe.txt`.

### 3.2. Geração de formas possessivas
O arquivo `automacoes/conjugacao_pronomes_possessivos.py` recebe um substantivo em zo’é e aplica as regras morfológicas implementadas para gerar formas associadas a diferentes pessoas gramaticais.

Para executar o programa, utilize:

`python conjugacao_pronomes_possessivos.py`

Informe o substantivo solicitado pelo programa. O resultado será apresentado no terminal e salvo no arquivo `conjugacoes_pronomes_possessivos_zoe.txt`.

### 3.3. Inserção de registros no banco de dados
O arquivo main.py coordena o processo de preparação e inserção de novos registros linguísticos no MongoDB.

Para iniciar o procedimento, acesse o arquivo `insercao_registros_BD/src/main.py` insira o texto de entrada em zo'é e de saída em português e execute:

`python main.py`

O programa solicita a preparação de um arquivo para revisão. Após sua geração:<br/>
1. Edite o arquivo JSON conforme as instruções do processo de revisão.
2. Salve as alterações e retorne ao terminal.
3. Confira a pré-visualização dos registros carregados.
4. Confirme a inserção digitando s ou cancele o procedimento digitando n.

A inserção depende dos módulos auxiliares responsáveis pela revisão, conversão dos dados e comunicação com o banco de dados, além da configuração adequada do MongoDB.

### 3.4. Construção do corpus paralelo
O arquivo `modelo_seq2seq/corpus.ipynb` reúne o processamento dos registros utilizados na construção do corpus paralelo zo’é–português.

Para executar o notebook:
1. Abra o Jupyter Notebook ou JupyterLab.
2. Carregue o arquivo `corpus.ipynb`.
3. Disponibilize o arquivo CSV de entrada utilizado pelo processamento, contendo os campos __id, source e target_.
4. Execute as células do notebook na ordem apresentada.

Durante o processamento, os registros passam por etapas de normalização e filtragem. Em seguida, são distribuídos aleatoriamente em três conjuntos:
* Treinamento: 80% dos registros;
* Validação: 10% dos registros;
* Teste: 10% dos registros.

Os conjuntos são utilizados em etapas distintas dos experimentos de tradução automática. Cada registro dos arquivos de saída é organizado com o texto em zo’é e sua tradução em português, separados por tabulação.

### 3.5. Treinamento e avaliação do modelo de tradução automática
O arquivo `modelo_seq2seq/zoe_model.ipynb` contém os experimentos com o modelo _seq2seq_ para tradução entre zo’é e português.

Para executar o notebook:
1. Abra o arquivo `zoe_model.ipynb` no Jupyter Notebook ou JupyterLab.
2. Disponibilize os arquivos de treinamento, validação e teste gerados na etapa anterior.
3. Confira os parâmetros de configuração do modelo, como hidden_size, batch_size e n_epochs.
4. Execute as células na ordem apresentada.

Durante o treinamento, o programa acompanha métricas como a função de perda (_loss_) e o _BLEU Score_. Os resultados são utilizados para comparar configurações do modelo e selecionar _checkpoints_ de acordo com a menor _loss_ de validação e o maior _BLEU Score_ de validação.

Ao final, são realizadas avaliações das traduções geradas a partir do conjunto de teste, incluindo o cálculo do _BLEU Score_ e a contabilização de correspondências exatas entre as traduções produzidas e as referências.

## 4. Observações
Os scripts de geração de formas verbais e possessivas possuem caráter auxiliar e preliminar. As regras morfológicas implementadas ainda dependem de validação linguística adicional, de modo que as formas geradas devem ser revisadas antes de sua utilização como registros linguísticos definitivos.

Da mesma forma, os experimentos de tradução automática possuem caráter exploratório. Os resultados devem ser interpretados considerando o tamanho e a composição do corpus disponível, bem como as limitações associadas ao desenvolvimento de modelos para línguas de poucos recursos.

## 5. Referência
Para maiores informações sobre a metodologia, as decisões de implementação e os resultados obtidos durante o desenvolvimento do projeto, consulte o relatório final de Iniciação Científica associado a este repositório.
