from connect4 import Connect4
from colorama import Fore, Style

def main():
    game = Connect4()
    
    print(f"\n{Fore.CYAN}Welcome to Connect 4!{Style.RESET_ALL}")
    print("Players take turns dropping pieces into columns (1-7)")
    print(f"Player 1: {Fore.RED}●{Style.RESET_ALL}")
    print(f"Player 2: {Fore.YELLOW}●{Style.RESET_ALL}\n")

    while True:
        game.display_board()
        
        # Show current player's turn
        player_color = Fore.RED if game.current_player == 1 else Fore.YELLOW
        print(f"\n{player_color}Player {game.current_player}'s turn{Style.RESET_ALL}")
        
        # Get player move
        while True:
            try:
                col = int(input("Enter column number (1-7): "))
                if game.is_valid_move(col):
                    break
                print("Invalid move! Column is full or out of range.")
            except ValueError:
                print("Please enter a valid number between 1 and 7.")

        # Make move
        last_move = game.drop_piece(col)
        
        # Check for winner
        if game.check_winner(last_move):
            game.display_board()
            print(f"\n{player_color}Player {game.current_player} wins!{Style.RESET_ALL}")
            break
            
        # Check for draw
        if game.is_board_full():
            game.display_board()
            print("\nIt's a draw!")
            break
            
        game.switch_player()

if __name__ == "__main__":
    main() 