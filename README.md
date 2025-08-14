
# 🎮 | Chico Science's Crab Defense
Projeto realizado para a disciplina de Introdução a Programação da Universidade Federal de Pernambuco
Alunos: João Guilherme Lemos Duarte de Oliveira (jgldo), Arthur Sean Cerqueira Campos (ascc2), Isabela Possídio Amorim (ipa), Arthur Fidney da Cunha Cavalcante Correia (afccc), Diogo Cavalcanti Carneiro de Albuquerque (dcca), Felipe Andrade Leite Santos (fals2)
<br>Relatório Técnico — Arquitetura do Jogo “Chico Science's Mangue Defense”

### ❗​| 0. Como Rodar

Baixe o Python 3.x
<br>Instale o Pygame com o comando: pip install pygame
<br>Use git clone https://github.com/arthursean/projeto-ip.git ou baixe o .zip pelo github
<br>execute o main.py
### 👀 | 1. Visão Geral
   
O projeto implementa um jogo no estilo Tower Defense, desafiando jogadores a administrar seus recursos e enfrentar hordas de inimigos. Inspirado no movimento manguebeat, liderado pelo ilustre cantor e compositor Chico Science, o jogo apresenta caranguejos, determinados a defender seu lar, protegem um mangue, ameaçado por sacolas, sacos e latas de lixo. Ao destruí-los, conseguem obter três tipos de upgrades, sendo eles latas de pitu, óculos escuros e cabeças de La Ursa que podem melhorar sua velocidade, alcance e força, respectivamente. Ele é construído em Python com a biblioteca Pygame utilizando uma arquitetura modular que separa os elementos centrais do jogo (torres, inimigos, botões, constantes, coletáveis) em arquivos independentes

### 📋 | 2. Arquitetura e Organização
   
O projeto segue uma arquitetura modular e orientada a objetos em partes específicas, separando responsabilidades por arquivos:

| Arquivo / Módulo| Função no Projeto|
| --- | ---|
| main.py (código principal)  | Loop principal do jogo, controle de estados, inicialização e renderização geral. |
| torre.py  | Define a classe Torre, responsável pelas torres que atacam inimigos, com atributos como posição, alcance e upgrades.  |
| enemies.py  | 	Contém as classes dos inimigos (rapido, tank, supertank) com métodos de movimentação, vida e dano.  |
| button.py  | Implementa um sistema de botões clicáveis (Button), utilizado na HUD e menus. |
| constantes.py  | 	Armazena valores fixos como dimensões de tela, caminhos de imagem, preços, velocidade de jogo e layout do mapa. |
| coletaveis.py | Define o dicionário COLETAVEIS com imagens e nomes dos coletáveis, além da classe Coletavel para spawn e interação.  |
 --------

Essa organização permite alta coesão e baixo acoplamento, facilitando manutenção e adição de novas funcionalidades.
### 📂 | 3. Estrutura Lógica do Jogo
O fluxo do jogo é controlado pelo loop principal e por um sistema de estados (state), que definem a tela e a lógica em execução:

-> title_screen → Tela inicial com botão de iniciar.

-> game_screen → Lógica principal do jogo: posicionamento de torres, movimentação de inimigos, coleta de itens e controle de ondas.

-> paused → Pausa do jogo, mantendo o estado da tela.

-> end_screen → Tela de vitória ou derrota.

### 📚 | 4. Bibliotecas e Ferramentas Utilizadas
Python: Linguagem principal por sua simplicidade, flexibilidade e ampla comunidade de desenvolvimento de jogos com Pygame.

Pygame: Biblioteca robusta para desenvolvimento de jogos 2D em Python, com suporte a gráficos, áudio, eventos de entrada e controle de tempo.

      pygame.display → Criação e manipulação da janela do jogo.
      
      pygame.image → Carregamento e escalonamento de sprites e texturas.
      
      pygame.mixer → Reprodução de áudio e música.
      
      pygame.sprite.Group → Organização e atualização de múltiplos objetos.
      
      pygame.event → Captura de eventos como cliques e fechamento da janela.
      
      pygame.font → Renderização de textos na tela.   
      
      pygame.time.Clock → Controle da taxa de atualização (FPS).
  
Random: Necessário para a geração aleatória de coletáveis, adicionando imprevisibilidade e rejogabilidade ao jogo.
<br>Piskel e Pixilart: Usado para a criação e adaptação dos sprites utilizados.

### 📝 | 5. Justificativa da Arquitetura

Separação de Módulos: Facilita a manutenção, permitindo que cada componente (torres, inimigos, botões) seja desenvolvido e testado isoladamente.

Uso de Pygame: Fornece todos os recursos essenciais para jogos 2D sem necessidade de dependências pesadas.

Sistema de Estados: Garante controle claro sobre as fases do jogo e previne execução de lógicas erradas em telas inativas.

