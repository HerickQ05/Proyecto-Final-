import pygame
from pygame.locals import *

# Constantes para inicializar la superficie del dibujo
Ventana_horizontal = 1000
Ventana_vertical = 600
BLANCO = (255, 255, 255)  # Color blanco
NEGRO = (0, 0, 0)  # Color negro
ROJO = (255, 0, 0)  # Color rojo
AZUL = (0, 0, 255)  # Color azul
AMARILLO = (255, 255, 0)  # Color amarillo
FPS = 60  # Fotogramas por segundo

# Definimos las palas
PALA_ANCHO = 15
PALA_ALTO = 100

# Definimos la pelota
PELOTA_RADIO = 10

def main():
    # Inicialización de pygame
    pygame.init()

    # Inicialización de la superficie de dibujo
    ventana = pygame.display.set_mode((Ventana_horizontal, Ventana_vertical))
    pygame.display.set_caption("Pong 1")

    # Crear un objeto Clock para controlar la tasa de fotogramas
    clock = pygame.time.Clock()

    # Inicializar las posiciones de las palas
    pala_izquierda = pygame.Rect(30, (Ventana_vertical - PALA_ALTO) // 2, PALA_ANCHO, PALA_ALTO)
    pala_derecha = pygame.Rect(Ventana_horizontal - 30 - PALA_ANCHO, (Ventana_vertical - PALA_ALTO) // 2, PALA_ANCHO, PALA_ALTO)

    # Inicializar la pelota
    pelota = pygame.Rect(Ventana_horizontal // 2 - PELOTA_RADIO, Ventana_vertical // 2 - PELOTA_RADIO, PELOTA_RADIO * 2, PELOTA_RADIO * 2)
    pelota_velocidad_x = 7
    pelota_velocidad_y = 7

    # Inicializar las puntuaciones
    puntuacion_izquierda = 0
    puntuacion_derecha = 0

    # Bucle principal
    jugando = True
    while jugando:
        # Rellenar la ventana con color negro
        ventana.fill(AZUL)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        # Movimiento de las palas
        teclas = pygame.key.get_pressed()
        
        # Movimiento de la pala izquierda (Jugador 1)
        if teclas[K_w] and pala_izquierda.top > 0:
            pala_izquierda.y -= 10
        if teclas[K_s] and pala_izquierda.bottom < Ventana_vertical:
            pala_izquierda.y += 10

        # Movimiento de la pala derecha (Jugador 2)
        if teclas[K_UP] and pala_derecha.top > 0:
            pala_derecha.y -= 10
        if teclas[K_DOWN] and pala_derecha.bottom < Ventana_vertical:
            pala_derecha.y += 10

        # Movimiento de la pelota
        pelota.x += pelota_velocidad_x
        pelota.y += pelota_velocidad_y

        # Rebote de la pelota en las paredes
        if pelota.top <= 0 or pelota.bottom >= Ventana_vertical:
            pelota_velocidad_y = -pelota_velocidad_y

        # Rebote de la pelota en las palas
        if pelota.colliderect(pala_izquierda) or pelota.colliderect(pala_derecha):
            pelota_velocidad_x = -pelota_velocidad_x

        # Puntuación cuando la pelota sale por los lados
        if pelota.left <= 0:
            puntuacion_derecha += 1
            pelota.x = Ventana_horizontal // 2 - PELOTA_RADIO
            pelota.y = Ventana_vertical // 2 - PELOTA_RADIO
            pelota_velocidad_x = -pelota_velocidad_x

        if pelota.right >= Ventana_horizontal:
            puntuacion_izquierda += 1
            pelota.x = Ventana_horizontal // 2 - PELOTA_RADIO
            pelota.y = Ventana_vertical // 2 - PELOTA_RADIO
            pelota_velocidad_x = -pelota_velocidad_x

        # Dibujar elementos en la ventana
        pygame.draw.rect(ventana, ROJO, pala_izquierda)  # Palas rojas
        pygame.draw.rect(ventana, ROJO, pala_derecha)
        pygame.draw.ellipse(ventana, BLANCO, pelota)

        # Dibujar la línea blanca central
        pygame.draw.line(ventana, BLANCO, (Ventana_horizontal // 2, 0), (Ventana_horizontal // 2, Ventana_vertical), 5)

        # Dibujar el cuadro negro detrás del puntaje
        cuadro_puntaje = pygame.Rect(Ventana_horizontal // 2 - 100, 5, 200, 40)
        pygame.draw.rect(ventana, NEGRO, cuadro_puntaje)

        # Mostrar la puntuación con letras amarillas
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"{puntuacion_izquierda} - {puntuacion_derecha}", True, AMARILLO)
        ventana.blit(texto_puntuacion, (cuadro_puntaje.centerx - texto_puntuacion.get_width() // 2, cuadro_puntaje.y + 5))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la tasa de fotogramas por segundo
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
