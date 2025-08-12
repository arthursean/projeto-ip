import pygame
bota_velocidade = pygame.image.load("imagens/pitu.png")
braco_forca = pygame.image.load("imagens/laursa.png")
arco_distancia = pygame.image.load("imagens/oculos.png")
COLETAVEIS = {"velocidade": bota_velocidade, "força":braco_forca, "distancia": arco_distancia}

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, nome):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect(center=(x, y))
        self.nome = nome  # Armazena o nome do coletável
    def update(self):
        pass