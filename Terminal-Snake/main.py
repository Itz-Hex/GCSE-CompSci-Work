from time import sleep
from random import randint
from collections import deque

from board import Board 

def main():
    board = Board(10, 10, "⬜")
        
    playing = True
    x = 0
    y = 0
    length = 4
    direction = "right"
    snake = []
    
    board.set_pos("🍎", randint(1,9), randint(1,9))
    
    for i in range(length+1):
        snake.append([i, 0])
        
    while playing:
        direction = input()

        if "A" in direction:
            direction = "up"
        elif "B" in direction:
            direction = "down"
        elif "C" in direction:
            direction = "right"
        elif "D" in direction:
            direction = "left"
        else:
            pass
        
        for part in snake:
            x = part[0]
            y = part[1]
            board.clear_pos(x, y)
                
        new_head_pos = list(snake[0])
        
        match direction:
            case "up":
                new_head_pos[1] -= 1
            case "down":
                new_head_pos[1] += 1
            case "right":
                new_head_pos[0] += 1
            case "left":
                new_head_pos[0] -= 1
                                
        if board.get_pos(new_head_pos[0], new_head_pos[1]) == "🍎":
            length += 1
            
            generated = False
            
            while not generated:
                apple_x = randint(0, 9)
                apple_y = randint(0, 9)
                if board.get_pos(apple_x, apple_y) == "🟩":
                    pass
                
                board.set_pos("🍎", randint(0,9), randint(0,9))
                generated = True
            
            snake.insert(0, new_head_pos)
        elif board.get_pos(new_head_pos[0], new_head_pos[1]) == "🟩": # board is being cleared of snake before this is check therefore its not working
            playing = False
            input("GAME OVER!")
            break
        else:
            snake[-1] = new_head_pos
            
            snake_deque = deque(snake)
            snake_deque.rotate(1)
            
            snake = list(snake_deque)
        
        for part in snake:
            x = part[0]
            y = part[1]
            board.set_pos("🟩", x, y)
        
        board.draw()
        
        sleep(0.6)

    
    return

if __name__ == "__main__":
    main()