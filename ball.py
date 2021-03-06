import pygame
import random
import sys
class Ball:


    def __init__(self,X,Y):

        self.velocity = [1,1]
        self.ball_image = pygame.image.load ('i.jpg'). convert()
        self.ball_boundary = self.ball_image.get_rect (center=(X,Y))
    
        self.rect = self.ball_image.get_rect (center=(X,Y))

if __name__ =='__main__':

    width = 800
    height = 600
    background_colour = 0,0,0
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bouncing Ball animation")
    num_balls = 4
    ball_list = []
    for number in range(num_balls):
        ball_list.append( Ball(random.randint(100, (width - 100)),random.randint(100, (height - 50))) )
    while True:
        for event in pygame.event.get():
                print event 
                if event.type == pygame.QUIT:
                        sys.exit(0)
        window.fill (background_colour)

        for ball in ball_list:
                if ball.ball_boundary.left < 0 or ball.ball_boundary.right > width:
                        
                        ball.velocity[0] = -1 * ball.velocity[0]
                if ball.ball_boundary.top < 0 or ball.ball_boundary.bottom > height:
                        
                        ball.velocity[1] = -1 * ball.velocity[1]

                ball.ball_boundary = ball.ball_boundary.move (ball.velocity)
                window.blit (ball.ball_image, ball.ball_boundary)
        pygame.display.flip()
