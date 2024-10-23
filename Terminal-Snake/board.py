from utilities import clear

class Board():
    def __init__(self, width, height, blank_char):
        self.width = width
        self.height = height
        self.blank_char = blank_char
        self.board = []
        
        for i in range(height):
            self.board.append([])
            for _ in range(width):
                self.board[i].append(blank_char)
    
    def draw(self):
        clear()
        for i in self.board:
            for j in i:
                print(j, end="")
            print()
            
    def set_pos(self, char, pos_x, pos_y):
        pos_x = pos_x % self.width
        pos_y = pos_y % self.height
        
        self.board[pos_y][pos_x] = char
        
    def clear_pos(self, pos_x, pos_y):
        pos_x = pos_x % self.width
        pos_y = pos_y % self.height
        
        self.board[pos_y][pos_x] = self.blank_char
        
    def get_pos(self, pos_x, pos_y):
        pos_x = pos_x % self.width
        pos_y = pos_y % self.height
        
        return self.board[pos_y][pos_x]
    