#  Appunti corso django

### GIT 
**git init** ; inizializzare git

**git add  file** : aggiungere un file

**git commit -m " commento "** : confermare le modifiche

**git push -u origin master**  : caricare modifiche su github

**git remote add origin https://github.com/stefanin/django.git** : clona il repository in locale

### python

python -m venv v_env : crea un ambiente virtuale 

v_env\Scripts\activate : attiva l'ambiente virtuale

# DJANGO

**pip install django** : installa Django

**django-admin startproject nome-progetto** : crea un progetto Django, in una directory contenente l'ambiente di sviluppo. Il file manage.py è affidata la gestione del progetto

Struttora dei progetti Django

__init__.py :  informa python che la dir è un pakage

admin.py    :  resgistrazine modelli e interfaccia di configurazione

admin.py    :  configurazione specifiche dell'prima_app

models.py   : classi dei modelli 

tests.py    :  funzioni di test dell'app

views.py    :  viste dell'app

migrations  :  cartella con funzioni per la migrazione


**python manage.py runserver** : avvia il server di test

**python manage.py startapp nome-apppicazione** : crea la struttura dell'app, dopo la creazione è nexessario dicharare l'app nel file progetto\settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news'  <------------- nuova app
]


.. Gestire i modelli :
le tabelle e colonne vanno dichiarati nel file models.py

news\models.py

python manage.py makemigration : prepara la migrazione delle tebelle

python manage.py makemigrations
Migrations for 'news':
  news\migrations\0001_initial.py
    - Create model Articolo
    - Create model Giornalista
    - Add field giornalista to articolo

python manage.py sqlmigrate news 0001 : effetua i comandi sql preparati dalla funzione makemigration

python manage.py migrate : effettua la migrazione

nella directori del progetto, viene creato il file db.sqlite3    


.. Database API

Sono le API di interfaccia con il database, con una shell è possibile importare le classi models per interafire con il db

python manage.py shell : apre una shell python

--------------CRUD -----------------------------

from news.models import Giornalista  : importa la classe Giornalista

Giornalista.objects.all() : elenca la tabella
g1 = Giornalista(nome="Mario", cognome="Rossi") : aggiunge un giornalista
g1.save()                                       : salva l'inserimento

g2.nome="Pinco"   :  inserisce un campo alla volta
g2.cognome= "Pallo"
g2.save()

Giornalista.objects.create(nome="Nome",cognome="Cognome") : inserisce e salva

Giornalista.objects.get(pk=1)  : seleziona la riga usando l'id o pk

Giornalista.objects.filter(nome="Mario") : filtra per campo

Giornalista.objects.exclude(cognome="Rossi") : elenco con esclusione


for g in Giornalista.objects.all():  # elenco con ciclo for
     g.nome

gio = Giornalista.objects.get(pk=2) #  modifica il vaolre diun record
gio.nome="Guido"
gio.cognome="Guidi"
gio.save()

gio = Giornalista.objects.get(pk=1) # cancella un record
gio.delete()

from news.models import Articolo
a1 = Articolo()
a1.titolo="primo titolo"
a1.contenuto="djkjsdfksaklsjfsakfdjaskjfksdfalsfkjsaja"
g = Giornalista.objects.get(id=3) # è necessario associare un oggetto Giornalista
a1.giornalista=g
a1.save()


a1.giornalista_id : relazione inversa restituisce l'id della tabella relazionata

nuovo = Articolo(titolo="secondo Articolo", contenuto=" dadaaajsakd", giornalista=Giornalista.objects.get(id=3))
nuovo.save() # inserisce un nuovo record con l'oggetto giornalista
nuovo
<Articolo: secondo Articolo>

# elenca tutti gli articoli del giornalista 
x = Giornalista.objects.get(id=3)
x.articolo.all()
<QuerySet [<Articolo: primo titolo>, <Articolo: secondo Articolo>]>
 
