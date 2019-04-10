# Óliver Máni
# Lokaverkefni
# pygame


import pygame
import random

## STILLANLEGT

# Þetta á að þýða að þegar delta er 40 eða minna þá á að byrja að hrista
START_SHAKE = 40
# Delta er sett á 120 þegar þú gerir rétt eða missir líf
defaultDeltaTime = 120

arrow = random.randint(0, 7)

# Teiknar stig og líf
def renderContent():
	window.blit(font.render('Stig: ' + str(score), False, BLACK), (20, 20))
	window.blit(font2.render(str(health), False, BLACK), (500, 20))
	window.blit(pygame.transform.scale(heart, (64,64)), (550, 20))
	
# Þetta fall velur random ör og setur það inná með animation'i
def newArrow():
	direction = ["left", "right", "up", "down"][random.randint(0,3)]
	pick = random.randint(0, 7)

	speed = 25

	if direction == "left":
		x = WIDTH
		while x > WIDTH/2-150:
			x -= speed
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (x, HEIGHT/2-150))
			pygame.display.update()
			window.fill(BACKGROUND)
			clock.tick(ticks)
	elif direction == "right":
		x = -300
		while x < WIDTH/2-150:
			x += speed
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (x, HEIGHT/2-150))
			pygame.display.update()
			window.fill(BACKGROUND)
			clock.tick(ticks)
	elif direction == "up":
		y = HEIGHT
		while y > HEIGHT/2-150:
			y -= speed
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (WIDTH/2-150, y))
			pygame.display.update()
			window.fill(BACKGROUND)
			clock.tick(ticks)
	elif direction == "down":
		y = -300
		while y < HEIGHT/2-150:
			y += speed
			renderContent()
			window.blit(pygame.transform.scale(arrows[pick], (300,300)), (WIDTH/2-150, y))
			pygame.display.update()
			window.fill(BACKGROUND)
			clock.tick(ticks)
	return pick


STATUS = "menu"

arrows = [pygame.image.load('resources/' + str(x) + ".png") for x in ("up", "down", "right","left", "oup", "odown", "oright", "oleft")]
heart = pygame.image.load('resources/heal.png')

# Ræsir pygame og hluti í pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Hleður inn letur
font = pygame.font.Font('resources/Pixeled.ttf', 16)
font2 = pygame.font.Font('resources/Pixeled.ttf', 32)
font3 = pygame.font.SysFont('Helvetica', 16, bold=True)

# býr til gluggann
window_size = WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode(window_size)

#litirnir
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
PURPLE = [255,0,255]
LIGHT_GRAY = [168,168,168]

#bakgrunnurinn er settur á ákveðinn lit, þetta er gert svona svo að það sé auðveldara að skipta um bakgrunn
BACKGROUND = LIGHT_GRAY

running = True

# title
pygame.display.set_caption('Örvaleikurinn')

window.fill(BACKGROUND)

# klukkan
clock = pygame.time.Clock()
ticks = 60

# stig og líf
score = 0
health = 3

# deltaTime byrjar alltaf með defaultDeltaTime sem er hægt að stilla með kóðanum eftst
deltaTime = defaultDeltaTime

# Öll hljóð
menu_music = pygame.mixer.Sound('resources/menu.ogg')
menu_music.play()
music = pygame.mixer.Sound('resources/bgplay.wav')
mistake_sound = pygame.mixer.Sound("resources/No.wav")

# can_press á að koma í veg fyrir að örvatakkarnir virki á meðan þeir eru að detta inn
can_press = True

# þetta er einhvernskonar tími í ticks sem er eftir þar til að þú missir líf
delta = deltaTime

# staðsetning á ör
arrow_x = WIDTH/2-150
arrow_y = HEIGHT/2-150

randomSpeed = 1

damage_effect = False

EFFECT = RED

