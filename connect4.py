from typing import List, Optional, Tuple
from colorama import Fore, Style, init

# Initialize colorama for colored output
init()

class Connect4:
    def __init__(self, rows: int = 6, cols: int = 7, win_count: int = 4):
        self.rows = rows
        self.cols = cols
        self.win_count = win_count
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 1
        self.symbols = {1: f'{Fore.RED}●{Style.RESET_ALL}', 
                       2: f'{Fore.YELLOW}●{Style.RESET_ALL}'}

    def display_board(self) -> None:
        # Print column numbers
        print('\n  ' + '   '.join(str(i) for i in range(1, self.cols + 1)))
        
        # Print the board
        for row in self.board:
            print('│ ' + ' │ '.join(cell for cell in row) + ' │')
            print('└───' + '┴───' * (self.cols - 1) + '┘')

    def is_valid_move(self, col: int) -> bool:
        return 1 <= col <= self.cols and self.board[0][col-1] == ' '

    def drop_piece(self, col: int) -> Optional[Tuple[int, int]]:
        if not self.is_valid_move(col):
            return None
        
        # Find the lowest empty position in the column
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col-1] == ' ':
                self.board[row][col-1] = self.symbols[self.current_player]
                return row, col-1
        return None

    def check_winner(self, last_move: Tuple[int, int]) -> bool:
        if last_move is None:
            return False

        row, col = last_move
        player_symbol = self.board[row][col]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horizontal, vertical, diagonals

        for dr, dc in directions:
            count = 1
            # Check in positive direction
            r, c = row + dr, col + dc
            while (0 <= r < self.rows and 0 <= c < self.cols and 
                   self.board[r][c] == player_symbol):
                count += 1
                r, c = r + dr, c + dc

            # Check in negative direction
            r, c = row - dr, col - dc
            while (0 <= r < self.rows and 0 <= c < self.cols and 
                   self.board[r][c] == player_symbol):
                count += 1
                r, c = r - dr, c - dc

            if count >= self.win_count:
                return True

        return False

    def is_board_full(self) -> bool:
        return all(cell != ' ' for cell in self.board[0])

    def switch_player(self) -> None:
        self.current_player = 3 - self.current_player  # Switches between 1 and 2 