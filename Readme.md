Installation de Bootstrap :
pip install django-bootstrap-v5

# exemple d'utilisation de bootstrap :
# Rappeler la librairie Bootstrap si appel dans Template hérité 
"""
Add to INSTALLED_APPS in your settings.py: 'bootstrap5',

{# Load the tag library #}
{% load bootstrap5 %}

{# Load CSS and JavaScript #}
{% bootstrap_css %}
{% bootstrap_javascript %}

{# Display django.contrib.messages as Bootstrap alerts #}
{% bootstrap_messages %}

{# Display a form #}
<form action="/url/to/submit/" method="post" class="form">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons %}
    <button type="submit" class="btn btn-primary">
      Submit
    </button>
  {% endbuttons %}
</form>
"""

Installation de Django :
Créer un répertoire de Projet
créer un environnement virtuel dans ce répertoire Projet (py -m venv django-env)
créer le projet Django dans ce répertoire Projet (pip install Django)

Lancer le serveur
py manage.py runserver

lancer le shell
py manage.py shell

Faire les migrations
py manage.py makemigrations (prépare la migration et les changements)
py manage.py migrate (génère la migration dans la Bdd)

Voir les librairies installées pour le projet
pip freeze (> requirements.txt)

# mail SMTP
# installation de aiostpd :
dans environnement virtuel : pip install aiosmtpd
# lancement du service de SMTP privé pour affichage dans terminal
py -m aiosmtpd -n -l localhost:8025

# conf dans Settings.py du projet :
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 8025

# url inversées :
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
'news-year-archive' = name dans fichiers url
yearvar = paramètres s'il y en a

# a faire : 
    # si Get request : Afficher form vide : OK
    # Si Post request : récupérer les données : OK
    # valider les données : tester avec nom de plus de 3 lettres : OK

    Envoyer un mail

    Gérer les exceptions

    Faire des tests :
    - tester validation error si nom gcl < 2 caractères

  -cabinetV2 form à remplacer (par CabinetForm) : laisser tel quel
  -mettre index.html dans répertoire Home : OK

 # Pour afficher le mail :
 passer le dict du formulaire d'achat
 et mettre en forme dans le TextArea : OK

- Rajouter un champ commentaire dans la table Achat
- Ajouter le bouton Javascript pour 1 config utilisateur

# utiliser Collapse avec Bootstrap plutôt que Jquery pour afficher les commentaires