"""
             ,adba,             88  Projet : Blocus
             8I  I8             88  But : Créer une version à deux joueurs du jeu 'Blokus' 
             "8bdP'             88  Création : 15/12/2023 10:22
888888888   ,d8"8b  88  ,adPPYb,88  
     a8P" .dP'   Yb,8I a8"    `Y88  
  ,d8P'   8P      888' 8b       88  
,d8"      8b,   ,dP8b  "8a,   ,d88  GitHub : https://github.com/ziadOUA/Blocus
888888888 `Y8888P"  Yb  `"8bbdP"88  MIT - NSI
"""

# ═══════════════════════════════ IMPORTATIONS ═══════════════════════════════

from tkinter import Label, Tk, Canvas, PhotoImage, Frame, BooleanVar, Checkbutton
from tkinter import messagebox
from tkinter.ttk import Style, Button
import os
import json
import webbrowser
from timeit import default_timer as timer
from settings_util import check_settings_file

# ════════════════════════════════════════════════════════════════════════════
# ════════════════════════════ CORPS DU PROGRAMME ════════════════════════════
# ════════════════════════════════════════════════════════════════════════════

# ══════════ Paramètres

check_settings_file() # On vérifie la présence du fichier paramètres
with open("settings.json", "r") as settings_file: # Ouverture initiale du fichier paramètres (nommé settings.json)
    settings_data = json.load(settings_file) # On récupère les données du fichier

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

player_2_pieces_list = [i[:] for i in player_1_pieces_list] # Ensemble de pièces du joueur 2, copié depuis celui du joueur 1

player_1_has_selected_piece = False
player_2_has_selected_piece = False
has_a_player_won = False
use_light_theme = settings_data['use_light_theme']         #
color_blind_mode = settings_data['color_blind_mode']       # Divers paramètres récupérés depuis le fichier paramètres
use_space_to_mirror = settings_data['use_space_to_mirror'] #

orientation_id = 0
mirror_id = 0

last_event_coordinates_copy = [] # Copie des dernières coordonnées de la souris
relative_positions = [[0, 0]] # Positions relatives par rapport à la souris
relative_positions_reference = [[0, 0]] # Idem, mais qui ne sera modifié que lors d'un changement de pièce

board = [] # Liste source du plateau
board_cells = [] # Contiendra les cases du plateau (pour facilement changer leur couleur) 
player_1_pieces_cells = [] # Contiendra les cases du range-pièces du joueur 1 (pour facilement changer leur couleur) 
player_2_pieces_cells = [] # Contiendra les cases du range-pièces du joueur 2 (pour facilement changer leur couleur)

adjacent_coordinates_hover = []

current_player = 0 # Le joueur 1 commence
board_cell_size = 38 # On définit la taille d'une case du plateau
board_size = 16 # On définit la taille du plateau

red_corners_coordinates = []    #
blue_corners_coordinates = []   #
common_corners_coordinates = [] # On sauvegardera dans ces listes les coordonnées de différents éléments pour les restaurer après
red_cases_coordinates = []      #
blue_cases_coordinates = []     #

player_1_score = 0 # Scores des joueurs
player_2_score = 0

settings_file.close() # On ferme le fichier de paramètres pour éviter les problèmes

# ══════════ Palette

if settings_data['use_purple_and_yellow']:
    # PRIMARY
    md_ref_palette_primary50 = "#8653ff"
    md_ref_palette_primary70 = "#b69bff"
    # TERTIARY
    md_ref_palette_tertiary50 = "#8a7600"
    md_ref_palette_tertiary70 = "#c6aa00"
    # LIGHT
    md_sys_color_primary_light = "#6e28f3"
    md_sys_color_tertiary_light = "#a89000"
    md_sys_color_background_light = "#fffbff"
    md_sys_color_on_surface_light = "#1c1b1e"
    md_sys_color_surface_variant_light = "#e7e0eb"
    md_sys_color_outline_variant_light = "#cac4cf"
    # DARK
    md_sys_color_primary_dark = "#9e79ff"
    md_sys_color_primary_container_dark = "#5400cc"
    md_sys_color_tertiary_dark = "#e5c500"
    md_sys_color_tertiary_container_dark = "#6e5e00"
    md_sys_color_background_dark = "#1c1b1e"
    md_sys_color_on_surface_dark = "#e6e1e6"
    md_sys_color_surface_variant_dark = "#49454e"
    md_sys_color_outline_variant_dark = "#49454e"

    piece_hover_red_overlay_dark = '#b2a240'
    piece_hover_red_overlay_light = '#776f40'
    piece_hover_blue_overlay_dark = '#8f7cbf'
    piece_hover_blue_overlay_light = '#7754b9'
    cannot_play_border_color_dark = '#ff8a78'
    cannot_play_border_color_light = '#c00100'

else:
    # PRIMARY
    md_ref_palette_primary50 = "#5a64ff"
    md_ref_palette_primary70 = "#9da3ff"
    # TERTIARY
    md_ref_palette_tertiary50 = "#ef0000"
    md_ref_palette_tertiary70 = "#ff8a78"
    # LIGHT
    md_sys_color_primary_light = "#343dff"
    md_sys_color_tertiary_light = "#c00100"
    md_sys_color_background_light = "#fffbff"
    md_sys_color_on_surface_light = "#1b1b1f"
    md_sys_color_surface_variant_light = "#e4e1ec"
    md_sys_color_outline_variant_light = "#c7c5d0"
    # DARK
    md_sys_color_primary_dark = "#7c84ff"
    md_sys_color_primary_container_dark = "#0000ef"
    md_sys_color_tertiary_dark = "#ff5540"
    md_sys_color_tertiary_container_dark = "#930100"
    md_sys_color_background_dark = "#1b1b1f"
    md_sys_color_on_surface_dark = "#e5e1e6"
    md_sys_color_surface_variant_dark = "#46464f"
    md_sys_color_outline_variant_dark = "#46464f"

    piece_hover_red_overlay_dark = '#bf857c' 
    piece_hover_red_overlay_light = '#a04040'
    piece_hover_blue_overlay_dark = '#8e91bf' 
    piece_hover_blue_overlay_light = '#5a5ebf'
    cannot_play_border_color_dark = '#e7c349'
    cannot_play_border_color_light = '#6e5e00'

# ══════════ Couleurs du programme

transparent = ''

if not use_light_theme:
    background_color = md_sys_color_background_dark # Couleur de fond du programme
    on_background_color = md_sys_color_on_surface_dark # Couleur des éléments placés sur le fond
    button_background_color = md_sys_color_background_dark # Couleur de fond des boutons
    button_outline_color = md_sys_color_on_surface_dark # Couleur de bordure des boutons
    button_text_color = md_sys_color_on_surface_dark # Couleur du texte des boutons
    surface_color = md_sys_color_surface_variant_dark # Couleur de surface (là où les pièces sont placées par exemple)

    placed_piece_red = md_sys_color_tertiary_dark # Couleur d'une pièce rouge placée
    valid_placement_red = md_sys_color_tertiary_container_dark # Couleur de survol d'une pièce rouge, si elle peut être placée à l'endroit choisi
    piece_hover_red = md_ref_palette_tertiary70 # Couleur de survol pour les pièces rouges

    placed_piece_blue = md_sys_color_primary_dark # Couleur d'une pièce bleue placée
    valid_placement_blue = md_sys_color_primary_container_dark # Couleur de survol d'une pièce bleue, si elle peut être placée à l'endroit choisi
    piece_hover_blue = md_ref_palette_primary70 # Couleur de survol pour les pièces bleues

    invalid_placement = md_sys_color_outline_variant_dark # Couleur de survol lorsque la pièce ne peut pas être placée à l'endroit choisi

    board_cell_outline_color = md_sys_color_outline_variant_dark # Couleur de bordure des cases du plateau

    piece_hover_blue_overlay = piece_hover_blue_overlay_dark # Couleur de bordure quand le joueur actif est le joueur 1
    piece_hover_red_overlay = piece_hover_red_overlay_dark # Couleur de bordure quand le joueur actif est le joueur 2
    cannot_play_border_color = cannot_play_border_color_dark # Couleur de bordure quand un des joueurs ne peut plus jouer

    selected_theme = 'dark'

else:
    background_color = md_sys_color_background_light # Couleur de fond du programme
    on_background_color = md_sys_color_on_surface_light # Couleur des éléments placés sur le fond
    button_background_color = md_sys_color_background_light # Couleur de fond des boutons
    button_outline_color = md_sys_color_on_surface_light # Couleur de bordure des boutons
    button_text_color = md_sys_color_on_surface_light # Couleur du texte des boutons
    surface_color = md_sys_color_surface_variant_light # Couleur de surface (là où les pièces sont placées par exemple)

    placed_piece_red = md_sys_color_tertiary_light # Couleur d'une pièce rouge placée
    valid_placement_red = md_ref_palette_tertiary70 # Couleur de survol d'une pièce rouge, si elle peut être placée à l'endroit choisi
    piece_hover_red = md_ref_palette_tertiary50 # Couleur de survol pour les pièces rouges

    placed_piece_blue = md_sys_color_primary_light # Couleur d'une pièce bleue placée
    valid_placement_blue = md_ref_palette_primary70 # Couleur de survol d'une pièce bleue, si elle peut être placée à l'endroit choisi
    piece_hover_blue = md_ref_palette_primary50 # Couleur de survol pour les pièces bleues

    invalid_placement = md_sys_color_outline_variant_light # Couleur de survol lorsque la pièce ne peut pas être placée à l'endroit choisi

    board_cell_outline_color = md_sys_color_outline_variant_light # Couleur de bordure des cases du plateau

    piece_hover_blue_overlay = piece_hover_blue_overlay_light # Couleur de bordure quand le joueur actif est le joueur 1
    piece_hover_red_overlay = piece_hover_red_overlay_light # Couleur de bordure quand le joueur actif est le joueur 2
    cannot_play_border_color = cannot_play_border_color_light # Couleur de bordure quand un des joueurs ne peut plus jouer

    selected_theme = 'light'

