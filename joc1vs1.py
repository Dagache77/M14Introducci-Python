import time
import pygame
from pygame.locals import *


AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/fonsjoc.png'
MUSICA_FONS = 'assets/PvZ.mp3'
WHITE = (255, 255, 255)
COR = 'assets/Cor.png'
EXPLOSIO = 'assets/explosió.png'


# Inicializar el contador de disparos y aciertos para ambos jugadores
disparos_jugador1 = 0
aciertos_jugador1 = 0
disparos_jugador2 = 0
aciertos_jugador2 = 0


# Load explosion image
explosion_image = pygame.image.load(EXPLOSIO)
# Load heart image
heart_image = pygame.image.load(COR)


# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 2
vides1 = 3
invulnerabilidad1 = False
temps_invulnerabilidad1 = 2
tiempo_desaparecido1 = 0


# Jugador 2:
player_image2 = pygame.image.load('assets/enemic.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 150))
velocitat_nau2 = 2
vides2 = 3
invulnerabilidad2 = False
temps_invulnerabilidad2 = 2
tiempo_desaparecido2 = 0


# Bala rectangular blanca:
bala_imatge = pygame.image.load('assets/bala.png')
bales_jugador1 = []
bales_jugador2 = []
velocitat_bales = 3
temps_entre_bales = 1000  # Decreased bullet cooldown time
temps_ultima_bala_jugador1 = 0
temps_ultima_bala_jugador2 = 0
temps_explosio = 500  # Duración de la explosión en milisegundos


pygame.init()


pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")


clock = pygame.time.Clock()
fps = 60


def imprimir_pantalla_fons(image, x, y):
   background = pygame.image.load(image).convert_alpha()
   pantalla.blit(background, (x, y))


def mostrar_texto(texto, tamano=20, color=WHITE, x=AMPLADA // 2, y=ALTURA // 2):
   font = pygame.font.SysFont(None, tamano)  # Cambiado None por 'Arial'
   texto_surface = font.render(texto, True, color)
   text_rect = texto_surface.get_rect(center=(x, y))
   pantalla.blit(texto_surface, text_rect)


def mostrar_tiempo(tiempo_restante, x, y):
   tiempo_formateado = "{:.2f}".format(tiempo_restante)  # Formatejar el tiemps amb dos decimals
   mostrar_texto("Time left: {}".format(tiempo_formateado), x=x, y=y)


# Tiempo límite de la partida
tiempo_limite = 300  # 5 minutos


# Tiempo inicial
tiempo_inicio = time.time()


# Variable para controlar el estado de pausa
pausa = False


def pausar_juego():
   global pausa
   pausa = not pausa


while True:
   current_time = pygame.time.get_ticks()


   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
       # Verificar si se presiona la tecla "Espacio" para pausar el juego
       if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           pausar_juego()


   keys = pygame.key.get_pressed()


   # Si el juego está en pausa, mostrar el texto y no actualizar el juego
   if pausa:
       mostrar_texto("PAUSE", tamano=40, x=AMPLADA // 2, y=ALTURA // 2)
       pygame.display.update()
       continue


   # Jugador 1 controls
   if keys[K_a]:
       player_rect.x = max(player_rect.x - velocitat_nau, 0)
   if keys[K_d]:
       player_rect.x = min(player_rect.x + velocitat_nau, AMPLADA - player_rect.width)
   # Disparo del jugador 1
   if keys[K_w] and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
       bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
       temps_ultima_bala_jugador1 = current_time
       disparos_jugador1 += 1


   # Jugador 2 controls
   if keys[K_LEFT]:
       player_rect2.x = max(player_rect2.x - velocitat_nau2, 0)
   if keys[K_RIGHT]:
       player_rect2.x = min(player_rect2.x + velocitat_nau2, AMPLADA - player_rect2.width)
   # Disparo del jugador 2
   if keys[K_UP] and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
       bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
       temps_ultima_bala_jugador2 = current_time
       disparos_jugador2 += 1


   imprimir_pantalla_fons(BACKGROUND_IMAGE, 0, 0)


   # Colisiones entre balas y jugadores
   for bala in bales_jugador1:
       if player_rect2.colliderect(bala):
           vides2 -= 1
           aciertos_jugador1 += 1
           bales_jugador1.remove(bala)
           # Mostrar explosión cuando un jugador pierde una vida
           pantalla.blit(explosion_image, player_rect2)
           pygame.display.update()
           pygame.time.delay(temps_explosio)  # Delay para mostrar la explosión
           break


   for bala in bales_jugador2:
       if player_rect.colliderect(bala):
           vides1 -= 1
           aciertos_jugador2 += 1
           bales_jugador2.remove(bala)
           # Mostrar explosión cuando un jugador pierde una vida
           pantalla.blit(explosion_image, player_rect)
           pygame.display.update()
           pygame.time.delay(temps_explosio)  # Delay para mostrar la explosión
           break


   # Verificar si algún jugador ha perdido todas sus vidas
   if vides1 <= 0 or vides2 <= 0 or (time.time() - tiempo_inicio) >= tiempo_limite:
       if vides1 <= 0:
           mostrar_texto("Player 2 wins", tamano=60, color=(255, 0, 0), x=165, y=70)
       elif vides2 <= 0:
           mostrar_texto("Player 1 wins", tamano=60, color=(255, 0, 0), x=165, y=70)
       elif (time.time() - tiempo_inicio) >= tiempo_limite:
           mostrar_texto("Time's up!", x=165, y=90)
       mostrar_texto("Press space to continue.", tamano=20, color=(255, 255, 255), x=165, y=130)
       mostrar_texto("Precisión jugador 1: {}%".format((aciertos_jugador1 / disparos_jugador1) * 100 if disparos_jugador1 > 0 else 0), tamano=17, color=WHITE, x=165, y=170)
       mostrar_texto("Precisión jugador 2: {}%".format((aciertos_jugador2 / disparos_jugador2) * 100 if disparos_jugador2 > 0 else 0), tamano=17, color=WHITE, x=165, y=185)
       pygame.display.update()
       while True:
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                   # Reiniciar el juego
                   disparos_jugador1 = 0
                   aciertos_jugador1 = 0
                   disparos_jugador2 = 0
                   aciertos_jugador2 = 0
                   vides1 = 3
                   vides2 = 3
                   player_rect.center = (AMPLADA // 2, ALTURA - 10)
                   player_rect2.center = (AMPLADA // 2, ALTURA - 150)
                   tiempo_inicio = time.time()
                   break
           else:
               continue
           break


   # Dibujar jugadores
   if tiempo_desaparecido1 <= 0:  # Si no está desaparecido
       pantalla.blit(player_image, player_rect)
   if tiempo_desaparecido2 <= 0:  # Si no está desaparecido
       pantalla.blit(player_image2, player_rect2)


   # Dibujar corazones para jugador 1
   for i in range(vides1):
       cor_x = AMPLADA - 20 - i * 20
       cor_y = ALTURA - 20
       pantalla.blit(heart_image, (cor_x, cor_y))
   # Dibujar corazones para jugador 2
   for i in range(vides2):
       cor_x = 10 + i * 20
       cor_y = 10
       pantalla.blit(heart_image, (cor_x, cor_y))


   # Mostrar el tiempo restante
   tiempo_transcurrido = time.time() - tiempo_inicio
   tiempo_restante = max(tiempo_limite - tiempo_transcurrido, 0)
   mostrar_tiempo(tiempo_restante, x=260, y=10)


   # Actualizar y dibujar balas
   for bala in bales_jugador1:
       bala.y -= velocitat_bales
       pantalla.blit(bala_imatge, bala)


   for bala in bales_jugador2:
       bala.y += velocitat_bales
       pantalla.blit(bala_imatge, bala)


   # Decrementar tiempo de desaparición
   tiempo_desaparecido1 = max(tiempo_desaparecido1 - 1 / fps, 0)
   tiempo_desaparecido2 = max(tiempo_desaparecido2 - 1 / fps, 0)


   pygame.display.update()
   clock.tick(fps)

