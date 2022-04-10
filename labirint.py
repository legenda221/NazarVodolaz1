from pygame import *  #  Подключает библиотеку "пайгейм"
mixer.init()
class GameSprite(sprite.Sprite):  # создаём класс-наследник "геймспрайт", от класса спрайт.спрайт
    def __init__(self, player_image, player_x, player_y, size_x, size_y):  # сщздание обьекта 
        sprite.Sprite.__init__(self)  # вызываем конструктор
        self.image = transform.scale(image.load(player_image), (size_x, size_y))  # создаем фон
        self.rect = self.image.get_rect()
        self.rect.x = player_x  # Свойству "rect.x"(отвечает за положение спрайта) задаём начальное положение "player_x"
        self.rect.y = player_y  # Cвойству "rect.y"(отвечает за положение спрайта) задаем начальное положение "player_x"
    def reset(self):  # ----
        window.blit(self.image, (self.rect.x, self.rect.y))  #отрисовка изображения

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):  # !!! Распишите какие параметры передаём. что это за параметры? !!!
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)  # !!! что это за строчка, зочем она, что деа=лает, что за параметры  !!!
        self.x_speed = player_x_speed  # Cвойству "x_speed" задаем начальную скорость "player_x_speed"
        self.y_speed = player_y_speed  # Cвойству "y_speed" задаем начальную скорость "player_y_speed"
    def update(self):  # разберем на уроке
         # ---- ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
         # ---- сначала движение по горизонтали
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
             # ---- если зашли за стенку, то встанем вплотную к стене
            platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:  # ---- идём направо, правый край персонажа - вплотную к левому краю стены
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)  # ---- если коснулись сразу нескольких, то правый край - минимальный из возможных
        elif self.x_speed < 0:  # ---- идем налево, ставим левый край персонажа вплотную к правому краю стены
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)  # ---- если коснулись нескольких стен, то левый край - максимальный
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
             # ---- если зашли за стенку, то встанем вплотную к стене
            platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:  # ---- идем вниз
            for p in platforms_touched:
                 # ---- Проверяем, какая из платформ снизу самая высокая, выравниваемся по ней, запоминаем её как свою опору:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:  # ---- идём вверх
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)  # ---- выравниваем верхний край по нижним краям стенок, на которые наехали

win_width = 700  # задаем ширину фона
win_height = 500  # задаем высоту фона
display.set_caption("Лабиринт")  # создаем название окна
window = display.set_mode((win_width, win_height))  # создаем поверхность дисплея
BLACK = (0, 0, 0)  # цвет

s = mixer.Sound('krupnaya-obezyana-krichit-i-besitsya.wav')
v = mixer.Sound('beshennyiy-lay-ovcharki.waw')

barriers = sprite.Group()  # создаем группу для обьектов

w1 = GameSprite('stone.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)  # задаем ширину 1 ширина 2 и высату 3
w2 = GameSprite('stine.png', 370, 100, 50, 400)

barriers.add(w1)  # обьединяем
barriers.add(w2)
 

packman = Player('packman.png', 5, win_height - 80, 80, 80, 0, 0)  # задаем параметры героя пакмена
monster = GameSprite('ninga.png', win_width - 80, 180, 80, 80)  # задаем антаганиста
final_sprite = GameSprite('hero.png', win_width - 85, win_height - 100, 80, 80)  # человечек при косание которого игра закончится
 
finish = False  #  !!! Что за переменная, что делает? !!!
# игровой цикл
run = True
while run:  #  Бесконечный цикл
    time.delay(50)  #  Задержка, цикл срабатывает каждую 0.05 секунд
    for e in event.get():
        if e.type == QUIT:  # выход
            run = False
        elif e.type == KEYDOWN:  # любая клавиша нажата
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_g:
                BLACK = (0, 155, 0)
            elif e.key == K_RIGHT:  # нажата клавиша вправо
                packman.x_speed = 5  # скоростделаем скорость 5
            elif e.key == K_UP : 
                packman.y_speed = -5
            elif e.key == K_DOWN :
                packman.y_speed = 5
        elif e.type == KEYUP:  # проверка на отпускание клавиши
            if e.key == K_LEFT : 
                packman.x_speed = 0
            elif e.key == K_RIGHT:  # отпускаем клавишу вправо
                packman.x_speed = 0  # скорость становится 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 3:
                BLACK = (0, 64, 0)
            elif e.button == 1:    
                packman.rect.x = e.pos[0]
                packman.rect.y = e.pos[1]
    if not finish: # если игра не законцена( финиш = фолс) то мы играем. если финиш = тру, то выходим из цикла
        # рисуем объекты
        w1.reset()
        w2.reset()
        window.fill(BLACK) # заливка 
        barriers.draw(window)
        monster.reset()
        final_sprite.reset() # отрисовавание спрайта
        packman.reset() # отрисовавание  игрогово спрайта 
        packman.update() # проверка спрайта на касание с объектами


        if sprite.collide_rect(packman, monster): # обноружение столкновения пкмана и монстрика
            s.play()
            finish = True # финальный спраййт
            img = image.load('nope.jpg') #надпись и картинка конец
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0)) # параметры для конечной заставки


        if sprite.collide_rect(packman, final_sprite): # если пакмен врезался не показываем картинку
            finish = True
            v.play()
            img = image.load('final.png')
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
 
    display.update() # чтоюы отображался на маниторе пользователя
        
