import os
import numpy as np
import pandas as pd


import numpy as np
import pandas as pd


def simulate_endings(
    n_simulations: int,
    p_honor_high: float = 0.40,        # 40 % terminam com honra alta
    p_help_if_high: float = 0.85,      # 85 % dos “honra alta” ajudam John
    p_help_if_low:  float = 0.35,      # 55 % dos “honra baixa” ajudam John
    p_bond4_high:   float = 0.70,      # 70 % dos “honra alta” chegam com vínculo 4
    p_bond4_low:    float = 0.40,      # 40 % dos “honra baixa” chegam com vínculo 4
    return_cutscene: bool = True
) -> tuple[pd.DataFrame, float | None]:
    """
    Retorna (df_resultados, prob_cutscene).

    A cut-scene do cavalo agora dispara **apenas** se o vínculo for
    exatamente nível 4, modelado pelas probabilidades p_bond4_high / _low.
    """
    rng = np.random.default_rng()

    # --- honra ----------------------------------------------------------
    honor_high = rng.random(n_simulations) < p_honor_high

    # --- escolha: ajudar John ou buscar dinheiro ------------------------
    help_john = np.empty(n_simulations, dtype=bool)
    help_john[ honor_high] = rng.random(honor_high.sum())    < p_help_if_high
    help_john[~honor_high] = rng.random((~honor_high).sum()) < p_help_if_low

    # --- vínculo do cavalo (NÍVEL 4) -----------------------------------
    bond_lv4 = np.empty(n_simulations, dtype=bool)
    bond_lv4[ honor_high] = rng.random(honor_high.sum())    < p_bond4_high
    bond_lv4[~honor_high] = rng.random((~honor_high).sum()) < p_bond4_low

    # --- finais ---------------------------------------------------------
    endings = np.empty(n_simulations, dtype=object)
    endings[ honor_high &  help_john] = "Final A"   # Redenção
    endings[ honor_high & ~help_john] = "Final B"   # Ganância Honrada
    endings[~honor_high &  help_john] = "Final C"   # Sacrifício Brutal
    endings[~honor_high & ~help_john] = "Final D"   # Derrota Total

    # --- probabilidade da cut-scene ------------------------------------
    cutscene_prob = bond_lv4.mean() if return_cutscene else None

    results = (
        pd.Series(endings, name="Final")
          .value_counts()
          .reindex(["Final A", "Final B", "Final C", "Final D"])
          .fillna(0)
          .rename_axis("Final")
          .reset_index(name="Ocorrências")
    )
    results["Probabilidade"] = results["Ocorrências"] / n_simulations * 100

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
    n = 1_000_000_000
    finais, prob_cutscene = simulate_endings(n_simulations=n)
    print("Distribuição dos finais simulados:")
    print(finais.to_string(index=False))
    print(f"\nProbabilidade da cutscene do cavalo: {prob_cutscene:.2%}")

    save_results_to_excel(finais, prob_cutscene, n_simulations=n)
