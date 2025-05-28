import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_regras():
    print("""
🎮 [1;32mBLACKJACK NUTRICIONAL – PvCPU[0m

[1mObjetivo:[0m
Acumule até [1;33m21 pontos[0m sem ultrapassá-los. Use cartas de alimentos saudáveis 🍎 e fast food 🍔 com sabedoria!

[1mCartas:[0m
- 🍎 Alimentos Saudáveis: menos pontos (1–5), menos risco
- 🍔 Fast Food: mais pontos (5–10), mais risco!

[1mMecânica:[0m
- Toda vez que comprar carta, responda a uma [1mlógica proposicional[0m:
  - ✅ Acertou: carta ganha +1 ponto e CPU recebe uma carta fast food!
  - ❌ Errou: CPU ganha uma carta saudável com -1 ponto (benefício).

[1mCPU:[0m
- Joga com estratégia baseada nos próprios pontos.
- Pode parar ou arriscar após você parar.

[1mVence:[0m quem estiver mais próximo de 21 sem estourar!

[1;34mBoa sorte e jogue com lógica![0m
""")

import random

# Cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

SAUDAVEIS = {
    "Maçã": 2, "Banana": 3, "Brócolis": 1, "Peixe": 4, "Frango": 5,
    "Arroz Integral": 3, "Aveia": 2, "Ovos": 1, "Nozes": 5, "Iogurte": 2,
    "Granola": 4, "Alface": 3, "Salmão": 5, "Espinafre": 2, "Batata Doce": 4
}

FAST_FOOD = {
    "Hambúrguer": 10, "Pizza": 9, "Batata Frita": 8, "Refrigerante": 7,
    "Sorvete": 6, "Donut": 5, "Cachorro-Quente": 4,
    "Torta de Chocolate": 6, "Bacon": 7, "Nuggets": 5, "Cheesecake": 8
}

