import pygame
import sys
import random
import math

# Inicializar Pygame
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

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
CAFE_CLARO = (210, 180, 140)
ROSADO = (255, 192, 203)

class Sonidos:
    def __init__(self):
        self.sonido_salto = None
        self.sonido_moneda = None
        self.sonido_golpe = None
        self.sonido_game_over = None
        self.sonido_crecer = None
        self.crear_sonidos()
        
    def crear_sonidos(self):
        try:
            self.sonido_salto = self.generar_tono(880, 0.15)
            self.sonido_moneda = self.generar_tono(1046.50, 0.2)
            self.sonido_golpe = self.generar_tono(440, 0.1)
            self.sonido_game_over = self.generar_tono_descendente()
            self.sonido_crecer = self.generar_tono_crecer()
            print("✅ Sonidos inicializados correctamente")
        except Exception as e:
            print(f"⚠️ Error al generar sonidos: {e}")
            self.crear_sonidos_fallback()
    
    def crear_sonidos_fallback(self):
        try:
            import array
            
            def crear_beep(frecuencia, duracion):
                sample_rate = 22050
                n_samples = int(sample_rate * duracion)
                wave = [int(32767 * 0.5 * math.sin(2 * math.pi * frecuencia * t / sample_rate)) 
                       for t in range(n_samples)]
                wave_array = array.array('h', wave)
                return pygame.mixer.Sound(buffer=wave_array)
            
            self.sonido_salto = crear_beep(880, 0.15)
            self.sonido_moneda = crear_beep(1046.50, 0.2)
            self.sonido_golpe = crear_beep(440, 0.1)
            self.sonido_game_over = crear_beep(440, 0.5)
            self.sonido_crecer = crear_beep(660, 0.3)
            print("✅ Sonidos fallback creados")
        except Exception as e:
            print(f"⚠️ No se pudieron crear sonidos: {e}")
    
    def generar_tono(self, frecuencia, duracion):
        try:
            import numpy as np
            sample_rate = 44100
            n_samples = int(sample_rate * duracion)
            t = np.linspace(0, duracion, n_samples, endpoint=False)
            onda = np.sin(2 * np.pi * frecuencia * t)
            envelope = np.exp(-3 * t)
            onda = onda * envelope
            onda = (onda * 16384).astype(np.int16)
            stereo = np.column_stack((onda, onda))
            return pygame.sndarray.make_sound(stereo)
        except Exception as e:
            print(f"Error generando tono: {e}")
            return None
    
    def generar_tono_descendente(self):
        try:
            import numpy as np
            sample_rate = 44100
            duracion = 1.0
            n_samples = int(sample_rate * duracion)
            t = np.linspace(0, duracion, n_samples, endpoint=False)
            frecuencia = 880 * np.exp(-5 * t)
            onda = np.sin(2 * np.pi * frecuencia * t)
            envelope = np.exp(-3 * t)
            onda = onda * envelope
            onda = (onda * 16384).astype(np.int16)
            stereo = np.column_stack((onda, onda))
            return pygame.sndarray.make_sound(stereo)
        except Exception as e:
            print(f"Error generando tono descendente: {e}")
            return None
    
    def generar_tono_crecer(self):
        try:
            import numpy as np
            sample_rate = 44100
            duracion = 0.5
            n_samples = int(sample_rate * duracion)
            t = np.linspace(0, duracion, n_samples, endpoint=False)
            frecuencia = 440 * (1 + 3 * t)
            onda = np.sin(2 * np.pi * frecuencia * t)
            envelope = np.exp(-2 * t)
            onda = onda * envelope
            onda = (onda * 16384).astype(np.int16)
            stereo = np.column_stack((onda, onda))
            return pygame.sndarray.make_sound(stereo)
        except Exception as e:
            print(f"Error generando tono crecer: {e}")
            return None
    
    def reproducir(self, sonido, volumen=0.5):
        if sonido is not None:
            try:
                sonido.set_volume(volumen)
                sonido.play()
            except Exception as e:
                print(f"Error reproduciendo sonido: {e}")

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
        self.papas = 0
        self.moviendo_izquierda = False
        self.moviendo_derecha = False
        self.puede_saltar = True
        self.sonidos = sonidos
        self.sonido_activado = True
        self.creciendo = False
        self.tiempo_crecimiento = 0
        self.tamanio_original = 45
        self.tamanio_objetivo = 45
        
    def update(self, plataformas, enemigos, monedas, powerups):
        self.vel_y += 0.8
        if self.vel_y > 15:
            self.vel_y = 15
            
        self.x += self.vel_x
        self.colision_plataformas(plataformas, True)
        
        self.y += self.vel_y
        self.en_suelo = False
        self.colision_plataformas(plataformas, False)
        
        if self.x < 0:
            self.x = 0
        if self.x > ANCHO - self.ancho:
            self.x = ANCHO - self.ancho
            
        # Animación de crecimiento
        if self.creciendo:
            self.tiempo_crecimiento += 1
            if self.tiempo_crecimiento <= 10:
                progreso = self.tiempo_crecimiento / 10
                self.ancho = int(self.tamanio_original + (self.tamanio_objetivo - self.tamanio_original) * progreso)
                self.alto = int(self.tamanio_original + (self.tamanio_objetivo - self.tamanio_original) * progreso)
                self.y = self.y - (self.alto - self.tamanio_original)
            else:
                self.creciendo = False
                self.tiempo_crecimiento = 0
        
        for enemigo in enemigos[:]:
            if self.colision(enemigo):
                if self.vel_y > 0 and self.y + self.alto - enemigo.y <= 30:
                    enemigos.remove(enemigo)
                    self.puntuacion += 100
                    if enemigo.tipo == "hamburguesa":
                        self.hamburguesas += 1
                    elif enemigo.tipo == "papas":
                        self.papas += 1
                    self.vel_y = -10
                    if self.sonido_activado:
                        self.sonidos.reproducir(self.sonidos.sonido_golpe, 0.7)
                else:
                    self.morir()
        
        for powerup in powerups[:]:
            if self.colision(powerup):
                powerups.remove(powerup)
                if powerup.tipo == "barquilla_helado":
                    self.crecer()
                self.puntuacion += 100
                if self.sonido_activado:
                    self.sonidos.reproducir(self.sonidos.sonido_crecer, 0.6)
        
        for moneda in monedas[:]:
            if self.colision(moneda):
                monedas.remove(moneda)
                self.monedas += 1
                self.puntuacion += 50
                if self.sonido_activado:
                    self.sonidos.reproducir(self.sonidos.sonido_moneda, 0.5)
    
    def crecer(self):
        if not self.creciendo and self.ancho == self.tamanio_original:
            self.tamanio_objetivo = 65
            self.creciendo = True
            self.tiempo_crecimiento = 0
                    
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
        self.ancho = self.tamanio_original
        self.alto = self.tamanio_original
        self.creciendo = False
        
    def draw(self, pantalla):
        pygame.draw.rect(pantalla, ROJO_MCD, (self.x, self.y, self.ancho, self.alto))
        
        tamaño_fuente = max(20, min(30, self.ancho // 2))
        fuente_m = pygame.font.Font(None, tamaño_fuente)
        texto_m = fuente_m.render("m", True, AMARILLO_MCD)
        texto_rect = texto_m.get_rect(center=(self.x + self.ancho//2, self.y - 5))
        pantalla.blit(texto_m, texto_rect)
        
        ojo_offset = self.ancho // 4
        ojo_tamaño = max(3, min(5, self.ancho // 9))
        pygame.draw.circle(pantalla, BLANCO, (self.x + ojo_offset, self.y + self.alto//3), ojo_tamaño)
        pygame.draw.circle(pantalla, BLANCO, (self.x + self.ancho - ojo_offset, self.y + self.alto//3), ojo_tamaño)
        pygame.draw.circle(pantalla, NEGRO, (self.x + ojo_offset - 1, self.y + self.alto//3), ojo_tamaño//2)
        pygame.draw.circle(pantalla, NEGRO, (self.x + self.ancho - ojo_offset - 1, self.y + self.alto//3), ojo_tamaño//2)
        
        boca_ancho = self.ancho // 2
        boca_alto = self.alto // 4
        pygame.draw.arc(pantalla, LABIO_AMARILLO, 
                       (self.x + self.ancho//4, self.y + self.alto//2, boca_ancho, boca_alto), 
                       math.radians(190), math.radians(350), max(2, self.ancho//15))
        
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

class PowerUp:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.ancho = 25
        self.alto = 25
        self.tipo = tipo
        self.animacion = 0
        
    def update(self):
        self.animacion += 0.1
        
    def draw(self, pantalla):
        if self.tipo == "barquilla_helado":
            y_offset = int(3 * math.sin(self.animacion))
            
            # Cono de barquilla
            puntos_cono = [
                (self.x + 12, self.y + 20 + y_offset),
                (self.x + 4, self.y + 10 + y_offset),
                (self.x + 20, self.y + 10 + y_offset)
            ]
            pygame.draw.polygon(pantalla, CAFE_CLARO, puntos_cono)
            
            # Bola de helado
            pygame.draw.circle(pantalla, ROSADO, (self.x + 12, self.y + 8 + y_offset), 8)
            pygame.draw.circle(pantalla, (255, 255, 255), (self.x + 12, self.y + 8 + y_offset), 6)
            
            # Brillitos
            pygame.draw.circle(pantalla, (255, 255, 200), (self.x + 10, self.y + 6 + y_offset), 2)
            
            # Texto "+" para indicar crecimiento
            fuente = pygame.font.Font(None, 14)
            texto = fuente.render("+", True, VERDE)
            pantalla.blit(texto, (self.x + 9, self.y + 2 + y_offset))

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

class Nivel1:
    def __init__(self, pantalla, reloj, fuente, fuente_grande, sonidos):
        self.pantalla = pantalla
        self.reloj = reloj
        self.fuente = fuente
        self.fuente_grande = fuente_grande
        self.sonidos = sonidos
        
        self.plataformas = [
            Plataforma(0, 550, ANCHO, 50),
            Plataforma(200, 500, 100, 20),
            Plataforma(400, 460, 100, 20),
            Plataforma(500, 420, 150, 20),
            Plataforma(150, 380, 100, 20),
            Plataforma(450, 340, 100, 20),
            Plataforma(300, 300, 100, 20),
        ]
        
        self.enemigos = [
            Enemigo(250, 490, "hamburguesa"),
            Enemigo(450, 450, "hamburguesa"),
            Enemigo(200, 370, "hamburguesa"),
            Enemigo(350, 290, "hamburguesa"),
        ]
        
        self.monedas = [
            Moneda(240, 460), Moneda(260, 460),
            Moneda(440, 420), Moneda(460, 420),
            Moneda(550, 390), Moneda(570, 390), Moneda(590, 390),
            Moneda(190, 340), Moneda(210, 340),
            Moneda(490, 300), Moneda(510, 300),
        ]
        
        self.powerups = []
        
        self.caja = CajaTriste(100, 500, self.sonidos)
        self.camara_x = 0
        self.fondo_offset = 0
        
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
                if evento.key == pygame.K_n:
                    return "next_level"
            self.caja.manejar_eventos(evento)
        return True
    
    def update(self):
        self.caja.update(self.plataformas, self.enemigos, self.monedas, self.powerups)
        
        for enemigo in self.enemigos:
            enemigo.update(self.plataformas)
            
        for moneda in self.monedas:
            moneda.update()
        
        for powerup in self.powerups:
            powerup.update()
        
        self.fondo_offset += 0.5
        
        if self.caja.y > ALTO:
            self.caja.morir()
            
        if len(self.enemigos) == 0:
            return "level_complete"
            
        return self.caja.vivo
    
    def draw(self):
        self.pantalla.fill(AZUL_CLARO)
        
        for i in range(3):
            x_nube = (i * 300 - self.fondo_offset) % (ANCHO + 300) - 150
            pygame.draw.ellipse(self.pantalla, BLANCO, (x_nube, 50, 80, 50))
            pygame.draw.ellipse(self.pantalla, BLANCO, (x_nube + 30, 40, 100, 60))
        
        pygame.draw.circle(self.pantalla, AMARILLO, (ANCHO - 70, 70), 40)
        
        for plataforma in self.plataformas:
            plataforma.draw(self.pantalla)
            
        for moneda in self.monedas:
            moneda.draw(self.pantalla)
            
        for enemigo in self.enemigos:
            enemigo.draw(self.pantalla)
            
        for powerup in self.powerups:
            powerup.draw(self.pantalla)
            
        self.caja.draw(self.pantalla)
        
        texto_puntuacion = self.fuente.render(f"Puntuación: {self.caja.puntuacion}", True, NEGRO)
        texto_vidas = self.fuente.render(f"❤️ Vidas: {self.caja.vidas}", True, ROJO)
        texto_monedas = self.fuente.render(f"💰 Monedas: {self.caja.monedas}", True, DORADO)
        texto_enemigos = self.fuente.render(f"🍔 Enemigos: {len(self.enemigos)}", True, MARRON)
        texto_sonido = self.fuente.render(f"🔊 M: {'ON' if self.caja.sonido_activado else 'OFF'}", True, NEGRO)
        
        fondo_texto = pygame.Surface((270, 140))
        fondo_texto.set_alpha(128)
        fondo_texto.fill(BLANCO)
        self.pantalla.blit(fondo_texto, (5, 5))
        
        self.pantalla.blit(texto_puntuacion, (10, 10))
        self.pantalla.blit(texto_vidas, (ANCHO - 150, 10))
        self.pantalla.blit(texto_monedas, (10, 50))
        self.pantalla.blit(texto_enemigos, (10, 90))
        self.pantalla.blit(texto_sonido, (10, 125))
        
        texto_controles = self.fuente.render("← → : Moverse   SPACE : Saltar   M : Silencio   N : Siguiente Nivel   ESC : Salir", True, NEGRO)
        self.pantalla.blit(texto_controles, (10, ALTO - 30))
        
        titulo = self.fuente_grande.render("NIVEL 1", True, ROJO_MCD)
        sombra = self.fuente_grande.render("NIVEL 1", True, AMARILLO_MCD)
        self.pantalla.blit(sombra, (ANCHO//2 - titulo.get_width()//2 + 2, ALTO - 78))
        self.pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO - 80))
        
        pygame.display.flip()
    
    def mostrar_completado(self):
        self.pantalla.fill(AZUL_CLARO)
        texto1 = self.fuente_grande.render("¡NIVEL 1 COMPLETADO!", True, VERDE)
        texto2 = self.fuente.render(f"Puntuación: {self.caja.puntuacion}", True, NEGRO)
        texto3 = self.fuente.render(f"💰 Monedas: {self.caja.monedas}   🍔 Hamburguesas: {self.caja.hamburguesas}", True, DORADO)
        texto4 = self.fuente.render("Presiona N para el Nivel 2 o ESC para salir", True, NEGRO)
        
        self.pantalla.blit(texto1, (ANCHO//2 - texto1.get_width()//2, ALTO//2 - 80))
        self.pantalla.blit(texto2, (ANCHO//2 - texto2.get_width()//2, ALTO//2 - 20))
        self.pantalla.blit(texto3, (ANCHO//2 - texto3.get_width()//2, ALTO//2 + 20))
        self.pantalla.blit(texto4, (ANCHO//2 - texto4.get_width()//2, ALTO//2 + 80))
        
        pygame.display.flip()
        
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_n:
                        return True
                    if evento.key == pygame.K_ESCAPE:
                        return False
        return False

class JuegoMario:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Mario_MAC - Niveles 1 y 2")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 72)
        self.sonidos = Sonidos()
        self.nivel_actual = 1
        
    def mostrar_menu_inicio(self):
        self.pantalla.fill(AZUL_CLARO)
        
        titulo = self.fuente_grande.render("CAJA FELIZ", True, ROJO_MCD)
        subtitulo = self.fuente.render("Aventura de 2 Niveles", True, AMARILLO_MCD)
        instruccion = self.fuente.render("Presiona 1 para NIVEL 1 o 2 para NIVEL 2", True, NEGRO)
        control = self.fuente.render("← → : Moverse   SPACE : Saltar   M : Silencio", True, NEGRO)
        
        caja_menu = CajaTriste(ANCHO//2 - 22, ALTO//2 - 50, self.sonidos)
        caja_menu.draw(self.pantalla)
        
        self.pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 80))
        self.pantalla.blit(subtitulo, (ANCHO//2 - subtitulo.get_width()//2, 150))
        self.pantalla.blit(instruccion, (ANCHO//2 - instruccion.get_width()//2, ALTO - 120))
        self.pantalla.blit(control, (ANCHO//2 - control.get_width()//2, ALTO - 80))
        
        pygame.display.flip()
        
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.nivel_actual = 1
                        return True
                    if evento.key == pygame.K_2:
                        self.nivel_actual = 2
                        return True
                    if evento.key == pygame.K_ESCAPE:
                        return False
        return False
    
    def jugar_nivel1(self):
        nivel = Nivel1(self.pantalla, self.reloj, self.fuente, self.fuente_grande, self.sonidos)
        
        while True:
            resultado = nivel.manejar_eventos()
            if resultado == False:
                return False
            if resultado == "next_level":
                return "go_to_nivel2"
            
            resultado_update = nivel.update()
            if resultado_update == "level_complete":
                if nivel.mostrar_completado():
                    return "go_to_nivel2"
                else:
                    return False
            elif resultado_update == False:
                if not self.mostrar_game_over(nivel.caja):
                    return False
                else:
                    nivel = Nivel1(self.pantalla, self.reloj, self.fuente, self.fuente_grande, self.sonidos)
                    continue
                
            nivel.draw()
            self.reloj.tick(60)
    
    def jugar_nivel2(self):
        # Plataformas del nivel 2 con plataforma 3 más cerca
        plataformas = [
            Plataforma(0, 550, ANCHO, 50),      # Suelo
            Plataforma(200, 500, 100, 20),      # Plataforma 1
            Plataforma(400, 460, 100, 20),      # Plataforma 2
            Plataforma(470, 420, 120, 20),      # Plataforma 3: movida de 600 a 470 (más cerca) y más ancha
            Plataforma(150, 380, 100, 20),      # Plataforma 4
            Plataforma(450, 340, 100, 20),      # Plataforma 5
            Plataforma(300, 300, 100, 20),      # Plataforma 6 (donde está la caja de papas)
            Plataforma(550, 260, 100, 20),      # Plataforma 7
            Plataforma(200, 220, 100, 20),      # Plataforma 8
            Plataforma(500, 180, 100, 20),      # Plataforma 9
        ]
        
        # Enemigos: solo hamburguesas y UNA caja de papas en la plataforma 6
        enemigos = [
            Enemigo(250, 490, "hamburguesa"),   # Plataforma 1
            Enemigo(510, 410, "hamburguesa"),   # Plataforma 3 (ahora más cerca)
            Enemigo(500, 330, "hamburguesa"),   # Plataforma 5
            Enemigo(330, 290, "papas"),         # UNA caja de papas en plataforma 6 (x=330 porque la plataforma está en 300)
        ]
        
        # Monedas
        monedas = [
            Moneda(240, 460), Moneda(260, 460),                     # Plataforma 1
            Moneda(440, 420), Moneda(460, 420),                     # Plataforma 2
            Moneda(510, 390), Moneda(530, 390),                     # Plataforma 3 (movida)
            Moneda(190, 340), Moneda(210, 340),                     # Plataforma 4
            Moneda(490, 300), Moneda(510, 300),                     # Plataforma 5
            Moneda(340, 260), Moneda(360, 260),                     # Plataforma 6
            Moneda(590, 230), Moneda(610, 230),                     # Plataforma 7
            Moneda(240, 190), Moneda(260, 190),                     # Plataforma 8
            Moneda(540, 150), Moneda(560, 150),                     # Plataforma 9
            Moneda(700, 500), Moneda(50, 500),                      # Suelo
            Moneda(750, 300), Moneda(30, 300),                      # Suelo
        ]
        
        # PowerUps: Barquillas de helado
        powerups = [
            PowerUp(350, 470, "barquilla_helado"),  # Plataforma 2
            PowerUp(520, 400, "barquilla_helado"),  # Plataforma 3
            PowerUp(200, 360, "barquilla_helado"),  # Plataforma 4
            PowerUp(500, 320, "barquilla_helado"),  # Plataforma 5
        ]
        
        caja = CajaTriste(100, 500, self.sonidos)
        fondo_offset = 0
        
        while caja.vivo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return False
                caja.manejar_eventos(evento)
            
            caja.update(plataformas, enemigos, monedas, powerups)
            
            for enemigo in enemigos:
                enemigo.update(plataformas)
                
            for moneda in monedas:
                moneda.update()
                
            for powerup in powerups:
                powerup.update()
            
            fondo_offset += 0.5
            
            if caja.y > ALTO:
                caja.morir()
                if not caja.vivo:
                    if not self.mostrar_game_over(caja):
                        return False
                    else:
                        caja = CajaTriste(100, 500, self.sonidos)
                        powerups = [
                            PowerUp(350, 470, "barquilla_helado"),
                            PowerUp(520, 400, "barquilla_helado"),
                            PowerUp(200, 360, "barquilla_helado"),
                            PowerUp(500, 320, "barquilla_helado"),
                        ]
                        continue
            
            # Dibujar todo
            self.pantalla.fill(AZUL_CLARO)
            
            # Nubes
            for i in range(5):
                x_nube = (i * 200 - fondo_offset) % (ANCHO + 200) - 100
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
            for plataforma in plataformas:
                plataforma.draw(self.pantalla)
                
            # Monedas
            for moneda in monedas:
                moneda.draw(self.pantalla)
                
            # Enemigos
            for enemigo in enemigos:
                enemigo.draw(self.pantalla)
                
            # PowerUps (barquillas de helado)
            for powerup in powerups:
                powerup.draw(self.pantalla)
                
            # Caja
            caja.draw(self.pantalla)
            
            # Textos
            texto_puntuacion = self.fuente.render(f"Puntuación: {caja.puntuacion}", True, NEGRO)
            texto_vidas = self.fuente.render(f"❤️ Vidas: {caja.vidas}", True, ROJO)
            texto_monedas = self.fuente.render(f"💰 Monedas: {caja.monedas}", True, DORADO)
            texto_hamburguesas = self.fuente.render(f"🍔 Hamburguesas: {caja.hamburguesas}", True, MARRON)
            texto_papas = self.fuente.render(f"🍟 Papas: {caja.papas}", True, ROJO_MCD)
            texto_sonido = self.fuente.render(f"🔊 M: {'ON' if caja.sonido_activado else 'OFF'}", True, NEGRO)
            texto_tamano = self.fuente.render(f"📦 Tamaño: {caja.ancho}x{caja.alto}", True, AZUL)
            
            fondo_texto = pygame.Surface((270, 190))
            fondo_texto.set_alpha(128)
            fondo_texto.fill(BLANCO)
            self.pantalla.blit(fondo_texto, (5, 5))
            
            self.pantalla.blit(texto_puntuacion, (10, 10))
            self.pantalla.blit(texto_vidas, (ANCHO - 150, 10))
            self.pantalla.blit(texto_monedas, (10, 50))
            self.pantalla.blit(texto_hamburguesas, (10, 90))
            self.pantalla.blit(texto_papas, (10, 125))
            self.pantalla.blit(texto_tamano, (10, 155))
            self.pantalla.blit(texto_sonido, (10, 185))
            
            texto_controles = self.fuente.render("← → : Moverse   SPACE : Saltar   M : Silencio   ESC : Salir", True, NEGRO)
            self.pantalla.blit(texto_controles, (10, ALTO - 30))
            
            titulo = self.fuente_grande.render("NIVEL 2", True, ROJO_MCD)
            sombra = self.fuente_grande.render("NIVEL 2", True, AMARILLO_MCD)
            self.pantalla.blit(sombra, (ANCHO//2 - titulo.get_width()//2 + 2, ALTO - 78))
            self.pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, ALTO - 80))
            
            # Mensaje de crecimiento
            if caja.creciendo:
                texto_crece = self.fuente.render("¡LA CAJA ESTÁ CRECIENDO!", True, VERDE)
                self.pantalla.blit(texto_crece, (ANCHO//2 - texto_crece.get_width()//2, ALTO//2 - 100))
            
            pygame.display.flip()
            self.reloj.tick(60)
        
        return True
    
    def mostrar_game_over(self, caja):
        self.pantalla.fill(AZUL_CLARO)
        texto1 = self.fuente_grande.render("GAME OVER", True, ROJO_MCD)
        texto2 = self.fuente.render(f"Puntuación Final: {caja.puntuacion}", True, NEGRO)
        texto3 = self.fuente.render(f"💰 Monedas: {caja.monedas}   🍔 Hamburguesas: {caja.hamburguesas}", True, DORADO)
        texto4 = self.fuente.render("Presiona R para reiniciar nivel o ESC para salir", True, NEGRO)
        
        self.pantalla.blit(texto1, (ANCHO//2 - texto1.get_width()//2, ALTO//2 - 100))
        self.pantalla.blit(texto2, (ANCHO//2 - texto2.get_width()//2, ALTO//2 - 20))
        self.pantalla.blit(texto3, (ANCHO//2 - texto3.get_width()//2, ALTO//2 + 20))
        self.pantalla.blit(texto4, (ANCHO//2 - texto4.get_width()//2, ALTO//2 + 80))
        
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
        if not self.mostrar_menu_inicio():
            pygame.quit()
            sys.exit()
        
        while True:
            if self.nivel_actual == 1:
                resultado = self.jugar_nivel1()
                if resultado == "go_to_nivel2":
                    self.nivel_actual = 2
                else:
                    break
            elif self.nivel_actual == 2:
                if not self.jugar_nivel2():
                    break
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego = JuegoMario()
    juego.run()
