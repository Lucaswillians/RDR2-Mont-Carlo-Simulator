import os
import numpy as np
import pandas as pd


def simulate_endings(
    n_simulations: int = 100_000_000,
    p_honor_high: float = 0.40,     # 40 % terminam com honra alta
    p_help_if_high: float = 0.85,   # 85 % dos “honra alta” ajudam John
    p_help_if_low: float = 0.35,    # 35 % dos “honra baixa” ajudam John
    p_max_bond: float = 0.70,       # 70 % dos “honra alta” têm vínculo 4 com o cavalo
    return_cutscene: bool = True
) -> tuple[pd.DataFrame, float | None]:
    """Retorna (df_resultados, prob_cutscene)."""
    
    rng = np.random.default_rng()

    honor_high = rng.random(n_simulations) < p_honor_high

    help_john = np.empty(n_simulations, dtype=bool)
    help_john[ honor_high] = rng.random(honor_high.sum())    < p_help_if_high
    help_john[~honor_high] = rng.random((~honor_high).sum()) < p_help_if_low

    max_bond = rng.random(n_simulations) < p_max_bond

    endings = np.empty(n_simulations, dtype=object)
    cutscene_counter = 0

    for i, (h_high, helps, bond) in enumerate(zip(honor_high, help_john, max_bond)):
        if h_high:                      # honra alta
            if helps:
                endings[i] = "Final A"  # Redenção
            else:
                endings[i] = "Final B"  # Ganância Honrada
            if bond:                    # cut-scene possível apenas aqui
                cutscene_counter += 1
        else:                           # honra baixa
            if helps:
                endings[i] = "Final C"  # Sacrifício Brutal
            else:
                endings[i] = "Final D"  # Derrota Total

    results = (
        pd.Series(endings, name="Final")
        .value_counts()
        .reindex(["Final A", "Final B", "Final C", "Final D"])  # ordenação fixa
        .fillna(0)
        .rename_axis("Final")
        .reset_index(name="Ocorrências")
    )
    results["Probabilidade"] = results["Ocorrências"] / n_simulations * 100

    cutscene_prob = cutscene_counter / n_simulations if return_cutscene else None
    return results, cutscene_prob


def save_results_to_excel(
    df: pd.DataFrame,
    cutscene_prob: float,
    n_simulations: int,
    filename: str = "resultados_rdr2.xlsx"
) -> None:
    """
    Salva/atualiza um arquivo Excel:
      • Adiciona aba cujo nome é o nº de simulações (ex.: "10000").
      • Inclui linha extra com a probabilidade da cutscene.
    """
    # adiciona linha com a cutscene
    df_to_save = df.copy()
    df_to_save.loc[len(df_to_save)] = {
        "Final": "Cutscene do Cavalo",
        "Ocorrências": "",
        "Probabilidade": round(cutscene_prob * 100, 2)
    }

    mode = "a" if os.path.isfile(filename) else "w"
    with pd.ExcelWriter(filename, engine="openpyxl", mode=mode) as writer:
        sheet_name = str(n_simulations)
        df_to_save.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"Resultados salvos na aba “{sheet_name}” do arquivo {filename!r}.")


if __name__ == "__main__":
    n = 100_000_000
    finais, prob_cutscene = simulate_endings(n_simulations=n)
    print("Distribuição dos finais simulados:")
    print(finais.to_string(index=False))
    print(f"\nProbabilidade da cutscene do cavalo: {prob_cutscene:.2%}")

    save_results_to_excel(finais, prob_cutscene, n_simulations=n)
