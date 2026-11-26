"""Verificação das aulas por execução e das entradas de maior risco."""

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AULAS = sorted((ROOT / "curso_python").glob("*/*.py"))
TOTAL_AULAS = 33
TIMEOUT_SEGUNDOS = 5

ENTRADAS_POR_AULA = {
    12: "Pessoa\n1,75\n70\n",
    14: "Pessoa\nTeste\n",
    15: "sim\n",
    17: "Demetrios\n",
    19: "s\n95120\n",
    20: "a\n",
    21: "123456\n",
    22: "Maria\n",
    23: "b\n",
    24: "Pessoa\nTeste\n",
    26: "2,5\n",
}


def numero_da_aula(caminho: Path) -> int:
    return int(caminho.stem.removeprefix("aula"))


def caminho_da_aula(numero: int) -> Path:
    return next(p for p in AULAS if numero_da_aula(p) == numero)


def rodar_python(*argumentos: str, entrada: str = "") -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, *argumentos],
        input=entrada,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SEGUNDOS,
        check=False,
    )


def executar(numero: int, entrada: str = "") -> subprocess.CompletedProcess:
    return rodar_python(str(caminho_da_aula(numero)), entrada=entrada)


def importar_aula(numero: int):
    caminho = caminho_da_aula(numero)
    spec = importlib.util.spec_from_file_location(caminho.stem, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class TestAulas(unittest.TestCase):
    def test_numeracao_das_aulas_e_contigua_e_sem_duplicatas(self):
        numeros = sorted(numero_da_aula(caminho) for caminho in AULAS)
        self.assertEqual(numeros, list(range(1, TOTAL_AULAS + 1)))
        self.assertEqual(len(set(AULAS)), TOTAL_AULAS)

    def test_todas_as_aulas_executam(self):
        self.assertEqual(len(AULAS), TOTAL_AULAS)
        for caminho in AULAS:
            numero = numero_da_aula(caminho)
            with self.subTest(aula=numero):
                resultado = executar(numero, ENTRADAS_POR_AULA.get(numero, ""))
                self.assertEqual(resultado.returncode, 0, resultado.stderr)

    def test_importar_nao_imprime_nem_pede_entrada(self):
        for caminho in AULAS:
            with self.subTest(aula=caminho.stem):
                codigo = f"import runpy; runpy.run_path({str(caminho)!r})"
                resultado = rodar_python("-c", codigo)
                self.assertEqual(resultado.returncode, 0, resultado.stderr)
                self.assertEqual(resultado.stdout, "")

    def test_imc_rejeita_zero_negativos_e_nao_finitos(self):
        aula12 = importar_aula(12)
        self.assertAlmostEqual(aula12.calcular_imc(70, 1.75), 22.857142857)
        casos_invalidos = [
            (70, 0),
            (-1, 1.75),
            (70, -1),
            (float("nan"), 1.75),
            (70, float("inf")),
        ]
        for peso, altura in casos_invalidos:
            with self.subTest(peso=peso, altura=altura), self.assertRaises(ValueError):
                aula12.calcular_imc(peso, altura)

    def test_imc_invalido_nao_encerra_com_excecao(self):
        for entrada in ["Pessoa\n0\n70\n", "Pessoa\nabc\n"]:
            resultado = executar(12, entrada)
            self.assertEqual(resultado.returncode, 0)
            self.assertIn("Entrada inválida", resultado.stdout)

    def test_senha_textual_nao_causa_erro(self):
        resultado = executar(19, "s\nabc\n")
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Sair", resultado.stdout)

    def test_sim_abreviada_e_normalizada(self):
        self.assertIn("Entrar", executar(19, " S \n95120\n").stdout)

    def test_rejeita_nao_letras(self):
        for aula in (20, 23):
            for entrada in ("12\n", "\n", "ab\n"):
                with self.subTest(aula=aula, entrada=entrada):
                    self.assertIn("Entrada inválida", executar(aula, entrada).stdout)

    def test_conversao_com_virgula_e_erro(self):
        self.assertIn("5.0", executar(26, "2,5\n").stdout)
        self.assertIn("Entrada inválida", executar(26, "abc\n").stdout)

    def test_precedencia_corrigida(self):
        saida = executar(11).stdout.splitlines()
        self.assertEqual(saida, ["610", "900", "570", "590.0", "600.0", "309.7", "58"])


if __name__ == "__main__":
    unittest.main()
