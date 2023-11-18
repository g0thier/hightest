# Automatisation Quiz ISTQB

## Instruction Zoé

> Bonjour Gauthier,  Super ! L'exercice d'automatisation consiste à développer un projet de test permettant de vérifier qu'un de nos quiz ISTQB correctement rempli donne lieu à un mail indiquant 100 % de réponses.  -Tutoriel conseillé : https://testautomationu.applitools.com/selenium-webdriver-tutorial-java/ -Outil utilisé : Selenium Java -Navigateur cible : Google Chrome -Scénario à suivre par l'automate : se rendre sur https://hightest.nc/, cliquer sur "Toolbox" puis sur le lien vers le quiz ISTQB Fondation en français. Réaliser le test en cliquant sur les bonnes réponses, valider le test. Sur la page d'après, entrer une adresse e-mail Yopmail et valider le formulaire. Se rendre ensuite sur Yopmail, consulter les mails et vérifier que le mail reçu indique bien 100 % de bonnes réponses. -Design pattern conseillé : Page Object Model -Outil de partage du code source : Github ou Bitbucket à votre convenance  Notre attention se portera en particulier sur la clarté du code, sa concision et sa maintenabilité.  Bonne journée,  Zoé

## To Do List 

Notes : 
 * Garder temps d'execution 
 * Continuer grace aux adresses urls si bug pendant le processus 
 * Faire une écriture etape par etape des réussites 

### Création mail Yopmail

~~**https://yopmail.com/fr/**~~
 * ~~https://yopmail.com/fr/~~
 * ~~Clic Générer une adresse au hasard~~
 * ~~Garder l'adresse dans la barre du lien~~

### Processus sur Hightest

**https://hightest.nc/**
 * https://hightest.nc/ ( check temps connexion procedure Curl peut-etre )
 * Clic Toolbox 

**changement de page pour /toolbox/**
 * Clic Quiz ISTQB niveau Foundation (version 2018) -> Français 

**Changement de page pour /ressources/test-istqb.php**
 * Attente Curl ou boucle ?? instruction avant test
 * Clic sur les Coches ( Check si les questions sont dans le même ordre et si les réponses sont dans le même ordre)
    * Creer un dictionnaire clefs reponses
    * Clic Terminé !
    
**Changement de page pour /ressources/reponses-test-istqb.php**
 * Entrer le mail et Clic envoyer

### Récupération des résultats mail Yopmail

**https://yopmail.com/fr/**
 * https://yopmail.com/fr/
 * Entrer l'adresse généré précédemment
 * Clic sur la flèche 

**https://yopmail.com/fr/wm**
 * Selection du message dans le corp du mail

### Sortie du rapport
 * Sortie du Rapport (format Json peu-etre)
