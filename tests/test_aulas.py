"""Verificação das aulas por execução e das entradas de maior risco."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
AULAS = sorted((ROOT / "curso_python").glob("*/*.py"))


def executar(numero, entrada=""):
    caminho = next(p for p in AULAS if p.stem == f"aula{numero:02}")
    return subprocess.run([sys.executable, str(caminho)], input=entrada,
                          capture_output=True, text=True, timeout=5)


class TestAulas(unittest.TestCase):
    def test_33_aulas_executam(self):
        entradas = {12: "Pessoa\n1,75\n70\n", 14: "Pessoa\nTeste\n",
                    15: "sim\n", 17: "Demetrios\n", 19: "s\n95120\n",
                    20: "a\n", 21: "123456\n", 22: "Maria\n",
                    23: "b\n", 24: "Pessoa\nTeste\n", 26: "2,5\n"}
        self.assertEqual(len(AULAS), 33)
        for caminho in AULAS:
            n = int(caminho.stem[4:])
            with self.subTest(aula=n):
                resultado = executar(n, entradas.get(n, ""))
                self.assertEqual(resultado.returncode, 0, resultado.stderr)

    def test_importar_nao_imprime_nem_pede_entrada(self):
        for caminho in AULAS:
            with self.subTest(aula=caminho.stem):
                codigo = ("import runpy; runpy.run_path(" + repr(str(caminho)) + ")")
                r = subprocess.run([sys.executable, "-c", codigo],
                                   input="", capture_output=True, text=True, timeout=5)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(r.stdout, "")

    def test_imc_rejeita_zero_negativos_e_nao_finitos(self):
        caminho = next(p for p in AULAS if p.stem == "aula12")
        spec = importlib.util.spec_from_file_location("aula12", caminho)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertAlmostEqual(modulo.calcular_imc(70, 1.75), 22.857142857)
        for peso, altura in [(70, 0), (-1, 1.75), (70, -1),
                             (float("nan"), 1.75), (70, float("inf"))]:
            with self.subTest(peso=peso, altura=altura), self.assertRaises(ValueError):
                modulo.calcular_imc(peso, altura)

    def test_imc_invalido_nao_encerra_com_excecao(self):
        for entrada in ["Pessoa\n0\n70\n", "Pessoa\nabc\n"]:
            r = executar(12, entrada)
            self.assertEqual(r.returncode, 0)
            self.assertIn("Entrada inválida", r.stdout)

    def test_senha_textual_nao_causa_erro(self):
        r = executar(19, "s\nabc\n")
        self.assertEqual(r.returncode, 0)
        self.assertIn("Sair", r.stdout)

    def test_sim_abreviada_e_normalizada(self):
        self.assertIn("Entrar", executar(19, " S \n95120\n").stdout)

    def test_rejeita_nao_letras(self):
        for aula in (20, 23):
            for entrada in ("12\n", "\n", "ab\n"):
                self.assertIn("Entrada inválida", executar(aula, entrada).stdout)

    def test_conversao_com_virgula_e_erro(self):
        self.assertIn("5.0", executar(26, "2,5\n").stdout)
        self.assertIn("Entrada inválida", executar(26, "abc\n").stdout)

    def test_precedencia_corrigida(self):
        saida = executar(11).stdout.splitlines()
        self.assertEqual(saida, ["610", "900", "570", "590.0",
                                 "600.0", "309.7", "58"])


if __name__ == "__main__":
    unittest.main()
