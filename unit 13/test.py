import tkinter as tk
import random

class LudoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ludo Game")

        # Canvas for the board
        self.canvas = tk.Canvas(self.master, width=600, height=600, bg='white')
        self.canvas.pack()

        # Initialize the grid
        self.grid = self.create_grid()

        # Draw the board
        self.draw_board()

        # Players, positions, and paths
        self.players = ['red', 'blue', 'green', 'yellow']
        self.current_player_index = 0  # Track current player
        self.positions = {player: {} for player in self.players}  # Track piece positions on grid
        self.pieces = self.init_pieces()  # Initialize player pieces
        self.paths = self.create_paths()  # Define paths for all players

        # Dice roll button
        self.roll_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Dice result display
        self.dice_label = tk.Label(self.master, text="Dice Roll: ")
        self.dice_label.pack()

        # Turn display
        self.turn_label = tk.Label(self.master, text=f"{self.players[self.current_player_index]}'s Turn")
        self.turn_label.pack()

        # State tracking for turn and dice
        self.dragged_piece = None
        self.dice_value = 0
        self.valid_moves = []

    def create_grid(self):
        """Create the Ludo grid layout."""
        grid = []
        for i in range(15):  # 15x15 grid
            row = []
            for j in range(15):
                row.append((i, j))
            grid.append(row)
        return grid

    def draw_board(self):
        """Draw the Ludo board on the canvas."""
        cell_size = 40
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')

        # Safe zones and home areas
        self.canvas.create_rectangle(0, 0, 6 * cell_size, 6 * cell_size, fill='red')  # Red home
        self.canvas.create_rectangle(9 * cell_size, 0, 15 * cell_size, 6 * cell_size, fill='blue')  # Blue home
        self.canvas.create_rectangle(0, 9 * cell_size, 6 * cell_size, 15 * cell_size, fill='green')  # Green home
        self.canvas.create_rectangle(9 * cell_size, 9 * cell_size, 15 * cell_size, 15 * cell_size, fill='yellow')  # Yellow home

        # Central safe zone
        self.canvas.create_rectangle(6 * cell_size, 6 * cell_size, 9 * cell_size, 9 * cell_size, fill='gray')

    def create_paths(self):
        """Define movement paths for each player."""
        paths = {
            'red': [(6, i) for i in range(5, -1, -1)] + [(i, 0) for i in range(6, 15)] + [(14, i) for i in range(1, 6)] + [(i, 5) for i in range(14, 6, -1)] + [(7, 6), (7, 7), (6, 7)],
            'blue': [(i, 8) for i in range(0, 6)] + [(6, i) for i in range(6, 15)] + [(7, 14), (8, 14)] + [(i, 13) for i in range(8, 15)] + [(14, i) for i in range(14, 8, -1)] + [(13, 8), (12, 8)],
            'green': [(8, i) for i in range(14, 8, -1)] + [(i, 8) for i in range(14, 6, -1)] + [(7, 7), (7, 6)] + [(i, 5) for i in range(6, -1, -1)] + [(0, i) for i in range(6, 14)] + [(1, 14), (2, 14)],
            'yellow': [(8, i) for i in range(6, 15)] + [(i, 14) for i in range(6, -1, -1)] + [(0, i) for i in range(14, 8, -1)] + [(1, 8), (2, 8)] + [(i, 7) for i in range(2, 6)] + [(6, 6), (6, 7)],
        }
        return paths

    def init_pieces(self):
        """Initialize player pieces."""
        pieces = {}
        positions = {
            'red': [(1, 1), (1, 2), (2, 1), (2, 2)],
            'blue': [(10, 1), (10, 2), (11, 1), (11, 2)],
            'green': [(1, 10), (1, 11), (2, 10), (2, 11)],
            'yellow': [(10, 10), (10, 11), (11, 10), (11, 11)]
        }

        cell_size = 40
        for player, coords in positions.items():
            pieces[player] = []
            for (row, col) in coords:
                x1, y1 = col * cell_size + 5, row * cell_size + 5
                x2, y2 = x1 + 30, y1 + 30
                piece = self.canvas.create_oval(x1, y1, x2, y2, fill=player, tags=player)
                pieces[player].append(piece)
                self.positions[player][piece] = (row, col)  # Track initial positions
        return pieces

    def roll_dice(self):
        """Simulate a dice roll and update turn display."""
        self.dice_value = random.randint(1, 6)
        self.dice_label.config(text=f"Dice Roll: {self.dice_value}")
        self.turn_label.config(text=f"{self.players[self.current_player_index]}'s Turn")
        self.valid_moves = self.calculate_valid_moves()

    def calculate_valid_moves(self):
        """Calculate valid moves for the current player's pieces."""
        player = self.players[self.current_player_index]
        valid_moves = []
        path = self.paths[player]

        for piece, position in self.positions[player].items():
            if position in path:
                current_index = path.index(position)
                new_index = current_index + self.dice_value
                if new_index < len(path):
                    valid_moves.append((piece, path[new_index]))
        return valid_moves

    def move_piece(self, piece):
        """Move a piece if it is a valid move."""
        if self.dice_value == 0 or not self.valid_moves:
            return  # Cannot move without rolling the dice

        player = self.players[self.current_player_index]
        for valid_piece, new_position in self.valid_moves:
            if valid_piece == piece:
                self.positions[player][piece] = new_position
                self.update_piece_position(piece, new_position)
                self.end_turn()
                return

    def update_piece_position(self, piece, position):
        """Update the piece's position on the canvas."""
        row, col = position
        x1, y1 = col * 40 + 5, row * 40 + 5
        x2, y2 = x1 + 30, y1 + 30
        self.canvas.coords(piece, x1, y1, x2, y2)

    def end_turn(self):
        """End the current player's turn and switch to the next player."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.dice_value = 0
        self.turn_label.config(text=f"{self.players[self.current_player_index]}'s Turn")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = LudoGame(root)
    root.mainloop()
