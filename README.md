# Fundamentos de Python

**Python 3 · Lógica de programação · Aprendizado aplicado a QA**

Trilha de 33 aulas independentes, organizada em seis temas. O projeto reúne exemplos executáveis, tratamento de entradas e verificações automatizadas para apoiar a evolução em programação.

[Índice das aulas](curso_python/README.md) · [Como executar](#como-executar) · [Testes e evidências](#testes-e-evidências) · [Contribuir](CONTRIBUTING.md)

## Trilha de estudo

| Etapa | Conteúdo | Aulas |
|---|---|---|
| [01 · Básico](curso_python/01_basico) | Sintaxe, tipos, conversões e variáveis | 01–08 |
| [02 · Operadores](curso_python/02_operadores) | Aritmética, concatenação e precedência | 09–11 |
| [03 · Entrada e formatação](curso_python/03_entrada_e_formatacao) | Entrada de dados, formatação e IMC | 12–14 |
| [04 · Condicionais e lógica](curso_python/04_condicionais_e_logica) | Comparação, operadores lógicos e decisões | 15–24 |
| [05 · Strings e conceitos](curso_python/05_strings_e_conceitos) | Fatiamento, exceções, identidade e flags | 25–30 |
| [06 · Repetições](curso_python/06_repeticoes) | while, atribuição e continue | 31–33 |

## Como executar

Instale Python 3 e Git. Não há dependências externas.

```bash
git clone https://github.com/Demetrios10/Fundamentos-Python.git
cd Fundamentos-Python
python curso_python/01_basico/aula01.py
```

No Windows, `py` pode substituir `python`; em alguns ambientes Linux/macOS, use `python3`. Troque o caminho pela aula desejada e execute uma de cada vez. Algumas aulas solicitam dados no terminal.

As aulas seguem a numeração do [índice completo](curso_python/README.md). Cada arquivo tem seu próprio `main()`; importar a aula não deve imprimir nem solicitar dados. Os dados e senhas presentes nos exercícios são fictícios e didáticos.

## Testes e evidências

Na raiz do repositório:

```bash
python -m unittest discover -s tests -v
```

O [relatório de 07/11/2026](evidencias/RELATORIO.md) registra **nove testes aprovados**, incluindo execução das 33 aulas com entradas de exemplo e importação sem efeitos colaterais. Outras verificações cobrem entradas inválidas e resultados conhecidos. Isso não representa cobertura de todas as combinações de entrada.

| Recurso | Finalidade |
|---|---|
| [tests/test_aulas.py](tests/test_aulas.py) | Verificações automatizadas |
| [evidencias/RELATORIO.md](evidencias/RELATORIO.md) | Mudanças e condições da execução registrada |
| [evidencias/execucao.txt](evidencias/execucao.txt) | Saída registrada da suíte |

## O que foi trabalhado

- Precedência, conversão de tipos e resultados de operações.
- Validação de valores positivos e finitos no exemplo de IMC, com vírgula decimal.
- Normalização de respostas e tratamento de entradas inválidas.
- Exceções específicas, identidade de objetos e operações com strings.
- Organização da execução e separação entre importação e interação no terminal.

## Próximos passos

Expandir os estudos com funções reutilizáveis, coleções, arquivos e aplicações de programação ao contexto de QA. Esses temas são objetivos de evolução, não módulos adicionais já entregues nesta trilha.

## Outros projetos e contato

[Automação web com Selenium](https://github.com/Demetrios10/Automacao-Selenium-Python) · [Perfil do autor](https://github.com/Demetrios10) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)

**Autor:** Demétrios Alves da Silva. Projeto de estudo, revisado documentalmente em 09/11/2026.
