import box
import pygame

PLAYER_SPEED = 5

boxData = lambda box: pygame.Rect(box.x, box.y, box.width, box.height)

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

window_size = WIDTH, HEIGHT = 640, 900

window = pygame.display.set_mode(window_size)

grass = pygame.image.load('myndir/gras.png')

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

SKY = (141, 217, 242)

running = True

pygame.display.set_caption('Leikur')

window.fill(SKY)

x = 0

clock = pygame.time.Clock()
ticks = 60

player = box.Box((WIDTH/2)-30, 30, 60, 60)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]:
		player.x -= PLAYER_SPEED
	if keys[pygame.K_d]:
		player.x += PLAYER_SPEED

	'''
	if keys[pygame.K_s]:
		player.y += PLAYER_SPEED
	if keys[pygame.K_w]:
		player.y -= PLAYER_SPEED

	for x in range(0, 640, 32):
		window.blit(grass, (x, 480-32))

	'''

	pygame.draw.rect(window, RED, boxData(player))
	window.blit(font.render('Stig: 0', False, WHITE), (500, 30))
	pygame.display.update()
	window.fill(SKY)
	clock.tick(ticks)
pygame.quit()
