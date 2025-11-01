"""
Script de exemplo para análise descritiva mínima.

- Gera um CSV de exemplo em `dados/exemplo.csv` se não existir.
- Calcula medidas de tendência central e dispersão da coluna "valor".
- Salva histograma em `outputs/histograma.png`.
- Uso: python analise_descritiva.py [--input path/to/file.csv]
"""

import argparse
import os
from typing import Dict

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def gerar_dados_exemplo(path: str = "dados/exemplo.csv") -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        rng = np.random.default_rng(42)
        df = pd.DataFrame({"valor": rng.normal(loc=50, scale=10, size=200)})
        df.to_csv(path, index=False)
        print(f"[info] Dados de exemplo gerados em: {path}")
    return path


def carregar_dados(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    df = pd.read_csv(path)
    return df


def calcular_estatisticas(vals: pd.Series) -> Dict[str, float]:
    vals = vals.dropna()
    if vals.empty:
        return {}
    stats = {
        "count": int(vals.count()),
        "mean": float(vals.mean()),
        "median": float(vals.median()),
        "std": float(vals.std(ddof=1)),
        "min": float(vals.min()),
        "max": float(vals.max()),
        "q1": float(vals.quantile(0.25)),
        "q3": float(vals.quantile(0.75)),
        "iqr": float(vals.quantile(0.75) - vals.quantile(0.25)),
    }
    return stats


def salvar_histograma(vals: pd.Series, out_path: str = "outputs/histograma.png", bins: int = 20):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.figure(figsize=(8, 5))
    plt.hist(vals.dropna(), bins=bins, color="#4C72B0", edgecolor="black")
    plt.title("Histograma — valor")
    plt.xlabel("valor")
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"[info] Histograma salvo em: {out_path}")


def main(argv: list = None) -> int:
    parser = argparse.ArgumentParser(description="Análise descritiva mínima")
    parser.add_argument("--input", "-i", help="Caminho para CSV com coluna 'valor'", default="dados/exemplo.csv")
    parser.add_argument("--output", "-o", help="Caminho para salvar histograma", default="outputs/histograma.png")
    args = parser.parse_args(argv)

    try:
        # Gera dados se necessário
        if args.input == "dados/exemplo.csv" and not os.path.exists(args.input):
            gerar_dados_exemplo(args.input)

        df = carregar_dados(args.input)
    except Exception as e:
        print(f"[erro] {e}")
        return 2

    if "valor" not in df.columns:
        print("[erro] Coluna 'valor' não encontrada no CSV. As colunas disponíveis são: " + ", ".join(df.columns))
        return 3

    stats = calcular_estatisticas(df["valor"])
    if not stats:
        print("[aviso] Nenhum valor numérico válido encontrado na coluna 'valor'.")
        return 4

    print("\nEstatísticas descritivas (coluna 'valor'):")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    salvar_histograma(df["valor"], out_path=args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
