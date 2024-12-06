import pygame
import sys

# Inicializando o pygame
pygame.init()

# Configurações da tela
LARGURA_TELA, ALTURA_TELA = 800, 600  # Define as dimensões da tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))  # Cria a janela do jogo
pygame.display.set_caption("Projétil Guiado com Classes")  # Define o título da janela

# Definição de cores (RGB)
BRANCO = (255, 255, 255)  # Cor de fundo
PRETO = (0, 0, 0)  # Cor do projétil
VERMELHO = (255, 0, 0)  # Cor do inimigo
AZUL = (0, 0, 255)  # Cor do herói

# Classe para o herói (controlado pelo jogador)
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        # Cria a superfície para representar o herói
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)  # Preenche com a cor do herói
        self.rect = self.image.get_rect()  # Obtém o retângulo da superfície
        self.rect.topleft = (x, y)  # Define a posição inicial
        self.velocidade = 5  # Define a velocidade do movimento

    def mover(self, x, y):
        """Move o herói na direção especificada."""
        self.rect.x += x  # Move no eixo X
        self.rect.y += y  # Move no eixo Y

    def disparar(self):
        """Cria e retorna um projétil disparado pelo herói."""
        return Projetil(self.rect.right, self.rect.centery - 5, 10, 10, PRETO)

# Classe para o inimigo (movimenta-se em direção ao herói)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor, velocidade):
        super().__init__()
        # Cria a superfície para representar o inimigo
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)  # Preenche com a cor do inimigo
        self.rect = self.image.get_rect()  # Obtém o retângulo da superfície
        self.rect.topleft = (x, y)  # Define a posição inicial
        self.velocidade = velocidade  # Define a velocidade do movimento

    def atualizar(self, alvo):
        """Move o inimigo em direção ao herói."""
        if self.rect.centery < alvo.rect.centery:  # Move para baixo se estiver acima do herói
            self.rect.y += self.velocidade
        elif self.rect.centery > alvo.rect.centery:  # Move para cima se estiver abaixo do herói
            self.rect.y -= self.velocidade

        if self.rect.left < alvo.rect.left:  # Move para a direita se estiver à esquerda do herói
            self.rect.x += self.velocidade
        elif self.rect.left > alvo.rect.left:  # Move para a esquerda se estiver à direita do herói
            self.rect.x -= self.velocidade

    def colisao_heroi(self, heroi):
        """Verifica se o inimigo colidiu com o herói."""
        return self.rect.colliderect(heroi.rect)  # Retorna True se houver colisão

# Classe para o projétil
class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        # Cria a superfície para representar o projétil
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)  # Preenche com a cor do projétil
        self.rect = self.image.get_rect()  # Obtém o retângulo da superfície
        self.rect.topleft = (x, y)  # Define a posição inicial

    def atualizar(self, alvo):
        """Atualiza a posição do projétil e ajusta sua trajetória para o alvo."""
        self.rect.x += 5  # Move o projétil para a direita
        if self.rect.centery < alvo.rect.centery:  # Ajusta para cima se o projétil estiver abaixo do alvo
            self.rect.y += 2
        elif self.rect.centery > alvo.rect.centery:  # Ajusta para baixo se o projétil estiver acima do alvo
            self.rect.y -= 2

        if self.rect.left > LARGURA_TELA:  # Remove o projétil se sair da tela
            self.kill()

# Função para exibir mensagens na tela (vitória ou derrota)
def exibir_mensagem(msg):
    # Define a fonte e cria o texto
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render(msg, True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
    tela.fill(BRANCO)  # Limpa a tela
    tela.blit(texto, texto_rect)  # Exibe o texto
    pygame.display.flip()

    # Aguarda até que o usuário clique para fechar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

# Instancia o herói e o inimigo
heroi = Hero(50, ALTURA_TELA // 2 - 50, 50, 100, AZUL)  # Define o herói
inimigo = Enemy(LARGURA_TELA - 100, ALTURA_TELA // 2 - 50, 50, 100, VERMELHO, 1)  # Define o inimigo

# Grupos de sprites (para facilitar a atualização e renderização)
grupo_sprites = pygame.sprite.Group()
grupo_sprites.add(heroi)  # Adiciona o herói ao grupo
grupo_sprites.add(inimigo)  # Adiciona o inimigo ao grupo

grupo_projeteis = pygame.sprite.Group()  # Grupo separado para os projéteis

# Relógio para controlar os frames por segundo (FPS)
relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    # Processa eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Fecha o jogo se o usuário clicar no "X"
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:  # Detecta teclas pressionadas
            if evento.key == pygame.K_SPACE:  # Dispara um projétil ao pressionar espaço
                projetil = heroi.disparar()
                grupo_projeteis.add(projetil)
                grupo_sprites.add(projetil)

    # Movimenta o herói com as setas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Move para a esquerda
        heroi.mover(-heroi.velocidade, 0)
    if keys[pygame.K_RIGHT]:  # Move para a direita
        heroi.mover(heroi.velocidade, 0)
    if keys[pygame.K_UP]:  # Move para cima
        heroi.mover(0, -heroi.velocidade)
    if keys[pygame.K_DOWN]:  # Move para baixo
        heroi.mover(0, heroi.velocidade)

    # Atualiza o estado do inimigo para seguir o herói
    inimigo.atualizar(heroi)

    # Verifica colisões entre projéteis e o inimigo
    for projetil in grupo_projeteis:
        projetil.atualizar(inimigo)
        if pygame.sprite.collide_rect(projetil, inimigo):  # Colisão com projétil
            projetil.kill()
            inimigo.kill()
            exibir_mensagem("You Win!")  # Exibe mensagem de vitória
            pygame.quit()
            sys.exit()

    # Verifica se o inimigo colidiu com o herói
    if inimigo.colisao_heroi(heroi):
        exibir_mensagem("You Lose!")  # Exibe mensagem de derrota
        pygame.quit()
        sys.exit()

    # Atualiza a tela
    tela.fill(BRANCO)  # Preenche a tela com a cor de fundo
    grupo_sprites.draw(tela)  # Desenha todos os sprites na tela

    pygame.display.flip()  # Atualiza o display
    relogio.tick(60)  # Mantém a taxa de atualização em 60 FPS