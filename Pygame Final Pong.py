import pygame
import random
import time

from pygame.locals import *

pygame.init()


DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK=(0 ,0 , 0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

paddleWidth = 100
paddleHeight = 2



gameDisplay=pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Pong")

clock=pygame.time.Clock()


#Make the paddle
def paddle(x,y,width,height,colour):#Make the paddle
    pygame.draw.rect(gameDisplay,colour,(x,y,width ,height), 0)

    
#make the pongball
def pongball(pongballX, pongballY, radius, colour):#Make the ball
    pygame.draw.circle(gameDisplay, colour,[pongballX, pongballY], radius, 0)

    
def livetext(livesamount):#Set up a crash function for the user if they crash
    font = pygame.font.SysFont(None, 45)
    text = font.render("Lives: "+str(livesamount),True,WHITE)
    gameDisplay.blit(text,(0,80))

    
def scoring(amount):#Function to display score
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score: "+str(amount),True,WHITE)
    gameDisplay.blit(text,(0,0))


def highestscore(highscoreamount,xpos,ypos):#Displays the high score
    font = pygame.font.SysFont(None,45)
    text = font.render("High Score: "+ str(highscoreamount),True,WHITE)
    gameDisplay.blit(text,(xpos,ypos))

        
def messageDisplay(fontDimensions,text,xPos,yPos):#Displays a message
    largeText = pygame.font.Font('freesansbold.ttf',fontDimensions)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = (xPos,yPos)
    gameDisplay.blit(textSurf, textRect)


def rules():#Function for the rules in the main menu
    rules=True
    gameDisplay.fill(BLACK)

    while rules:
        for event in pygame.event.get():#Allows you to do the events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:#Detects if they want to go back to menu
                if rectMenus.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                    menu()

        messageDisplay(18,"Rules",500,32)
        messageDisplay(25,"Don't let the ball hit below the paddle",500,150)#Rules
        messageDisplay(25,"Use A key or Left arrow key to move left", 500, 250)
        messageDisplay(25,"Use D key or Right arrow key to move right", 500, 350)
        messageDisplay (25, "To win, get a score of 50", 500,450)
        messageDisplay (25,"You have 3 lives",500,550)

        rectMenus=pygame.draw.rect(gameDisplay,RED,(900,0,100,30),0)
        messageDisplay(15,"Back to Menu",950,15)
        pygame.display.update()


def text_objects(text, font):#Helps display a message
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def menu():#Sets main menu
    highscore=0

    while True:   
        menu = True

        while menu:#Checks for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #pygame.mouse.get_pos,will get the coordinates of which the user clicks on
                    #Collidepoint checks if user clicks on the selected area
                    if rectStart.collidepoint(pygame.mouse.get_pos()) and event.button == 1:#Checks for which rectangle user clicks on
                        highscore=gameLoop(highscore)
                        break#Breaks out of the menu and calls for game
                    
                    elif rectMenu.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                        rules()
                        break#Breaks out of menu and calls for menu
                    
                    elif rectQuit.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                        pygame.quit()
                        #Quit the game

            pygame.display.update()
            clock.tick(1000)
            gameDisplay.fill(BLACK)
            #Make the title and start,quit,rules buttons..
            messageDisplay(40,"Rye's Ponggame", 500,32)#Title
            rectStart = pygame.draw.rect(gameDisplay, GREEN, (200, 100, 210, 50), 0)
            messageDisplay(35,"Play", 300,130)#Play button
            rectMenu = pygame.draw.rect(gameDisplay, BLUE,(200,300,210,50),0)
            messageDisplay(35,"Rules",300,330)#Rules button
            rectQuit = pygame.draw.rect(gameDisplay,RED,(200,500,210,50),0)
            messageDisplay(35,"Quit",300,530)#Quit button
            highestscore(highscore,500,300)#Displays the high score in the menus

        
       
#Make the game functionable
def gameLoop(highscore):#highscore as a parameter so we can return the high score with ease
    paddleX=(DISPLAY_WIDTH * 0.45)#Declare Variables
    paddleY=(DISPLAY_HEIGHT * 0.8)#Paddle coordinate
    paddlexVelocity=0#Paddle Speed
    ballStartX= 630#Ball Start Coords
    ballStartY= 72
    ballRadius = 8
    score=0
    lives = 3
    ballxVelocity = 2#Ball speed
    ballyVelocity = 2
    gameExit = False

    #Checks if user is doing any events(Checking for left and right arrows)
    while not(gameExit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    paddlexVelocity = -2.5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    paddlexVelocity = 2.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    paddlexVelocity = 0
            if event.type == pygame.MOUSEBUTTONDOWN:#Detects for back to menu or quitting the entire menu
                if rectMenuTwo.collidepoint(pygame.mouse.get_pos()):#Back to menu
                    if event.button == 1:
                        return highscore
                if rectQuitTwo.collidepoint(pygame.mouse.get_pos()):#Quits the program
                    if event.button == 1:
                        pygame.quit()

        rectMenuTwo=pygame.draw.rect(gameDisplay,BLUE,(900,0,100,30),0)
        rectQuitTwo=pygame.draw.rect(gameDisplay,RED,(900,770,100,30),0)
        paddleX+=paddlexVelocity

        #Check if ball hits wall or paddle
        if ballStartX+ballRadius >= DISPLAY_WIDTH:
            ballxVelocity *= -1#if ball hits right wall, bounce
        if ballStartX >= paddleX and ballStartX <= paddleX + paddleWidth:#checks if x pos of ball is touching paddle
            if ballStartY + ballRadius == paddleY:#checks if y pos of ball is touching paddle
                ballyVelocity *= -1
                score+=1             
        if ballStartX - ballRadius <= 0:#Makes sure ball doesn't leave the screen and bounces the ball
            ballxVelocity *= -1
        if ballStartY - ballRadius <= 0:
            ballyVelocity *= -1
        ballStartX += ballxVelocity
        ballStartY += ballyVelocity#Adds the velocity of the ball movements
        #Checks if paddle leaves screen
        if paddleX < 0:
            paddlexVelocity = 0
            paddleX=0
        if paddleX + paddleWidth >= DISPLAY_WIDTH:
            paddlexVelocity = 0
            paddleX=DISPLAY_WIDTH - paddleWidth
        if ballStartY == DISPLAY_HEIGHT: #Sees if the ball ever goes under the paddle, if so, crashes
            ballStartX=630#once it crashes, replace the ball at original spot
            ballStartY=72
            paddleX=(DISPLAY_WIDTH * 0.45)
            paddleY=(DISPLAY_HEIGHT * 0.8)
            lives -=1

        #Endgame conditions
        if score >= highscore:#Checks for a highscore
            highscore = score
        if lives == 0:#Displays a losing message if they lose
            gameDisplay.fill(BLACK)
            messageDisplay(100,"You lost!",500,400)
            pygame.display.update()
            clock.tick(60)
            time.sleep(1.5)
            return highscore            
        if score == 50:#Displays a winning message if they win
            gameDisplay.fill(BLACK)
            messageDisplay (100,"You win!",500,400)
            pygame.display.update()
            time.sleep(1.5)
            return highscore
            
 
        gameDisplay.fill(BLACK)#Set background
        paddle(paddleX,paddleY,paddleWidth,paddleHeight,WHITE)#Call for paddle
        pygame.draw.rect(gameDisplay,BLUE,(900,0,100,30),0)#Makes the option of letting them return to the menu during the game
        messageDisplay(15,"Back to Menu",950,15)
        pygame.draw.rect(gameDisplay,RED,(900,770,100,30),0)#Makes the option of quitting the entire game
        messageDisplay(15,"Quit",950,785)
        pongball(ballStartX, ballStartY, ballRadius, WHITE)#Display the ball
        scoring(score)#Displays the current score 
        highestscore(highscore,0,40)#Displays high score during the game
        livetext(lives)#Display lives
        clock.tick(720)
        pygame.display.update()



menu()#Call for the game

