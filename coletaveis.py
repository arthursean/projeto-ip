import pygame
bota_velocidade = pygame.image.load("projeto-ip/Bota_velocidade.gif")
braco_forca = pygame.image.load("projeto-ip/forca_imagem.gif")
arco_distancia = pygame.image.load("projeto-ip/arco_e_flecha.gif")
COLETAVEIS = {"velocidade": bota_velocidade, "força":braco_forca, "distancia": arco_distancia}

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        pass