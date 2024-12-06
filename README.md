# 🎮 Projétil Guiado com Pygame

Este repositório contém dois projetos desenvolvidos em Python, utilizando a biblioteca Pygame, para demonstrar como criar sistemas de jogo interativos com:

- **Herói**: Um retângulo que pode disparar projéteis.
- **Inimigo**: Um retângulo móvel que é o alvo dos projéteis.
- **Projétil guiado**: Os projéteis ajustam sua trajetória para acertar o inimigo.

## 🚀 Como funciona o jogo?
1. **Projeto 1:**
   - O jogador controla um herói (retângulo azul) fixo na lateral esquerda da tela.
   - O herói dispara projéteis (ao pressionar espaço) que seguem em direção ao inimigo (retângulo vermelho).
   - O inimigo se move automaticamente para cima e para baixo na lateral direita da tela.
   - Quando um projétil colide com o inimigo, ambos são removidos da tela.

2. **Projeto 2:**
   - O jogador controla um herói móvel (retângulo azul) usando as setas do teclado.
   - O inimigo (retângulo vermelho) se movimenta em direção ao herói.
   - O jogo termina se o inimigo colidir com o herói ou se o jogador acertar o inimigo com um projétil.

## 📂 Estrutura do código
### Classes principais
- **Hero (Herói):**
  - Representa o personagem que dispara projéteis.
  - Contém o método `disparar()` para criar novos projéteis.
  - No Projeto 2, inclui movimentos controlados pelo teclado.

- **Enemy (Inimigo):**
  - Representa o alvo móvel.
  - Contém o método `atualizar()` para realizar o movimento.

- **Projetil (Projétil):**
  - Representa os projéteis disparados pelo herói.
  - Ajusta sua trajetória para seguir o inimigo.
  - Remove-se da tela caso:
    - Saia dos limites.
    - Colida com o inimigo.

### Grupos de sprites
- `grupo_sprites`: Armazena todos os objetos visuais do jogo (herói, inimigo, projéteis).
- `grupo_projeteis`: Armazena apenas os projéteis para facilitar manipulação e colisões.

### Ciclo principal
1. **Eventos:**
   - Detecta o encerramento da janela.
   - Captura a tecla **espaço** para disparar projéteis.
   - No Projeto 2, captura as teclas direcionais para movimentar o herói.

2. **Atualizações:**
   - Move o inimigo.
   - Move os projéteis e verifica colisões.

3. **Renderização:**
   - Limpa a tela.
   - Desenha os objetos visuais.
   - Atualiza a exibição.

## 🛠️ Pré-requisitos
- Python 3.8+ (ou versão mais recente).
- Pygame: Para instalar, execute o comando:
  ```bash
  pip install pygame
  ```

## ▶️ Como executar o jogo?
1. Baixe o código ou clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/projetil-guiado.git
   cd projetil-guiado
   ```
2. Execute os scripts:
   - Para o Projeto 1: `python projetil_guiado_1.py`
   - Para o Projeto 2: `python projetil_guiado_2.py`

## 🔧 Personalizações
- **Velocidade do inimigo**: Ajuste o parâmetro `velocidade` na criação do objeto `Enemy`.
- **Trajetória do projétil**: Modifique o método `atualizar()` da classe `Projetil`.
- **Formas ou imagens**: Substitua as superfícies padrão (`pygame.Surface`) por imagens carregadas com `pygame.image.load()`.

## 🚀 Próximos passos
- Implementar pontuação para contabilizar acertos.
- Adicionar múltiplos inimigos e projéteis simultâneos.
- Incluir diferentes níveis de dificuldade.

## 📝 Licença
Este projeto está licenciado sob a [Creative Commons](https://creativecommons.org/licenses/). Consulte o arquivo `LICENSE` para mais detalhes.

---

Se tiver dúvidas ou sugestões, entre em contato. Divirta-se programando! 🚀
