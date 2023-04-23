from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

racket1 = Player('platform.jpg', 30, 200,10,50,10)
racket2 = Player('platform.jpg',520,200,10,50,10)
ball = GameSprite('tennis.png',200,200,50,50,10)

speed_x = 1
speed_y = 1

font.init()
font = font.SysFont('veranda', 70)
loseL = font.render('player L lose', True, (180,0,0))
loseR = font.render('player R lose', True, (180,0,0))

# font1 = font.SysFont('veranda', 20)
res = font.render('R to reset', True, (180,0,0))

game = True
finish = False
clock = time.Clock()
FPS = 60

time_wait = 5*FPS
wait= time_wait

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
                ball.rect.x = 200
                ball.rect.y = 200
        
    if not finish:
        if wait <= 0:
            if speed_y > 0:
                speed_y +=1
            else:
                speed_y -= 1
            wait = time_wait
        else:
            wait -= 1

        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if racket1.rect.colliderect(ball.rect) or racket2.rect.colliderect(ball.rect):
            speed_x *= -1
            if speed_x > 0:
                speed_x +=1
            else:
                speed_x -= 1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(loseL, (150,200))
            window.blit(res, (150,win_height - 200))
            
           # game = False
        if ball.rect.x > win_width:
            finish = True
            window.blit(loseR, (150,200))
            #game = False

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)


