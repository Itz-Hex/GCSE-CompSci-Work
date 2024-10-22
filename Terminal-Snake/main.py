from time import sleep

from board import Board 

def main():
    board = Board(10, 10, "□")
        
    playing = True
    x = 0
    y = 0
    length = 2
    direction = "up"
    old_dir = direction
        
    while playing:
        old_dir = direction
        direction = input()
        
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
        
        if direction == "down":
            y += 1
        elif direction == "up":
            y -= 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        
        for i in range(1, length+1):
            if direction == "down":
                board.set_pos("■", x, y-i)
            elif direction == "up":
                board.set_pos("■", x, y+i)    
            elif direction == "left":
                board.set_pos("■", x+i, y)    
            elif direction == "right":
                board.set_pos("■", x-i, y)    
        
        board.draw()
        
        sleep(0.6)
    
    return

if __name__ == "__main__":
    main()