import pygame, sys, random
from pygame.locals import *
pygame.init()

def game() :
	width, height = 600, 400
	screen= pygame.display.set_mode((width,height))
	pygame.display.set_caption('My Star Catcher Game')
	background=pygame.image.load('newbg.jpg')
	background=pygame.transform.scale(background, (width,height))
	
	
#load target
	targetnum=5
	target=[]
	for i in range(targetnum) : 	
		targetimage= pygame.image.load('ball.png')
		targetimage=pygame.transform.scale(targetimage, (20,20))
		target.append([])
		target[i]=targetimage
	targetpos=[]
	targetspace=height/targetnum-10
	for i in range(targetnum):
		targetpos.append([])
		for j in range(2):
			targetpos[i].append(i*j*targetspace+50)

	#targetvisible = True

	#target visible
	targetvisible=[]
	for i in range(targetnum):
		targetvisible.append(True)
	
#load player
	player = pygame.image.load('hoop.png')	
	
	player=pygame.transform.scale(player, (40,40))
	px,py = width/2,height/2
	

	clock=pygame.time.Clock()
	gamespeed=100	
	movex = movey = 0
	speed=[]
	for i in range(targetnum):
		speed.append([])
		for j in range(2) :
			speed[i].append(gamespeed*random.randint(1,5))
	
#scores
	score=0
	
	gamefont=pygame.font.Font(None, 30)
	scoretext=gamefont.render('Player Score: '+str(score), 2, [255,0,0])
	boxsize=scoretext.get_rect()
	scoreXpos=(width-boxsize[2])/2
	
	while True:
		#targetpos.move_ip(speed)
		seconds=clock.tick()/1000.0
		scoretext=gamefont.render('Player Score: '+str(score), 2, [255,0,0])
		screen.blit(background, (0,0))
		screen.blit(player, (px,py))
		screen.blit(scoretext, [scoreXpos, 20])

#targets blitted
		for i in range(targetnum):
			if targetvisible[i] :
				targetpos[i][0]+=seconds*speed[i][0]
				targetpos[i][1]+=seconds*speed[i][1]
				targetimage=target[i]
				x=targetpos[i][0]
				y=targetpos[i][1]
				screen.blit(targetimage, (x,y))
			else:
				targetimage=target[i]
				x=width-50
				y=height-(i+1)*targetspace
				screen.blit(targetimage, (x,y))
		
		#if targetvisible==True :
			#seconds=clock.tick()/1000.0
			#targetpos[0]+=seconds*speed[0]
			#targetpos[1]+=seconds*speed[1]
			#screen.blit(target,targetpos)
		#else:
			#screen.blit(target,(width-50,height-50))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					movex = 2
				if event.key == K_LEFT:
					movex = -2 
				if event.key == K_UP:
					movey = -2
				if event.key == K_DOWN:
					movey = 2
			elif event.type == KEYUP:
				if event.key == K_RIGHT:
					movex = 0
				if event.key == K_LEFT:
					movex = 0
				if event.key == K_UP:
					movey = 0
 				if event.key == K_DOWN:
					movey = 0
		px=px+movex
		py=py+movey
		for i in range(targetnum):
		
			if targetpos[i][0]+20 > width or targetpos[i][0] < 0:
				speed[i][0]=-speed[i][0]
				targetpos[i][0]+=seconds*speed[i][0]
		
			if targetpos[i][1] > height or targetpos[i][1] < 0:
				speed[i][1]=-speed[i][1]
				targetpos[i][1]+=seconds*speed[i][1]
		
#collision
		for i in range(targetnum):
			if abs(targetpos[i][0]-px) < 20 and abs(targetpos[i][1]-py) < 20:
				targetvisible[i]=False
				score+=10
				targetpos[i]=[width+100,height+100]

if __name__=='__main__':
	game()
