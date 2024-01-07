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

from tkinter import Label, Tk, Canvas, PhotoImage
from tkinter import messagebox
from tkinter.ttk import Style, Button, Frame
import os
from playsound import playsound
import webbrowser

# ════════════════════════════════════════════════════════════════════════════
# ════════════════════════════ CORPS DU PROGRAMME ════════════════════════════
# ════════════════════════════════════════════════════════════════════════════

# ══════════ Variables & Constantes

version_number = '1.0.0' # Version du projet

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
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']] # Ensemble de pièces du joueur 1

player_2_pieces_list = [i[:] for i in player_1_pieces_list] # Ensemble de pièces du joueur 2, copiée depuis celui du joueur 1

j1_has_selected_piece = False
j2_has_selected_piece = False

orientation_id = 0

last_event_coordinates_copy = []
directions_from_center_copy = []

board = []
board_cells = []
player_1_pieces_cells = []
player_2_pieces_cells = []

current_player = 0 # Le joueur 1 commence
board_cell_size = 38 # On définit la taille d'une case du plateau
board_size = 16 # On définit la taille du plateau

red_corners_coordinates = []
blue_corners_coordinates = []
common_corners_coordinates = []

player_1_score = 0 # Scores des joueurs
player_2_score = 0

# Palette source

# PRIMARY
md_ref_palette_primary0 = "#000000"
md_ref_palette_primary10 = "#00006e"
md_ref_palette_primary20 = "#0001ac"
md_ref_palette_primary25 = "#0001cd"
md_ref_palette_primary30 = "#0000ef"
md_ref_palette_primary35 = "#1a21ff"
md_ref_palette_primary40 = "#343dff"
md_ref_palette_primary50 = "#5a64ff"
md_ref_palette_primary60 = "#7c84ff"
md_ref_palette_primary70 = "#9da3ff"
md_ref_palette_primary80 = "#bec2ff"
md_ref_palette_primary90 = "#e0e0ff"
md_ref_palette_primary95 = "#f1efff"
md_ref_palette_primary98 = "#fbf8ff"
md_ref_palette_primary99 = "#fffbff"
md_ref_palette_primary100 = "#ffffff"
# TERTIARY
md_ref_palette_tertiary0 = "#000000"
md_ref_palette_tertiary10 = "#410000"
md_ref_palette_tertiary20 = "#690100"
md_ref_palette_tertiary25 = "#7e0100"
md_ref_palette_tertiary30 = "#930100"
md_ref_palette_tertiary35 = "#a90100"
md_ref_palette_tertiary40 = "#c00100"
md_ref_palette_tertiary50 = "#ef0000"
md_ref_palette_tertiary60 = "#ff5540"
md_ref_palette_tertiary70 = "#ff8a78"
md_ref_palette_tertiary80 = "#ffb4a8"
md_ref_palette_tertiary90 = "#ffdad4"
md_ref_palette_tertiary95 = "#ffedea"
md_ref_palette_tertiary98 = "#fff8f6"
md_ref_palette_tertiary99 = "#fffbff"
md_ref_palette_tertiary100 = "#ffffff"
# NEUTRAL
md_ref_palette_neutral0 = "#000000"
md_ref_palette_neutral10 = "#1b1b1f"
md_ref_palette_neutral20 = "#303034"
md_ref_palette_neutral25 = "#3c3b3f"
md_ref_palette_neutral30 = "#47464a"
md_ref_palette_neutral35 = "#535256"
md_ref_palette_neutral40 = "#5f5e62"
md_ref_palette_neutral50 = "#78767a"
md_ref_palette_neutral60 = "#929094"
md_ref_palette_neutral70 = "#adaaaf"
md_ref_palette_neutral80 = "#c8c5ca"
md_ref_palette_neutral90 = "#e5e1e6"
md_ref_palette_neutral95 = "#f3eff4"
md_ref_palette_neutral98 = "#fcf8fd"
md_ref_palette_neutral99 = "#fffbff"
md_ref_palette_neutral100 = "#ffffff"
# NEUTRAL VARIANT
md_ref_palette_neutral_variant0 = "#000000"
md_ref_palette_neutral_variant10 = "#1b1b23"
md_ref_palette_neutral_variant20 = "#303038"
md_ref_palette_neutral_variant25 = "#3b3b43"
md_ref_palette_neutral_variant30 = "#46464f"
md_ref_palette_neutral_variant35 = "#52515b"
md_ref_palette_neutral_variant40 = "#5e5d67"
md_ref_palette_neutral_variant50 = "#777680"
md_ref_palette_neutral_variant60 = "#91909a"
md_ref_palette_neutral_variant70 = "#acaab4"
md_ref_palette_neutral_variant80 = "#c7c5d0"
md_ref_palette_neutral_variant90 = "#e4e1ec"
md_ref_palette_neutral_variant95 = "#f2effa"
md_ref_palette_neutral_variant98 = "#fbf8ff"
md_ref_palette_neutral_variant99 = "#fffbff"
md_ref_palette_neutral_variant100 = "#ffffff"
# LIGHT
md_sys_color_primary_light = "#343dff"
md_sys_color_on_primary_light = "#ffffff"
md_sys_color_primary_container_light = "#e0e0ff"
md_sys_color_on_primary_container_light = "#00006e"
md_sys_color_secondary_light = "#984061"
md_sys_color_on_secondary_light = "#ffffff"
md_sys_color_secondary_container_light = "#ffd9e2"
md_sys_color_on_secondary_container_light = "#3e001d"
md_sys_color_tertiary_light = "#c00100"
md_sys_color_on_tertiary_light = "#ffffff"
md_sys_color_tertiary_container_light = "#ffdad4"
md_sys_color_on_tertiary_container_light = "#410000"
md_sys_color_error_light = "#ba1a1a"
md_sys_color_error_container_light = "#ffdad6"
md_sys_color_on_error_light = "#ffffff"
md_sys_color_on_error_container_light = "#410002"
md_sys_color_background_light = "#fffbff"
md_sys_color_on_background_light = "#1b1b1f"
md_sys_color_surface_light = "#fffbff"
md_sys_color_on_surface_light = "#1b1b1f"
md_sys_color_surface_variant_light = "#e4e1ec"
md_sys_color_on_surface_variant_light = "#46464f"
md_sys_color_outline_light = "#777680"
md_sys_color_inverse_on_surface_light = "#f3eff4"
md_sys_color_inverse_surface_light = "#303034"
md_sys_color_inverse_primary_light = "#bec2ff"
md_sys_color_shadow_light = "#000000"
md_sys_color_surface_tint_light = "#343dff"
md_sys_color_outline_variant_light = "#c7c5d0"
md_sys_color_scrim_light = "#000000"
# DARK
# md_sys_color_primary_dark = "#bec2ff"
md_sys_color_primary_dark = "#7c84ff"
md_sys_color_on_primary_dark = "#0001ac"
md_sys_color_primary_container_dark = "#0000ef"
md_sys_color_on_primary_container_dark = "#e0e0ff"
md_sys_color_secondary_dark = "#ffb1c8"
md_sys_color_on_secondary_dark = "#5e1133"
md_sys_color_secondary_container_dark = "#7b2949"
md_sys_color_on_secondary_container_dark = "#ffd9e2"
# md_sys_color_tertiary_dark = "#ffb4a8"
md_sys_color_tertiary_dark = "#ff5540"
md_sys_color_on_tertiary_dark = "#690100"
md_sys_color_tertiary_container_dark = "#930100"
md_sys_color_on_tertiary_container_dark = "#ffdad4"
md_sys_color_error_dark = "#ffb4ab"
md_sys_color_error_container_dark = "#93000a"
md_sys_color_on_error_dark = "#690005"
md_sys_color_on_error_container_dark = "#ffdad6"
md_sys_color_background_dark = "#1b1b1f"
md_sys_color_on_background_dark = "#e5e1e6"
md_sys_color_surface_dark = "#1b1b1f"
md_sys_color_on_surface_dark = "#e5e1e6"
md_sys_color_surface_variant_dark = "#46464f"
md_sys_color_on_surface_variant_dark = "#c7c5d0"
md_sys_color_outline_dark = "#91909a"
md_sys_color_inverse_on_surface_dark = "#1b1b1f"
md_sys_color_inverse_surface_dark = "#e5e1e6"
md_sys_color_inverse_primary_dark = "#343dff"
md_sys_color_shadow_dark = "#000000"
md_sys_color_surface_tint_dark = "#bec2ff"
md_sys_color_outline_variant_dark = "#46464f"
md_sys_color_scrim_dark = "#000000"

