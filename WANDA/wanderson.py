import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Defina as dimensões da janela
largura = 800
altura = 600

# Carrega o personagem 
personagem_superficies = []
personagem_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'WANDA/Samurai/PARADO{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    personagem_superficies.append(img)

# Classe do jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(branco)
        self.rect = self.image.get_rect()
        self.rect.center = (largura // 2, altura // 2)

    def update(self):
        # Atualiza a lógica do jogador aqui
        pass

# Cria a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("O mundo de wanda")

# Cria o jogador
jogador = Jogador()

# Cria um grupo para todos os sprites e adiciona o jogador ao grupo
todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza todos os sprites
    todos_sprites.update()

    # Preenche o fundo com a cor preta
    janela.fill(preto)

    # Desenha todos os sprites na tela
    todos_sprites.draw(janela)

    # Atualiza a tela
    pygame.display.flip()

    
    



