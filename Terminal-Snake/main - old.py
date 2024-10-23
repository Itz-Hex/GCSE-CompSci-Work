from time import sleep
from random import randint

from board import Board 

def main():
    board = Board(10, 10, "⬜")
        
    playing = True
    x = 0
    y = 0
    length = 2
    direction = "up"
    old_dir = direction
    snake = []
    
    board.set_pos("🍎", randint(1,9), randint(1,9))
    
    for i in range(length):
        snake.append([0, i])
        
    while playing:
        old_dir = direction
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
        
        for i in range(1, length+1):
            if old_dir == "down":
                board.clear_pos(x, y-i)
            elif old_dir == "up":
                board.clear_pos(x, y+i)    
            elif old_dir == "left":
                board.clear_pos(x+i, y)    
            elif old_dir == "right":
                board.clear_pos(x-i, y) 
        
        board.clear_pos(x, y)
        
        apple_helper = [0,0]
        
        if direction == "down":
            y += 1
            apple_helper = [0, 1]
        elif direction == "up":
            y -= 1
            apple_helper = [0, -1]
        elif direction == "left":
            x -= 1
            apple_helper = [-1, 0]
        elif direction == "right":
            x += 1
            apple_helper = [1, 0]
            
        input(board.get_pos(x + apple_helper[0] , y + apple_helper[1] ))
            
        if board.get_pos(x + apple_helper[0] , y + apple_helper[1] ) == "🍎":
            input("HI")
            board.set_pos("🍎", randint(0,9), randint(0,9))
            length += 1
        
        for i in range(1, length+1):
            if direction == "down":
                board.set_pos("🟩", x, y-i)
            elif direction == "up":
                board.set_pos("🟩", x, y+i)    
            elif direction == "left":
                board.set_pos("🟩", x+i, y)    
            elif direction == "right":
                board.set_pos("🟩", x-i, y)    
        
        board.draw()
        
        sleep(0.6)

    
    return

if __name__ == "__main__":
    main()