# ══════════ Classe principale


class Blocus:
    def __init__(self, master):
        global style, label_style, small_label_style, medium_label_style, large_label_style, xlarge_label_style
        
        self.master = master
        self.master.geometry('1280x720') # On définit la taille initiale de la fenêtre
        self.master.title('Blocus') # On définit le titre de la fenêtre

        style = Style() # On définit un style
        style.theme_use('default') # On utilise le style par défaut pour modifier plus facilement les boutons
        # On ajoute du style pour les boutons
        style.configure('TButton', background=button_background_color, focuscolor=button_background_color, relief='flat')
        # Modification du thème en fonction de l'état des boutons
        style.map('TButton', background=[('active', button_background_color)], relief=[('pressed', 'flat')])
        style.configure('TFrame', background=background_color) # On change la couleur de fond des cadres "Frame"

        small_label_style = {'background': background_color, 'foreground': invalid_placement, 'font': ('Consolas', 10)}
        medium_label_style = {'background': background_color, 'foreground': on_background_color, 'font': ('Arial', 12)}
        large_label_style = {'background': background_color, 'foreground': on_background_color, 'font': ('Arial', 15)}
        xlarge_label_style = {'background': background_color, 'foreground': on_background_color, 'font': ('Arial', 20)}

        self.main_menu() # Affiche le menu principal dès le démarrage du programme
    
    def reset_variables(self): # Toutes les variables sont réinitialisées
        global player_1_pieces_list, player_2_pieces_list
        global player_1_has_selected_piece, player_2_has_selected_piece, has_a_player_won
        global orientation_id, last_event_coordinates_copy, relative_positions, relative_positions_reference
        global board, board_cells, player_1_pieces_cells, player_2_pieces_cells
        global current_player, player_1_score, player_2_score
        global red_corners_coordinates, blue_corners_coordinates, common_corners_coordinates, red_cases_coordinates, blue_cases_coordinates
        global background_color, on_background_color, surface_color
        global button_background_color, button_outline_color, button_text_color
        global placed_piece_red, valid_placement_red, piece_hover_red, piece_hover_red_overlay
        global placed_piece_blue, valid_placement_blue, piece_hover_blue, piece_hover_blue_overlay
        global cannot_play_border_color, invalid_placement, board_cell_outline_color
        global use_space_to_mirror, color_blind_mode, use_middle_starting_cases, use_light_theme, selected_theme

        with open("settings.json", "r") as settings_file:
            settings_data = json.load(settings_file)
        
        if settings_data['use_purple_and_yellow']:
            # PRIMARY
            md_ref_palette_primary50 = "#8653ff"
            md_ref_palette_primary70 = "#b69bff"
            # TERTIARY
            md_ref_palette_tertiary50 = "#8a7600"
            md_ref_palette_tertiary70 = "#c6aa00"
            # LIGHT
            md_sys_color_primary_light = "#6e28f3"
            md_sys_color_tertiary_light = "#a89000"
            md_sys_color_background_light = "#fffbff"
            md_sys_color_on_surface_light = "#1c1b1e"
            md_sys_color_surface_variant_light = "#e7e0eb"
            md_sys_color_outline_variant_light = "#cac4cf"
            # DARK
            md_sys_color_primary_dark = "#9e79ff"
            md_sys_color_primary_container_dark = "#5400cc"
            md_sys_color_tertiary_dark = "#e5c500"
            md_sys_color_tertiary_container_dark = "#6e5e00"
            md_sys_color_background_dark = "#1c1b1e"
            md_sys_color_on_surface_dark = "#e6e1e6"
            md_sys_color_surface_variant_dark = "#49454e"
            md_sys_color_outline_variant_dark = "#49454e"

            piece_hover_red_overlay_dark = '#b2a240'
            piece_hover_red_overlay_light = '#776f40'
            piece_hover_blue_overlay_dark = '#8f7cbf'
            piece_hover_blue_overlay_light = '#7754b9'
            cannot_play_border_color_dark = '#ff8a78'
            cannot_play_border_color_light = '#c00100'
        
        else:
            # PRIMARY
            md_ref_palette_primary50 = "#5a64ff"
            md_ref_palette_primary70 = "#9da3ff"
            # TERTIARY
            md_ref_palette_tertiary50 = "#ef0000"
            md_ref_palette_tertiary70 = "#ff8a78"
            # LIGHT
            md_sys_color_primary_light = "#343dff"
            md_sys_color_tertiary_light = "#c00100"
            md_sys_color_background_light = "#fffbff"
            md_sys_color_on_surface_light = "#1b1b1f"
            md_sys_color_surface_variant_light = "#e4e1ec"
            md_sys_color_outline_variant_light = "#c7c5d0"
            # DARK
            md_sys_color_primary_dark = "#7c84ff"
            md_sys_color_primary_container_dark = "#0000ef"
            md_sys_color_tertiary_dark = "#ff5540"
            md_sys_color_tertiary_container_dark = "#930100"
            md_sys_color_background_dark = "#1b1b1f"
            md_sys_color_on_surface_dark = "#e5e1e6"
            md_sys_color_surface_variant_dark = "#46464f"
            md_sys_color_outline_variant_dark = "#46464f"
        
            piece_hover_red_overlay_dark = '#bf857c'
            piece_hover_red_overlay_light = '#a04040'
            piece_hover_blue_overlay_dark = '#8e91bf'
            piece_hover_blue_overlay_light = '#5a5ebf'
            cannot_play_border_color_dark = '#e7c349'
            cannot_play_border_color_light = '#6e5e00'
        
        use_light_theme = settings_data['use_light_theme']

        if not use_light_theme:
            background_color = md_sys_color_background_dark
            on_background_color = md_sys_color_on_surface_dark
            button_background_color = md_sys_color_background_dark
            button_outline_color = md_sys_color_on_surface_dark
            button_text_color = md_sys_color_on_surface_dark
            surface_color = md_sys_color_surface_variant_dark

            placed_piece_red = md_sys_color_tertiary_dark
            valid_placement_red = md_sys_color_tertiary_container_dark
            piece_hover_red = md_ref_palette_tertiary70

            placed_piece_blue = md_sys_color_primary_dark
            valid_placement_blue = md_sys_color_primary_container_dark
            piece_hover_blue = md_ref_palette_primary70

            invalid_placement = md_sys_color_outline_variant_dark

            board_cell_outline_color = md_sys_color_outline_variant_dark

            piece_hover_blue_overlay = piece_hover_blue_overlay_dark
            piece_hover_red_overlay = piece_hover_red_overlay_dark
            cannot_play_border_color = cannot_play_border_color_dark

            selected_theme = 'dark' # Servira pour les différentes icônes du programme
        else:
            background_color = md_sys_color_background_light
            on_background_color = md_sys_color_on_surface_light
            button_background_color = md_sys_color_background_light
            button_outline_color = md_sys_color_on_surface_light
            button_text_color = md_sys_color_on_surface_light
            surface_color = md_sys_color_surface_variant_light

            placed_piece_red = md_sys_color_tertiary_light
            valid_placement_red = md_ref_palette_tertiary70
            piece_hover_red = md_ref_palette_tertiary50

            placed_piece_blue = md_sys_color_primary_light
            valid_placement_blue = md_ref_palette_primary70
            piece_hover_blue = md_ref_palette_primary50

            invalid_placement = md_sys_color_outline_variant_light

            board_cell_outline_color = md_sys_color_outline_variant_light

            piece_hover_blue_overlay = piece_hover_blue_overlay_light
            piece_hover_red_overlay = piece_hover_red_overlay_light
            cannot_play_border_color = cannot_play_border_color_light

            selected_theme = 'light' # Servira pour les différentes icônes du programme

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

        player_1_has_selected_piece = False
        player_2_has_selected_piece = False
        has_a_player_won = False
        color_blind_mode = settings_data['color_blind_mode']
        use_space_to_mirror = settings_data['use_space_to_mirror']
        use_middle_starting_cases = settings_data['use_middle_starting_cases']

        orientation_id = 0

        last_event_coordinates_copy = []
        relative_positions = [[0, 0]]
        relative_positions_reference = [[0, 0]]

        board = []
        board_cells = []
        player_1_pieces_cells = []
        player_2_pieces_cells = []

        current_player = 0

        red_corners_coordinates = []
        blue_corners_coordinates = []
        common_corners_coordinates = []
        red_cases_coordinates = []
        blue_cases_coordinates = []

        player_1_score = 0
        player_2_score = 0

        settings_file.close() # On ferme le fichier de paramètres pour éviter les problèmes

    def main_menu(self):
        global how_to_play_label, main_menu_frame
        
        for i in self.master.winfo_children():
            i.destroy() # On supprime tout le contenu de la fenêtre
        
        self.reset_variables() # On appelle la fonction qui réinitialise les variables du programme

        self.master.configure(bg=background_color) # On change la couleur de fond de la fenêtre

        style.configure('TButton', background=button_background_color, focuscolor=button_background_color, relief='flat') # On s'assure que les boutons ont bien les bonnes couleurs
        style.map('TButton', background=[('active', button_background_color), ('disabled', button_background_color)], relief=[('pressed', 'flat')])

        main_menu_frame = Frame(self.master, background=background_color) # On crée le cadre principal
        main_menu_frame.pack(expand=True) # On affiche le cadre dans la fenêtre
        main_menu_frame.columnconfigure(4, weight=1)

        play = Label(self.master, text="Appuyez pour Jouer", **large_label_style) # On crée le texte "Appuyez pour Jouer"
        play.pack(pady=50) # On affiche le texte dans le cadre

        version_label = Label(main_menu_frame, text=version_number, background=background_color, foreground=invalid_placement, font=('Consolas', 15)) # On crée le texte qui affiche la version du programme
        version_label.grid(row=0, column=5) # Le texte est affiché

        blocus_logo_canvas = Canvas(main_menu_frame, width=840, height=224, bd=0, highlightthickness=0, relief='flat', background=background_color) # On crée le canvas sur lequel sera placé le logo du programme
        blocus_logo_canvas.grid(column=0, row=1, columnspan=6, pady=10) # Le canvas est placé
        
        with open("settings.json", "r") as settings_file:
            settings_data = json.load(settings_file)

        self.blocus_logo = PhotoImage(file=f"res/img/{selected_theme}/blocus_logo.png") if not settings_data['use_purple_and_yellow'] else PhotoImage(file=f"res/img/{selected_theme}/blocus_logo_alt.png") # On récupère l'image du logo
        blocus_logo_canvas.create_image(0, 0, anchor='nw', image=self.blocus_logo) # On place le logo sur le canvas mentionné ci-dessus

        settings_file.close()

        self.github_logo = PhotoImage(file=f'res/img/{selected_theme}/github_logo.png') # On récupère l'image du logo GitHub
        github_button = Button(main_menu_frame, image=self.github_logo, command=self.open_github_page, compound='center', width=2, cursor="hand2") # On crée le bouton qui ouvrira le lien GitHub du projet dans le navigateur
        github_button.grid(column=0, row=0) # Le bouton est placé

        self.about_icon = PhotoImage(file=f'res/img/{selected_theme}/about_icon.png') # On récupère l'image de l'icône "about_icon.png"
        about_button = Button(main_menu_frame, image=self.about_icon, command=self.about_blocus_duo, compound='center', width=2, cursor="hand2") # On crée le bouton qui affichera les auteurs du projet
        about_button.grid(column=2, row=0) # Le bouton est placé

        self.settings_icon = PhotoImage(file=f'res/img/{selected_theme}/settings_icon.png') # On récupère l'image de l'icône "about_icon.png"
        settings_button = Button(main_menu_frame, image=self.settings_icon, command=self.settings, compound='center', width=2, cursor="hand2") # On crée le bouton qui affichera les auteurs du projet
        settings_button.grid(column=1, row=0) # Le bouton est placé

        how_to_play_label = Label(main_menu_frame, text='Comment jouer ?', **small_label_style, cursor="hand2")
        how_to_play_label.grid(column=3, row=0, padx=5)
        how_to_play_label.bind("<Motion>", self.add_underline_how_to_play_label) # Survol : on souligne le texte
        how_to_play_label.bind("<Leave>", self.remove_underline_how_to_play_label) # La souris quitte le texte, on enlève le soulignage
        how_to_play_label.bind("<Button-1>", self.how_to_play) # On clique sur le texte : ouverture de la page "Comment jouer"

        main_menu_frame.bind("<Button-1>", self.blocus_duo)    #
        play.bind("<Button-1>", self.blocus_duo)               # On "bind" plusieurs éléments pour que le jeu soit lancé en cliquant sur ces éléments
        blocus_logo_canvas.bind("<Button-1>", self.blocus_duo) #
    
    def about_blocus_duo(self):
        messagebox.showinfo("Blocus", "Projet supervisé de NSI\nZiad (ziadOUA) & Djibril")
    
    def open_github_page(self):
        webbrowser.open_new('https://github.com/ziadOUA/Blocus')
    
    def add_underline_how_to_play_label(self, event):
        global how_to_play_label
        how_to_play_label["font"] = ('Consolas', 10, 'underline') # On souligne le texte

    def remove_underline_how_to_play_label(self, event):
        global how_to_play_label
        how_to_play_label["font"] = ('Consolas', 10) # On ne souligne plus le texte
    
    def how_to_play(self, event):
        for i in self.master.winfo_children():
            i.destroy() # On supprime tout le contenu de la fenêtre
        
        main_menu_frame = Frame(self.master, background=background_color) # On crée un cadre principal, pour pouvoir facilement centrer les différents éléments
        main_menu_frame.pack(expand=True)

        top_part = Frame(main_menu_frame, background=background_color)
        top_part.grid(row=0, column=0, sticky='ew')
        top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        self.back_icon = PhotoImage(file=f'res/img/{selected_theme}/back_icon.png') # On récupère l'image de l'icône "back_icon.png"
        back_button = Button(top_part, image=self.back_icon, command=self.main_menu, compound='center', width=2, cursor="hand2") # On crée un bouton retour
        back_button.grid(column=0, row=0) # Le bouton est placé

        how_to_play_label = Label(top_part, text='Comment jouer', **xlarge_label_style) # Création d'un titre principal
        how_to_play_label.grid(column=1, row=0, sticky='ew')

        Label(top_part, text='                ', background=background_color).grid(column=2, row=0) # Espace servant à centrer le titre principal

        controls_container = Frame(main_menu_frame, background=background_color) # Cadre qui contiendra les explications relatives aux contrôles
        controls_container.grid(row=1, column=0, sticky='w', pady=10)

        left_click_icon_canvas = Canvas(controls_container, width=40, height=40, bd=0, highlightthickness=0, relief='flat', background=background_color) # Canvas qui contiendra l'image "left_click_icon"
        left_click_icon_canvas.grid(column=0, row=0)

        self.left_click_icon = PhotoImage(file=f"res/img/{selected_theme}/mouse_left_click_icon.png") # On récupère l'image de l'icône "mouse_left_click_icon.png"
        left_click_icon_canvas.create_image(0, 0, anchor='nw', image=self.left_click_icon) # L'image est placée dans le canvas

        left_click_label = Label(controls_container, text='Sélectionnez une pièce en faisant un click gauche', **medium_label_style) # Informations sur comment sélectionner une pièce
        left_click_label.grid(column=1, row=0, sticky='w', padx=10)
        # Informations supplémentaires sur le click gauche
        Label(controls_container, text='→ Vous pouvez la remettre en appuyant n\'importe où sur le range-pièces', **medium_label_style).grid(column=1, row=1, sticky='w', padx=10)
        Label(controls_container, text='→ Placez-la sur le plateau lorsque la pièce se colore de la couleur du joueur actif', **medium_label_style).grid(column=1, row=2, sticky='w', padx=10)
        
        right_click_icon_canvas = Canvas(controls_container, width=40, height=40, bd=0, highlightthickness=0, relief='flat', background=background_color) # Canvas qui contiendra l'image "right_click_icon"
        right_click_icon_canvas.grid(column=0, row=3)

        self.right_click_icon = PhotoImage(file=f"res/img/{selected_theme}/mouse_right_click_icon.png") # On récupère l'image de l'icône "mouse_right_click_icon.png"
        right_click_icon_canvas.create_image(0, 0, anchor='nw', image=self.right_click_icon) # L'image est placée dans le canvas

        right_click_label = Label(controls_container, text='Tournez la pièce en faisant un click droit', **medium_label_style) # Informations sur comment tourner une pièce
        right_click_label.grid(column=1, row=3, sticky='w', padx=10)

        middle_click_icon_canvas = Canvas(controls_container, width=40, height=40, bd=0, highlightthickness=0, relief='flat', background=background_color) # Canvas qui contiendra l'image "middle_click_icon"
        middle_click_icon_canvas.grid(column=0, row=4)

        self.middle_click_icon = PhotoImage(file=f"res/img/{selected_theme}/mouse_middle_click_icon.png") # On récupère l'image de l'icône "mouse_middle_click_icon.png"
        middle_click_icon_canvas.create_image(0, 0, anchor='nw', image=self.middle_click_icon) # L'image est placée dans le canvas

        middle_click_label = Label(controls_container, text='Miroitez la pièce en faisant un click du milieu', **medium_label_style) # Informations sur comment miroiter une pièce
        middle_click_label.grid(column=1, row=4, sticky='w', padx=10)
        # Informations supplémentaires sur le click du milieu
        Label(controls_container, text='→ Avec la touche [ESPACE] si activé dans les paramètres', **medium_label_style).grid(column=1, row=5, sticky='w', padx=10)

        game_rules_container = Frame(main_menu_frame, background=background_color) # Cadre qui contiendra les règles du jeu
        game_rules_container.grid(column=0, row=6, sticky='ew', pady=20)

        game_rules_title = Label(game_rules_container, text='Règles', **xlarge_label_style) # Titre de la section
        game_rules_title.grid(row=0, column=0, pady=10, sticky='w')

        rules = ['• Les premières pièces doivent être placées dans les cases colorées', 
                 '• Des pièces de même couleur ne peuvent se toucher que par les coins', 
                 '• Dès qu\'un joueur est bloqué, l\'autre joueur joue jusqu\'à ce qu\'il le soit aussi'] # Liste de règles
        
        for rule in rules:
            Label(game_rules_container, text=rule, **medium_label_style).grid(row=rules.index(rule) + 1, column=0, sticky='w') # On place les différentes règles grâce à une boucle (pour éviter d'inutiles répétitions)

    def blocus_duo(self, event):
        global board_canvas, board_cells, board, win_label, board_top_part, current_player, player_1_pieces, player_2_pieces, player_1_pieces_list, player_1_pieces_cells, player_2_pieces_cells
        global red_corners_coordinates, blue_corners_coordinates, common_corners_coordinates
        global board_cells, player_1_pieces_cells, player_2_pieces_cells
        global board_cell_size, board_size
        global red_starting_corner, blue_starting_corner
        global player_1_score_label, player_2_score_label
        global player_1_hint_button, player_2_hint_button
        global player_1_pieces_top_part, player_2_pieces_top_part
        global player_1_pieces_container, player_2_pieces_container
        
        for i in self.master.winfo_children():
            i.destroy() # idem

        main_menu_frame = Frame(self.master, background=background_color) # On crée un cadre principal, pour pouvoir facilement centrer les différents éléments
        main_menu_frame.pack(expand=True)

        board = [[' ' for _ in range(board_size)] for _ in range(board_size)] # Création du plateau grâce à une compréhension de liste
        
        if not use_middle_starting_cases:
            board[-1][0] = 'RC' # On place les cases de départ, où la première pièce de couleur correspondante devra être placée
            board[0][-1] = 'BC'
            red_corners_coordinates.append([0, board_size - 1]) # On ajoute les coordonnées des cases de départ mentionnées ci-dessus
            blue_corners_coordinates.append([board_size - 1, 0])
        else:
            board[4][4] = 'RC' # On place les cases de départ, où la première pièce de couleur correspondante devra être placée
            board[-5][-5] = 'BC'
            red_corners_coordinates.append([4, 4]) # On ajoute les coordonnées des cases de départ mentionnées ci-dessus
            blue_corners_coordinates.append([board_size - 5, board_size - 5])

        board_canvas = Canvas(main_menu_frame, width=board_size * board_cell_size, height=board_size * board_cell_size, bd=0, highlightthickness=1, relief='flat', highlightbackground=board_cell_outline_color, background=background_color) # On crée un canvas pour le plateau
        board_canvas.grid(column=1, row=2, padx=10) # On place le canvas

        player_1_pieces_container = Frame(main_menu_frame, highlightbackground=placed_piece_red, highlightthickness=5, height=626, width=274, background=surface_color)
        player_1_pieces_container.grid(row=2, column=0) # On place le nouveau cadre dans le cadre principal
        player_1_pieces = Canvas(player_1_pieces_container, width=264, height=616, bd=0, highlightthickness=0, relief='solid') # On crée un canvas qui affiche les pièces du joueur 1
        player_1_pieces.pack() # On place le canvas

        player_2_pieces_container = Frame(main_menu_frame, highlightbackground=background_color, highlightthickness=5, height=626, width=274, background=surface_color)
        player_2_pieces_container.grid(row=2, column=2) # On place le nouveau cadre dans le cadre principal
        player_2_pieces = Canvas(player_2_pieces_container, width=264, height=616, bd=0, highlightthickness=0, relief='solid') # On crée un canvas qui affiche les pièces du joueur 2
        player_2_pieces.pack() # On place le canvas

        board_top_part = Frame(main_menu_frame, background=background_color) # On crée un cadre pour la partie supérieure au plateau
        board_top_part.grid(row=1, column=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        board_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        self.back_icon = PhotoImage(file=f'res/img/{selected_theme}/back_icon.png') # On récupère l'image de l'icône "back_icon.png"
        back_button = Button(board_top_part, image=self.back_icon, command=self.main_menu, compound='center', width=2, cursor="hand2") # On crée un bouton retour
        back_button.grid(column=0, row=0) # Le bouton est placé
        
        win_label = Label(board_top_part, **xlarge_label_style) #On crée un texte qui affiche le tour du joueur
        win_label.grid(column=1, row=0, sticky='ew') # On place le texte 

        Label(board_top_part, text='                ', background=background_color).grid(column=2, row=0) # Création d'un objet servant à centrer le texte qui affiche le tour du joueur
        
        player_1_pieces_top_part = Frame(main_menu_frame, background=background_color) # On crée un cadre pour la partie supérieure aux pièces du joueur 1
        player_1_pieces_top_part.grid(column=0, row=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        player_1_pieces_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        self.hint_icon = PhotoImage(file=f'res/img/{selected_theme}/hint_icon.png') # On récupère l'image de l'icône "hint_icon.png"
        player_1_hint_button = Button(player_1_pieces_top_part, image=self.hint_icon, command=self.get_hint, compound='center', width=2, cursor="hand2") # On crée un bouton indice pour le joueur 1
        player_1_hint_button.grid(column=0, row=0) # Le bouton est placé

        player_1_score_label = Label(player_1_pieces_top_part, **xlarge_label_style) # On crée un texte qui affiche le score du joueur 1
        player_1_score_label.grid(column=1, row=0, sticky='ew') # Le texte est placé
        player_1_score_label['text'] = f'Score : {player_1_score}' # Le contenu du texte est mis à jour

        Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) # Création d'un objet servant à centrer le texte qui affiche le score du joueur 1
        
        player_2_pieces_top_part = Frame(main_menu_frame, background=background_color) # On crée un cadre pour la partie supérieure aux pièces du joueur 2
        player_2_pieces_top_part.grid(column=2, row=1, sticky='ew') # On place le nouveau cadre dans le cadre principal
        player_2_pieces_top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) # Création d'un objet servant à centrer le texte qui affiche le score du joueur 2

        player_2_hint_button = Button(player_2_pieces_top_part, image=self.hint_icon, command=self.get_hint, compound='center', width=2, cursor="hand2") # On crée un bouton indice pour le joueur 2
        Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) # On crée un objet qui prend la place du bouton indice du joueur 2, caché par défaut

        player_2_score_label = Label(player_2_pieces_top_part, **xlarge_label_style) # On crée un texte qui affiche le score du joueur 2
        player_2_score_label.grid(column=1, row=0, sticky='ew') # Le texte est placé
        player_2_score_label['text'] = f'Score : {player_2_score}' # Le contenu du texte est mis à jour

        if not use_middle_starting_cases:
            x1 = 1
            y1 = (board_size - 1) * board_cell_size + 1
        else:
            x1 = 1 + 4 * board_cell_size
            y1 = 4 * board_cell_size + 1
        x2 = x1 + board_cell_size - 1
        y2 = y1 + board_cell_size - 1
        red_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_red, width=0) # On crée un cercle rouge dans la case de départ du joueur 1

        if not use_middle_starting_cases:
            x1 = (board_size - 1) * board_cell_size + 1
            y1 = 1
        else:
            x1 = (board_size - 5) * board_cell_size + 1
            y1 = 1 + (board_size - 5) * board_cell_size
        x2 = x1 + board_cell_size - 1
        y2 = y1 + board_cell_size - 1
        blue_starting_corner = board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=valid_placement_blue, width=0) # On crée un cercle rouge dans la case de départ du joueur 2

        for line in range(board_size):
            row = []
            for column in range(board_size):
                x1 = column * board_cell_size + 1
                y1 = line * board_cell_size + 1
                x2 = x1 + board_cell_size - 1
                y2 = y1 + board_cell_size - 1 
                cell = board_canvas.create_rectangle(x1, y1, x2, y2, fill=transparent, outline=board_cell_outline_color) # On crée un rectangle pour chaque case du plateau
                row.append(cell)
            board_cells.append(row) # Tous les objets correspondant aux cases sont ajoutés à la liste "board_cells", qui permettra de les éditer facilement

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

        # On "bind" le plateau à des événements
        board_canvas.bind("<Button-1>", self.on_board_click) # Clic : la pièce sélectionnée est placée
        if use_space_to_mirror:
            board_canvas.bind_all('<space>', self.mirror_piece) # Si le paramètre est activé, fait que la touche espace miroite la pièce sélectionnée
        else:
            board_canvas.bind('<Button-2>', self.mirror_piece)
            board_canvas.unbind_all('<space>')
        board_canvas.bind("<Button-3>", self.rotate_piece) # Clic droit : rotation de la pièce sélectionnée
        board_canvas.bind("<Motion>", self.on_board_hover) # La souris bouge sur le plateau
        board_canvas.bind("<Leave>", self.on_board_leave) # La souris quitte le canvas

        # On "bind" les range-pièces à des événements
        player_1_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic : la pièce est sélectionnée
        player_1_pieces.bind("<Motion>", self.on_pieces_hover) # Survol
        player_1_pieces.bind("<Leave>", self.on_pieces_leave) # La souris quitte le range-pièces du joueur 1
        player_2_pieces.bind("<Button-1>", self.on_player_pieces_click) # Clic : la pièce est sélectionnée
        player_2_pieces.bind("<Motion>", self.on_pieces_hover) # Survol
        player_2_pieces.bind("<Leave>", self.on_pieces_leave) # La souris quitte le range-pièces du joueur 2

    def on_board_click(self, event):
        global board, current_player, adjacent_coordinates, relative_positions, player_1_has_selected_piece, player_2_has_selected_piece, has_a_player_won
        global board_cell_size, board_size
        global player_1_score, player_2_score
        global player_1_pieces_top_part, player_2_pieces_top_part
        global player_1_hint_button, player_2_hint_button
        global player_1_pieces_container, player_2_pieces_container
        global win_label
        
        column_event = event.x // board_cell_size
        line_event = event.y // board_cell_size
        if line_event > board_size - 1: line_event = board_size - 1;
        if column_event > board_size - 1: column_event = board_size - 1;

        # start = timer() # DEBUG

        if board[line_event][column_event] in ['RH', 'BH']: # Vérifie que, lorsque le plateau est cliqué, la pièce pouvait bien être placée
            for line in range(board_size):
                for column in range(board_size):
                    if board[line][column] == 'RH':
                        board[line][column] = 'R'
                        red_cases_coordinates.append([column, line])
                        for k in adjacent_coordinates:
                            player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=background_color)
                        
                        if color_blind_mode:
                            x1 = column * board_cell_size + 1
                            y1 = line * board_cell_size + 1
                            x2 = x1 + board_cell_size - 1
                            y2 = y1 + board_cell_size - 1 
                            board_canvas.create_rectangle(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=background_color, width=0)

                        player_1_has_selected_piece = False
                    elif board[line][column] == 'BH':
                        board[line][column] = 'B'
                        blue_cases_coordinates.append([column, line])
                        for k in adjacent_coordinates:
                            player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=background_color)
                        player_2_has_selected_piece = False

            if current_player == 0:
                player_1_score += len(adjacent_coordinates) # On ajoute au score le nombre de carreaux placés sur le plateau
            else:
                player_2_score += len(adjacent_coordinates) # On ajoute au score le nombre de carreaux placés sur le plateau

            self.define_possible_corners() # On place les coins où des pièces peuvent être placées

            if current_player == 0:
                if self.can_still_play(player=1): # On vérifie si le joueur 2 peut bien jouer
                    current_player = 1 # On change de joueur
                    player_1_hint_button.grid_forget() # On retire le bouton indice du joueur 1...
                    Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) #... remplacé par un objet vide, pour centrer le texte du score
                    player_2_hint_button = Button(player_2_pieces_top_part, image=self.hint_icon, command=self.get_hint, compound='center', width=2, cursor="hand2") # Le bouton indice du joueur 2 est redéfini
                    player_2_hint_button.grid(column=2, row=0) # Le bouton est placé
                    player_1_pieces_container.configure(highlightbackground=background_color)
                    player_2_pieces_container.configure(highlightbackground=placed_piece_blue) # On met un bord coloré autour du range-pièces du joueur actif 
                else:
                    player_2_pieces_container.configure(highlightbackground=cannot_play_border_color)
            else:
                if self.can_still_play(player=0): # On vérifie si le joueur 1 peut bien jouer
                    current_player = 0 # On change de joueur
                    player_2_hint_button.grid_forget() # On retire le bouton indice du joueur 2...
                    Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0) #... remplacé par un objet vide, pour centrer le texte du score
                    player_1_hint_button = Button(player_1_pieces_top_part, image=self.hint_icon, command=self.get_hint, compound='center', width=2, cursor="hand2") # Le bouton indice du joueur 1 est redéfini
                    player_1_hint_button.grid(column=0, row=0) # Le bouton est placé
                    player_1_pieces_container.configure(highlightbackground=placed_piece_red) # On met un bord coloré autour du range-pièces du joueur actif
                    player_2_pieces_container.configure(highlightbackground=background_color)
                else:
                    player_1_pieces_container.configure(highlightbackground=cannot_play_border_color)
            
            if not self.can_still_play(player=0) and not self.can_still_play(player=1): # Si aucun des deux joueurs ne peut jouer
                current_player = 999 # Le jeu est bloqué
                
                player_1_still_has_a_piece = False
                player_2_still_has_a_piece = False

                for line in range(28): # On enlève autant de points que de carrés non-placés
                    for column in range(12):
                        if player_1_pieces_list[line][column] == 'O':
                            player_1_score -= 1
                            player_1_still_has_a_piece = True
                        if player_2_pieces_list[line][column] == 'O':
                            player_2_score -= 1
                            player_2_still_has_a_piece = True
                
                if not player_1_still_has_a_piece:
                    player_1_score += 15 # Ajoute 15 au score si toutes les pièces ont été posées
                if not player_2_still_has_a_piece:
                    player_2_score += 15 # Ajoute 15 au score si toutes les pièces ont été posées
                
                player_1_score_label['text'] = f"Score : {player_1_score}" # On met à jour le texte qui affiche le score du joueur actif
                player_1_score_label.update()
                player_2_score_label['text'] = f"Score : {player_2_score}"
                player_2_score_label.update()
                
                if player_1_score > player_2_score:
                    win_label['text'] = 'Victoire du Joueur 1' # Si le score du joueur 1 est supérieur à celui du joueur 2, alors victoire du joueur 1
                    has_a_player_won = True
                elif player_1_score < player_2_score:
                    win_label['text'] = 'Victoire du Joueur 2' # Si le score du joueur 1 est inférieur à celui du joueur 2, alors victoire du joueur 2
                    has_a_player_won = True
                elif player_1_score == player_2_score:
                    win_label['text'] = 'Égalité' # Si les deux scores sont égaux, alors égalité
                    has_a_player_won = False
                win_label.update() # On met à jour le texte pour qu'il affiche l'état du jeu
                
                player_1_hint_button.grid_forget() # On retire les boutons indice des deux joueurs...
                player_2_hint_button.grid_forget()
                Label(player_1_pieces_top_part, text='                ', background=background_color).grid(column=0, row=0) #... remplacés par des objets vides pour centrer les scores
                Label(player_2_pieces_top_part, text='                ', background=background_color).grid(column=2, row=0)
                player_1_pieces_container.configure(highlightbackground=cannot_play_border_color) # On ajoute une bordure jaune autour des pièces des deux joueurs
                player_2_pieces_container.configure(highlightbackground=cannot_play_border_color)
            
            adjacent_coordinates = []
            relative_positions = [[0, 0]]
            self.update_board_canvas() # On met à jour le canvas du plateau

            # end = timer() # DEBUG
            # print(f'Piece placed in {round((end - start) * 1000)} ms') # DEBUG

    def on_board_hover(self, event):
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
            self.draw_piece_on_board(column_event, line_event) # "Dessine" la pièce sélectionnée sur le plateau, ou bien un carré si aucune pièce n'est sélectionnée

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
            return False # Renvoie "False" si la pièce est en dehors du plateau
        return True

    def reset_hover(self):
        global board
        
        for line in board:
            for k, n in enumerate(line):
                if n == 'H' or n == 'RH' or n == 'BH':
                    line[k] = ' '

    def define_possible_corners(self):
        global board_size
        
        memoire = [] # Création de variables "mémoires" dans le but de stocker des choses
        memoire2 = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Directions : HAUT, BAS, DROITE, GAUCHE
        directions_corners = [(1, 1), (-1, -1), (1, -1), (-1, 1)] # Coins : DROIT SUPÉRIEUR, GAUCHE INFÉRIEUR, DROIT INFÉRIEUR, GAUCHE SUPÉRIEUR

        if current_player == 0:
            player_color = 'R'
            color_corners_coordinates = red_corners_coordinates
        else:
            player_color = 'B'
            color_corners_coordinates = blue_corners_coordinates
        
        for line in range(board_size):
            for column in range(board_size): # On fait une itération sur l'ensemble des cases du plateau
                invalid_element = False # Divers drapeaux
                touches_corner = False
                touches_red_corner = False
                touches_blue_corner = False
                
                if board[line][column] == ' ': # Si la case est vide
                    for direction in directions:
                        if self.is_within_the_main_board(column + direction[0], line + direction[1]): # On vérifie si la direction dans laquelle on recherche est comprise dans le plateau, pour éviter des erreurs de dépassement d'index
                            if board[line + direction[1]][column + direction[0]] == player_color: # On vérifie si la case est en contact direct avec une case de couleur du joueur actif
                                invalid_element = True # La case est invalidée le cas échéant

                    if not invalid_element: # Si la case n'est pas déjà invalide
                        for direction in directions_corners:
                            if self.is_within_the_main_board(column + direction[0], line + direction[1]): # On vérifie si le coin qu'on essaie de voir est bien compris dans le plateau, pour les mêmes raisons que ci-dessus
                                if board[line + direction[1]][column + direction[0]] == player_color: # Si au moins un des coins est de la couleur du joueur actif
                                    touches_corner = True #... on lève le drapeau "touches_corner"

                        if touches_corner:
                            memoire.append([column, line]) # Les coordonnées de la case sont ajoutées à la mémoire

                if board[line][column] in ['RC', 'BC']:
                    for direction in directions_corners: # Boucle qui servira à tester si la case testée est un coin commun entre une pièce rouge et bleue
                        if self.is_within_the_main_board(column + direction[0], line + direction[1]):
                            if board[line + direction[1]][column + direction[0]] == 'R':
                                touches_red_corner = True
                            elif board[line + direction[1]][column + direction[0]] == 'B':
                                touches_blue_corner = True

                    if touches_red_corner and touches_blue_corner:
                        memoire2.append([column, line]) # Les coordonnées de la case sont ajoutées à la mémoire

        for element in memoire:
            if board[element[1]][element[0]] == ' ':
                color_corners_coordinates.append(element) # Ajoute les coordonnées testées à la liste correspondant à la couleur du joueur actif

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
        global board_size, relative_positions, relative_positions_reference
        global orientation_id, mirror_id

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if player == 0:
            player_pieces_list = player_1_pieces_list
            player_corner_value = 'RC'
            player_color = 'R'
        else:
            player_pieces_list = player_2_pieces_list
            player_corner_value = 'BC'
            player_color = 'B'

        for line in range(board_size): # Itération sur l'ensemble du plateau
            for column in range(board_size):
                if board[line][column] == player_corner_value or board[line][column] == 'RBC':
                    for piece_line in range(len(player_pieces_list)):
                        for piece_column in range(len(player_pieces_list[0])):
                            if player_pieces_list[piece_line][piece_column] == 'O': # Itération sur l'ensemble des pièces du joueur passé comme paramètre dans la fonction
                                self.get_adjacent_pieces_coordinates(player_pieces_list, piece_column, piece_line, True)
                                
                                for _ in range(4): # Teste les différentes rotations possibles
                                    directions_from_center_rotated = [list(direction) for direction in relative_positions_reference]

                                    if orientation_id == 0:
                                        directions_from_center_rotated = [list(direction) for direction in relative_positions_reference] # 0°
                                    elif orientation_id == 1:
                                        directions_from_center_rotated = [[-direction[1], direction[0]] for direction in relative_positions_reference] # 90°
                                    elif orientation_id == 2:
                                        directions_from_center_rotated = [[-direction[0], -direction[1]] for direction in relative_positions_reference] # 180°
                                    elif orientation_id == 3:
                                        directions_from_center_rotated = [[direction[1], -direction[0]] for direction in relative_positions_reference] # 270°
                                    
                                    orientation_id = (orientation_id + 1) % 4

                                    for _ in range(4): # Miroite les pièces
                                        directions_from_center_mirrored = [list(direction) for direction in directions_from_center_rotated]

                                        for i, direction in enumerate(directions_from_center_rotated):
                                            directions_from_center_mirrored[i][0] = direction[0] if mirror_id in {0, 2, 3} else -direction[0] # On inverse les valeurs horizontales si "mirror_id" est égal à 0, 2 ou 3
                                            directions_from_center_mirrored[i][1] = direction[1] if mirror_id in {0, 1, 2} else -direction[1] # On inverse les valeurs verticales si "mirror_id" est égal à 0, 1 ou 2
                                        
                                        mirror_id = (mirror_id + 1) % 4

                                        relative_positions = directions_from_center_mirrored

                                        out_of_bounds = False
                                        can_fit = True
                                        can_be_placed = True

                                        for position in relative_positions:
                                            if not self.is_within_the_main_board(column + position[0], line + position[1]): # La pièce est invalidée si une partie dépasse le plateau
                                                out_of_bounds = True
                                                can_fit = False
                                                can_be_placed = False
                                            
                                        if not out_of_bounds:
                                            for position in relative_positions:
                                                if board[line + position[1]][column + position[0]] in ['R', 'B']: # La pièce est invalidée si elle empiète sur d'autres pièces
                                                    can_fit = False
                                                    can_be_placed = False
                                        
                                        if can_fit:
                                            for position in relative_positions:
                                                for direction in directions:
                                                    if self.is_within_the_main_board(column + position[0] + direction[0], line + position[1] + direction[1]): # La pièce est invalidée si elle est en contact avec d'autres pièces du même joueur
                                                        if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == player_color:
                                                            can_be_placed = False
                                    
                                        if can_be_placed:
                                            return True # On retourne "True" dès qu'une pièce est valide, pour économiser du temps de calcul
        return False # Le joueur ne peut plus jouer

    def get_hint(self):
        global player_1_pieces_list, player_2_pieces_list
        global board_size, relative_positions
        global orientation_id, player_1_score, player_2_score, mirror_id
        global player_1_has_selected_piece, player_2_has_selected_piece

        if player_1_has_selected_piece or player_2_has_selected_piece: # Empêche le joueur de demander un indice tout en ayant une pièce sélectionnée
            return None # Si tel est le cas, l'éxecution de la fonction est stoppée, afin d'économiser du temps de calcul

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        has_found_a_piece = False

        if current_player == 0:
            player_pieces_list = player_1_pieces_list
            player_corner_value = 'RC'
            player_color = 'R'
            player_score = player_1_score
            player_score_label = player_1_score_label
        else:
            player_pieces_list = player_2_pieces_list
            player_corner_value = 'BC'
            player_color = 'B'
            player_score = player_2_score
            player_score_label = player_2_score_label
        
        self.reset_hover()

        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == player_corner_value or board[line][column] == 'RBC':
                    for piece_line in range(len(player_pieces_list)):
                        for piece_column in range(len(player_pieces_list[0])):
                            if player_pieces_list[piece_line][piece_column] == 'O':
                                if not has_found_a_piece:
                                    self.get_adjacent_pieces_coordinates(player_pieces_list, piece_column, piece_line, True)

                                    for _ in range(4): # On teste pour toutes les rotations possibles
                                        directions_from_center_rotated = [list(direction) for direction in relative_positions_reference]

                                        if orientation_id == 0:
                                            directions_from_center_rotated = [list(direction) for direction in relative_positions_reference] # 0°
                                        elif orientation_id == 1:
                                            directions_from_center_rotated = [[-direction[1], direction[0]] for direction in relative_positions_reference] # 90°
                                        elif orientation_id == 2:
                                            directions_from_center_rotated = [[-direction[0], -direction[1]] for direction in relative_positions_reference] # 180°
                                        elif orientation_id == 3:
                                            directions_from_center_rotated = [[direction[1], -direction[0]] for direction in relative_positions_reference] # 270°
                                        
                                        orientation_id = (orientation_id + 1) % 4

                                        for _ in range(4): # On miroite la pièce
                                            directions_from_center_mirrored = [list(direction) for direction in directions_from_center_rotated]

                                            for i, direction in enumerate(directions_from_center_rotated):
                                                directions_from_center_mirrored[i][0] = direction[0] if mirror_id in {0, 2, 3} else -direction[0] # On inverse les valeurs horizontales si "mirror_id" est égal à 0, 2 ou 3
                                                directions_from_center_mirrored[i][1] = direction[1] if mirror_id in {0, 1, 2} else -direction[1] # On inverse les valeurs verticales si "mirror_id" est égal à 0, 1 ou 2

                                            relative_positions = directions_from_center_mirrored
                                            mirror_id = (mirror_id + 1) % 4

                                            out_of_bounds = False # Divers drapeaux servants aux tests
                                            can_fit = True
                                            can_be_placed = True

                                            for position in relative_positions:
                                                # La pièce n'est valide que si elle ne sort pas du plateau
                                                if not self.is_within_the_main_board(column + position[0], line + position[1]):
                                                    out_of_bounds = True
                                                    can_fit = False
                                                    can_be_placed = False
                                                
                                            if not out_of_bounds:
                                                for position in relative_positions:
                                                # La pièce n'est valide que si elle n'empiète pas sur d'autres pièces
                                                    if board[line + position[1]][column + position[0]] in ['R', 'B']:
                                                        can_fit = False
                                                        can_be_placed = False
                                            
                                            if can_fit:
                                                for position in relative_positions:
                                                    for direction in directions:
                                                        # La pièce n'est valide que si elle n'entre pas en contact avec des pièces du joueur qui demande l'indice
                                                        if self.is_within_the_main_board(column + position[0] + direction[0], line + position[1] + direction[1]):
                                                            if board[line + position[1] + direction[1]][column + position[0] + direction[0]] == player_color:
                                                                can_be_placed = False
                                            
                                            if player_score >= 2 and can_be_placed and not has_found_a_piece: # L'indice n'est donné que si le joueur a assez de score (au moins 2)
                                                for position in relative_positions:
                                                    # On place des "H" dans la liste du plateau (board) là où une pièce peut être posée
                                                    board[line + position[1]][column + position[0]] = 'H'
                                                for line in range(board_size):
                                                    for column in range(board_size):
                                                        # On colore en gris là où une pièce peut être posée
                                                        if board[line][column] == ' ': board_canvas.itemconfig(board_cells[line][column], fill=background_color, outline=board_cell_outline_color);
                                                        if board[line][column] == 'H': board_canvas.itemconfig(board_cells[line][column], fill=invalid_placement, outline=board_cell_outline_color);
                                                has_found_a_piece = True # On lève le drapeau pour éviter que la fonction montre tous les placements possibles
                                                if current_player == 0:
                                                    player_1_score -= 2
                                                    player_1_score_label['text'] = f'Score : {player_1_score}' # On met à jour le texte qui affiche le score du joueur actif
                                                    player_1_score_label.update()
                                                else:
                                                    player_2_score -= 2
                                                    player_2_score_label['text'] = f'Score : {player_2_score}' # On met à jour le texte qui affiche le score du joueur actif
                                                    player_2_score_label.update()

    def draw_piece_on_board(self, event_x, event_y):
        global board, board_canvas, board_cells, relative_positions
        global board_size
        global red_cases_coordinates, blue_cases_coordinates
        
        out_of_bounds = False # Divers drapeaux servants aux tests
        can_be_drawn = True
        can_be_placed = False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for position in relative_positions:
            if not self.is_within_the_main_board(event_x + position[0], event_y + position[1]): # La pièce sort du plateau, elle n'est donc plus dessinée
                out_of_bounds = True
                for red_case_coordinate in red_cases_coordinates:
                    board_canvas.itemconfig(board_cells[red_case_coordinate[1]][red_case_coordinate[0]], fill=placed_piece_red, outline=placed_piece_red) # On restaure les couleurs des pièces placées
                
                for blue_case_coordinate in blue_cases_coordinates:
                    board_canvas.itemconfig(board_cells[blue_case_coordinate[1]][blue_case_coordinate[0]], fill=placed_piece_blue, outline=placed_piece_blue)

        self.reset_hover()

        if not out_of_bounds:
            memoire = []
            for position in relative_positions:
                for direction in directions:
                    if self.is_within_the_main_board(event_x + position[0] + direction[0], event_y + position[1] + direction[1]):
                        memoire.append(board[event_y + position[1] + direction[1]][event_x + position[0] + direction[0]]) # On enregistre les cases qui entourent la pièce sélectionnée

                if (current_player == 0 and 'R' not in memoire) or (current_player == 1 and 'B' not in memoire):
                    color_corners_coordinates = red_corners_coordinates if current_player == 0 else blue_corners_coordinates
                    if [event_x + position[0], event_y + position[1]] in color_corners_coordinates or [event_x + position[0], event_y + position[1]] in common_corners_coordinates:
                        can_be_placed = True
                else:
                    can_be_placed = False # Le placement de la pièce est invalide si la mémoire contient une case de la couleur du joueur actif
                
                if board[event_y + position[1]][event_x + position[0]] in ['R', 'B']:
                    # La pièce ne peut être placée à cet endroit car elle empiète sur d'autres pièces
                    can_be_drawn = False

            for red_case_coordinate in red_cases_coordinates:
                board_canvas.itemconfig(board_cells[red_case_coordinate[1]][red_case_coordinate[0]], fill=placed_piece_red, outline=placed_piece_red) # On restaure les couleurs des pièces placées
                board[red_case_coordinate[1]][red_case_coordinate[0]] = 'R'
            
            for blue_case_coordinate in blue_cases_coordinates:
                board_canvas.itemconfig(board_cells[blue_case_coordinate[1]][blue_case_coordinate[0]], fill=placed_piece_blue, outline=placed_piece_blue) # On restaure les couleurs des pièces placées
                board[blue_case_coordinate[1]][blue_case_coordinate[0]] = 'B'

            for position in relative_positions:
                if player_1_has_selected_piece and can_be_placed and can_be_drawn: # On indique que le placement est valide
                    board[event_y + position[1]][event_x + position[0]] = 'RH'
                elif player_2_has_selected_piece and can_be_placed and can_be_drawn:
                    board[event_y + position[1]][event_x + position[0]] = 'BH'
                else:
                    if board[event_y + position[1]][event_x + position[0]] == 'R':
                        board_canvas.itemconfig(board_cells[event_y + position[1]][event_x + position[0]], fill=piece_hover_red_overlay, outline=piece_hover_red_overlay) # La pièce est montrée "au-dessus" des autres pièces
                    elif board[event_y + position[1]][event_x + position[0]] == 'B':
                        board_canvas.itemconfig(board_cells[event_y + position[1]][event_x + position[0]], fill=piece_hover_blue_overlay, outline=piece_hover_blue_overlay) # La pièce est montrée "au-dessus" des autres pièces
                    elif board[event_y + position[1]][event_x + position[0]] in ['RC', 'BC', 'RBC', ' ']:
                        board[event_y + position[1]][event_x + position[0]] = 'H' # On indique que le placement est invalide dans le restant des cas

        for line in range(board_size):
            for column in range(board_size): # On ajoute les couleurs en fonction du contenu de la liste
                if board[line][column] == ' ': board_canvas.itemconfig(board_cells[line][column], fill=transparent, outline=board_cell_outline_color);
                if board[line][column] == 'H': board_canvas.itemconfig(board_cells[line][column], fill=invalid_placement, outline=board_cell_outline_color);
                if board[line][column] == 'RH': board_canvas.itemconfig(board_cells[line][column], fill=valid_placement_red, outline=valid_placement_red);
                if board[line][column] == 'BH': board_canvas.itemconfig(board_cells[line][column], fill=valid_placement_blue, outline=valid_placement_blue);

    def on_board_leave(self, event):
        global board_size
        
        self.reset_hover()
        
        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == ' ':
                    board_canvas.itemconfig(board_cells[line][column], fill=transparent, outline=board_cell_outline_color)
        
        for red_case_coordinate in red_cases_coordinates:
            board_canvas.itemconfig(board_cells[red_case_coordinate[1]][red_case_coordinate[0]], fill=placed_piece_red, outline=placed_piece_red) # On restaure les couleurs des pièces placées
            
        for blue_case_coordinate in blue_cases_coordinates:
            board_canvas.itemconfig(board_cells[blue_case_coordinate[1]][blue_case_coordinate[0]], fill=placed_piece_blue, outline=placed_piece_blue) # On restaure les couleurs des pièces placées

    def update_board_canvas(self):
        global board, board_canvas, board_cells
        global red_starting_corner, blue_starting_corner
        global win_label, player_1_score_label, player_2_score_label
        global player_1_score, player_2_score
        global board_size
        
        for line in range(board_size):
            for column in range(board_size):
                if board[line][column] == 'R':
                    color = placed_piece_red
                    outline = placed_piece_red
                elif board[line][column] == 'B':
                    color = placed_piece_blue
                    outline = placed_piece_blue
                else:
                    color = transparent
                    outline = board_cell_outline_color
                # Met à jour la couleur des cases en fonction de ce que contient la liste du plateau
                board_canvas.itemconfig(board_cells[line][column], fill=color, outline=outline)
        
        player_1_score_label['text'] = f"Score : {player_1_score}" # On met à jour le texte qui affiche le score du joueur actif
        player_1_score_label.update()
        player_2_score_label['text'] = f"Score : {player_2_score}"
        player_2_score_label.update()
    
    def on_player_pieces_click(self, event):
        global player_1_pieces_list, player_1_pieces, player_1_pieces_cells, player_2_pieces_list, player_2_pieces, player_2_pieces_cells
        global current_player, adjacent_coordinates, player_1_has_selected_piece, relative_positions, orientation_id, player_2_has_selected_piece

        column_event = event.x // 22
        line_event = event.y // 22
        if column_event > 11: column_event = 11;
        if line_event > 28: line_event = 28;

        if event.widget == player_1_pieces: # Définition de variables en fonction du range-pièces cliqué
            player_pieces = player_1_pieces
            player_pieces_list = player_1_pieces_list
            player_pieces_cells = player_1_pieces_cells
            player_id = 0
            player_has_selected_piece = player_1_has_selected_piece
            valid_placement_color = valid_placement_red
            placed_piece_color = placed_piece_red
        else:
            player_pieces = player_2_pieces
            player_pieces_list = player_2_pieces_list
            player_pieces_cells = player_2_pieces_cells
            player_id = 1
            player_has_selected_piece = player_2_has_selected_piece
            valid_placement_color = valid_placement_blue
            placed_piece_color = placed_piece_blue

        if player_id == current_player and not player_has_selected_piece and player_pieces_list[line_event][column_event] == 'O': # On vérifie que la case choisie n'est pas vide
            adjacent_coordinates = self.get_adjacent_pieces_coordinates(player_pieces_list, column_event, line_event, True) # On cherche à obtenir les coordonnées de tous les "O" autour des coordonnées cliquées
            for k in adjacent_coordinates: # On retire la pièce du range-pièces
                player_pieces_list[k[1]][k[0]] = ' ' 
                player_pieces.itemconfig(player_pieces_cells[k[1]][k[0]], fill=valid_placement_color)
            player_1_has_selected_piece = True if player_id == 0 else False # On lève le drapeau pour le joueur concerné
            player_2_has_selected_piece = True if player_id == 1 else False
            orientation_id = 0 # On réinitialise l'orientation
        elif player_id == current_player and player_has_selected_piece:
            for k in adjacent_coordinates: # La pièce est replacée dans le range-pièces
                player_pieces_list[k[1]][k[0]] = 'O'
                player_pieces.itemconfig(player_pieces_cells[k[1]][k[0]], fill=placed_piece_color)
            player_1_has_selected_piece = False if player_id == 0 else player_1_has_selected_piece # On lève le drapeau pour le joueur concerné
            player_2_has_selected_piece = False if player_id == 1 else player_2_has_selected_piece
            adjacent_coordinates = []
    
    def on_pieces_hover(self, event):
        global player_1_pieces_list, player_1_pieces, player_1_pieces_cells, player_2_pieces_list, player_2_pieces, player_2_pieces_cells
        global current_player, adjacent_coordinates_hover, relative_positions, last_event_coordinates_copy
        global player_1_has_selected_piece, player_2_has_selected_piece

        column_event = event.x // 22
        line_event = event.y // 22
        if column_event > 11: column_event = 11;
        if line_event > 28: line_event = 28;

        adjacent_coordinates_hover = []

        last_coords = [column_event, line_event]
        # Le code ci-dessous n'est exécuté qu'à chaque fois que la souris change de case, au lieu de l'exécuter au moindre mouvement
        if last_event_coordinates_copy != last_coords:
            last_event_coordinates_copy = [i for i in last_coords]

            if event.widget == player_1_pieces: # Définition de variables en fonction du range-pièces cliqué
                player_pieces = player_1_pieces
                player_pieces_list = player_1_pieces_list
                player_pieces_cells = player_1_pieces_cells
                player_id = 0
                player_has_selected_piece = player_1_has_selected_piece
                placed_piece_color = placed_piece_red
                hover_piece_color = piece_hover_red
            else:
                player_pieces = player_2_pieces
                player_pieces_list = player_2_pieces_list
                player_pieces_cells = player_2_pieces_cells
                player_id = 1
                player_has_selected_piece = player_2_has_selected_piece
                placed_piece_color = placed_piece_blue
                hover_piece_color = piece_hover_blue

            if player_id == current_player and not player_has_selected_piece:
                if player_pieces_list[line_event][column_event] == 'O': # On vérifie que la case choisie n'est pas vide
                    adjacent_coordinates_hover = self.get_adjacent_pieces_coordinates(player_pieces_list, column_event, line_event, False)
                    for k in adjacent_coordinates_hover:
                        player_pieces.itemconfig(player_pieces_cells[k[1]][k[0]], fill=hover_piece_color) # On colore la pièce survolée
                else:
                    relative_positions = [[0, 0]]
                    for line in range(28):
                        for column in range(11):
                            if player_pieces_list[line][column] == 'O':
                                # On recolore toutes les pièces du range-pièces concerné dans la couleur du joueur actif
                                player_pieces.itemconfig(player_pieces_cells[line][column], fill=placed_piece_color)

    def on_pieces_leave(self, event):
        global adjacent_coordinates_hover

        # On recolore toutes les pièces du range-pièces concerné dans la couleur du joueur actif
        if event.widget == player_1_pieces and not player_1_has_selected_piece and current_player == 0:
            for k in adjacent_coordinates_hover:
                player_1_pieces.itemconfig(player_1_pieces_cells[k[1]][k[0]], fill=placed_piece_red)
        elif event.widget == player_2_pieces and not player_2_has_selected_piece and current_player == 1:
            for k in adjacent_coordinates_hover:
                player_2_pieces.itemconfig(player_2_pieces_cells[k[1]][k[0]], fill=placed_piece_blue)

    def rotate_piece(self, event):
        global orientation_id, relative_positions, relative_positions_reference, directions_from_center_rotated

        if player_1_has_selected_piece or player_2_has_selected_piece:
            orientation_id = (orientation_id + 1) % 4 # On augmente la valeur
            directions_from_center_rotated = [list(direction) for direction in relative_positions_reference]

            if orientation_id == 0:
                directions_from_center_rotated = [list(direction) for direction in relative_positions_reference] # 0°
            elif orientation_id == 1:
                directions_from_center_rotated = [[-direction[1], direction[0]] for direction in relative_positions_reference] # 90°
            elif orientation_id == 2:
                directions_from_center_rotated = [[-direction[0], -direction[1]] for direction in relative_positions_reference] # 180°
            elif orientation_id == 3:
                directions_from_center_rotated = [[direction[1], -direction[0]] for direction in relative_positions_reference] # 270°

            relative_positions = directions_from_center_rotated
            self.draw_piece_on_board(last_event_coordinates_copy[0], last_event_coordinates_copy[1]) # On met à jour la pièce affichée avec les nouvelles valeurs
    
    def mirror_piece(self, event):
        global mirror_id, relative_positions, relative_positions_reference, directions_from_center_rotated

        if player_1_has_selected_piece or player_2_has_selected_piece:
            mirror_id = (mirror_id + 1) % 4 # On augmente la valeur
            directions_from_center_mirrored = [list(direction) for direction in directions_from_center_rotated] # On crée une copie de la liste "directions_from_center_rotated" sur laquelle on se basera
            
            for i, direction in enumerate(directions_from_center_rotated):
                directions_from_center_mirrored[i][0] = direction[0] if mirror_id in {0, 2, 3} else -direction[0] # On inverse les valeurs horizontales si "mirror_id" est égal à 0, 2 ou 3
                directions_from_center_mirrored[i][1] = direction[1] if mirror_id in {0, 1, 2} else -direction[1] # On inverse les valeurs verticales si "mirror_id" est égal à 0, 1 ou 2

            relative_positions = directions_from_center_mirrored
            self.draw_piece_on_board(last_event_coordinates_copy[0], last_event_coordinates_copy[1]) # On met à jour la pièce affichée avec les nouvelles valeurs

    def get_adjacent_pieces_coordinates(self, pieces_list, selected_case_x, selected_case_y, generate_relative_positions):
        global relative_positions, relative_positions_reference, directions_from_center_rotated
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        adjacent_cells = []
        relative_positions = []
        memoire = [[selected_case_x, selected_case_y]]

        while memoire: # On recommence tant que "memoire" n'est pas vide
            case_x, case_y = memoire.pop() # On enlève des coordonnées, affectées aux variables case_x et case_y

            # Condition, vraie si la case vérifiée est un "O" et n'est pas déjà dans la liste "adjacent_cells"
            if pieces_list[case_y][case_x] == 'O' and [case_x, case_y] not in adjacent_cells:
                adjacent_cells.append([case_x, case_y]) # On ajoute les coordonnées à la liste "adjacent_cells"
                for direction_x, direction_y in directions: # On vérifie dans les 4 directions différentes
                    adj_x = case_x + direction_x
                    adj_y = case_y + direction_y

                    # On verifie si la case que l'on essaie de vérifier se trouve bien au sein du range-pièces
                    if 0 <= adj_y < len(pieces_list) and 0 <= adj_x < len(pieces_list[0]):
                        if pieces_list[adj_y][adj_x] == 'O': # Si la case testée contient un "O"...
                            memoire.append([adj_x, adj_y]) # ...On l'ajoute à la mémoire pour qu'elle soit testée à son tour

        if generate_relative_positions:
            for adjacent_coordinates in adjacent_cells:
                relative_positions.append([adjacent_coordinates[0] - selected_case_x, adjacent_coordinates[1] - selected_case_y]) # On génère un ensemble de directions relatives par rapport à la souris
            relative_positions_reference = [list(direction) for direction in relative_positions]
            directions_from_center_rotated = [list(direction) for direction in relative_positions]

        return adjacent_cells

    def settings(self):
        global color_blind_mode_state, alternative_color_scheme_state, use_space_to_mirror_state, use_middle_starting_cases_state, use_light_theme_state
        
        for i in self.master.winfo_children():
            i.destroy() # On supprime tout le contenu de la fenêtre
        
        main_menu_frame = Frame(self.master, background=background_color) # On crée le cadre principal
        main_menu_frame.pack(expand=True) # On affiche le cadre dans la fenêtre

        top_part = Frame(main_menu_frame, background=background_color) # On crée un cadre supérieur contenant le titre de la page et un bouton retour
        top_part.grid(column=0, row=0, sticky='ew')
        top_part.columnconfigure(1, weight=1) # On configure la colonne 1 (= 2° colonne), pour qu'elle prenne toute la place possible

        settings_label = Label(top_part, text='Paramètres', **xlarge_label_style) # Titre de la page (Paramètres)
        settings_label.grid(column=1, row=0, sticky='ew')
        
        self.back_icon = PhotoImage(file=f'res/img/{selected_theme}/back_icon.png') # On récupère l'image de l'icône "back_icon.png"
        back_button = Button(top_part, image=self.back_icon, command=self.main_menu, compound='center', width=2, cursor="hand2") # On crée un bouton retour
        back_button.grid(column=0, row=0, sticky='w', pady=20)

        Label(top_part, text='                ', background=background_color).grid(column=2, row=0) # Espace servant à centrer le titre

        color_settings_section_label = Label(main_menu_frame, text='COULEURS', **small_label_style) # Titre de la section des paramètres de couleurs
        color_settings_section_label.grid(column=0, row=1, sticky='w')

        with open("settings.json", "r") as settings_file: # On ouvre le fichier paramètres
            settings_data = json.load(settings_file) # On récupère les données du fichier

        use_light_theme_state = BooleanVar() # Création de l'option "Thème clair"
        use_light_theme_state.set(settings_data['use_light_theme'])
        use_light_theme_checkbox = Checkbutton(
                                        main_menu_frame, 
                                        text='Thème clair', 
                                        onvalue=True, 
                                        offvalue=False, 
                                        variable=use_light_theme_state, 
                                        command=self.update_settings, 
                                        **large_label_style,
                                        bd=0,
                                        highlightthickness=0, 
                                        activebackground=background_color,
                                        activeforeground=on_background_color,
                                        relief='flat',
                                        selectcolor=background_color) # On crée une case à cocher
        use_light_theme_checkbox.grid(column=0, row=2, sticky='w')

        alternative_color_scheme_state = BooleanVar() # Création de l'option "Utiliser du violet et du jaune"
        alternative_color_scheme_state.set(settings_data['use_purple_and_yellow'])
        alternative_color_scheme_checkbox = Checkbutton(
                                                main_menu_frame, 
                                                text='Utiliser du violet et du jaune', 
                                                onvalue=True, 
                                                offvalue=False, 
                                                variable=alternative_color_scheme_state, 
                                                command=self.update_settings, 
                                                **large_label_style,
                                                bd=0,
                                                highlightthickness=0,
                                                activebackground=background_color,
                                                activeforeground=on_background_color,
                                                relief='flat',
                                                selectcolor=background_color) # On crée une case à cocher
        alternative_color_scheme_checkbox.grid(column=0, row=3, sticky='w')

        Label(main_menu_frame, text=' ', background=background_color).grid(column=0, row=4) # On crée un espace entre les différentes sections

        accessibility_settings_section_label = Label(main_menu_frame, text='ACCESSIBILITÉ', **small_label_style) # Titre de la section des paramètres d'accessibilité
        accessibility_settings_section_label.grid(column=0, row=5, sticky='w')

        color_blind_mode_state = BooleanVar() # Création de l'option "Mode daltonien"
        color_blind_mode_state.set(settings_data['color_blind_mode'])
        color_blind_mode_checkbox = Checkbutton(
                                        main_menu_frame, 
                                        text='Mode daltonien', 
                                        onvalue=True, 
                                        offvalue=False, 
                                        variable=color_blind_mode_state, 
                                        command=self.update_settings, 
                                        **large_label_style,
                                        bd=0,
                                        highlightthickness=0,
                                        activebackground=background_color,
                                        activeforeground=on_background_color,
                                        relief='flat',
                                        selectcolor=background_color) # On crée une case à cocher
        color_blind_mode_checkbox.grid(column=0, row=6, sticky='w')

        use_space_to_mirror_state = BooleanVar() # Création de l'option "Utiliser la touche espace pour miroiter"
        use_space_to_mirror_state.set(settings_data['use_space_to_mirror'])
        use_space_to_mirror_checkbox = Checkbutton(
                                        main_menu_frame, 
                                        text='Utiliser la touche espace pour miroiter', 
                                        onvalue=True, 
                                        offvalue=False, 
                                        variable=use_space_to_mirror_state, 
                                        command=self.update_settings, 
                                        **large_label_style,
                                        bd=0,
                                        highlightthickness=0,
                                        activebackground=background_color,
                                        activeforeground=on_background_color,
                                        relief='flat',
                                        selectcolor=background_color) # On crée une case à cocher
        use_space_to_mirror_checkbox.grid(column=0, row=7, sticky='w')

        Label(main_menu_frame, text=' ', background=background_color).grid(column=0, row=8) # On crée un espace entre les différentes sections

        game_settings_section_label = Label(main_menu_frame, text='COMPORTEMENT DU JEU', **small_label_style) # Titre de la section des paramètres d'accessibilité
        game_settings_section_label.grid(column=0, row=9, sticky='w')

        use_middle_starting_cases_state = BooleanVar() # Création de l'option "Mettre les cases de départ au centre"
        use_middle_starting_cases_state.set(settings_data['use_middle_starting_cases'])
        use_middle_starting_cases_checkbox = Checkbutton(
                                        main_menu_frame, 
                                        text='Mettre les cases de départ au centre', 
                                        onvalue=True, 
                                        offvalue=False, 
                                        variable=use_middle_starting_cases_state, 
                                        command=self.update_settings, 
                                        **large_label_style,
                                        bd=0,
                                        highlightthickness=0,
                                        activebackground=background_color,
                                        activeforeground=on_background_color,
                                        relief='flat',
                                        selectcolor=background_color) # On crée une case à cocher
        use_middle_starting_cases_checkbox.grid(column=0, row=10, sticky='w')

        settings_file.close() # On ferme le fichier de paramètres pour éviter les problèmes
    
    def update_settings(self):
        with open("settings.json", "r") as settings_file: # On ouvre le fichier paramètres
            settings_data = json.load(settings_file) # On récupère les données du fichier

        # Le fichier paramètres est mis à jour en fonction des choix de l'utilisateur
        settings_data['color_blind_mode'] = color_blind_mode_state.get()
        settings_data['use_light_theme'] = use_light_theme_state.get()
        settings_data['use_red_and_blue'] = not alternative_color_scheme_state.get()
        settings_data['use_purple_and_yellow'] = alternative_color_scheme_state.get()
        settings_data['use_space_to_mirror'] = use_space_to_mirror_state.get()
        settings_data['use_middle_starting_cases'] = use_middle_starting_cases_state.get() 

        with open("settings.json", "w") as settings_file:
            json.dump(settings_data, settings_file, indent=4) # On écrit les modifications dans le fichier
        
        settings_file.close() # On ferme le fichier de paramètres pour éviter les problèmes


if __name__ == "__main__":
    root = Tk() # On crée la fenêtre principale du jeu
    root.configure(bg=background_color) # On change la couleur de fond de la fenêtre
    icon = PhotoImage(file='res/img/blocus_icon.png') # On récupère l'image "blocus_icon.png"
    root.iconphoto(True, icon) # On ajoute une icône à la fenêtre
    Blocus(root) # On appelle la classe Blocus
    root.mainloop()
