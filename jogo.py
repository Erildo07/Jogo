import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tiro Simples")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Configuração do jogador
player_width, player_height = 50, 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 5

# Lista de tiros
bullets = []
bullet_speed = 7

# Lista de inimigos
enemies = []
enemy_speed = 3
enemy_spawn_rate = 30  # Quanto menor, mais inimigos aparecem

# Clock para controle de FPS
clock = pygame.time.Clock()

# Loop do jogo
running = True
while running:
    screen.fill(BLACK)  # Limpa a tela
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controles do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_width // 2, player_y])
    
    # Atualizar tiros
    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > 0]
    
    # Criar inimigos
    if random.randint(1, enemy_spawn_rate) == 1:
        enemies.append([random.randint(0, WIDTH - 20), 0])
    
    # Atualizar inimigos
    for enemy in enemies:
        enemy[1] += enemy_speed
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]
    
    # Colisões
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if enemy[0] < bullet[0] < enemy[0] + 20 and enemy[1] < bullet[1] < enemy[1] + 20:
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    
    # Desenhar jogador
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    
    # Desenhar tiros
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], 5, 10))
    
    # Desenhar inimigos
    for enemy in enemies:
        pygame.draw.circle(screen, RED, (enemy[0] + 10, enemy[1] + 10), 10)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
