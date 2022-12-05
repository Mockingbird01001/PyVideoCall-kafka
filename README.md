# PyVideoCall-kafka
Simple outils de visio conferance (video + audio) avec pyKafka entre deux utilisateurs, sera mis ajout pour accueillir un grand nombre d'utilisateurs.
la librairie utilisé pour le traitement de l'audio est "pyAudio" elle n'est plus maintenue, c'est ce qui nous a poussé a créer un env sous python3.8.
creation de deux topic pour l'image et le audio comme le montre le schema suivant:

---
!!! Note Importante: 
Dans cette version les deux utilisateurs connaissent leurs IP ce qui rends les choses plus simple.
---


### lancer l'environement sous linux:
```
source lastHope/bin/activate
```

#version Basic:
### l'utilisateur_1 lance son producer via la commande:*
```
cd user_1/sender/
python producter.py
 
```
### Executer le consumer pour avoir un rendu graphique
```
cd user_1/reciever/
python flaskServer.py
```

idem pour le user_2
### l'utilisateur lance son producer via la commande:*
```
cd user_2/sender/
python producter.py
 
```
### Executer le consumer pour avoir un rendu graphique
```
cd user_2/reciever/
python flaskServer.py
```
