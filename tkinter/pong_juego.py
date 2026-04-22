import tkinter as tk
import random

class JuegoPong:
    def __init__(self, root):
        self.root = root
        self.root.title("PONG - Juego Clásico")
        self.root.resizable(False, False)
        
        # Configuración del juego
        self.ancho = 800
        self.alto = 500
        self.jugando = True
        
        # Puntajes
        self.puntaje_jugador = 0
        self.puntaje_ia = 0
        
        # Velocidades
        self.velocidad_bola_x = 4
        self.velocidad_bola_y = 4
        self.velocidad_paleta = 20
        
        # Crear canvas (lienzo para dibujar)
        self.canvas = tk.Canvas(root, width=self.ancho, height=self.alto, bg="black")
        self.canvas.pack()
        
        # Crear elementos del juego
        self.crear_elementos()
        
        # Mostrar puntajes
        self.mostrar_puntajes()
        
        # Controles del teclado
        self.root.bind("<Up>", self.mover_paleta_jugador_arriba)
        self.root.bind("<Down>", self.mover_paleta_jugador_abajo)
        self.root.bind("<space>", self.reiniciar_juego)
        
        # Animación
        self.mover_bola()
        
    def crear_elementos(self):
        # Paleta del jugador (izquierda)
        self.paleta_jugador = self.canvas.create_rectangle(
            20, self.alto//2 - 50, 35, self.alto//2 + 50,
            fill="white", outline="white"
        )
        
        # Paleta de la IA (derecha)
        self.paleta_ia = self.canvas.create_rectangle(
            self.ancho - 35, self.alto//2 - 50, self.ancho - 20, self.alto//2 + 50,
            fill="white", outline="white"
        )
        
        # Bola
        self.bola = self.canvas.create_oval(
            self.ancho//2 - 8, self.alto//2 - 8,
            self.ancho//2 + 8, self.alto//2 + 8,
            fill="white", outline="white"
        )
        
        # Línea central punteada
        for i in range(0, self.alto, 30):
            self.canvas.create_line(self.ancho//2, i, self.ancho//2, i+15, fill="white")
    
    def mostrar_puntajes(self):
        # Texto de puntajes
        self.texto_puntaje = self.canvas.create_text(
            self.ancho//2, 30,
            text=f"{self.puntaje_jugador}  |  {self.puntaje_ia}",
            font=("Arial", 24, "bold"),
            fill="white"
        )
    
    def actualizar_puntajes(self):
        self.canvas.itemconfig(self.texto_puntaje, 
                              text=f"{self.puntaje_jugador}  |  {self.puntaje_ia}")
    
    def mover_paleta_jugador_arriba(self, event):
        if self.jugando:
            pos = self.canvas.coords(self.paleta_jugador)
            if pos[1] > 0:
                self.canvas.move(self.paleta_jugador, 0, -self.velocidad_paleta)
    
    def mover_paleta_jugador_abajo(self, event):
        if self.jugando:
            pos = self.canvas.coords(self.paleta_jugador)
            if pos[3] < self.alto:
                self.canvas.move(self.paleta_jugador, 0, self.velocidad_paleta)
    
    def mover_ia(self):
        # IA simple que sigue la bola
        bola_pos = self.canvas.coords(self.bola)
        ia_pos = self.canvas.coords(self.paleta_ia)
        
        centro_ia = (ia_pos[1] + ia_pos[3]) / 2
        centro_bola = (bola_pos[1] + bola_pos[3]) / 2
        
        if centro_ia < centro_bola - 20 and ia_pos[3] < self.alto:
            self.canvas.move(self.paleta_ia, 0, self.velocidad_paleta)
        elif centro_ia > centro_bola + 20 and ia_pos[1] > 0:
            self.canvas.move(self.paleta_ia, 0, -self.velocidad_paleta)
    
    def mover_bola(self):
        if not self.jugando:
            return
            
        # Mover la bola
        self.canvas.move(self.bola, self.velocidad_bola_x, self.velocidad_bola_y)
        
        # Obtener posiciones actuales
        bola_pos = self.canvas.coords(self.bola)
        jugador_pos = self.canvas.coords(self.paleta_jugador)
        ia_pos = self.canvas.coords(self.paleta_ia)
        
        # Rebote en paredes superior e inferior
        if bola_pos[1] <= 0 or bola_pos[3] >= self.alto:
            self.velocidad_bola_y = -self.velocidad_bola_y
        
        # Colisión con paleta del jugador
        if (bola_pos[0] <= jugador_pos[2] and 
            bola_pos[2] >= jugador_pos[0] and
            bola_pos[1] <= jugador_pos[3] and 
            bola_pos[3] >= jugador_pos[1]):
            
            self.velocidad_bola_x = abs(self.velocidad_bola_x)
            # Cambiar ángulo según donde golpea
            self.velocidad_bola_y = self.calcular_angulo(bola_pos, jugador_pos)
            # Aumentar velocidad gradualmente
            self.velocidad_bola_x *= 1.05
            self.velocidad_bola_y *= 1.05
        
        # Colisión con paleta de la IA
        elif (bola_pos[2] >= ia_pos[0] and 
              bola_pos[0] <= ia_pos[2] and
              bola_pos[1] <= ia_pos[3] and 
              bola_pos[3] >= ia_pos[1]):
            
            self.velocidad_bola_x = -abs(self.velocidad_bola_x)
            self.velocidad_bola_y = self.calcular_angulo(bola_pos, ia_pos)
            self.velocidad_bola_x *= 1.05
            self.velocidad_bola_y *= 1.05
        
        # Punto para la IA (bola pasó la paleta izquierda)
        elif bola_pos[0] <= 0:
            self.puntaje_ia += 1
            self.actualizar_puntajes()
            self.reiniciar_posiciones()
            if self.puntaje_ia >= 7:
                self.game_over("IA GANA!")
        
        # Punto para el jugador (bola pasó la paleta derecha)
        elif bola_pos[2] >= self.ancho:
            self.puntaje_jugador += 1
            self.actualizar_puntajes()
            self.reiniciar_posiciones()
            if self.puntaje_jugador >= 7:
                self.game_over("¡JUGADOR GANA!")
        
        # Mover IA
        self.mover_ia()
        
        # Continuar animación
        self.root.after(16, self.mover_bola)  # ~60 FPS
    
    def calcular_angulo(self, bola_pos, paleta_pos):
        # Calcula el ángulo de rebote según donde golpea la paleta
        centro_paleta = (paleta_pos[1] + paleta_pos[3]) / 2
        centro_bola = (bola_pos[1] + bola_pos[3]) / 2
        offset = centro_bola - centro_paleta
        max_offset = 60  # Altura máxima de la paleta
        return offset / max_offset * 8  # Factor de ángulo
    
    def reiniciar_posiciones(self):
        # Centrar la bola
        self.canvas.coords(self.bola, 
                          self.ancho//2 - 8, self.alto//2 - 8,
                          self.ancho//2 + 8, self.alto//2 + 8)
        
        # Reiniciar velocidades
        self.velocidad_bola_x = 4 * random.choice([-1, 1])
        self.velocidad_bola_y = 4 * random.choice([-1, 1])
        
        # Centrar paletas
        self.canvas.coords(self.paleta_jugador,
                          20, self.alto//2 - 50,
                          35, self.alto//2 + 50)
        
        self.canvas.coords(self.paleta_ia,
                          self.ancho - 35, self.alto//2 - 50,
                          self.ancho - 20, self.alto//2 + 50)
    
    def reiniciar_juego(self, event=None):
        self.jugando = True
        self.puntaje_jugador = 0
        self.puntaje_ia = 0
        self.actualizar_puntajes()
        self.reiniciar_posiciones()
        
        # Eliminar mensaje de game over si existe
        if hasattr(self, 'texto_game_over'):
            self.canvas.delete(self.texto_game_over)
    
    def game_over(self, mensaje):
        self.jugando = False
        self.texto_game_over = self.canvas.create_text(
            self.ancho//2, self.alto//2,
            text=f"GAME OVER\n{mensaje}\nPresiona ESPACIO para jugar de nuevo",
            font=("Arial", 20, "bold"),
            fill="yellow",
            justify="center"
        )

# Crear ventana y ejecutar juego
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPong(root)
    root.mainloop()
