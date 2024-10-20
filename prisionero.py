import random

# Definimos las acciones posibles
COOPERATE = "cooperate"
DEFECT = "defect"

# Recompensas según las decisiones de ambos jugadores
PAYOFF_MATRIX = {
    (COOPERATE, COOPERATE): (2, 2),
    (COOPERATE, DEFECT): (0, 3),
    (DEFECT, COOPERATE): (3, 0),
    (DEFECT, DEFECT): (1, 1),
}

def prisoner_dilemma(player1_strategy, player2_strategy, rounds=5):
    """
    Simula el dilema del prisionero para dos jugadores en múltiples rondas.
    
    player1_strategy y player2_strategy son funciones que reciben las acciones previas
    y devuelven "cooperate" o "defect".
    """
    p1_score = 0
    p2_score = 0
    p1_last_action = None
    p2_last_action = None

    for i in range(rounds):
        # Cada jugador decide su acción
        p1_action = player1_strategy(p2_last_action)
        p2_action = player2_strategy(p1_last_action)
        
        # Obtenemos las recompensas para ambos jugadores según sus decisiones
        p1_reward, p2_reward = PAYOFF_MATRIX[(p1_action, p2_action)]
        
        # Acumulamos las recompensas
        p1_score += p1_reward
        p2_score += p2_reward
        
        # Actualizamos las últimas acciones
        p1_last_action = p1_action
        p2_last_action = p2_action
        
        print(f"Round {i+1}: Player 1 -> {p1_action}, Player 2 -> {p2_action}")
        print(f"Scores: Player 1: {p1_score}, Player 2: {p2_score}\n")

    return p1_score, p2_score


# Estrategias simples para cada jugador
def always_cooperate(_):
    """El jugador siempre coopera."""
    return COOPERATE

def always_defect(_):
    """El jugador siempre traiciona."""
    return DEFECT

def random_strategy(_):
    """El jugador elige una acción de forma aleatoria."""
    return random.choice([COOPERATE, DEFECT])

# Ejecutamos el dilema del prisionero con dos estrategias predeterminadas
prisoner_dilemma(always_cooperate, always_defect)
