# Inclui o cabeçalho padrão do ROS para carimbar a mensagem com tempo e ID de sequência
std_msgs/Header header

# Definição dos estados do jogo como constantes
uint8 GAMESTATE_INITAL=0
uint8 GAMESTATE_READY=1
uint8 GAMESTATE_SET=2
uint8 GAMESTATE_PLAYING=3
uint8 GAMESTATE_FINISHED=4
uint8 game_state  # Sem atribuição de valor aqui

# Secondary state, penaltyshoot is penalty shootout at the end of the game,
# penaltykick is a kick during the game
uint8 STATE_NORMAL=0
uint8 STATE_PENALTYSHOOT=1
uint8 STATE_OVERTIME=2
uint8 STATE_TIMEOUT=3
uint8 STATE_DIRECT_FREEKICK=4
uint8 STATE_INDIRECT_FREEKICK=5
uint8 STATE_PENALTYKICK=6
uint8 STATE_CORNER_KICK=7
uint8 STATE_GOAL_KICK=8
uint8 STATE_THROW_IN=9
uint8 secondary_state  # Sem atribuição de valor aqui

# Para a versão mais recente do controlador de jogo
# Indica qual time tem a cobrança de falta ou pênalti
uint8 secondary_state_team
# Indica em qual fase de execução o estado secundário está
uint8 MODE_PREPARATION=0
uint8 MODE_PLACING=1
uint8 MODE_END=2
uint8 secondary_state_mode

bool first_half
uint8 own_score
uint8 rival_score

# Segundos restantes para o final da metade do jogo
int16 seconds_remaining
# Segundos restantes para eventos como kickoff
int16 secondary_seconds_remaining

bool has_kick_off
bool penalized
uint16 seconds_till_unpenalized

# Cores do time
uint8 BLUE=0
uint8 RED=1
uint8 team_color

bool drop_in_team
uint16 drop_in_time

# Número do tiro de pênalti atual durante o shootout
uint8 penalty_shot
# Padrão binário indicando tiros de pênalti bem-sucedidos (1 para bem-sucedido, 0 para malsucedido)
uint16 single_shots

string coach_message

bool[] team_mates_with_penalty
bool[] team_mates_with_red_card
