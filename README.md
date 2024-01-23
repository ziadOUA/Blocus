<img src="https://i.postimg.cc/1t942d38/BLOCUS.png">

<h1 align="center">Blocus</h1>

<div align="center">
  <p>Projet de NSI Supervisé : Jeu de plateau à deux joueurs</p>
  <img src="https://m3-markdown-badges.vercel.app/stars/9/2/ziadoua/blocus">
  <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Python/python2.svg">
  <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/JSON/json2.svg">
  <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Figma/figma2.svg">
  <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Markdown/markdown2.svg">
</div>

<br>

# Cahier des charges

Le but du projet était de créer une version à deux joueurs du jeu "Blokus". Il s'agira donc d'une réplique du jeu "Blokus DUO".<br>
Les technologies utilisées seront le langage Python (v3) ainsi que le module Tkinter, qui servira à réaliser l'interface utilisateur.

<div align="center">
  <img src="https://i.postimg.cc/MTZGVgn0/91-Rt6r-Dwah-L-AC-SL1500.png" height="250px">
  <p><i>Boîte du jeu Blokus DUO</i></p>
</div>

Le projet se nommera "Blocus".

## 1. Recherches initiales

Sources :<br>
[Règles officielles de Blokus DUO](https://www.jeuxavolonte.asso.fr/regles/blokus_duo.pdf)

### 1.1. Matériel du jeu

Nous allons énoncer le matériel de la version Blokus DUO<br>
Le jeu se compose des éléments suivants :
- Un plateau de 14x14 cases
- 42 pièces (21 pièces pour chaque joueur)
- 2 range-pièces

<div align="center">
  <img src="https://i.postimg.cc/50rvN8gM/pieces-player-one.png" height="250">
  <p><i>Pièces du Joueur 1</i></p>
</div>

### 1.2. But du jeu

L'objectif pour chaque joueur est de poser un maximum de carrés (constituant les pièces posées) sur le plateau.

### 1.3. Déroulement d'une partie

La partie débute sur les joueurs qui placent une pièce de leur choix sur leur case de départ.

<div align="center">
  <img src="https://i.postimg.cc/nVy24QbL/starting-position.png" height="100">
  <p><i>Case de départ du Joueur 1</i></p>
</div>

Les pièces placées ensuite doivent toucher une pièce de même couleur par un ou plusieurs coins, et jamais par les côtés. Des pièces de couleurs différentes peuvent néanmoins se toucher par les côtés.<br>
Les pièces peuvent être tournées ou miroitées, et leur placement ne peut pas être modifié jusqu'à la fin de la partie.

### 1.4. Fin de partie

Lorsqu'un joueur est bloqué (lorsqu'il ne peut plus placer de pièces) il doit laisser l'autre jouer jusqu'à ce qu'il soit bloqué à son tour.<br>
Le score est ensuite calculé :
- +1 point pour chaque carré posé
- -1 points pour chaque carré non posé
- +15 points si les 21 pièces ont été posées
- +20 points si les 21 pièces ont été posées avec le carré solitaire en dernière position

<div align="center">
  <img src="https://i.postimg.cc/tg6FD90H/finished-game.png" height="250">
  <p><i>Partie terminée</i></p>
</div>

## 2. Structures de données

### 2.1. Plateau

Pour caractériser le plateau, on utilisera une liste de listes :
```
  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
```
Cette liste servira de base au programme, qui sera la base de l'interface graphique.<br>
→ **Il faudra placer les pièces, en faisant attention au fait que plus on descend dans le plateau plus la valeur de y augmente**, ce qui veut dire que l'index de la case du coin supérieur gauche est de [0, 0].

### 2.2. Range-pièces

Pour caractériser les range-pièces, on utilisera une liste de listes :
```
  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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
```
→ Les pièces sont caractérisées par un ensemble de "O". **On utilisera une fonction qui permettra de "récupérer" ls coordonnées de tous les "O"**.

### 2.3. Scores

Nous utiliserons des variables pour tracker le score des deux joueurs.<br>
```python
  player_1_score = 0
  player_2_score = 0
```

### 2.4. Pièces

Les pièces seront placées dans la liste en fonction de leur état :
- Si le placement est invalide, la pièce sera affichée en utilisant des "H"
  - Exemple :
  ```
      ' ', 'H', 'H'
      ' ', 'H', ' '
      'H', 'H', ' '
  ```
- Si le placement est valide, la pièce sera affichée en utilisant, soit "RH" pour le joueur 1, soit "BH" pour le joueur 2
  - Exemple :
  ```
      ' ', 'RH', 'RH'   ' ', 'BH', 'BH'
      ' ', 'RH', ' '    ' ', 'BH', ' '
      'RH','RH', ' '    'BH','BH', ' '
  ```
- Si la pièce est placée, elle sera affichée en utilisant, soit "R" pour le joueur 1, soit "B" pour le joueur 2
  - Exemple :
  ```
      ' ', 'R', 'R'   ' ', 'B', 'B'
      ' ', 'R', ' '   ' ', 'B', ' '
      'R', 'R', ' '   'B' ,'B', ' '
  ```

## 3. Interface graphique

### 3.1. Menu principal

<!-- <img src="https://i.postimg.cc/L50T2qXk/main-menu.png"> -->

Boutons de gauche à droite :
- Bouton GitHub (la page GitHub du projet dans le navigateur par défaut)
- Bouton paramètres
- Bouton "À Propos" du projet

### 3.2. Interface de jeu

<img src="https://i.postimg.cc/Qt5kDbM0/game-interface.png">

Divers boutons :
- Bouton indice
- Bouton retour

→ Le range-pièces du joueur actif a une bordure colorée.

### 3.3. Paramètres