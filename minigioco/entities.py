from settings import * 
import pygame 


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Superficie quadrata che contiene il triangolo:
        size = PLAYER_SIZE * 2 + 4 
        self.original_image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.draw_ship(self.original_image)

        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))

        # Posiziona il float per movimento preciso
        self.pos = pygame.math.Vector2(self.rect.center)

        # Stats
        self.hp = PLAYER_MAX_HP
        # self.ammo = PLAYER_START_AMMO
        # self.fuel = PLAYER_START_FUEL
        # self.dmg = PLAYER_DMG
        self.speed = PLAYER_SPEED
        self.angle = 90.0

    def __str__(self):
        return "Una nave intergalattica pronta a qualunque cosa per portare a termine la missione"

    # =======================================
    def draw_ship(self, surface):
        posX = surface.get_width() // 2
        posY = surface.get_height() // 2
        r = PLAYER_SIZE

        # Tre vertici del triangolo (punta in alto )
        points = [
            (posX,    posY - r), # Punta
            (posX - r,   posY + r), # Basso-Sinistra
            (posX + r,  posY + r ) # Basso-Destra
        ]
        pygame.draw.polygon(surface, CYAN, points)
        pygame.draw.polygon(surface, WHITE, points, 2) # bordo 

    # =======================================
    # Position functions
    def _move(self):
        """Muove con mouse o con le frecce, la confina nel quadrante """
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        # in caso di controlli alternativi (es. rasp modificare questta mappa )
        if keys[pygame.K_w] or keys[pygame.K_UP]: dy -= 1 
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx += 1

        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707
        
        self.pos.x += dx * self.speed
        self.pos.y += dy * self.speed

        # Limita lo schermo 
        r = PLAYER_SIZE
        self.pos.x = max(r, min(SCREEN_HEIGHT -r, self.pos.x))
        self.pos.y = max(r, min(SCREEN_WIDTH -r, self.pos.y))
    
    def update(self):
        self._move()
   