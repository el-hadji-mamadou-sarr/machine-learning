Quelle est la différence fondamentale entre la programmation traditionnelle et le Machine Learning ? Explique avec tes propres mots.
- Dans la programmation traditionnelle, la régle est codée à l'avance.
Alors que le machine learning permet de deviner la régle par apprentissage.

Pour chacun de ces problèmes, identifie quelle famille de ML tu utiliserais et pourquoi :

Détecter si un email est un spam
- apprentissage suppervisée

Regrouper des articles de presse par thème sans les avoir lus
- apprentissage non suppervisés

Entraîner un robot à marcher
- renforcement

Pourquoi est-il important de séparer les données en "entraînement" et "évaluation" ? Qu'est-ce qui risque de se passer si tu évalues sur les mêmes données qu'utilisées pour entraîner ?
- il faut séparer les 2 données, puisque pour évaluer le modéle, il faudrait donner au modéle des données qu'il n'a jamais vu. 
Tu rique de ne pas avoir une bonne évaluation du modéle puiqu'il a déja appris de ces données.


Imagine que tu veuilles construire un modèle qui prédit si un patient a une maladie. Quelles étapes du pipeline te sembleraient les plus critiques ? Pourquoi ?
- La collection et la préparation des données est la plus critique. Il faudrait les infromations exacts sur le patient parceque une mauvaise extraction des symptomes du patients pourrait entrainer un mauvais entrainement du modéle.

Dans ta vie ou ton domaine, cite un problème concret que tu aimerais résoudre avec le ML. Quelle famille utiliserais-tu ?
- prédiction du nombre de place libre dans le train. apprentissage suppervisés pusique les données ont des étiquettes (station, direction, instant)