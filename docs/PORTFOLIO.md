# Estudo de caso · Fundamentos de Python

[README e execução](../README.md) · [Portfólio do autor](https://github.com/Demetrios10/Demetrios10/blob/main/PORTFOLIO.md)

## Problema e objetivo

Organizar exercícios de programação em uma trilha que possa ser estudada, executada e revisada. O projeto pratica lógica, entradas, conversões, decisões e repetições como base para automação de testes.

## Solução e decisões

São 33 aulas em seis temas. Os arquivos têm execução independente e uma função `main()`, permitindo importar o módulo sem imprimir ou solicitar dados. O projeto usa apenas a biblioteca padrão do Python.

As validações tratam entradas inválidas e regras dos exemplos, como valores positivos e finitos no cálculo de IMC e conversão de vírgula decimal. Os testes combinam execução de scripts, entradas de exemplo e asserções de resultados conhecidos.

## O que revisar no código

| Arquivo | O que demonstra |
|---|---|
| [Índice das aulas](../curso_python/README.md) | Progressão e navegação |
| [Cálculo de IMC](../curso_python/03_entrada_e_formatacao/aula12.py) | Separação do cálculo e validação de entradas |
| [Precedência](../curso_python/02_operadores/aula11.py) | Resultados que podem ser conferidos por asserções |
| [Suíte](../tests/test_aulas.py) | Execução das 33 aulas, importação e casos de entrada inválida |

## Evidência e limites

O [relatório de 07/11/2026](../evidencias/RELATORIO.md) registra nove testes aprovados. A [saída da execução](../evidencias/execucao.txt) permite conferir o resultado. Um teste percorre todas as aulas com entradas de exemplo; outro confere importação sem efeitos colaterais.

São exercícios didáticos, com dados fictícios. A suíte não cobre todas as combinações de entrada e não transforma os exemplos em uma aplicação de produção. Nesta revisão do portfólio, o código foi consultado e a documentação ajustada; a suíte não foi executada novamente.

## Próxima evolução

Adicionar estudos de funções reutilizáveis, coleções e arquivos, com novos exemplos e verificações proporcionais ao comportamento introduzido.

Revisão: 09/11/2026.
