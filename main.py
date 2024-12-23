import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("지렁이 게임")
        self.clock = pygame.time.Clock()
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (BLOCK_SIZE, 0)  # 초기 방향: 오른쪽
        self.food = [self.spawn_food(), self.spawn_food()]  # 먹이를 2개로 설정
        self.score = 0
        self.running = True
        self.font = pygame.font.SysFont("Arial", 24)

    def spawn_food(self):
        x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
        return (x, y)

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def draw_food(self):
        for food_item in self.food:
            pygame.draw.rect(self.screen, FOOD_COLOR, (*food_item, BLOCK_SIZE, BLOCK_SIZE))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.snake.insert(0, new_head)

        if new_head in self.food:
            self.score += 1
            self.food.remove(new_head)  # 먹이를 제거
            # 새로운 먹이를 추가
            self.food.append(self.spawn_food())
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in self.snake[1:]:
            self.running = False

    def run(self):
        while self.running:
            self.screen.fill(BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, BLOCK_SIZE):
                        self.direction = (0, -BLOCK_SIZE)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -BLOCK_SIZE):
                        self.direction = (0, BLOCK_SIZE)
                    elif event.key == pygame.K_LEFT and self.direction != (BLOCK_SIZE, 0):
                        self.direction = (-BLOCK_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-BLOCK_SIZE, 0):
                        self.direction = (BLOCK_SIZE, 0)

            self.move_snake()
            self.check_collision()
            self.draw_snake()
            self.draw_food()
            self.draw_score()  # 점수 표시

            pygame.display.flip()
            self.clock.tick(10)  # 게임 속도 조절

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
game.run()  # 게임 실행