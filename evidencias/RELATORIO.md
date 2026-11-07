# Evolução dos fundamentos de Python

Data: 07/11/2026.

## Alterações

- 33 aulas com execução protegida por `if __name__ == "__main__"`.
- Correções de comentários e resultados de precedência (600.0 e 58).
- Conversões de tipos demonstram o tipo do valor convertido.
- IMC matemático valida valores positivos e finitos e aceita vírgula decimal.
- Respostas sim/não normalizadas; senha de demonstração tratada como texto.
- Exemplos de vogais rejeitam entradas vazias, números e múltiplas letras.
- `except ValueError` substitui captura genérica no exercício de conversão.
- Exemplos de identidade, flags, strings e atribuição composta revisados.
- Radar simplificado só avalia velocidade no ponto de medição.

## Execução

Comando: `python -m unittest discover -s tests -v`.

9 testes aprovados em 10,623 segundos. Uma verificação percorre as 33 aulas com dados de exemplo e outra importa cada aula sem efeitos colaterais. As demais cobrem entradas inválidas e resultados específicos. Não significa cobertura exaustiva de todas as entradas possíveis.

Python 3.14, Windows, sem dependências externas.
