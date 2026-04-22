import pygame
import sys
import random
import math

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Constantes del juego
ANCHO = 800
ALTO = 600
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
DORADO = (255, 215, 0)
AZUL_CLARO = (135, 206, 235)
MARRON = (139, 69, 19)
GRIS = (128, 128, 128)
ROJO_MCD = (218, 41, 28)
AMARILLO_MCD = (255, 205, 0)
LABIO_AMARILLO = (255, 220, 50)

class Sonidos:
    def __init__(self):
        self.sonido_salto = None
        self.sonido_moneda = None
        self.sonido_golpe = None
        self.sonido_game_over = None
        self.crear_sonidos()
        
    def crear_sonidos(self):
        try:
            self.sonido_salto = self.generar_tono(880, 0.15)
            self.sonido_moneda = self.generar_tono(1046.50, 0.2)
            self.sonido_golpe = self.generar_tono(440, 0.1)
            self.sonido_game_over = self.generar_tono_descendente()
        except:
            print("No se pudieron generar sonidos")
    
    def generar_tono(self, frecuencia, duracion):
        try:
            import numpy as np
            sample_rate = 44100
            n_samples = int(sample_rate * duracion)
            t = np.linspace(0, n_samples / sample_rate, n_samples)
            onda = np.sin(2 * np.pi * frecuencia * t)
            envelope = np.exp(-3 * t)
            onda = onda * envelope
            onda = (onda * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(onda)
        except:
            return None
    
    def generar_tono_descendente(self):
        try:
            import numpy as np
            sample_rate = 44100
            duracion = 1.0
            n_samples = int(sample_rate * duracion)
            t = np.linspace(0, duracion, n_samples)
            frecuencia = 880 * np.exp(-5 * t)
            onda = np.sin(2 * np.pi * frecuencia * t)
            envelope = np.exp(-3 * t)
            onda = onda * envelope
            onda = (onda * 32767).astype(np.int16)
            return pygame.sndarray.make_sound(onda)
        except:
            return None
    
    def reproducir(self, sonido, volumen=0.5):
        if sonido is not None:
            sonido.set_volume(volumen)
            sonido.play()

class CajaTriste:
    def __init__(self, x, y, sonidos):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.ancho = 45
        self.alto = 45
        self.en_suelo = True
        self.vivo = True
        self.puntuacion = 0
        self.vidas = 3
        self.monedas = 0
        self.hamburguesas = 0
        self.moviendo_izquierda = False
        self.moviendo_derecha = False
        self.puede_saltar = True
        self.sonidos = sonidos
        self.sonido_activado = True
        
    def update(self, plataformas, enemigos, monedas):
        # Aplicar gravedad
        self.vel_y += 0.8
        if self.vel_y > 15:
            self.vel_y = 15
            
        # Movimiento horizontal
        self.x += self.vel_x
        
        # Colisiones con plataformas (horizontal)
        self.colision_plataformas(plataformas, True)
        
        # Movimiento vertical
        self.y += self.vel_y
        self.en_suelo = False
        
        # Colisiones con plataformas (vertical)
        self.colision_plataformas(plataformas, False)
        
        # Limitar bordes de pantalla
        if self.x < 0:
            self.x = 0
        if self.x > ANCHO - self.ancho:
            self.x = ANCHO - self.ancho
            
        # Colisiones con enemigos
        for enemigo in enemigos[:]:
            if self.colision(enemigo):
                if self.vel_y > 0 and self.y + self.alto - enemigo.y <= 30:
                    enemigos.remove(enemigo)
                    self.puntuacion += 100
                    self.hamburguesas += 1 if enemigo.tipo == "hamburguesa" else 0
                    self.vel_y = -10
                    if self.sonido_activado:
                        self.sonidos.reproducir(self.sonidos.sonido_golpe, 0.7)
                else:
                    self.morir()
        
        # Colisiones con monedas
        for moneda in monedas[:]:
            if self.colision(moneda):
                monedas.remove(moneda)
                self.monedas += 1
                self.puntuacion += 50
                if self.sonido_activado:
                    self.sonidos.reproducir(self.sonidos.sonido_moneda, 0.5)
                    
    def colision_plataformas(self, plataformas, es_horizontal):
        for plataforma in plataformas:
            if self.colision(plataforma):
                if es_horizontal:
                    if self.vel_x > 0:
                        self.x = plataforma.x - self.ancho
                    elif self.vel_x < 0:
                        self.x = plataforma.x + plataforma.ancho
                else:
                    if self.vel_y > 0:
                        self.y = plataforma.y - self.alto
                        self.vel_y = 0
                        self.en_suelo = True
                        self.puede_saltar = True
                    elif self.vel_y < 0:
                        self.y = plataforma.y + plataforma.alto
                        self.vel_y = 0
                        
    def colision(self, otro):
        return (self.x < otro.x + otro.ancho and
                self.x + self.ancho > otro.x and
                self.y < otro.y + otro.alto and
                self.y + self.alto > otro.y)
    
    def morir(self):
        self.vidas -= 1
        if self.vidas > 0:
            self.respawn()
        else:
            self.vivo = False
            if self.sonido_activado:
                self.sonidos.reproducir(self.sonidos.sonido_game_over, 0.8)
            
    def respawn(self):
        self.x = 100
        self.y = 500
        self.vel_x = 0
        self.vel_y = 0
        self.en_suelo = True
        self.puede_saltar = True
        
    def draw(self, pantalla):
        # Caja principal ROJA
        pygame.draw.rect(pantalla, ROJO_MCD, (self.x, self.y, self.ancho, self.alto))
        
        # OJOS BLANCOS
        pygame.draw.circle(pantalla, BLANCO, (self.x + 12, self.y + 12), 5)
        pygame.draw.circle(pantalla, BLANCO, (self.x + 33, self.y + 12), 5)
        pygame.draw.circle(pantalla, NEGRO, (self.x + 11, self.y + 11), 2)
        pygame.draw.circle(pantalla, NEGRO, (self.x + 32, self.y + 11), 2)
        
        # BOCA TRISTE (hacia ABAJO) - Labios amarillos
        pygame.draw.arc(pantalla, LABIO_AMARILLO, 
                       (self.x + 12, self.y + 18, 21, 12), 
                       math.radians(190), math.radians(350), 3)
        
    def manejar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                self.vel_x = -5
                self.moviendo_izquierda = True
            elif evento.key == pygame.K_RIGHT:
                self.vel_x = 5
                self.moviendo_derecha = True
            elif evento.key == pygame.K_SPACE and self.en_suelo and self.puede_saltar:
                self.vel_y = -14
                self.en_suelo = False
                self.puede_saltar = False
                if self.sonido_activado:
                    self.sonidos.reproducir(self.sonidos.sonido_salto, 0.6)
            elif evento.key == pygame.K_m:
                self.sonido_activado = not self.sonido_activado
                print(f"🔊 Sonido: {'ON' if self.sonido_activado else 'OFF'}")
                
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                self.vel_x = 0
                self.moviendo_izquierda = False
            elif evento.key == pygame.K_RIGHT:
                self.vel_x = 0
                self.moviendo_derecha = False

class Plataforma:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
    def draw(self, pantalla):
        pygame.draw.rect(pantalla, MARRON, (self.x, self.y, self.ancho, self.alto))
        pygame.draw.rect(pantalla, VERDE, (self.x, self.y - 5, self.ancho, 5))

class Moneda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.animacion = 0
        self.rotacion = 0
        
    def update(self):
        self.animacion += 0.1
        self.rotacion += 0.2
        
    def draw(self, pantalla):
        brillo = abs(int(100 * math.sin(self.animacion)))
        
        pygame.draw.ellipse(pantalla, (0, 0, 0, 50), 
                           (self.x + 2, self.y + 18, 16, 6))
        
        pygame.draw.circle(pantalla, (255, 215 - brillo//2, 0), 
                          (self.x + 10, self.y + 10), 10)
        pygame.draw.circle(pantalla, DORADO, 
                          (self.x + 10, self.y + 10), 8)
        pygame.draw.circle(pantalla, (255, 255, 100), 
                          (self.x + 10, self.y + 10), 5)
        
        angulo = self.rotacion
        for i in range(4):
            x_brillo = self.x + 10 + int(8 * math.cos(angulo + i * math.pi/2))
            y_brillo = self.y + 10 + int(8 * math.sin(angulo + i * math.pi/2))
            pygame.draw.circle(pantalla, (255, 255, 200), 
                             (x_brillo, y_brillo), 2)
        
        puntos = []
        for i in range(5):
            ang = math.radians(i * 72 - 90)
            x_punto = self.x + 10 + int(4 * math.cos(ang))
            y_punto = self.y + 10 + int(4 * math.sin(ang))
            puntos.append((x_punto, y_punto))
        pygame.draw.polygon(pantalla, (255, 200, 0), puntos, 1)
        
        fuente = pygame.font.Font(None, 15)
        texto = fuente.render("$", True, (255, 215, 0))
        pantalla.blit(texto, (self.x + 5, self.y + 5))

class Enemigo:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.ancho = 30
        self.alto = 30
        self.vel_x = 2
        self.direccion = 1
        self.tipo = tipo
        
    def update(self, plataformas):
        self.x += self.vel_x * self.direccion
        
        if self.x <= 50 or self.x >= ANCHO - 80:
            self.direccion *= -1
            
    def draw(self, pantalla):
        if self.tipo == "hamburguesa":
            pygame.draw.ellipse(pantalla, (205, 133, 63), (self.x, self.y, 30, 12))
            pygame.draw.rect(pantalla, MARRON, (self.x, self.y + 8, 30, 8))
            pygame.draw.rect(pantalla, VERDE, (self.x, self.y + 12, 30, 4))
            pygame.draw.ellipse(pantalla, (205, 133, 63), (self.x, self.y + 16, 30, 8))
            pygame.draw.circle(pantalla, BLANCO, (self.x + 8, self.y + 5), 3)
            pygame.draw.circle(pantalla, BLANCO, (self.x + 22, self.y + 5), 3)
            pygame.draw.circle(pantalla, NEGRO, (self.x + 8, self.y + 5), 1)
            pygame.draw.circle(pantalla, NEGRO, (self.x + 22, self.y + 5), 1)
            pygame.draw.line(pantalla, NEGRO, (self.x + 5, self.y + 2), (self.x + 12, self.y + 4), 2)
            pygame.draw.line(pantalla, NEGRO, (self.x + 18, self.y + 4), (self.x + 25, self.y + 2), 2)
            
        elif self.tipo == "papas":
            pygame.draw.rect(pantalla, ROJO_MCD, (self.x, self.y, 30, 25))
            pygame.draw.rect(pantalla, AMARILLO_MCD, (self.x, self.y, 30, 5))
            for i in range(3):
                pygame.draw.rect(pantalla, AMARILLO, (self.x + 5 + i*7, self.y + 8, 4, 12))
            pygame.draw.circle(pantalla, BLANCO, (self.x + 8, self.y + 18), 3)
            pygame.draw.circle(pantalla, BLANCO, (self.x + 22, self.y + 18), 3)
            pygame.draw.circle(pantalla, NEGRO, (self.x + 8, self.y + 18), 1)
            pygame.draw.circle(pantalla, NEGRO, (self.x + 22, self.y + 18), 1)

class JuegoMario:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Caja Triste - Boca Abajo 😢")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.sonidos = Sonidos()
        
        # Plataformas
        self.plataformas = [
            Plataforma(0, 550, ANCHO, 50),
            Plataforma(200, 500, 100, 20),
            Plataforma(400, 460, 100, 20),
            Plataforma(600, 420, 100, 20),
            Plataforma(150, 380, 100, 20),
            Plataforma(450, 340, 100, 20),
            Plataforma(300, 300, 100, 20),
            Plataforma(550, 260, 100, 20),
            Plataforma(200, 220, 100, 20),
            Plataforma(500, 180, 100, 20),
        ]
        
        # Enemigos
        self.enemigos = [
            Enemigo(250, 490, "hamburguesa"),
            Enemigo(450, 450, "papas"),
            Enemigo(650, 410, "hamburguesa"),
            Enemigo(200, 370, "papas"),
            Enemigo(500, 330, "hamburguesa"),
            Enemigo(350, 290, "papas"),
        ]
        
        # Monedas
        self.monedas = [
            Moneda(240, 460), Moneda(260, 460),
            Moneda(440, 420), Moneda(460, 420),
            Moneda(640, 380), Moneda(660, 380),
            Moneda(190, 340), Moneda(210, 340),
            Moneda(490, 300), Moneda(510, 300),
            Moneda(340, 260), Moneda(360, 260),
            Moneda(700, 500), Moneda(50, 500),
            Moneda(750, 300), Moneda(30, 300),
        ]
        
        self.caja = CajaTriste(100, 500, self.sonidos)
        self.camara_x = 0
        self.jugando = True
        self.fondo_offset = 0
        
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
            self.caja.manejar_eventos(evento)
        return True
    
    def update(self):
        self.caja.update(self.plataformas, self.enemigos, self.monedas)
        
        for enemigo in self.enemigos:
            enemigo.update(self.plataformas)
            
        for moneda in self.monedas:
            moneda.update()
        
        self.camara_x = max(0, min(self.caja.x - ANCHO // 2, 1000))
        self.fondo_offset += 0.5
        
        if self.caja.y > ALTO:
            self.caja.morir()
            
        return self.caja.vivo
    
    def draw(self):
        self.pantalla.fill(AZUL_CLARO)
        
        # Nubes
        for i in range(5):
            x_nube = (i * 200 - self.fondo_offset) % (ANCHO + 200) - 100
            pygame.draw.ellipse(self.pantalla, BLANCO, (x_nube, 50, 80, 50))
            pygame.draw.ellipse(self.pantalla, BLANCO, (x_nube + 30, 40, 100, 60))
            pygame.draw.ellipse(self.pantalla, BLANCO, (x_nube + 60, 50, 80, 50))
        
        # Sol
        pygame.draw.circle(self.pantalla, AMARILLO, (ANCHO - 70, 70), 40)
        for i in range(12):
            angulo = i * math.pi * 2 / 12
            x_rayo = ANCHO - 70 + int(55 * math.cos(angulo))
            y_rayo = 70 + int(55 * math.sin(angulo))
            pygame.draw.line(self.pantalla, AMARILLO, (ANCHO - 70, 70), (x_rayo, y_rayo), 4)
        
        # Plataformas
        for plataforma in self.plataformas:
            plataforma.draw(self.pantalla)
            
        # Monedas
        for moneda in self.monedas:
            moneda.draw(self.pantalla)
            
        # Enemigos
        for enemigo in self.enemigos:
            enemigo.draw(self.pantalla)
            
        # Caja Triste
        self.caja.draw(self.pantalla)
        
        # Textos
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.caja.puntuacion}", True, NEGRO)
        texto_vidas = self.fuente.render(f"❤️ Vidas: {self.caja.vidas}", True, ROJO)
        texto_monedas = self.fuente.render(f"💰 Monedas: {self.caja.monedas}", True, DORADO)
        texto_hamburguesas = self.fuente.render(f"🍔 Hamburguesas: {self.caja.hamburguesas}", True, MARRON)
        texto_sonido = self.fuente.render(f"🔊 M: {'ON' if self.caja.sonido_activado else 'OFF'}", True, NEGRO)
        
        fondo_texto = pygame.Surface((270, 140))
        fondo_texto.set_alpha(128)
        fondo_texto.fill(BLANCO)
        self.pantalla.blit(fondo_texto, (5, 5))
        
        self.pantalla.blit(texto_puntuacion, (10, 10))
        self.pantalla.blit(texto_vidas, (ANCHO - 150, 10))
        self.pantalla.blit(texto_monedas, (10, 50))
        self.pantalla.blit(texto_hamburguesas, (10, 90))
        self.pantalla.blit(texto_sonido, (10, 125))
        
        texto_controles = self.fuente.render("← → : Moverse   SPACE : Saltar   M : Silencio   ESC : Salir", True, NEGRO)
        self.pantalla.blit(texto_controles, (10, ALTO - 30))
        
        titulo = self.fuente_grande.render("CAJA TRISTE", True, ROJO_MCD)
        sombra = self.fuente_grande.render("CAJA TRISTE", True, AMARILLO_MCD)
        self.pantalla.blit(sombra, (ANCHO//2 - titulo.get_width()//2 + 2, ALTO - 78))
        self.pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO - 80))
        
        pygame.display.flip()
    
    def mostrar_game_over(self):
        self.pantalla.fill(AZUL_CLARO)
        texto1 = self.fuente_grande.render("GAME OVER", True, ROJO_MCD)
        texto2 = self.fuente.render(f"Puntuación Final: {self.caja.puntuacion}", True, NEGRO)
        texto3 = self.fuente.render(f"💰 Monedas: {self.caja.monedas}   🍔 Hamburguesas: {self.caja.hamburguesas}", True, DORADO)
        texto4 = self.fuente.render("Presiona R para reiniciar o ESC para salir", True, NEGRO)
        
        self.pantalla.blit(texto1, (ANCHO//2 - texto1.get_width()//2, ALTO//2 - 100))
        self.pantalla.blit(texto2, (ANCHO//2 - texto2.get_width()//2, ALTO//2 - 20))
        self.pantalla.blit(texto3, (ANCHO//2 - texto3.get_width()//2, ALTO//2 + 20))
        self.pantalla.blit(texto4, (ANCHO//2 - texto4.get_width()//2, ALTO//2 + 80))
        
        moneda_grande = Moneda(ANCHO//2 - 30, ALTO//2 - 180)
        moneda_grande.draw(self.pantalla)
        
        pygame.display.flip()
        
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        return True
                    if evento.key == pygame.K_ESCAPE:
                        return False
        return False
    
    def run(self):
        while self.jugando:
            if not self.manejar_eventos():
                break
                
            if not self.update():
                if not self.mostrar_game_over():
                    break
                else:
                    self.__init__()
                    
            self.draw()
            self.reloj.tick(60)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego = JuegoMario()
    juego.run()
