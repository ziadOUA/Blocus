<img src="https://i.postimg.cc/1t942d38/BLOCUS.png">

<h1 align="center">Blocus</h1>

<div align="center">
  <p>Projet d'NSI Supervisé : Jeu de plateau à deux joueurs</p>
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
