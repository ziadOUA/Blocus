"""
             ,adba,             88  Projet : Blocus
             8I  I8             88  But : Créer une version à deux joueurs du jeu 'Blokus' 
             "8bdP'             88  Création : 15/12/2023 10:22
888888888   ,d8"8b  88  ,adPPYb,88  Dernière modification : 26/12/2023
     a8P" .dP'   Yb,8I a8"    `Y88  
  ,d8P'   8P      888' 8b       88  
,d8"      8b,   ,dP8b  "8a,   ,d88  
888888888 `Y8888P"  Yb  `"8bbdP"88  MIT - NSI
"""

# ═══════════════════════════════ IMPORTATIONS ═══════════════════════════════

from tkinter import Label, Tk, Canvas
from tkinter import messagebox
from tkinter.ttk import Style, Button, Frame
import os

# ════════════════════════════════════════════════════════════════════════════
# ════════════════════════════ CORPS DU PROGRAMME ════════════════════════════
# ════════════════════════════════════════════════════════════════════════════

# ══════════ Variables & Constantes

player_1_pieces_list = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', 'O', 'O', ' ', 'O', ' ', 'O', ' ', ' ', 'O', ' ', ' '],
                        [' ', 'O', 'O', ' ', 'O', 'O', 'O', ' ', 'O', 'O', 'O', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
                        [' ', ' ', 'O', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', 'O', 'O', ' ', 'O', 'O', 'O', ' ', ' ', 'O', 'O', ' '],
                        [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' '],
                        [' ', 'O', 'O', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' '],
                        [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', 'O', ' '],
                        [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' '],
                        [' ', ' ', 'O', ' ', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' ', ' ', 'O', ' '],
                        [' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'O', 'O', ' '],
                        [' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', 'O', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', 'O', 'O', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O', ' '],
                        [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' '],
                        [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' '],
                        [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O', ' '],
                        [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', ' '],
                        [' ', 'O', 'O', ' ', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O', 'O', 'O', 'O', ' '],
                        [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

player_2_pieces_list = [i[:] for i in player_1_pieces_list]

j1_has_selected_piece = False
j2_has_selected_piece = False

orientation_id = 0

last_event_coordinates_copy = []
directions_from_center_copy = []

board = []

current_player = 0 # Le joueur 1 commence
board_cell_size = 38
board_size = 16

red_corners_coordinates = []
blue_corners_coordinates = []
common_corners_coordinates = []

# Palette source

md_sys_color_primary_light = "#164fe1"
md_ref_palette_primary70 = "#90a7ff"
md_sys_color_on_primary_light = "#ffffff"
md_sys_color_primary_container_light = "#dce1ff"
md_sys_color_on_primary_container_light = "#001551"

md_sys_color_secondary_light = "#595d72"
md_sys_color_on_secondary_light = "#ffffff"
md_sys_color_secondary_container_light = "#dee1f9"
md_sys_color_on_secondary_container_light = "#161b2c"

md_sys_color_tertiary_light = "#c00100"
md_ref_palette_tertiary70 = "#ff8a78"
md_sys_color_on_tertiary_light = "#ffffff"
md_sys_color_tertiary_container_light = "#ffdad4"
md_sys_color_on_tertiary_container_light = "#410000"

md_sys_color_background_light = "#ffffff"
md_sys_color_on_background_light = "#1b1b1f"
md_sys_color_surface_light = "#fefbff"
md_sys_color_on_surface_light = "#1b1b1f"
md_sys_color_surface_variant_light = "#e2e1ec"
md_sys_color_on_surface_variant_light = "#45464f"
md_sys_color_outline_light = "#767680"
md_sys_color_inverse_on_surface_light = "#f2f0f4"
md_sys_color_inverse_surface_light = "#303034"
md_sys_color_inverse_primary_light = "#b7c4ff"
md_sys_color_shadow_light = "#000000"
md_sys_color_surface_tint_light = "#164fe1"
md_sys_color_outline_variant_light = "#c6c5d0"
md_sys_color_scrim_light = "#000000"

# Palette

background_color = md_sys_color_background_light # Couleur de fond du programme
surface_color = md_sys_color_surface_variant_light # Couleur de surface (là où les pièces sont placées par exemple)

placed_piece_red = md_sys_color_tertiary_light # Couleur d'une pièce rouge placée
valid_placement_red = md_ref_palette_tertiary70 # Couleur de survol d'une pièce rouge, si elle peut être placée à l'endroit choisi
placed_piece_blue = md_sys_color_primary_light # Couleur d'une pièce bleue placée
valid_placement_blue = md_ref_palette_primary70 # Couleur de survol d'une pièce bleue, si elle peut être placée à l'endroit choisi
invalid_placement = md_sys_color_outline_variant_light # Couleur de survol lorsque la pièce ne peut pas être placée à l'endroit choisi

board_cell_outline_color = md_sys_color_outline_variant_light # Couleur de bordure des cases du plateau

# ══════════ Classe principale


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1280x720') # On définit la taille initiale de la fenêtre
        self.master.title('Blocus') # On définit le titre de la fenêtre

        style = Style() # On définit un style
        style.theme_use('default') # On utilise le style par défaut pour modifier plus facilement les boutons
        style.configure('TButton', font=('Arial', 30, 'bold'), background='red') # On ajoute du style pour les boutons
        style.configure('TFrame', background=background_color) # On change la couleur de fond des cadres "Frame"
        style.map('TButton', background=[('active', '#ff0000'), ('disabled', '#f0f0f0')])

        self.main_menu() # Affiche le menu principal dès le démarrage du programme

    def main_menu(self):
        for i in self.master.winfo_children():
            i.destroy() # On supprime tout le contenu de la fenêtre

        main_menu_frame = Frame(self.master) # On crée le cadre principal
        main_menu_frame.pack(expand=True) # On affiche le cadre dans la fenêtre

        game_mode_grid_style = {"padx": 10, "sticky": "ew"} # On définit un style par défaut pour les éléments ajoutés à la grille

        label = Label(main_menu_frame, text="BLOCUS") # On crée le texte "BLOCUS"
        label.grid(column=1, row=1, pady=10, **game_mode_grid_style) # On affiche le texte dans le cadre

        play_button = Button(main_menu_frame, text="Jouer", command=self.select_game_mode) # On crée le bouton "Jouer"
        play_button.grid(row=4, column=1, **game_mode_grid_style) # On affiche le bouton "Jouer"

        about_button = Button(main_menu_frame, text="À propos", command=lambda: messagebox.showinfo("Blocus", "Projet supervisé de NSI\nZiad & Djibril")) # On crée le bouton "À propos"
        about_button.grid(row=5, column=1, **game_mode_grid_style, pady=10) # On affiche le bouton

    def select_game_mode(self):
        for i in self.master.winfo_children():
            i.destroy() # idem

        main_menu_frame = Frame(self.master)
        main_menu_frame.pack(expand=True)

        game_mode_grid_style = {"padx": 10, "sticky": "ew"}

        label = Label(main_menu_frame, text="Sélectionnez le mode de jeu")
        label.grid(row=0, column=1, pady=10, **game_mode_grid_style)

        back_button = Button(main_menu_frame, text="Retour", command=self.main_menu, style='TButton') #
        back_button.grid(row=1, column=1, **game_mode_grid_style)

        start_blocus_classic_game_button = Button(main_menu_frame, text="Blocus Classic", command=self.blocus_classic, style='TButton') #
        start_blocus_classic_game_button.grid(row=2, column=1, **game_mode_grid_style, pady=10)

        start_blocus_power_game_button = Button(main_menu_frame, text="Blocus Power", command=self.blocus_power)
        start_blocus_power_game_button.grid(row=3, column=1, **game_mode_grid_style)

        start_tetrix_duo_game_button = Button(main_menu_frame, text="Tetrix Duo", command=self.tetrix_duo)
        start_tetrix_duo_game_button.grid(row=4, column=1, **game_mode_grid_style, pady=10)

    def blocus_classic(self):
        global board_canvas, board_cells, board, player_turn_label, top_part, current_player, player_1_pieces, player_2_pieces, player_1_pieces_list, player_1_pieces_cells, player_2_pieces_cells
        global red_corners_coordinates, blue_corners_coordinates, common_corners_coordinates
        global board_cell_size, board_size
        global red_starting_corner, blue_starting_corner
        for i in self.master.winfo_children():
            i.destroy() # idem

        main_menu_frame = Frame(self.master)
        main_menu_frame.pack(expand=True)

        board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # Création du plateau grâce à une compréhension de liste
        board[-1][0] = 'RC' # On place les coins initiaux, où la première pièce de couleur correspondante devra être placée
        board[0][-1] = 'BC'

        red_corners_coordinates.append([0, board_size - 1]) # On ajoute les coordonées des cases de coin mentionnées ci-dessus
        blue_corners_coordinates.append([board_size - 1, 0])

        board_canvas = Canvas(main_menu_frame, width=board_size * board_cell_size + 3, height=board_size * board_cell_size + 3, bd=0, highlightthickness=0, relief='ridge') # On crée un canvas pour le board
        board_canvas.grid(column=1, row=1, padx=10) # On place le canvas

        player_1_pieces = Canvas(main_menu_frame, width=264, height=616, bd=0, highlightthickness=0, relief='ridge')
        player_1_pieces.grid(column=0, row=1)

        player_2_pieces = Canvas(main_menu_frame, width=264, height=616, bd=0, highlightthickness=0, relief='ridge')
        player_2_pieces.grid(column=2, row=1)

        top_part = Frame(main_menu_frame) # On crée un cadre pour la partie supérieure au plateau
        top_part.grid(row=0, column=1) # On place le nouveau cadre dans le cadre principal

        back_button = Button(top_part, text="< Retour", command=self.main_menu) # On crée un bouton retour
        back_button.grid(column=0, row=0) # Le bouton est placé
        player_turn_label = Label(top_part, font=('default', 20), background=background_color, padx=20)
        player_turn_label.grid(column=1, row=0)
        player_turn_label['text'] = f'Joueur {current_player + 1}'

        board_cells = []
        player_1_pieces_cells = []
        player_2_pieces_cells = []

        for line in range(board_size):
            row = []
            for column in range(board_size):
                x1 = column * board_cell_size + 1
                y1 = line * board_cell_size + 1
                x2 = x1 + board_cell_size + 1
                y2 = y1 + board_cell_size + 1
                cell = board_canvas.create_rectangle(x1, y1, x2, y2, fill=background_color, outline=board_cell_outline_color) # On crée un rectangle pour chaque case
                if line == board_size - 1 and column == 0:
                    red_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_red, width=0)
                elif line == 0 and column == board_size - 1:
                    blue_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_blue, width=0)
                row.append(cell)
            board_cells.append(row)

        for line in range(28):
            row_j1 = []
            row_j2 = []
            for column in range(12):
                x1 = column * 22
                y1 = line * 22
                x2 = x1 + 22
                y2 = y1 + 22
                if player_1_pieces_list[line][column] == 'O':
                    cell_j1 = player_1_pieces.create_rectangle(x1, y1, x2, y2, fill=placed_piece_red, width=0)
                    cell_j2 = player_2_pieces.create_rectangle(x1, y1, x2, y2, fill=placed_piece_blue, width=0)
                else:
                    cell_j1 = player_1_pieces.create_rectangle(x1, y1, x2, y2, fill=surface_color, width=0) # On crée un rectangle pour chaque case
                    cell_j2 = player_2_pieces.create_rectangle(x1, y1, x2, y2, fill=surface_color, width=0)
                row_j1.append(cell_j1)
                row_j2.append(cell_j2)
            player_1_pieces_cells.append(row_j1)
            player_2_pieces_cells.append(row_j2)

        # On "bind" le board à des événements
        board_canvas.bind("<Button-1>", self.on_plateau_click) # Clic : la pièce selectionnée est placée
        board_canvas.bind("<Button-3>", self.rotate_piece) # Clic droit : rotation de la pièce selectionnée
        board_canvas.bind("<Motion>", self.on_plateau_hover) # La souris bouge
        board_canvas.bind("<Leave>", self.on_plateau_leave) # La souris quitte le canvas

        # On "bind" les pièces à des événements
        player_1_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic
        player_1_pieces.bind("<Motion>", self.on_pièces_hover_j1) # La souris bouge
        # player_1_pieces.bind("<Leave>", self.on_plateau_leave) # La souris quitte le canvas
        player_2_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic
        # player_2_pieces.bind("<Motion>", self.on_pièces_hover) # La souris bouge
        # player_2_pieces.bind("<Leave>", self.on_pièces_leave) # La souris quitte le canvas

    def blocus_power(self):
        for i in self.master.winfo_children():
            i.destroy()
        label = Label(text="Page Two!!!")
        label.pack(pady=50, padx=50)
        button1 = Button(text="Back to Home", command=self.main_menu)
        button1.pack()

    def tetrix_duo(self):
        for i in self.master.winfo_children():
            i.destroy()
        label = Label(text="Page THREE!!!")
        label.pack(pady=50, padx=50)
        button1 = Button(text="Back to Home", command=self.main_menu)
        button1.pack()

    def on_plateau_click(self, event):
        global board, current_player, adjacent_coords, relative_positions, j1_has_selected_piece, j2_has_selected_piece
        global board_cell_size, board_size
        column_event = event.x // board_cell_size
        line_event = event.y // board_cell_size
        if line_event > board_size - 1: line_event = board_size - 1;
        if column_event > board_size - 1: column_event = board_size - 1;

        if board[line_event][column_event] == 'RH' or board[line_event][column_event] == 'BH':
            for line in board:
                for k, n in enumerate(line):
                    if n == 'RH':
                        line[k] = 'R'
                        j1_has_selected_piece = False
                        for k in adjacent_coords:
                            player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=background_color)
                    elif n == 'BH':
                        line[k] = 'B'
                        for k in adjacent_coords:
                            player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=background_color)
                        j2_has_selected_piece = False
            self.define_possible_corners()
            current_player = (current_player + 1) % 2 # On change de joueur
            adjacent_coords = []
            relative_positions = [[0, 0]]
            self.update_canvas()

    def on_plateau_hover(self, event):
        global board, board_canvas, board_cells
        global last_event_coordinates_copy, relative_positions
        global board_cell_size, board_size
        column_event = event.x // board_cell_size
        line_event = event.y // board_cell_size
        if line_event > board_size - 1: line_event = board_size - 1;
        if column_event > board_size - 1: column_event = board_size - 1;

        last_coords = [column_event, line_event]
        if last_event_coordinates_copy != last_coords:
            last_event_coordinates_copy = [i for i in last_coords]
            if j1_has_selected_piece or j2_has_selected_piece:
                self.draw_piece_on_board(column_event, line_event)

            else: # À OPTIMISER / SIMPLIFIER CAR RÉPÉTITION INUTILE
                for line in board:
                    for k, n in enumerate(line):
                        if n == 'H':
                            line[k] = ' '

                if board[line_event][column_event] == ' ':
                    board[line_event][column_event] = 'H'

                for line in range(board_size):
                    for column in range(board_size):
                        if board[line][column] == ' ':
                            board_canvas.itemconfig(board_cells[line][column], fill=background_color)
                        if board[line][column] == 'H':
                            board_canvas.itemconfig(board_cells[line][column], fill=invalid_placement)

            os.system('CLS')
            for line in board:
                print(line)
            print(red_corners_coordinates)
            print(blue_corners_coordinates)
            print(common_corners_coordinates)

        for red_corner_coord in red_corners_coordinates:
            if board[red_corner_coord[1]][red_corner_coord[0]] == ' ':
                board[red_corner_coord[1]][red_corner_coord[0]] = 'RC'

        for blue_corner_coord in blue_corners_coordinates:
            if board[blue_corner_coord[1]][blue_corner_coord[0]] == ' ':
                board[blue_corner_coord[1]][blue_corner_coord[0]] = 'BC'

        for common_corner_coord in common_corners_coordinates:
            if board[common_corner_coord[1]][common_corner_coord[0]] in ['RC', 'BC']:
                board[common_corner_coord[1]][common_corner_coord[0]] = 'RBC'

    def is_within_the_main_board(self, event_x, event_y):
        global board_size
        if event_x < 0 or event_y < 0 or event_x > board_size - 1 or event_y > board_size - 1:
            return False
        return True

    def define_possible_corners(self):
        global board_size
        memoire = []
        memoire2 = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        directions_corners = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for line in range(board_size):
            for column in range(board_size):
                invalid_element = False
                touches_corner = False
                touches_red_corner = False
                touches_blue_corner = False
                if board[line][column] == ' ':
                    for direction in directions:
                        if self.is_within_the_main_board(column + direction[0], line + direction[1]):
                            if current_player == 0:
                                if board[line + direction[1]][column + direction[0]] == 'R':
                                    invalid_element = True
                            else:
                                if board[line + direction[1]][column + direction[0]] == 'B':
                                    invalid_element = True

                    if not invalid_element:
                        for direction in directions_corners:
                            if self.is_within_the_main_board(column + direction[0], line + direction[1]):
                                if current_player == 0:
                                    if board[line + direction[1]][column + direction[0]] == 'R':
                                        touches_corner = True
                                else:
                                    if board[line + direction[1]][column + direction[0]] == 'B':
                                        touches_corner = True

                        if touches_corner:
                            memoire.append([column, line])

                if board[line][column] == 'RC' or board[line][column] == 'BC':
                    for direction in directions_corners:
                        if self.is_within_the_main_board(column + direction[0], line + direction[1]):
                            if board[line + direction[1]][column + direction[0]] == 'R':
                                touches_red_corner = True
                            if board[line + direction[1]][column + direction[0]] == 'B':
                                touches_blue_corner = True

                    if touches_red_corner and touches_blue_corner:
                        memoire2.append([column, line])

        for element in memoire:
            if current_player == 0:
                if board[element[1]][element[0]] == ' ':
                    red_corners_coordinates.append(element)
            else:
                if board[element[1]][element[0]] == ' ':
                    blue_corners_coordinates.append(element)

        for element in memoire2:
            if board[element[1]][element[0]] in ['R', 'B']:
                pass
            else:
                common_corners_coordinates.append(element)
                try:
                    red_corners_coordinates.remove(element)
                except ValueError:
                    pass
                try:
                    blue_corners_coordinates.remove(element)
                except ValueError:
                    pass

    def draw_piece_on_board(self, event_x, event_y):
        global board, board_canvas, board_cells
        global board_size
        out_of_bounds = False
        can_be_drawn = True
        can_be_placed = False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for position in relative_positions:
            adj_x, adj_y = event_x + position[0], event_y + position[1]
            if not (0 <= adj_x <= board_size - 1 and 0 <= adj_y <= board_size - 1):
                out_of_bounds = True

        for line in board:
            for k, n in enumerate(line):
                if n == 'H' or n == 'RH' or n == 'BH':
                    line[k] = ' '

        if not out_of_bounds:
            memoire = []
            for position in relative_positions:
                for direction in directions:
                    if self.is_within_the_main_board(event_x + position[0] + direction[0], event_y + position[1] + direction[1]):
                        memoire.append(board[event_y + position[1] + direction[1]][event_x + position[0] + direction[0]])

                if current_player == 0:
                    if 'R' not in memoire:
                        if [event_x + position[0], event_y + position[1]] in red_corners_coordinates:
                            can_be_placed = True
                        if [event_x + position[0], event_y + position[1]] in common_corners_coordinates:
                            can_be_placed = True
                    else:
                        can_be_placed = False
                else:
                    if 'B' not in memoire:
                        if [event_x + position[0], event_y + position[1]] in blue_corners_coordinates:
                            can_be_placed = True
                        if [event_x + position[0], event_y + position[1]] in common_corners_coordinates:
                            can_be_placed = True
                    else:
                        can_be_placed = False

            for position in relative_positions:
                if board[event_y + position[1]][event_x + position[0]] == 'R' or board[event_y + position[1]][event_x + position[0]] == 'B':
                    can_be_drawn = False

            for position in relative_positions:
                if can_be_drawn:
                    if j1_has_selected_piece and can_be_placed:
                        board[event_y + position[1]][event_x + position[0]] = 'RH'
                    elif j2_has_selected_piece and can_be_placed:
                        board[event_y + position[1]][event_x + position[0]] = 'BH'
                    else:
                        board[event_y + position[1]][event_x + position[0]] = 'H'

        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == ' ': board_canvas.itemconfig(board_cells[line][column], fill=background_color, outline=board_cell_outline_color);
                if board[line][column] == 'H': board_canvas.itemconfig(board_cells[line][column], fill=invalid_placement, outline=board_cell_outline_color);
                if board[line][column] == 'RH': board_canvas.itemconfig(board_cells[line][column], fill=valid_placement_red, outline=valid_placement_red);
                if board[line][column] == 'BH': board_canvas.itemconfig(board_cells[line][column], fill=valid_placement_blue, outline=valid_placement_blue);

    def on_plateau_leave(self, event):
        global board_size
        for line in board:
            for k, n in enumerate(line):
                if n == 'H' or n == 'RH' or n == 'BH':
                    line[k] = ' '
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == ' ':
                    board_canvas.itemconfig(board_cells[i][j], fill=background_color)

    def update_canvas(self):
        global board, board_canvas, board_cells
        global red_starting_corner, blue_starting_corner
        global player_turn_label
        global board_size
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 'R':
                    color = placed_piece_red
                    outline = placed_piece_red
                elif board[i][j] == 'B':
                    color = placed_piece_blue
                    outline = placed_piece_blue
                else:
                    color = background_color
                    outline = board_cell_outline_color
                board_canvas.itemconfig(board_cells[i][j], fill=color, outline=outline) # Édite la couleur des cases en fonction de ce qu'il y a dedans
        if board[-1][0] == 'R':
            board_canvas.itemconfig(red_starting_corner, fill=placed_piece_red)
        if board[0][-1] == 'B':
            board_canvas.itemconfig(blue_starting_corner, fill=placed_piece_blue)
        player_turn_label['text'] = f"Joueur {current_player + 1}" # On met à jour le texte qui affiche le tour du joueur actif
        player_turn_label.update()

    def on_player_pieces_click(self, event):
        global player_1_pieces_list, player_1_pieces, player_1_pieces_cells, player_2_pieces_list, player_2_pieces, player_2_pieces_cells
        global current_player, adjacent_coords, j1_has_selected_piece, relative_positions, orientation_id, j2_has_selected_piece
        if event.widget == player_1_pieces and current_player == 0:
            if not j1_has_selected_piece:
                column_event = event.x // 22
                line_event = event.y // 22
                if column_event > 11: column_event = 11;
                if line_event > 28: line_event = 28;
                if player_1_pieces_list[line_event][column_event] != ' ': # On vérifie que la case choisie n'est pas vide
                    adjacent_coords = self.get_adjacent_pieces_coordinates(player_1_pieces_list, column_event, line_event) # On cherche à obtenir les coordonnées de tous les "O" autour des coordonnées clickées
                    for k in adjacent_coords:
                        player_1_pieces_list[k[1]][k[0]] = ' '
                        player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=valid_placement_red)
                    j2_has_selected_piece = False
                    j1_has_selected_piece = True
                    orientation_id = 0 # On réinitialise l'orientation
            else:
                for k in adjacent_coords: # La pièce est replacée
                    player_1_pieces_list[k[1]][k[0]] = 'O'
                    player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=placed_piece_red)
                j1_has_selected_piece = False
                adjacent_coords = []
        elif event.widget == player_2_pieces and current_player == 1:
            if not j2_has_selected_piece:
                column_event = event.x // 22
                line_event = event.y // 22
                if column_event > 11: column_event = 11;
                if line_event > 28: line_event = 28;
                if player_2_pieces_list[line_event][column_event] != ' ':
                    adjacent_coords = self.get_adjacent_pieces_coordinates(player_2_pieces_list, column_event, line_event)
                    for k in adjacent_coords:
                        player_2_pieces_list[k[1]][k[0]] = ' '
                        player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=valid_placement_blue)
                    j1_has_selected_piece = False
                    j2_has_selected_piece = True
                    orientation_id = 0 
            else:
                for k in adjacent_coords:
                    player_2_pieces_list[k[1]][k[0]] = 'O'
                    player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=placed_piece_blue)
                j2_has_selected_piece = False
                adjacent_coords = []

    def on_pièces_hover_j1(self, event):
        global current_player
        # column_event = event.x // 22
        # line_event = event.y // 22
        # if column_event > 11: column_event = 11;
        # if line_event > 28: line_event = 28;

        # if current_player == 0:
        #     if pièces_joueur_1_liste[line_event][column_event] != ' ': # On vérifie que la case choisie n'est pas vide
        #         adjacent_coords = self.get_adjacent_pieces_coordinates(pièces_joueur_1_liste, column_event, line_event)
        #         for k in adjacent_coords:
        #             player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill='white')
        #         player_1_pieces.update()

    # def on_pièces_leave(self, event):
        # if last_cell is not None:
        #     last_color = board_canvas.itemcget(last_cell, "fill")
        #     if last_color != "red" and last_color != 'blue':
        #         board_canvas.itemconfig(last_cell, fill="white")

    def rotate_piece(self, event):
        global orientation_id, relative_positions
        orientation_id = (orientation_id + 1) % 4

        directions_from_center_rotated = [list(direction) for direction in relative_positions]

        if orientation_id == 0:
            pass  # 0°
        elif orientation_id == 1:
            for i, direction in enumerate(relative_positions):
                directions_from_center_rotated[i][0] = -direction[1]
                directions_from_center_rotated[i][1] = direction[0] # 90°
        elif orientation_id == 2:
            for i, direction in enumerate(relative_positions):
                directions_from_center_rotated[i][0] = -direction[0]
                directions_from_center_rotated[i][1] = -direction[1] # 180°
        elif orientation_id == 3:
            for i, direction in enumerate(relative_positions):
                directions_from_center_rotated[i][0] = direction[1]
                directions_from_center_rotated[i][1] = -direction[0] # 270°

        relative_positions = directions_from_center_rotated
        self.draw_piece_on_board(last_event_coordinates_copy[0], last_event_coordinates_copy[1])


    def get_adjacent_pieces_coordinates(self, liste_pièces, selected_case_x, selected_case_y):
        global relative_positions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cases_adjacentes = []
        relative_positions = []
        memoire = [[selected_case_x, selected_case_y]]

        # While the stack is not empty, meaning there are still cases to check
        while memoire:
            # Pop a case from the stack
            # This is the current case we are checking
            case_x, case_y = memoire.pop()

            # If the case contains 'O' and has not been visited yet
            # We check if it's not in the connected_Os list to avoid duplicates
            if liste_pièces[case_y][case_x] == 'O' and [case_x, case_y] not in cases_adjacentes:
                # Add the case to the list of connected 'O's
                # This means we have found a new 'O' that is connected to the selected case
                cases_adjacentes.append([case_x, case_y])

                # Loop over each direction
                for dx, dy in directions:
                    # Calculate the coordinates of the adjacent case
                    # This is done by adding the direction to the current case's coordinates
                    adj_x = case_x + dx
                    adj_y = case_y + dy

                    # Check if the coordinates are within the grid boundaries
                    # This is to avoid index errors
                    if 0 <= adj_y < len(liste_pièces) and 0 <= adj_x < len(liste_pièces[0]):
                        # If the adjacent case contains 'O', add it to the stack
                        # This means we have found a new 'O' to check in the next iterations
                        if liste_pièces[adj_y][adj_x] == 'O':
                            memoire.append([adj_x, adj_y])

        for adjacent_coords in cases_adjacentes:
            relative_positions.append([adjacent_coords[0] - selected_case_x, -(selected_case_y - adjacent_coords[1])])

        # Return the list of coordinates of connected 'O's
        # This is the final output of the function
        return cases_adjacentes


if __name__ == "__main__":
    root = Tk()
    root.configure(bg=background_color)
    App(root)
    root.mainloop()