PERGUNTAS_LOGICAS = [
    {
        "pergunta": "Se 'p → q' é verdadeiro, qual situação torna isso falso?",
        "opcoes": ["p verdadeiro; q falso", "p falso; q falso", "p falso; q verdadeiro"],
        "resposta": 0
    },
    {
        "pergunta": "A negação de 'Todos os alimentos são saudáveis' é:",
        "opcoes": ["Nenhum alimento é saudável", "Algum alimento não é saudável", "Todos os alimentos não são saudáveis"],
        "resposta": 1
    },
    {
        "pergunta": "Se 'Se corro, então me canso' (p → q) é verdadeiro, qual opção é inválida?",
        "opcoes": ["Corro e me canso", "Não corro e me canso", "Corro e não me canso"],
        "resposta": 2
    },
    {
        "pergunta": "Qual é a contrapositiva de 'Se comer fast food, terá mais calorias'?",
        "opcoes": [
            "Se não comer fast food, terá menos calorias", 
            "Se não tiver mais calorias, então não comeu fast food", 
            "Se tiver mais calorias, então comeu fast food"
        ],
        "resposta": 1
    },
    {
        "pergunta": "A negação de 'Nenhum fast food é saudável' é:",
        "opcoes": ["Todos os fast foods são saudáveis", "Algum fast food é saudável", "Nenhum alimento saudável é fast food"],
        "resposta": 1
    },
    {
        "pergunta": "Se 'Todos os saudáveis praticam exercícios' e 'Carlos não pratica exercícios', então:",
        "opcoes": [
            "Carlos é saudável",
            "Carlos não é saudável",
            "Carlos é atleta"
        ],
        "resposta": 1
    },
    {
        "pergunta": "A contrária de 'Se você comer bem, então terá saúde' é:",
        "opcoes": [
            "Se você tiver saúde, então comeu bem",
            "Se você não tiver saúde, então não comeu bem",
            "Se você não comer bem, então não terá saúde"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Negar 'Se corre, então emagrece' resulta em:",
        "opcoes": [
            "Corre e não emagrece",
            "Não corre e não emagrece",
            "Não corre e emagrece"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Qual das opções representa uma tautologia?",
        "opcoes": [
            "p ∨ ¬p",
            "p ∧ ¬p",
            "¬(p ∨ q)"
        ],
        "resposta": 0
    },
    {
        "pergunta": "A equivalência de 'p → q' é:",
        "opcoes": [
            "¬p ∨ q",
            "¬q ∨ p",
            "p ∧ ¬q"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Qual das frases é uma contradição?",
        "opcoes": [
            "p ∧ ¬p",
            "p ∨ q",
            "¬(p ∧ ¬p)"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Se 'Todo alimento natural é nutritivo', qual opção nega isso corretamente?",
        "opcoes": [
            "Nenhum alimento natural é nutritivo",
            "Algum alimento natural não é nutritivo",
            "Todos os alimentos não são nutritivos"
        ],
        "resposta": 1
    },
    {
        "pergunta": "Se 'Nenhum refrigerante é saudável', qual opção é equivalente?",
        "opcoes": [
            "Todo refrigerante não é saudável",
            "Algum refrigerante é saudável",
            "Nenhum alimento saudável é refrigerante"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Se 'Se beber água, então melhora o metabolismo' é falso, então:",
        "opcoes": [
            "Bebeu água e melhorou o metabolismo",
            "Não bebeu água e não melhorou",
            "Bebeu água e não melhorou o metabolismo"
        ],
        "resposta": 2
    },
    {
        "pergunta": "Negar 'Algum alimento processado é nutritivo' é:",
        "opcoes": [
            "Nenhum alimento processado é nutritivo",
            "Todos os alimentos são processados",
            "Algum alimento natural não é nutritivo"
        ],
        "resposta": 0
    }
]


def criar_baralho():
    baralho = [(a, v, "saudavel") for a, v in SAUDAVEIS.items()] +               [(a, v, "fastfood") for a, v in FAST_FOOD.items()]
    random.shuffle(baralho)
    return baralho

def calcular_pontos(mao):
    return sum(c[1] for c in mao)

def mostrar_mao(nome, mao, esconder_ultima=False):
    print(f"\n{BOLD}{nome} - Mão atual:{RESET}")
    for i, (alimento, valor, tipo) in enumerate(mao):
        if esconder_ultima and i == len(mao) - 1:
            print("- ??? (oculta)")
        else:
            cor = GREEN if tipo == "saudavel" else RED
            emoji = "🍎" if tipo == "saudavel" else "🍔"
            print(f"- {cor}{alimento} ({valor} pts){RESET} {emoji}")
    if esconder_ultima:
        print(f"Total visível: {calcular_pontos(mao[:-1])}+")
    else:
        print(f"Total: {calcular_pontos(mao)}")

def fazer_pergunta():
    pergunta = random.choice(PERGUNTAS_LOGICAS)
    print(f"\n{CYAN}📚 Pergunta lógica:{RESET}")
    print(f"{YELLOW}{pergunta['pergunta']}{RESET}")
    for i, op in enumerate(pergunta["opcoes"], 1):
        print(f"{i}. {op}")
    while True:
        try:
            resposta = int(input("Sua resposta (1-3): "))
            if resposta in [1, 2, 3]:
                return resposta - 1 == pergunta["resposta"]
        except ValueError:
            pass
        print("Entrada inválida.")

def turno_jogador(baralho, mao_jogador, mao_cpu):
    while True:
        mostrar_mao("👤 Jogador", mao_jogador)
        mostrar_mao("🤖 CPU", mao_cpu, esconder_ultima=True)

        if calcular_pontos(mao_jogador) >= 21:
            break

        acao = input("\nDeseja (1) Comprar carta ou (2) Parar? ").strip()
        while acao not in ["1", "2"]:
            acao = input("Digite 1 para comprar ou 2 para parar: ").strip()
        if acao == "2":
            break

        acertou = fazer_pergunta()
        if acertou:
            carta = baralho.pop()
            alimento, valor, tipo = carta
            valor = valor + 1 if tipo == "saudavel" else max(4, valor - 1)
            mao_jogador.append((alimento, valor, tipo))
            penal = random.choice(list(FAST_FOOD.items()))
            mao_cpu.append((penal[0], penal[1], "fastfood"))
            print(f"\n{GREEN}Você acertou!{RESET} Ganhou carta modificada: {alimento} ({valor})")
            print(f"{RED}CPU penalizada! Uma carta fast food foi adicionada.{RESET}")
        else:
            carta = random.choice(list(FAST_FOOD.items()))
            mao_jogador.append((carta[0], carta[1], "fastfood"))
            bonus = baralho.pop()
            mao_cpu.append(bonus)
            print(f"\n{RED}Você errou!{RESET} Ganhou carta ruim: {carta[0]} ({carta[1]})")
            print(f"{GREEN}CPU ganhou um bônus oculto.{RESET}")

def turno_cpu(baralho, mao_cpu):
    while calcular_pontos(mao_cpu) < 17 or (17 <= calcular_pontos(mao_cpu) <= 20 and random.random() < 0.4):
        carta = baralho.pop()
        mao_cpu.append(carta)
        print(f"{CYAN}CPU comprou uma carta...{RESET}")

def jogar():
    print(f"{MAGENTA}\n🎮 Bem-vindo ao Blackjack Nutricional PvCPU!{RESET}")
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_cpu = [baralho.pop(), baralho.pop()]
    turno_jogador(baralho, mao_jogador, mao_cpu)
    turno_cpu(baralho, mao_cpu)

    pj, pc = calcular_pontos(mao_jogador), calcular_pontos(mao_cpu)

    print(f"\n{BOLD}===== RESULTADO FINAL ====={RESET}")
    mostrar_mao("👤 Jogador", mao_jogador)
    mostrar_mao("🤖 CPU", mao_cpu)

    if pj > 21 and pc > 21:
        print(f"{YELLOW}Ambos estouraram! Empate.{RESET}")
    elif pj > 21:
        print(f"{RED}Você estourou! CPU vence.{RESET}")
    elif pc > 21:
        print(f"{GREEN}CPU estourou! Você venceu!{RESET}")
    elif pj > pc:
        print(f"{GREEN}Você venceu! 🏆{RESET}")
    elif pj < pc:
        print(f"{RED}CPU venceu!{RESET}")
    else:
        print(f"{YELLOW}Empate!{RESET}")

# Loop principal
while True:
    mostrar_regras()
    jogar()
    again = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if again != 's':
        print("Até logo!")
        break