#!/usr/bin/env python3

import sys, pygame, random

WHITE = [255,255,255]
BLACK = [0,0,0]

class Game:
  def __init__(self):
    pygame.init()
    self.height = 480
    self.width = 640
    self.screen = pygame.display.set_mode([self.width, self.height])

  def event_update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          paddle1.y -= paddle1.speed
        if event.key == pygame.K_DOWN:
          paddle1.y += paddle1.speed
         

class Ball:
  def __init__(self):
    self.y = int(game.height/2)
    self.x = int(game.width/2)
    self.radius = 10
    self.speed = [-5,-1]

class Paddle():
  def __init__(self, x, y):
    self.x = x
    self.y = y 
    self.height = 90
    self.width = 20
    self.speed = 30

game = Game()  
ball = Ball()
paddle1 = Paddle(10, 240)
paddle2 = Paddle(610, 240)

while True:
  if ball.x - ball.radius  < 0 or ball.x + ball.radius > game.width:
    ball.x = int(game.height/2)
    ball.y = int(game.width/2)
  if ball.y - ball.radius < 0 or ball.y + ball.radius > game.height:
    ball.speed[1] = -ball.speed[1]
  if paddle1.y < 0:
    paddle1.y = 0
  if paddle1.y + paddle1.height > game.height:
    paddle1.y = game.height - paddle1.height
  if ball.x - ball.radius < paddle1.x + paddle1.width and ball.y < paddle1.y + paddle1.height and ball.y > paddle1.y:
    ball.speed[0] = -ball.speed[0] 
  if ball.y + ball.radius > paddle1.y and ball.x > paddle1.x and ball.x < paddle1.x + paddle1.width:
    ball.speed[1] = -ball.speed[1]
  if ball.x + ball.radius > paddle2.x and ball.y < paddle2.y + paddle2.height and ball.y > paddle2.y:
    ball.speed[0] = -ball.speed[0]

  
  game.event_update()
  game.screen.fill([0,0,0])
  
  ball.x += ball.speed[0]
  ball.y += ball.speed[1]
  
  pygame.draw.rect(game.screen, WHITE, [paddle1.x, paddle1.y, paddle1.width, paddle1.height])
  pygame.draw.rect(game.screen, WHITE, [paddle2.x, paddle2.y, paddle2.width, paddle2.height])
  pygame.draw.circle(game.screen, WHITE, [ball.x, ball.y], ball.radius)
  pygame.display.update()

