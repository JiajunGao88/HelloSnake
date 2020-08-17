import pygame
import random

pygame.init()
FPS = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
score = 0

snake_pos = [[240, 250], [230, 250], [220, 250]]
head_pos = [250, 250]
food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

display = pygame.display.set_mode((500, 500))


def main():

    display.fill(black)
    pygame.display.set_caption("Irregular Snake")

    playGame()


def playGame():
    global food_pos, head_pos, snake_pos, score

    direction = "RIGHT"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        snake_pos.insert(0, list(head_pos))

        if direction == "LEFT":
            head_pos[0] -= 10
        if direction == "RIGHT":
            head_pos[0] += 10
        if direction == "UP":
            head_pos[1] -= 10
        if direction == "DOWN":
            head_pos[1] += 10

        display.fill(black)

        # Draw a snake
        for position in snake_pos:
            draw_rect(white, position)

        # Draw a food
        draw_rect(green, food_pos)

        # Determine
        if head_pos != food_pos:
            snake_pos.pop()
        else:
            score += 1
            food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]

        pygame.display.update()
        FPS.tick(20)

        if hit_the_wall() or hit_the_self():
            print(f"Your final score is: {score}")
            pygame.quit()


def draw_rect(color, i):
    pygame.draw.rect(display, color, (i[0], i[1], 10, 10))


def hit_the_self():
    if head_pos in snake_pos[1:]:
        return True
    else:
        return False


def hit_the_wall():
    if head_pos[0] >= 500 or head_pos[0] < 0 or head_pos[1] >= 500 or head_pos[1] < 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