while running:
	if STATUS == "menu":
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.QUIT:
					running = False
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					STATUS = "play"
					menu_music.stop()
					music.play()
				elif event.key == pygame.K_i:
					STATUS = "instruction"


		window.blit(font.render("BIL = SPILA", False, BLACK), (20, 350))
		window.blit(font.render("i = LEIDBEININGAR", False, BLACK), (20, 300))
	elif STATUS == "play":
		# þetta gerir rauða bakgrunninn sem kemur þegar maður missir líf og þessi kóði lætur hann fade'a út
		if damage_effect:
			eff = 20
			r,g,b = BACKGROUND
			if r > 168:
				if r - eff >= 168:
					BACKGROUND[0] = r - eff
				else:
					BACKGROUND[0] = 168
			if g < 168:
				if g + eff <= 168:
					BACKGROUND[1] = g + eff
				else:
					BACKGROUND[1] = 168
			if b < 168:
				if b + eff <= 168:
					BACKGROUND[2] = b + eff
				else:
					BACKGROUND[2] = 168
			if r == 168 and g == 168 and b == 168:
				damage_effect = False

		# ef þú varst of lengi
		if delta <= 0:
			can_press = False
			health -= 1
			mistake_sound.play()

			arrow_x = WIDTH/2-150
			arrow_y = HEIGHT/2-150
			can_press = True
			delta = deltaTime
			if health < 1:
				STATUS = "gameover"
				BACKGROUND = LIGHT_GRAY
				window.fill(BACKGROUND)
				continue
			else:
				arrow = newArrow()
		# ef tíminn er að renna út
		if delta <= START_SHAKE:
			arrow_x += random.randint(int(-randomSpeed), int(randomSpeed))
			arrow_y += random.randint(int(-randomSpeed), int(randomSpeed))
			randomSpeed += .5
		else:
			arrow_x = WIDTH/2-150
			arrow_y = HEIGHT/2-150
			randomSpeed = 1
		# events, hér eru öll key input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key >= 273 and event.key <= 276 and can_press:
					arrow_pushed = event.key-273
					if arrow_pushed >= 0 and arrow_pushed <= 3:
						# ef það var ýtt á rétta takkann
						if arrow_pushed == arrow or (arrow == 4 and arrow_pushed == 1) or (arrow == 5 and arrow_pushed == 0) or (arrow == 6 and arrow_pushed == 3) or (arrow == 7 and arrow_pushed == 2):
							# ÞÁ FÆRÐU STIG
							score += 1
							if deltaTime > START_SHAKE + 10:
								deltaTime -= 1
							can_press = False
							delta = deltaTime
							arrow = newArrow()
							can_press = True
						else:
							# ANNARS MISSIRÐU LÍF
							health -= 1
							mistake_sound.play()
							damage_effect = True
							BACKGROUND = [255,0,0] #rauður bakgrunnur, geri þetta til að RED breytist ekki í gráan

							if health < 1:
								STATUS = "gameover"
								BACKGROUND = LIGHT_GRAY
								window.fill(BACKGROUND)
								#music.stop()
							elif delta > START_SHAKE:
								delta = START_SHAKE
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
					deltaTime = defaultDeltaTime
					randomSpeed = 1
					delta = deltaTime
					STATUS = "menu"
					music.stop()
					menu_music.play()
		window.blit(font2.render("Leik lokid", False, BLACK), (WIDTH/2-150, 20))
		window.blit(font3.render("Ýttu á bil til þess að fara til baka í main menu", False, BLACK), (20, 400))
	elif STATUS == "instruction":
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					STATUS = "menu"
		window.blit(font3.render("Leikurinn virkar þannig að það koma örvar á skjáinn og þú átt að ýta á örvatakkanna til að fá stig,", False, BLACK), (20, 20))
		window.blit(font3.render("ef þú ýtir í ranga átt, þú missir þú líf. Þú hefur bara þrjú líf til að byrja með.", False, BLACK), (20, 40))
		window.blit(font3.render("Ef örin er svört þá átt þú að ýta á örvatakkann sem bendir í sömu átt (í lyklaborðinu), en ef það", False, BLACK), (20, 80))
		window.blit(font3.render("kæmi röndótt ör (svört og hvít) þá áttu að ýta á örvatakkann sem bendir í hina áttina.", False, BLACK), (20, 100))

		window.blit(pygame.transform.scale(arrows[6], (300,300)), (60, 100))
		window.blit(pygame.transform.scale(arrows[3], (300,300)), (300, 170))

		window.blit(font.render("Yttu a ESC til ad fara ut", False, BLACK), (60, 400))
	pygame.display.update()
	window.fill(BACKGROUND)
	clock.tick(ticks)
pygame.quit()
