# Food_Crops

**Rapport du projet Food Crops**


Eleves:
- Maxim Mangematin--Mathey
- Pablo Berton

**

Ce projet a été développé à l'aide de l'environnement PyCharm sur des 
ordinateurs sous windows 11 et utilisant Python 3.8.

**

Le programme se lance en éxécutant le fichier Main.py qui permet 
l'instanciation du programme ainsi que le chargement de la base de
données, menant vers la demande d'information permettant de faire les
recherches dans la base de données directement depuis la console.

**

Le projet a été divisé en deux étapes et pour chacune d'elles, les tâches 
ont été répartis entre les membres du groupe. La création de l'interface 
Describable qui est utilisé par la quasi totalité des autres classes a 
été la première étapes du programme, suivi de la classe abstraite Unit. 
Ensuite, les différentes unités on été programmé, ainsi que les classes 
Indicator et Commodity, accompagnées de leurs enum. Cette première étape 
c'est achevé avec la création de la classe Measurement ainsi que celle des 
classes FoodCropFactory et FoodCropDataset pour lesquels seuls les constructeurs 
on été implémenté. Maxim c'est majoritairement occupé de la création des enum 
ainsi que de l'initialisation des classes FoodCropFactory et FoodCropDataset 
et de leurs dictionnaires en s'informant sur le fonctionnement de ces nouveaux 
objets et Pablo c 'est occupé de la création des différentes classes et de leurs 
constructeurs.

La deuxième étape consiste en la création des méthodes spécifiques aux classes
FoodCropFactory et FoodCropDataset ainsi qu'à la programmation du fichier
Main.py qui permet d'éxécuter le programme. Après un travail commun afin de
prendre en main la bibliothèque Pandas pour le chargement du jeux de données
et finaliser la méthode load() de FoodCropDataset, Maxim c'est dirigé vers la 
programmation de la méthode findMeasurement(), qui est le coeur du programme.
Pablo c'est occupé du fichier Main.py afin de rendre le programme utilisable
sans copier/coller d'instructions. 

Le projet c'est ensuite achevé avec la programmation des différentes méthodes
de description des objets, une phase de test et de débogage qui nous a proposé
différentes erreurs que nous avons pu résoudre.

**

Dans l'ensemble, le projet c'est bien déroulé mais certains problèmes ont
tout de même été rencontrés.

Tout d'abord, à cause de problèmes extérieurs, nous n'avons pas pu travailler
ensemble lors de la totalité des séances. Cependant, ce problème a été résolu
très simplement avec l'utilisation de ce git qui a permis de partagé l'avancé du
travail.

Une autre difficulté a été de prendre du recul sur le sujet en se permettant de 
modifier le type de certains attributs par rapport à son type initial lorsque ce 
dernier ne correspondait pas au besoin du programme, lorsqu'il n'était pas 
spécifié ou encore qu'il paraissait erroné.

Enfin, des problèmes techniques ont aussi été rencontrés, que ce soit à cause
de l'utilisation d'un nouvel objet ou d'une nouvelle bibliothèque, ou pendant
la phase de test. Ces premiers problèmes ont été résolus par des recherches sur
le fonctionnement de ces objets alors que la phase de test a été plus ardu.
Entre autre, nous avons rencontré un conflit entre metaclass que nous avons pu 
résoudre avec une aide extérieure, mais qui nous a fait découvrir ce concept
propre à python. La dernière difficulté rencontrée a été la syntaxe vis-à-vis
de l'importation des classes présentes sur un autre fichier python mais qui a 
encore été résolu grace des recherches de documentation.