Sprites e Groups: Permitem atualização e renderização eficientes de múltiplos objetos, melhorando performance e clareza do código.

### 💻 | 6. Divisão de trabalho

Diogo Albuquerque - Upgrades, Apresentação

Felipe Andrade - Interface, Música, Coletáveis, Apresentação

João Guilherme - Inimigos, Animação, Sprites

Isabela Possídio - Hud, botões, constantes, compra e venda

Arthur Sean - Torres, correção de bugs, balanceamento

Arthur Fidney -  Mapa, path dos inimigos, sistema de vida

**Comandos condicionais**

    Usados em praticamente todo o código para tomar decisões.
    
    Ex.:
    
    if grid_x > c.mapWidth - 2: (na função create_tower) para verificar se a posição está fora dos limites.
    
    if placing_torres: (no loop principal) para exibir a torre no cursor apenas quando o jogador estiver posicionando torres.
    
    if vida <= 0: e elif(len(remaining_times)==0 and not cur_enemies): (no loop principal) para decidir vitória ou derrota.

**Laços de repetição**

    Usados para percorrer elementos repetidamente.
    
    for t in torretas: (na função sel_torres) para verificar qual torre foi clicada.
    
    for event in pygame.event.get(): (no loop principal) para processar eventos do jogo.
    
    for enemy in cur_enemies: (no loop principal) para atualizar e desenhar inimigos.

**Listas**

    Usadas para armazenar coleções ordenadas de elementos.
    
    remaining_waves = timeline e remaining_times = list(cur_wave.keys()) para controlar a ordem de spawn dos inimigos.
    
    cur_enemies = [] para manter todos os inimigos ativos.
    
    list(COLETAVEIS.keys()) para sortear o nome do coletável.

**Funções**

    Criadas para organizar e reutilizar código.
    
    create_tower(x, y, money) cria e posiciona uma torre.
    
    sel_torres(x, y, torre_marcada) seleciona uma torre clicada pelo jogador.

**Tuplas e Dicionários**

    Tuplas: usadas para coordenadas (grid_x, grid_y) e para posições de desenho, ex.: torre.Torre((grid_x, grid_y)).

    Dicionários:
    
    COLETAVEIS (importado) para associar nome de coletável à sua imagem.
    
    cur_wave e timeline para mapear momentos (frames) a listas de inimigos que vão aparecer.

### 🔍 | 7. Desafios, erros e lições aprendidas

-**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**

O maior erro do projeto ocorreu quando, ao invés de passar os dados da animação para a main, um integrante acabou fazendo o merge no sentido contrário, passando os dados da main para a animação. Isso foi resolvido revertendo o merge com o comando git revert -m, o que levou algum tempo até entendermos o problema e aplicarmos a solução correta. Apesar do contratempo, o processo nos ajudou a compreender melhor o funcionamento do Git e a importância de atenção ao realizar merges.

-**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**

O maior desafio do projeto foi equilibrar a dificuldade do jogo, ajustando as porcentagens de drop de upgrades, o ganho de moedas, o preço do caranguejo e a quantidade de inimigos. Foi necessário testar diversas combinações, analisar o impacto de cada ajuste e jogar repetidas vezes para encontrar um ponto ideal: desafiador, mas possível de vencer. Com paciência e trabalho em equipe, conseguimos chegar a um equilíbrio que deixou a experiência divertida e justa.

-**Quais as lições aprendidas durante o projeto?**

Durante o projeto, aprendemos a importância de planejamento, comunicação e testes constantes. Percebemos que pequenos erros de atenção, como no uso de comandos do Git, podem gerar retrabalho, e que trabalhar em equipe exige organização para evitar conflitos no código. Também desenvolvemos habilidades técnicas, como equilibrar mecânicas de jogo e ajustar parâmetros para criar uma experiência divertida e desafiadora. No final, entendemos que a colaboração e a persistência são essenciais para transformar ideias em um produto funcional.

### 📷 | 8. Capturas de tela
<img width="2367" height="1392" alt="image" src="https://github.com/user-attachments/assets/3a27a69a-24f3-4b16-9146-08d9df36c8a3" />
<img width="1472" height="877" alt="image" src="https://github.com/user-attachments/assets/54503a1d-61f0-4ff0-a368-f4d74bc68574" />
<img width="1476" height="879" alt="image" src="https://github.com/user-attachments/assets/ffa29268-b2ef-4e81-bfc8-5b23c5ae4c6a" />
<img width="2365" height="1396" alt="image" src="https://github.com/user-attachments/assets/9cd90006-4246-46e6-878e-8e2a2ac88f9e" />
<img width="2354" height="1413" alt="image" src="https://github.com/user-attachments/assets/bbea2174-0232-456e-b209-a3ec5ed5b7eb" />




