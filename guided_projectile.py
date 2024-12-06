import pygame
import sys

# Inicializando o pygame
pygame.init()

# Configurações da tela
LARGURA_TELA, ALTURA_TELA = 800, 600  # Largura e altura da janela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))  # Cria a tela do jogo
pygame.display.set_caption("Projétil Guiado com Classes")  # Define o título da janela

# Definição de cores (RGB)
BRANCO = (255, 255, 255)  # Cor de fundo da tela
PRETO = (0, 0, 0)  # Cor do projétil
VERMELHO = (255, 0, 0)  # Cor do inimigo
AZUL = (0, 0, 255)  # Cor do herói

# Classe para o herói (retângulo que dispara projéteis)
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        """
        Inicializa o herói.
        :param x: Posição inicial no eixo X.
        :param y: Posição inicial no eixo Y.
        :param largura: Largura do retângulo.
        :param altura: Altura do retângulo.
        :param cor: Cor do retângulo.
        """
        super().__init__()
        self.image = pygame.Surface((largura, altura))  # Cria uma superfície para representar o herói
        self.image.fill(cor)  # Preenche a superfície com a cor do herói
        self.rect = self.image.get_rect()  # Obtém o retângulo associado à superfície
        self.rect.topleft = (x, y)  # Define a posição inicial do herói

    def disparar(self):
        """
        Cria e retorna um projétil disparado pelo herói.
        :return: Instância da classe Projetil.
        """
        return Projetil(self.rect.right, self.rect.centery - 5, 10, 10, PRETO)

# Classe para o inimigo (retângulo que se move e é alvo dos projéteis)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor, velocidade):
        """
        Inicializa o inimigo.
        :param x: Posição inicial no eixo X.
        :param y: Posição inicial no eixo Y.
        :param largura: Largura do retângulo.
        :param altura: Altura do retângulo.
        :param cor: Cor do retângulo.
        :param velocidade: Velocidade de movimento vertical.
        """
        super().__init__()
        self.image = pygame.Surface((largura, altura))  # Cria uma superfície para representar o inimigo
        self.image.fill(cor)  # Preenche a superfície com a cor do inimigo
        self.rect = self.image.get_rect()  # Obtém o retângulo associado à superfície
        self.rect.topleft = (x, y)  # Define a posição inicial do inimigo
        self.velocidade = velocidade  # Define a velocidade de movimento

    def atualizar(self):
        """
        Move o inimigo para cima e para baixo na tela.
        Inverte a direção ao colidir com os limites superior ou inferior da tela.
        """
        self.rect.y += self.velocidade
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.velocidade = -self.velocidade  # Inverte a direção do movimento

# Classe para o projétil
class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        """
        Inicializa o projétil.
        :param x: Posição inicial no eixo X.
        :param y: Posição inicial no eixo Y.
        :param largura: Largura do projétil.
        :param altura: Altura do projétil.
        :param cor: Cor do projétil.
        """
        super().__init__()
        self.image = pygame.Surface((largura, altura))  # Cria uma superfície para representar o projétil
        self.image.fill(cor)  # Preenche a superfície com a cor do projétil
        self.rect = self.image.get_rect()  # Obtém o retângulo associado à superfície
        self.rect.topleft = (x, y)  # Define a posição inicial do projétil

    def atualizar(self, alvo):
        """
        Atualiza a posição do projétil e ajusta a trajetória para o alvo.
        :param alvo: Instância da classe Enemy, alvo do projétil.
        """
        self.rect.x += 5  # Move o projétil para a direita
        if self.rect.centery < alvo.rect.centery:  # Ajusta a posição vertical para seguir o alvo
            self.rect.y += 2
        elif self.rect.centery > alvo.rect.centery:
            self.rect.y -= 2

        if self.rect.left > LARGURA_TELA:  # Remove o projétil se sair da tela
            self.kill()

# Instanciando os objetos
heroi = Hero(50, ALTURA_TELA // 2 - 50, 50, 100, AZUL)  # Cria o herói
inimigo = Enemy(LARGURA_TELA - 100, ALTURA_TELA // 2 - 50, 50, 100, VERMELHO, 5)  # Cria o inimigo

# Grupos de sprites
grupo_sprites = pygame.sprite.Group()  # Grupo que contém todos os sprites
grupo_sprites.add(heroi)
grupo_sprites.add(inimigo)

grupo_projeteis = pygame.sprite.Group()  # Grupo específico para projéteis

# Relógio para controle do FPS
relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():  # Processa os eventos
        if evento.type == pygame.QUIT:  # Se o jogador fechar a janela
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:  # Verifica teclas pressionadas
            if evento.key == pygame.K_SPACE:  # Dispara um projétil ao pressionar espaço
                projetil = heroi.disparar()
                grupo_projeteis.add(projetil)  # Adiciona o projétil ao grupo
                grupo_sprites.add(projetil)  # Adiciona ao grupo geral de sprites

    # Atualiza o estado do inimigo
    inimigo.atualizar()

    # Atualiza o estado dos projéteis
    for projetil in grupo_projeteis:
        projetil.atualizar(inimigo)
        if pygame.sprite.collide_rect(projetil, inimigo):  # Detecta colisão entre projétil e inimigo
            projetil.kill()  # Remove o projétil
            inimigo.kill()  # Remove o inimigo ao ser atingido

    # Atualiza a tela
    tela.fill(BRANCO)  # Preenche a tela com a cor de fundo
    grupo_sprites.draw(tela)  # Desenha todos os sprites na tela

    pygame.display.flip()  # Atualiza a exibição da tela
    relogio.tick(60)  # Mantém a taxa de quadros em 60 FPS