# Palette

background_color = md_sys_color_background_dark # Couleur de fond du programme
on_background_color = md_sys_color_on_surface_dark # Couleur des éléments placés sur le fond
button_background_color = md_sys_color_background_dark # Couleur de fond des boutons
button_outline_color = md_sys_color_on_surface_dark # Couleur de bordure des boutons
button_text_color = md_sys_color_on_surface_dark # Couleur du texte des boutons
surface_color = md_sys_color_surface_variant_dark # Couleur de surface (là où les pièces sont placées par exemple)

placed_piece_red = md_sys_color_tertiary_dark # Couleur d'une pièce rouge placée
valid_placement_red = md_sys_color_tertiary_container_dark # Couleur de survol d'une pièce rouge, si elle peut être placée à l'endroit choisi

placed_piece_blue = md_sys_color_primary_dark # Couleur d'une pièce bleue placée
valid_placement_blue = md_sys_color_primary_container_dark # Couleur de survol d'une pièce bleue, si elle peut être placée à l'endroit choisi

invalid_placement = md_sys_color_outline_variant_dark # Couleur de survol lorsque la pièce ne peut pas être placée à l'endroit choisi

board_cell_outline_color = md_sys_color_outline_variant_dark # Couleur de bordure des cases du plateau

# ══════════ Classe principale


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1280x720') # On définit la taille initiale de la fenêtre
        self.master.title('Blocus') # On définit le titre de la fenêtre

        style = Style() # On définit un style
        style.theme_use('default') # On utilise le style par défaut pour modifier plus facilement les boutons
        style.configure('TButton', font=('Arial', 30, 'bold'), background=button_background_color, focuscolor=button_background_color, relief='flat') # On ajoute du style pour les boutons
        style.configure('TFrame', background=background_color) # On change la couleur de fond des cadres "Frame"
        style.map('TButton', background=[('active', button_background_color), ('disabled', button_background_color)], relief=[('pressed', 'flat')]) # Modification du thème en fonction de l'état des boutons

        self.main_menu() # Affiche le menu principal dès le démarrage du programme
    
    def reset_variables(self): # Toutes les variables sont réinitialisées
        global player_1_pieces_list, player_2_pieces_list
        global j1_has_selected_piece, j2_has_selected_piece
        global orientation_id, last_event_coordinates_copy, directions_from_center_copy
        global board, board_cells, player_1_pieces_cells, player_2_pieces_cells
        global current_player, player_1_score, player_2_score
        global red_corners_coordinates, blue_corners_coordinates, common_corners_coordinates

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
        board_cells = []
        player_1_pieces_cells = []
        player_2_pieces_cells = []

        current_player = 0 # Le joueur 1 commence

        red_corners_coordinates = []
        blue_corners_coordinates = []
        common_corners_coordinates = []

        player_1_score = 0
        player_2_score = 0

    def main_menu(self):
        for i in self.master.winfo_children():
            i.destroy() # On supprime tout le contenu de la fenêtre
        
        self.reset_variables() # On appelle la fonction qui réinitialise les variables du programme

        main_menu_frame = Frame(self.master) # On crée le cadre principal
        main_menu_frame.pack(expand=True) # On affiche le cadre dans la fenêtre
        main_menu_frame.columnconfigure(2, weight=1)

        play = Label(self.master, text="Appuyez pour Jouer", background=background_color, foreground=on_background_color, font=('Arial', 15)) # On crée le texte "Appuyez pour Jouer"
        play.pack(pady=50) # On affiche le texte dans le cadre

        version_label = Label(main_menu_frame, text=version_number, background=background_color, foreground=invalid_placement, font=('Consolas', 15)) # On crée le texte qui affiche la version du programme
        version_label.grid(row=0, column=3) # Le texte est affiché

        blocus_logo_canvas = Canvas(main_menu_frame, width=840, height=224, bd=0, highlightthickness=0, relief='flat', background=background_color) # On crée le canvas sur lequel sera placé le logo du programme
        blocus_logo_canvas.grid(column=0, row=1, columnspan=4, pady=10) # Le canvas est placé
        self.blocus_logo = PhotoImage(file="res/img/blocus_logo.png") # On récupère l'image du logo
        blocus_logo_canvas.create_image(0, 0, anchor='nw', image=self.blocus_logo) # On place le logo sur le canvas mentionné ci-dessus

        self.github_logo = PhotoImage(file='res/img/github_logo.png') # On récupère l'image du logo GitHub
        github_button = Button(main_menu_frame, image=self.github_logo, command=lambda: webbrowser.open_new('https://github.com/ziadOUA/Blocus'), compound='center', width=2) # On crée le bouton qui ouvrira le lien GitHub du projet dans le navigateur
        github_button.grid(column=0, row=0) # Le bouton est placé

        self.about_icon = PhotoImage(file='res/img/about_icon.png') # On récupère l'image de l'icône "about_icon.png"
        about_button = Button(main_menu_frame, image=self.about_icon, command=self.about_blocus_duo, compound='center', width=2) # On crée le bouton qui affichera les auteurs du projet
        about_button.grid(column=1, row=0) # Le bouton est placé

        main_menu_frame.bind("<Button-1>", self.blocus_duo)    #
        play.bind("<Button-1>", self.blocus_duo)               # On "bind" plusieurs éléments pour que le jeu soit lancé en cliquant sur ces éléments
        blocus_logo_canvas.bind("<Button-1>", self.blocus_duo) #
    
    def about_blocus_duo(self):
        messagebox.showinfo("Blocus", "Projet supervisé de NSI\nZiad (ziadOUA) & Djibril")

    def blocus_duo(self, event):
        global board_canvas, board_cells, board, player_turn_label, board_top_part, current_player, player_1_pieces, player_2_pieces, player_1_pieces_list, player_1_pieces_cells, player_2_pieces_cells
        global red_corners_coordinates, blue_corners_coordinates, common_corners_coordinates
        global board_cells, player_1_pieces_cells, player_2_pieces_cells
        global board_cell_size, board_size
        global red_starting_corner, blue_starting_corner
        global player_1_score_label, player_2_score_label
        global player_1_hint_button, player_2_hint_button
        global player_1_pieces_top_part, player_2_pieces_top_part
        
        for i in self.master.winfo_children():
            i.destroy() # idem

        main_menu_frame = Frame(self.master) # On crée un cadre principal, pour pouvoir facilement centrer les différents éléments
        main_menu_frame.pack(expand=True)

        board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # Création du plateau grâce à une compréhension de liste
        board[-1][0] = 'RC' # On place les coins initiaux, où la première pièce de couleur correspondante devra être placée
        board[0][-1] = 'BC'

        red_corners_coordinates.append([0, board_size - 1]) # On ajoute les coordonnées des cases de coin mentionnées ci-dessus
        blue_corners_coordinates.append([board_size - 1, 0])

        board_canvas = Canvas(main_menu_frame, width=board_size * board_cell_size, height=board_size * board_cell_size, bd=0, highlightthickness=1, relief='flat', highlightbackground=board_cell_outline_color) # On crée un canvas pour le plateau
        board_canvas.grid(column=1, row=2, padx=10) # On place le canvas

        player_1_pieces = Canvas(main_menu_frame, width=264, height=616, bd=0, highlightthickness=0, relief='solid') # On crée un canvas qui affiche les pièces du joueur 1
        player_1_pieces.grid(column=0, row=2) # On place le canvas

        player_2_pieces = Canvas(main_menu_frame, width=264, height=616, bd=0, highlightthickness=0, relief='solid') # On crée un canvas qui affiche les pièces du joueur 2
        player_2_pieces.grid(column=2, row=2) # On place le canvas

        board_top_part = Frame(main_menu_frame, padding=10) # On crée un cadre pour la partie supérieure au plateau
        board_top_part.grid(row=1, column=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        board_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        self.back_icon = PhotoImage(file='res/img/back_icon.png') # On récupère l'image de l'icône "back_icon.png"
        back_button = Button(board_top_part, image=self.back_icon, command=self.main_menu, compound='center', width=2) # On crée un bouton retour
        back_button.grid(column=0, row=0) # Le bouton est placé
        
        player_turn_label = Label(board_top_part, font=('default', 20), background=background_color, foreground=on_background_color) #On crée un texte qui affiche le tour du joueur
        player_turn_label.grid(column=1, row=0, sticky='ew') # On place le texte 
        player_turn_label['text'] = f'Joueur {current_player + 1}' # On met à jour le contenu du texte

        Label(board_top_part, text='                ', background=background_color).grid(column=2, row=0) # Création d'un objet servant à centrer le texte qui affiche le tour du joueur
        
        player_1_pieces_top_part = Frame(main_menu_frame) # On crée un cadre pour la partie supérieure aux pièces du joueur 1
        player_1_pieces_top_part.grid(column=0, row=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        player_1_pieces_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        self.hint_icon = PhotoImage(file='res/img/hint_icon.png') # On récupère l'image de l'icône "hint_icon.png"
        player_1_hint_button = Button(player_1_pieces_top_part, image=self.hint_icon, command=lambda:self.get_hint(0), compound='center', width=2) # On crée un bouton indice pour le joueur 1
        player_1_hint_button.grid(column=0, row=0) # Le bouton est placé

        player_1_score_label = Label(player_1_pieces_top_part, font=('default', 20), background=background_color, pady=20, foreground=on_background_color) # On crée un texte qui affiche le score du joueur 1
        player_1_score_label.grid(column=1, row=0, sticky='ew') # Le texte est placé
        player_1_score_label['text'] = f'Score : {player_1_score}' # Le contenu du texte est mis à jour

        Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) # Création d'un objet servant à centrer le texte qui affiche le score du joueur 1
        
        player_2_pieces_top_part = Frame(main_menu_frame) # On crée un cadre pour la partie supérieure aux pièces du joueur 2
        player_2_pieces_top_part.grid(column=2, row=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        player_2_pieces_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) # Création d'un objet servant à centrer le texte qui affiche le score du joueur 2

        player_2_hint_button = Button(player_2_pieces_top_part, image=self.hint_icon, command=lambda:self.get_hint(1), compound='center', width=2) # On crée un bouton indice pour le joueur 2
        Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) # On crée un objet qui prend la place du bouton indice du joueur 2, caché par défaut

        player_2_score_label = Label(player_2_pieces_top_part, font=('default', 20), background=background_color, pady=20, foreground=on_background_color) # On crée un texte qui affiche le score du joueur 2
        player_2_score_label.grid(column=1, row=0, sticky='ew') # Le texte est placé
        player_2_score_label['text'] = f'Score : {player_2_score}' # Le contenu du texte est mis à jour

        for line in range(board_size):
            row = []
            for column in range(board_size):
                x1 = column * board_cell_size + 1
                y1 = line * board_cell_size + 1
                x2 = x1 + board_cell_size - 1
                y2 = y1 + board_cell_size - 1
                cell = board_canvas.create_rectangle(x1, y1, x2, y2, fill=background_color, outline=board_cell_outline_color) # On crée un rectangle pour chaque case du plateau
                row.append(cell)
            board_cells.append(row) # Tous les objets correspondant aux cases sont ajoutés à la liste "board_cells", qui permettra de les éditer facilement
        
        x1 = 1
        y1 = (board_size - 1) * board_cell_size + 1
        x2 = x1 + board_cell_size - 1
        y2 = y1 + board_cell_size - 1
        red_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_red, width=0) # On crée un cercle rouge dans le coin de départ du joueur 1

        x1 = (board_size - 1) * board_cell_size + 1
        y1 = 1
        x2 = x1 + board_cell_size - 1
        y2 = y1 + board_cell_size - 1
        blue_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_blue, width=0) # On crée un cercle rouge dans le coin de départ du joueur 2

        for line in range(28):
            row_j1 = []
            row_j2 = []
            for column in range(12):
                x1 = column * 22
                y1 = line * 22
                x2 = x1 + 22
                y2 = y1 + 22
                if player_1_pieces_list[line][column] == 'O':
                    cell_j1 = player_1_pieces.create_rectangle(x1, y1, x2, y2, fill=placed_piece_red, width=0)  #
                    cell_j2 = player_2_pieces.create_rectangle(x1, y1, x2, y2, fill=placed_piece_blue, width=0) #
                else:                                                                                           # On crée un rectangle coloré en fonction du joueur pour chaque case contenant "O", sinon la case est grise
                    cell_j1 = player_1_pieces.create_rectangle(x1, y1, x2, y2, fill=surface_color, width=0)     #
                    cell_j2 = player_2_pieces.create_rectangle(x1, y1, x2, y2, fill=surface_color, width=0)     #
                row_j1.append(cell_j1)
                row_j2.append(cell_j2)
            player_1_pieces_cells.append(row_j1) # Tous les objets correspondant aux cases sont ajoutés aux listes "player_1_pieces_cells" et "player_1_pieces_cells", qui permettera de les éditer facilement
            player_2_pieces_cells.append(row_j2)

        # On "bind" le board à des événements
        board_canvas.bind("<Button-1>", self.on_plateau_click) # Clic : la pièce sélectionnée est placée
        board_canvas.bind("<Button-3>", self.rotate_piece) # Clic droit : rotation de la pièce sélectionnée
        board_canvas.bind("<Motion>", self.on_plateau_hover) # La souris bouge sur le plateau
        board_canvas.bind("<Leave>", self.on_board_leave) # La souris quitte le canvas

        # On "bind" les pièces à des événements
        player_1_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic : la pièce est sélectionnée
        # player_1_pieces.bind("<Motion>", self.on_pièces_hover_j1)
        # player_1_pieces.bind("<Leave>", self.on_plateau_leave)
        player_2_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic : la pièce est sélectionnée
        # player_2_pieces.bind("<Motion>", self.on_pièces_hover)
        # player_2_pieces.bind("<Leave>", self.on_pièces_leave)

    def on_plateau_click(self, event):
        global board, current_player, adjacent_coords, relative_positions, j1_has_selected_piece, j2_has_selected_piece
        global board_cell_size, board_size
        global player_1_score, player_2_score
        global player_1_pieces_top_part, player_2_pieces_top_part
        global player_1_hint_button, player_2_hint_button
        global player_turn_label
        
        column_event = event.x // board_cell_size
        line_event = event.y // board_cell_size
        if line_event > board_size - 1: line_event = board_size - 1;
        if column_event > board_size - 1: column_event = board_size - 1;

        if board[line_event][column_event] in ['RH', 'BH']: # Vérifie que, lorsque le plateau est cliqué, la pièce pouvait bien être placée
            for line in board:
                for k, n in enumerate(line):
                    if n == 'RH':
                        line[k] = 'R' # Remplace tous les "RH" par des "R"
                        j1_has_selected_piece = False
                        for k in adjacent_coords:
                            player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=background_color) # La pièce est retirée de l'ensemble de pièces du joueur 1
                    elif n == 'BH':
                        line[k] = 'B' # Remplace tous les "BH" par des "B"
                        for k in adjacent_coords:
                            player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=background_color) # La pièce est retirée de l'ensemble de pièces du joueur 2
                        j2_has_selected_piece = False
            
            if current_player == 0:
                player_1_score += len(adjacent_coords) # On ajoute au score le nombre de carreaux placés sur le plateau
            else:
                player_2_score += len(adjacent_coords)

            self.define_possible_corners() # On place les coins où des pièces peuvent être placées

            if current_player == 0:
                if self.can_still_play(player=1): # On vérifie si le joueur 2 peut bien jouer
                    current_player = 1 # On change de joueur
                    self.update_turn_label() # On met à jour le texte du joueur que concerne le tour
                    player_1_hint_button.grid_forget() # On retire le bouton indice du joueur 1...
                    Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) #... remplacé par un objet vide, pour centrer le texte du score
                    player_2_hint_button = Button(player_2_pieces_top_part, image=self.hint_icon, command=lambda:self.get_hint(1), compound='center', width=2) # Le bouton indice du joueur 2 est redéfini
                    player_2_hint_button.grid(column=2, row=0) # Le bouton est placé
            else:
                if self.can_still_play(player=0): # On vérifie si le joueur 1 peut bien jouer
                    current_player = 0 # On change de joueur
                    self.update_turn_label() # On met à jour le texte du joueur que concerne le tour
                    player_2_hint_button.grid_forget() # On retire le bouton indice du joueur 2...
                    Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) #... remplacé par un objet vide, pour centrer le texte du score
                    player_1_hint_button = Button(player_1_pieces_top_part, image=self.hint_icon, command=lambda:self.get_hint(0), compound='center', width=2) # Le bouton indice du joueur 1 est redéfini
                    player_1_hint_button.grid(column=0, row=0) # Le bouton est placé
            
            if not self.can_still_play(player=0) and not self.can_still_play(player=1): # Si aucun des deux joueurs ne peut jouer
                current_player = 999 # Le jeu est bloqué
                if player_1_score > player_2_score:
                    player_turn_label['text'] = 'Victoire du Joueur 1' # Si le score du joueur 1 est supérieur à celui du joueur 2, alors victoire du joueur 1
                elif player_1_score < player_2_score:
                    player_turn_label['text'] = 'Victoire du Joueur 2' # Si le score du joueur 1 est inférieur à celui du joueur 2, alors victoire du joueur 2
                elif player_1_score == player_2_score:
                    player_turn_label['text'] = 'Égalité' # Si les deux scores sont égaux, alors égalité
                player_turn_label.update() # On met à jour le texte pour qu'il affiche l'état du jeu
                player_1_hint_button.grid_forget() # On retire les boutons indice des deux joueurs...
                player_2_hint_button.grid_forget()
                Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) #... remplacés par des objets vides pour centrer les scores
                Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0)
            
            adjacent_coords = []
            relative_positions = [[0, 0]]

            self.update_board_canvas() # On met à jour le canvas du plateau
            # playsound.playsound('./res/audio/piece_place.wav')

    def on_plateau_hover(self, event):
        global board, board_canvas, board_cells
        global last_event_coordinates_copy, relative_positions
        global board_cell_size, board_size
        
        column_event = event.x // board_cell_size
        line_event = event.y // board_cell_size
        if line_event > board_size - 1: line_event = board_size - 1;
        if column_event > board_size - 1: column_event = board_size - 1;

        last_coords = [column_event, line_event]
        if last_event_coordinates_copy != last_coords: # Le code ci-dessous n'est exécuté qu'à chaque fois que la souris change de case du plateau, au lieu de l'exécuter au moindre mouvement
            last_event_coordinates_copy = [i for i in last_coords]
            if j1_has_selected_piece or j2_has_selected_piece:
                self.draw_piece_on_board(column_event, line_event) # "Déssine" la pièce sélectionnée sur le plateau

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

            # os.system('CLS')   # DEBUG
            # for line in board: # -> Affichage du plateau
            #     print(line)    # DEBUG

        for red_corner_coord in red_corners_coordinates:
            if board[red_corner_coord[1]][red_corner_coord[0]] == ' ':
                board[red_corner_coord[1]][red_corner_coord[0]] = 'RC' # S'assure de replacer les coins rouges "RC", au cas où ils ont été retirés par une pièce en survol

        for blue_corner_coord in blue_corners_coordinates:
            if board[blue_corner_coord[1]][blue_corner_coord[0]] == ' ':
                board[blue_corner_coord[1]][blue_corner_coord[0]] = 'BC' # S'assure de replacer les coins bleus "BC", au cas où ils ont été retirés par une pièce en survol

        for common_corner_coord in common_corners_coordinates:
            if board[common_corner_coord[1]][common_corner_coord[0]] in ['RC', 'BC']:
                board[common_corner_coord[1]][common_corner_coord[0]] = 'RBC' # S'assure de replacer les coins communs "RBC", au cas où ils ont été retirés par une pièce en survol

    def is_within_the_main_board(self, event_x, event_y):
        global board_size
        if event_x < 0 or event_y < 0 or event_x > board_size - 1 or event_y > board_size - 1:
            return False 
        return True # Renvoie "True" si la pièce est en dehors du plateau

    def define_possible_corners(self):
        global board_size
        
        memoire = [] # Création de variables "mémoires" dans le but de stocker des choses
        memoire2 = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Directions : HAUT, BAS, DROITE, GAUCHE
        directions_corners = [(1, 1), (-1, -1), (1, -1), (-1, 1)] # Coins : DROIT SUPÉRIEUR, GAUCHE INFÉRIEUR, DROIT INFÉRIEUR, GAUCHE SUPÉRIEUR
        
        for line in range(board_size):
            for column in range(board_size): # On fait une itération sur l'ensemble des cases du plateau
                invalid_element = False # Divers drapeaux
                touches_corner = False
                touches_red_corner = False
                touches_blue_corner = False
                
                if board[line][column] == ' ': # Si la case est vide
                    for direction in directions:
                        if self.is_within_the_main_board(column + direction[0], line + direction[1]): # On vérifie si la direction dans laquelle on recherche est comprise dans le plateau, pour éviter des erreurs de dépassement d'index
                            if current_player == 0:
                                if board[line + direction[1]][column + direction[0]] == 'R': # On vérifie si la case est en contact direct avec une case de couleur (rouge dans ce cas)
                                    invalid_element = True # La case est invalidée le cas échéant
                            else:
                                if board[line + direction[1]][column + direction[0]] == 'B': # On vérifie si la case est en contact direct avec une case de couleur (rouge dans ce cas)
                                    invalid_element = True # La case est invalidée le cas échéant

                    if not invalid_element: # Si la case n'est pas déjà invalide
                        for direction in directions_corners:
                            if self.is_within_the_main_board(column + direction[0], line + direction[1]): # On vérifie si le coin qu'on essaie de voir est bien compris dans le plateau, pour les mêmes raisons que ci-dessus
                                if current_player == 0:
                                    if board[line + direction[1]][column + direction[0]] == 'R': # Si au moins un des coins est rouge, et que le joueur actif est le joueur 1...
                                        touches_corner = True #... on lève le drapeau "touches_corner"
                                else:
                                    if board[line + direction[1]][column + direction[0]] == 'B': # Si au moins un des coins est bleu, et que le joueur actif est le joueur 2...
                                        touches_corner = True #... on lève le drapeau "touches_corner"

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
        
        for red_corner_coord in red_corners_coordinates:
            if board[red_corner_coord[1]][red_corner_coord[0]] == ' ':
                board[red_corner_coord[1]][red_corner_coord[0]] = 'RC'

        for blue_corner_coord in blue_corners_coordinates:
            if board[blue_corner_coord[1]][blue_corner_coord[0]] == ' ':
                board[blue_corner_coord[1]][blue_corner_coord[0]] = 'BC'

        for common_corner_coord in common_corners_coordinates:
            if board[common_corner_coord[1]][common_corner_coord[0]] in ['RC', 'BC']:
                board[common_corner_coord[1]][common_corner_coord[0]] = 'RBC'
    
    def can_still_play(self, player):
        global player_1_pieces_list, player_2_pieces_list
        global board_size, relative_positions
        global orientation_id

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        has_found_a_piece = False
        can_still_play = False

        if player == 0:
            player_pieces_list = player_1_pieces_list
            player_corner_value = 'RC'
        else:
            player_pieces_list = player_2_pieces_list
            player_corner_value = 'BC'

        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == player_corner_value or board[line][column] == 'RBC':
                    for piece_line in range(len(player_pieces_list)):
                        for piece_column in range(len(player_pieces_list[0])):
                            if player_pieces_list[piece_line][piece_column] == 'O':
                                if not has_found_a_piece:
                                    self.get_adjacent_pieces_coordinates(player_pieces_list, piece_column, piece_line)
                                    
                                    for _ in range(4):
                                        directions_from_center_rotated = [list(direction) for direction in relative_positions]

                                        orientation_id = (orientation_id + 1) % 4

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

                                        out_of_bounds = False
                                        can_fit = True
                                        can_be_placed = True

                                        for position in relative_positions:
                                            if not self.is_within_the_main_board(column + position[0], line + position[1]):
                                                out_of_bounds = True
                                                can_fit = False
                                                can_be_placed = False
                                            
                                        if not out_of_bounds:
                                            for position in relative_positions:
                                                if board[line + position[1]][column + position[0]] in ['R', 'B']:
                                                    can_fit = False
                                                    can_be_placed = False
                                        
                                        if can_fit:
                                            for position in relative_positions:
                                                for direction in directions:
                                                    if self.is_within_the_main_board(column + position[0] + direction[0], line + position[1] + direction[1]):
                                                        if player == 0:
                                                            if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == 'R':
                                                                can_be_placed = False
                                                        else:
                                                            if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == 'B':
                                                                can_be_placed = False
                                    
                                        if can_be_placed:
                                            can_still_play = True
        return can_still_play

    def get_hint(self, player):
        global player_1_pieces_list, player_2_pieces_list
        global board_size, relative_positions
        global orientation_id, player_1_score, player_2_score

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        has_found_a_piece = False

        if player == 0:
            player_pieces_list = player_1_pieces_list
            player_corner_value = 'RC'
        else:
            player_pieces_list = player_2_pieces_list
            player_corner_value = 'BC'
        
        for line in board:
            for k, n in enumerate(line):
                if n == 'H':
                    line[k] = ' '

        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == player_corner_value or board[line][column] == 'RBC':
                    for piece_line in range(len(player_pieces_list)):
                        for piece_column in range(len(player_pieces_list[0])):
                            if player_pieces_list[piece_line][piece_column] == 'O':
                                if not has_found_a_piece:
                                    self.get_adjacent_pieces_coordinates(player_pieces_list, piece_column, piece_line)

                                    for _ in range(4):
                                        directions_from_center_rotated = [list(direction) for direction in relative_positions]

                                        orientation_id = (orientation_id + 1) % 4

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

                                        out_of_bounds = False
                                        can_fit = True
                                        can_be_placed = True

                                        for position in relative_positions:
                                            if not self.is_within_the_main_board(column + position[0], line + position[1]):
                                                out_of_bounds = True
                                                can_fit = False
                                                can_be_placed = False
                                            
                                        if not out_of_bounds:
                                            for position in relative_positions:
                                                if board[line + position[1]][column + position[0]] in ['R', 'B']:
                                                    can_fit = False
                                                    can_be_placed = False
                                        
                                        if can_fit:
                                            for position in relative_positions:
                                                for direction in directions:
                                                    if self.is_within_the_main_board(column + position[0] + direction[0], line + position[1] + direction[1]):
                                                        if current_player == 0:
                                                            if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == 'R':
                                                                can_be_placed = False
                                                        else:
                                                            if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == 'B':
                                                                can_be_placed = False
                                        
                                        if (current_player == 0 and player_1_score >= 2) or (current_player == 1 and player_2_score >= 2):
                                            if can_be_placed:
                                                if not has_found_a_piece:
                                                    for position in relative_positions:
                                                        board[line + position[1]][column + position[0]] = 'H'
                                                    for line in range(board_size):
                                                        for column in range(board_size):
                                                            if board[line][column] == ' ': board_canvas.itemconfig(board_cells[line][column], fill=background_color, outline=board_cell_outline_color);
                                                            if board[line][column] == 'H': board_canvas.itemconfig(board_cells[line][column], fill=invalid_placement, outline=board_cell_outline_color);
                                                            has_found_a_piece = True
                                                    if current_player == 0:
                                                        player_1_score -= 2
                                                        player_1_score_label['text'] = f"Score : {player_1_score}" # On met à jour le texte qui affiche le tour du joueur actif
                                                        player_1_score_label.update()
                                                    else:
                                                        player_2_score -= 2
                                                        player_2_score_label['text'] = f"Score : {player_2_score}" # On met à jour le texte qui affiche le tour du joueur actif
                                                        player_2_score_label.update()

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

    def on_board_leave(self, event):
        global board_size
        for line in board:
            for k, n in enumerate(line):
                if n == 'H' or n == 'RH' or n == 'BH':
                    line[k] = ' '
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == ' ':
                    board_canvas.itemconfig(board_cells[i][j], fill=background_color, outline=board_cell_outline_color)

    def update_board_canvas(self):
        global board, board_canvas, board_cells
        global red_starting_corner, blue_starting_corner
        global player_turn_label, player_1_score_label, player_2_score_label
        global player_1_score, player_2_score
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
        
        player_1_score_label['text'] = f"Score : {player_1_score}" # On met à jour le texte qui affiche le tour du joueur actif
        player_1_score_label.update()
        player_2_score_label['text'] = f"Score : {player_2_score}" # On met à jour le texte qui affiche le tour du joueur actif
        player_2_score_label.update()
    
    def update_turn_label(self):
        global player_turn_label
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
                    adjacent_coords = self.get_adjacent_pieces_coordinates(player_1_pieces_list, column_event, line_event) # On cherche à obtenir les coordonnées de tous les "O" autour des coordonnées cliquées
                    for k in adjacent_coords:
                        player_1_pieces_list[k[1]][k[0]] = ' '
                        player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=valid_placement_red)
                    j2_has_selected_piece = False
                    j1_has_selected_piece = True
                    orientation_id = 0 # On réinitialise l'orientation
                # playsound.playsound('./res/audio/piece_taken.wav', block=False)
            else:
                # playsound.playsound('./res/audio/piece_back.wav', block=False)
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
                # playsound.playsound('./res/audio/piece_taken.wav', block=False)
            else:
                # playsound.playsound('./res/audio/piece_back.wav', block=False)
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

        # playsound.playsound('./res/audio/piece_rotate.wav', block=False)

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
    icon = PhotoImage(file='res/img/blocus_icon.png')
    root.iconphoto(True, icon)
    App(root)
    root.mainloop()
