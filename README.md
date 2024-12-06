# Projétil Guiado com Pygame

Este é um projeto simples desenvolvido em **Python**, utilizando a biblioteca **Pygame**, para demonstrar como criar um sistema de jogo com:
- **Herói**: Um retângulo que pode disparar projéteis.
- **Inimigo**: Um retângulo móvel que é o alvo dos projéteis.
- **Projétil guiado**: Os projéteis ajustam sua trajetória para acertar o inimigo.

## 🎮 Como funciona o jogo?
- O jogador controla um **herói** (retângulo azul) fixo na lateral esquerda da tela.
- O **herói** dispara projéteis (ao pressionar **espaço**) que seguem em direção ao **inimigo** (retângulo vermelho).
- O **inimigo** se move automaticamente para cima e para baixo na lateral direita da tela.
- Quando um **projétil** colide com o **inimigo**, ambos são removidos da tela.

---

## 📂 Estrutura do código

### Classes principais
1. **Hero (Herói)**:
   - Representa o personagem que dispara projéteis.
   - Contém o método `disparar()` para criar novos projéteis.
   
2. **Enemy (Inimigo)**:
   - Representa o alvo móvel.
   - Contém o método `atualizar()` para realizar o movimento vertical.

3. **Projetil (Projétil)**:
   - Representa os projéteis disparados pelo herói.
   - Ajusta sua trajetória para seguir o inimigo.
   - Remove-se da tela caso:
     - Saia dos limites da tela.
     - Colida com o inimigo.

### Grupos de sprites
- `grupo_sprites`: Armazena todos os objetos visuais do jogo (herói, inimigo, projéteis).
- `grupo_projeteis`: Armazena apenas os projéteis para facilitar a manipulação e detecção de colisões.

### Ciclo principal
1. **Eventos**:
   - Detecta o encerramento da janela ou o pressionamento da tecla **espaço** para disparar projéteis.
2. **Atualizações**:
   - Move o inimigo.
   - Move os projéteis e verifica colisões.
3. **Renderização**:
   - Limpa a tela.
   - Desenha todos os objetos na tela.
   - Atualiza a exibição.

---

## 🛠️ Pré-requisitos

1. **Python 3.8+** (ou versão mais recente).
2. **Pygame**:
   - Para instalar, execute:
     ```bash
     pip install pygame
     ```

---

## ▶️ Como executar o jogo?

1. **Baixe o código** ou clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/projetil-guiado.git
   cd projetil-guiado
   ```
2. **Execute o script**:
   ```bash
   python projetil_guiado.py
   ```

---

## 🔧 Personalizações

### Alterar o comportamento:
- **Velocidade do inimigo**: Ajuste o parâmetro `velocidade` na criação do objeto `Enemy`.
- **Trajetória do projétil**: Modifique o método `atualizar()` da classe `Projetil`.

### Substituir as formas:
- **Adicionar imagens**:
  Substitua as superfícies padrão (`pygame.Surface`) por imagens carregadas com `pygame.image.load()`.

---

## 🚀 Próximos passos

- Implementar pontuação para contabilizar acertos.
- Adicionar múltiplos inimigos e projéteis simultâneos.
- Incluir diferentes níveis de dificuldade.

---

## 📝 Licença

Este projeto é de uso livre para estudos e práticas. Caso deseje utilizar ou modificar para outros fins, sinta-se à vontade. 😊

---

Se tiver dúvidas ou sugestões, entre em contato. Divirta-se programando! 🚀
