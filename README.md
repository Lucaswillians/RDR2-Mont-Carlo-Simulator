# 🎯 Questão – Simulação de Finais em *Red Dead Redemption 2* com Método de Monte Carlo

No jogo *Red Dead Redemption 2*, o personagem Arthur Morgan sempre morre no final da história principal. Porém, a forma como ele morre depende de duas variáveis principais:

- O nível de **honra** do jogador (alta ou baixa).
- A **escolha final** de Arthur: ajudar John Marston a fugir ou voltar para buscar o dinheiro.

Além disso, existe uma **cutscene secreta e emocional**, em que Arthur se **despede do cavalo antes de morrer**. Essa cena **só é exibida se**:

1. O jogador tiver **honra alta**.
2. O cavalo atual estiver com **afinidade no nível máximo (vínculo 4)**.

---

## 🧱 Os finais possíveis são:

- **Final A – Redenção:** Honra alta + ajudar John.  
  Arthur morre em paz vendo o nascer do sol.  
  ✅ Pode conter a *cutscene* do cavalo.

- **Final B – Ganância Honrada:** Honra alta + buscar o dinheiro.  
  Arthur morre lutando contra Micah.  
  ✅ Pode conter a *cutscene* do cavalo.

- **Final C – Sacrifício Brutal:** Honra baixa + ajudar John.  
  Arthur é espancado até a morte por Micah.  
  ❌ Sem *cutscene* do cavalo.

- **Final D – Derrota Total:** Honra baixa + buscar o dinheiro.  
  Arthur é esfaqueado por Micah.  
  ❌ Sem *cutscene* do cavalo.

---

## 📊 Dados de 10.000 jogadores:

- 40% terminaram com **honra alta**, 60% com **honra baixa**.

Entre os jogadores com **honra alta**:
- 85% ajudaram John → **Final A**
- 15% buscaram o dinheiro → **Final B**

Entre os jogadores com **honra baixa**:
- 35% ajudaram John → **Final C**
- 65% buscaram o dinheiro → **Final D**

Dos jogadores com **honra alta**, estima-se que **70% têm afinidade máxima com o cavalo** no final.

---

## ❓ Perguntas:

Com base nesses dados e utilizando o **método de Monte Carlo** com **10.000 simulações**:

1. Qual é a **probabilidade estimada de ocorrência** de cada final?
2. Qual é o **final mais comum** entre os jogadores?
3. Qual é a **probabilidade de o jogador ver a *cutscene* da despedida do cavalo?**
4. Descreva, **passo a passo**, como a simulação de Monte Carlo poderia ser implementada para estimar esses resultados.

---

## ✅ Gabarito Esperado

### 📌 Probabilidades dos finais:

- **Final A:** 40% × 85% = **34%**
- **Final B:** 40% × 15% = **6%**
- **Final C:** 60% × 35% = **21%**
- **Final D:** 60% × 65% = **39%**

🔺 **Final mais comum:** Final D – Derrota Total (**39%**)

---

### 🐴 Probabilidade da *cutscene* do cavalo:

Somente pode ocorrer nos finais A e B, **e apenas se houver afinidade máxima (70%)**:

- (Final A + Final B) = 34% + 6% = **40%**
- *Cutscene* = 40% × 70% = **28%**

✅ **Resposta:** 28% dos jogadores presenciam a despedida do cavalo.

---

## 🛠️ Etapas da Simulação (Monte Carlo):

1. Repetir o experimento **10.000 vezes**.
2. Para cada simulação:
   - Sortear se o jogador tem **honra alta (40%)** ou **baixa (60%)**.
   - Se **honra alta**:
     - Sortear entre Final A (85%) ou Final B (15%).
     - Sortear se tem **afinidade máxima com o cavalo (70%)** – relevante para a *cutscene*.
   - Se **honra baixa**:
     - Sortear entre Final C (35%) ou Final D (65%) – sem chance de *cutscene*.
3. Contar quantas vezes **cada final** ocorreu.
4. Contar quantas vezes a ***cutscene* do cavalo** apareceu.
5. Dividir os resultados pelo total de simulações (**10.000**) para obter as probabilidades.
