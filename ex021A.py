import pygame

def tocar_mp3(arquivo_mp3):
    """Toca um arquivo MP3 usando o Pygame.

    Args:
        'ex021.mp3' (str): Caminho completo para o arquivo MP3.
    """

    pygame.mixer.init()
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    arquivo = "D:\_CURSOS e ESTUDOS\PHYTON\PYTHON PASTA PYCHARM\PythonExercicios\ex021.mp3"  # Substitua pelo caminho do seu arquivo
    tocar_mp3(arquivo)
