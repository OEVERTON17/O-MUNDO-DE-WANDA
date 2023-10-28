import pygame
import sys

def animacao_personagem():
    global jogador_index
    jogador_index += 0.11
    if jogador_index > len(jogador_parado_superficies) - 1:
        jogador_index = 0
    
    janela.blit(jogador_parado_superficies[int(jogador_index)], jogador_retangulo)

def animacao_npc():
    global npc_index
    npc_index += 0.11
    if npc_index > len(npc_parado_superficies) - 1:
        npc_index = 0
        
        janela.blit(npc_parado_superficies[int(npc_index)], npc_retangulo)

    
# Inicializa o Pygame
pygame.init()

# Defina as dimensões da janela
largura = 1530
altura = 800

# Inicialize a janela
janela = pygame.display.set_mode((1530, 800))
pygame.display.set_caption("O MUNDO DE WANDA")

# Carrega a imagem de fundo
fundo_imagem = pygame.image.load("WANDA/Plano_De_Fundo/Game_image1.png").convert()
fundo_imagem = pygame.transform.scale(fundo_imagem, (1530, 800))
                                                                           
# Carrega as imagens do personagem
jogador_index = 0
jogador_parado_superficies = []
                                     
# Carrega as imagens do npc 

npc_index = 0 
npc_parado_superficies = []
                                     
 # Carrega a música
pygame.mixer.music.load('WANDA/MUSICA/SUMMER.mp3')
# play na musica
pygame.mixer_music.play()                                 
                                                             
# Carrega o Personagem parado                                            
for imagem in range(1, 7):
    img = pygame.image.load(f'WANDA/Samurai/PARADO/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (300, 300))
    jogador_parado_superficies.append(img)

# Carrega o NPC parado
for imagem in range(1, 4):
    img = pygame.image.load(f'WANDA/NPC/PARADO/PARADO{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (300, 300))
    npc_parado_superficies.append(img)


# Velocidade do movimento do personagem
jogador_retangulo = pygame.Rect(50, 50, 50, 50)
movimento_personagem = 5


# Posição inicial do NPC
npc_retangulo = pygame.Rect( 50, 50, 50, 50)





relogio = pygame.time.Clock()


# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
                               
                               
                               
    # Captura os eventos de tecla pressionada
    keys = pygame.key.get_pressed()
    jogador_retangulo.x += (keys[pygame.K_d] - keys[pygame.K_a]) * movimento_personagem
    jogador_retangulo.y += (keys[pygame.K_s] - keys[pygame.K_w]) * movimento_personagem
    
    
    if jogador_retangulo.y > 400:
        jogador_retangulo.y = 400;
    
    if jogador_retangulo.y < 60:
        jogador_retangulo.y = 60;
        
    if jogador_retangulo.x  > 1320:
        jogador_retangulo.x  = 1320;
    
    if   jogador_retangulo.x < 60:
        jogador_retangulo.x = 60;  
       

             
         
   
# Desenha a imagem de fundo na posição 
    janela.blit(fundo_imagem,(0, 0))
    
    animacao_personagem() 

# Atualiza a tela

    pygame.display.update()
    
        
    relogio.tick (60)
    
    
