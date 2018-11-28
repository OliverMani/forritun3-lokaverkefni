# Óliver Máni
# Lokaverkefni
# pygame


import pygame
import random

arrow = random.randint(0, 7)

def renderContent():
	window.blit(font.render('Stig: ' + str(score), False, BLACK), (20, 20))
	window.blit(font2.render(str(health), False, BLACK), (500, 20))
	window.blit(pygame.transform.scale(heart, (64,64)), (550, 20))
	

def newArrow():
	direction = ["left", "right", "up", "down"][random.randint(0,3)]
	pick = random.randint(0, 7)



	if direction == "left":
		x = WIDTH
		while x > WIDTH/2-150:
			x -= 50
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (x, HEIGHT/2-150))
			pygame.display.update()
			window.fill(RED)
			clock.tick(ticks)
	elif direction == "right":
		x = -300
		while x < WIDTH/2-150:
			x += 50
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (x, HEIGHT/2-150))
			pygame.display.update()
			window.fill(RED)
			clock.tick(ticks)
	elif direction == "up":
		y = HEIGHT
		while y > HEIGHT/2-150:
			y -= 50
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (WIDTH/2-150, y))
			pygame.display.update()
			window.fill(RED)
			clock.tick(ticks)
	elif direction == "down":
		y = -300
		while y < HEIGHT/2-150:
			y += 50
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (WIDTH/2-150, y))
			pygame.display.update()
			window.fill(RED)
			clock.tick(ticks)
	return pick


STATUS = "menu"

arrows = [pygame.image.load('resources/' + str(x) + ".png") for x in ("up", "down", "right","left", "oup", "odown", "oright", "oleft")]
heart = pygame.image.load('resources/heal.png')

pygame.init()
pygame.font.init()

font = pygame.font.Font('resources/Pixeled.ttf', 16)
font2 = pygame.font.Font('resources/Pixeled.ttf', 32)

window_size = WIDTH, HEIGHT = 640, 480

window = pygame.display.set_mode(window_size)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

SKY = (141, 217, 242)

running = True

pygame.display.set_caption('Örvaleikurinn')

window.fill(RED)

clock = pygame.time.Clock()
ticks = 60

score = 0
health = 3

pygame.mixer.init()
menu_music = pygame.mixer.Sound('resources/menu.ogg')
menu_music.play()
music = pygame.mixer.Sound('resources/bgplay.wav')

mistake_sound = pygame.mixer.Sound("resources/No.wav")

can_press = True

deltaTime = 60

delta = deltaTime

arrow_x = WIDTH/2-150
arrow_y = HEIGHT/2-150

randomSpeed = 1

while running:
		

	if STATUS == "menu":
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					STATUS = "play"
					menu_music.stop()
					music.play()
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					running = False
		window.blit(font.render("Yttu a bil til ad byrja", False, BLACK), (200, 400))
	elif STATUS == "play":
		if delta <= 0:
			can_press = False
			health -= 1
			mistake_sound.play()
			arrow = newArrow()
			
			can_press = True
			delta = ticks

		if delta <= 25:
			arrow_x += random.randint(-randomSpeed, randomSpeed)
			arrow_y += random.randint(-randomSpeed, randomSpeed)
			randomSpeed += 1
		else:
			arrow_x = WIDTH/2-150
			arroy_y = HEIGHT/2-150
			randomSpeed = 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key >= 273 and event.key <= 276 and can_press:
					arrow_pushed = event.key-273
					if arrow_pushed >= 0 and arrow_pushed <= 3:
						if arrow_pushed == arrow or (arrow == 4 and arrow_pushed == 1) or (arrow == 5 and arrow_pushed == 0) or (arrow == 6 and arrow_pushed == 3) or (arrow == 7 and arrow_pushed == 2):
							score += 1
							#if deltaTime > 25:
							#	deltaTime -= 1
							can_press = False
							delta = deltaTime
							print(delta)

							arrow = newArrow()
							can_press = True
						else:
							health -= 1
							mistake_sound.play()
							if health < 1:
								STATUS = "gameover"
								window.fill(RED)
								#music.stop()
							elif delta > 25:
								delta = 25


					
		delta -= 1

		renderContent()
		window.blit(pygame.transform.scale(arrows[arrow], (300,300)), (arrow_x, arrow_y))
		
		

	elif STATUS == "gameover":
		renderContent()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					health = 3
					score = 0
					deltaTime = 60
					randomSpeed = 1
					delta = deltaTime
					STATUS = "play"
		window.blit(font2.render("Leik lokið", False, BLACK), (WIDTH/2-150, 20))

	pygame.display.update()
	window.fill(RED)
	clock.tick(ticks)
pygame.quit()
