# RDR2-Mont-Carlo-Simulator

 ## 🎯 Questão – Método de Monte Carlo aplicado aos finais de Red Dead Redemption 2
### No jogo Red Dead Redemption 2, o protagonista Arthur Morgan tem destinos diferentes ao final da campanha, dependendo das decisões tomadas pelo jogador e do nível de honra atingido ao longo da história. Apesar de todos os finais levarem à morte de Arthur, o modo como ele morre varia significativamente, refletindo suas escolhas morais e ações finais.

Considere os seguintes 4 finais principais:

- Final A – Redenção: Arthur tem honra alta e ajuda John a fugir. Ele morre de forma serena, vendo o nascer do sol, depois de garantir a fuga do amigo.

- Final B – Ganância Honrada: Arthur tem honra alta e decide voltar para pegar o dinheiro. Morre em luta contra Micah, com alguma dignidade, mas ainda motivado pela ganância.

- Final C – Sacrifício Brutal: Arthur tem honra baixa, mas ainda assim decide ajudar John a escapar. Morre espancado por Micah, sem compaixão.

- Final D – Derrota Total: Arthur tem honra baixa e escolhe voltar pelo dinheiro. Micah o esfaqueia brutalmente, sendo o final mais trágico e sem redenção.

Com base em dados coletados de 10.000 jogadores:

- 40% dos jogadores terminam o jogo com honra alta, e 60% com honra baixa.

Entre os jogadores com honra alta:

- 85% ajudam John (Final A)

- 15% vão atrás do dinheiro (Final B)

Entre os jogadores com honra baixa:

- 35% ajudam John (Final C)

- 65% vão atrás do dinheiro (Final D)

Pergunta:
### Utilizando o método de Monte Carlo, simule (ou descreva como simular) o processo para estimar a probabilidade de cada final acontecer. Após a simulação com 10.000 execuções, determine:

A probabilidade estimada de cada final.

Qual final é o mais comum entre os jogadores, segundo os dados.

✅ Gabarito esperado (resumo da resolução):
Simulação Monte Carlo: repetir 10.000 vezes o processo de:

Sortear se o jogador termina com honra alta (40%) ou baixa (60%).

Com base nisso, sortear a decisão final do Arthur.

Cálculo esperado:

- Final A – Redenção: 40% * 85% = 34%

- Final B – Ganância Honrada: 40% * 15% = 6%

- Final C – Sacrifício Brutal: 60% * 35% = 21%

- Final D – Derrota Total: 60% * 65% = 39%

- ➡️ Final mais provável: Final D – Derrota Total com 39% de chance.
