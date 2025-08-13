import pygame

bota_velocidade = pygame.image.load("assets/imagens/pitu.png")
braco_forca = pygame.image.load("assets/imagens/laursa.png")
arco_distancia = pygame.image.load("assets/imagens/oculos.png")
COLETAVEIS = {"velocidade": bota_velocidade, "força": braco_forca, "distancia": arco_distancia}

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, nome):
        super().__init__()
        self.nome = nome
        self.image = imagem
        self.rect = self.image.get_rect(center=(x, y))

        self.sheets = {
            "velocidade": ("assets/imagens/sheet_pitu.png", 23),
            "força": ("assets/imagens/sheet_laursa.png", 11),
            "distancia": ("assets/imagens/sheet_oculos.png", 12)
        }
        sheet_path, self.num_frames = self.sheets.get(nome, (None, 1))
        self.animacao = self.load(sheet_path, self.num_frames)
        self.pos_animacao = 0
        self.tempo_animacao = pygame.time.get_ticks()
        self.frame_delay = 80  # ms entre frames

    def load(self, path, tamanho):
        sprite_sheet = pygame.image.load(path).convert_alpha()
        size = sprite_sheet.get_height()  # Assume frame quadrado
        animation_list = []
        for x in range(tamanho):
            temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
            animation_list.append(temp_img)
        return animation_list

    def animar(self):
        self.image = self.animacao[self.pos_animacao]
        self.tempo_animacao = pygame.time.get_ticks()
        self.pos_animacao += 1
        if self.pos_animacao >= len(self.animacao):
            self.pos_animacao = 0

    def update(self):
        if pygame.time.get_ticks() - self.tempo_animacao > self.frame_delay:
            self.animar()