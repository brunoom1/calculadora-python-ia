#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Interativa da Calculadora Python
Simula a interface completa em linha de comando
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path("app/src")))

from calculator import Calculator
from locale_manager import LocaleManager


def print_header():
    print("\n" + "="*70)
    print("CALCULADORA PYTHON 1.0.0-alpha — Demo Interativa".center(70))
    print("="*70)
    print("\nInstruções:")
    print("  Digite: numero operador numero")
    print("  Exemplos:")
    print("    5 + 3")
    print("    10,50 + 5,50")
    print("    1.234,56 + 2.100,44")
    print("  Comandos especiais:")
    print("    'exit' ou 'sair' — Sair")
    print("    'limpar' — Limpar histórico")
    print("\nFormato pt-BR suportado:")
    print("  • Decimal: vírgula (,)")
    print("  • Milhar: ponto (.)")
    print("  Exemplos: 1.234,56 (um mil duzentos e trinta e quatro vírgula cinquenta e seis)")
    print("\n" + "="*70 + "\n")


def main():
    calc = Calculator()
    locale = LocaleManager.get_instance()
    historico = []

    print_header()

    while True:
        try:
            print("\n[Operação] ", end="", flush=True)
            entrada = input().strip()

            if not entrada:
                continue

            if entrada.lower() in ['exit', 'sair', 'quit']:
                print("\nAté logo! Calculadora encerrada.")
                break

            if entrada.lower() == 'limpar':
                historico = []
                print("\n✅ Histórico limpo!")
                continue

            if entrada.lower() == 'historico':
                if historico:
                    print("\n[Histórico]")
                    for i, op in enumerate(historico, 1):
                        print(f"  {i}. {op}")
                else:
                    print("\n✗ Histórico vazio")
                continue

            # Parsear entrada
            partes = entrada.split()
            if len(partes) < 3:
                print("\n✗ Formato inválido. Use: numero operador numero")
                print("  Exemplo: 5 + 3")
                continue

            # Extrair
            num1_str = partes[0]
            operador = partes[1]
            num2_str = partes[2]

            # Validar operador
            if operador not in ['+', '-', '*', '/', '×', '÷', '−']:
                print(f"\n✗ Operador inválido: {operador}")
                print("  Use: + - * / (ou × ÷ −)")
                continue

            # Converter símbolos
            op_map = {'×': '*', '÷': '/', '−': '-'}
            if operador in op_map:
                operador = op_map[operador]

            try:
                # Parse com LocaleManager
                print(f"\n  Parseando: '{num1_str}' → ", end="", flush=True)
                num1 = locale.parse_number(num1_str)
                print(f"{num1}")

                print(f"  Parseando: '{num2_str}' → ", end="", flush=True)
                num2 = locale.parse_number(num2_str)
                print(f"{num2}")

                # Calcular
                print(f"\n  Calculando: {num1} {operador} {num2}...")
                resultado = calc.calculate(num1, num2, operador)

                if isinstance(resultado, str):
                    print(f"\n  ⚠️  {resultado}")
                    print("\n✗ ERRO")
                else:
                    # Formatar resultado
                    resultado_formatado = locale.format_number(resultado)
                    print(f"\n  ✅ Resultado: {resultado_formatado}")
                    print(f"  (Valor bruto: {resultado})")

                    # Adicionar ao histórico
                    operacao_str = f"{num1_str} {operador} {num2_str} = {resultado_formatado}"
                    historico.append(operacao_str)

            except ValueError as e:
                print(f"\n✗ Erro ao parsear: {e}")

        except KeyboardInterrupt:
            print("\n\n⏹️  Interrupção do usuário. Encerrando...")
            break
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "="*70)
    print("Obrigado por usar a Calculadora Python!".center(70))
    print("="*70 + "\n")


if __name__ == "__main__":
    sys.exit(main() or 0)
