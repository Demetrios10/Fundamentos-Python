# Fundamentos de Python

**Python 3 · Lógica de programação · Estudos práticos**

33 aulas práticas organizadas em uma trilha de seis temas, da sintaxe básica aos laços de repetição.

[Explorar as aulas](curso_python/README.md) · [Como executar](#como-executar) · [Perfil do autor](https://github.com/Demetrios10)

## Conteúdo

| Pasta | Assunto | Aulas |
| --- | --- | --- |
| [01_basico](curso_python/01_basico) | Sintaxe, tipos e variáveis | 1–8 |
| [02_operadores](curso_python/02_operadores) | Operadores e precedência | 9–11 |
| [03_entrada_e_formatacao](curso_python/03_entrada_e_formatacao) | Entrada de dados e formatação | 12–14 |
| [04_condicionais_e_logica](curso_python/04_condicionais_e_logica) | Condicionais, comparação e lógica | 15–24 |
| [05_strings_e_conceitos](curso_python/05_strings_e_conceitos) | Strings, exceções e identidade | 25–30 |
| [06_repeticoes](curso_python/06_repeticoes) | Repetições e atribuição | 31–33 |

Consulte o [índice completo das aulas](curso_python/README.md).

## Como executar

Instale Python 3 e clone o repositório:

```bash
git clone https://github.com/Demetrios10/Fundamentos-Python.git
cd Fundamentos-Python
python curso_python/01_basico/aula01.py
```

Troque o caminho pelo exercício desejado. No Windows, você também pode usar `py` no lugar de `python`. Não há dependências externas. Algumas aulas pedem dados no terminal; execute uma de cada vez.

## Organização

As aulas estão agrupadas em seis temas e numeradas com dois dígitos. Os exemplos têm finalidade didática e incluem dados e senhas de demonstração.

## Melhorias e verificações

As 33 aulas podem ser importadas sem imprimir ou pedir dados; a execução acontece em `main()`. Foram corrigidos exemplos de precedência, conversão, identidade, strings e radar. As aulas interativas de maior risco tratam entradas inválidas e números com vírgula.

Execute as verificações na raiz do projeto, sem dependências externas:

```bash
python -m unittest discover -s tests -v
```

A suíte executa as 33 aulas com dados de exemplo, verifica importações sem efeitos e cobre entradas inválidas e resultados conhecidos. Consulte [o relatório](evidencias/RELATORIO.md).

## Próximos estudos

- Funções e reaproveitamento de código
- Listas, tuplas e dicionários
- Leitura e escrita de arquivos
- Automação aplicada a QA

## Contexto profissional

Este repositório registra meus estudos de programação como Analista de Testes (QA), apoiando minha evolução em automação de testes. Minha experiência profissional abrange meios de pagamento, adquirência, serviços financeiros e seguros.

## Autor

[Demétrios Alves Da Silva](https://github.com/Demetrios10)
