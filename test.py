import tkinter as tk 
#ttkbootstrap
import ttkbootstrap as ttkbs 
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.scrolled import ScrolledText
import ttkbootstrap.dialogs.dialogs as dialog 
import PIL as pil #pillow
from tkinter import filedialog #file dialog
import infinity_module #mon module
import os 
import sys 
import json #ouverture fichier .json
from googletrans import LANGUAGES #les langues possibles
import webbrowser


class App():
    def close(self):
        self.fenetre.destroy()
        sys.exit()

    def save_img(self):
        self.resize_img()
        # Redimensionner l'image tout en conservant le rapport d'aspect
        self.new_imagedos = self.pil_filename.resize((self.largeur, self.hauteur))
        
        self.new_imagedos.save(self.filename)

    def resize_img(self):
        print("resize img")
        print(self)
        if self.pil_filename != None:
            self.entry_hauteur = infinity_module.imgresizer.resize(self=self.img, filename=self.filename, hauteur=self.hauteur, largeur=self.largeur, entry_h=self.val_entry_h, entry_l=self.val_entry_l, type_val="entry_h")
            self.entry_largeur = infinity_module.imgresizer.resize(self=self.img, filename=self.filename, hauteur=self.hauteur, largeur=self.largeur, entry_h=self.val_entry_h, entry_l=self.val_entry_l, type_val="entry_l")
            self.hauteur = infinity_module.imgresizer.resize(self=self.img, filename=self.filename, hauteur=self.hauteur, largeur=self.largeur, entry_h=self.val_entry_h, entry_l=self.val_entry_l, type_val="hauteur")
            self.largeur = infinity_module.imgresizer.resize(self=self.img, filename=self.filename, hauteur=self.hauteur, largeur=self.largeur, entry_h=self.val_entry_h, entry_l=self.val_entry_l, type_val="largeur")

    def ouvrir_img(self):
        self.filename = filedialog.askopenfilename(title="Ouvrir l'image :",filetypes=(("Fichier image","*.png; *.jpeg; *.jpg"),("PNG","*.png"),("JPEG","*.jpeg;*.jpg"),("tout les fichiers","*.*")))
        print(f"/{self.filename}/")
        if self.filename: 
            self.nom_win = str(self.debut_nom_win) + " - Image : " + str(self.filename)
            self.fenetre.title(str(self.nom_win))
            self.pil_filename = infinity_module.imgresizer.openning(self.img, self.filename)

            self.hauteur = self.pil_filename.size[0]
            self.largeur = self.pil_filename.size[1]

            print(self.hauteur)
            print(self.largeur)
            print(self.img)
            self.resize_img()

    def win_img_resizer(self):
        self.debut_nom_win = "Infinity Pack - Img Resizer"
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        self.img = infinity_module.imgresizer()
        self.pil_filename = None

        self.bouton_open = ttkbs.Button(self.frame_win, text="Ouvrir l'image :", command=lambda:self.ouvrir_img())
        self.bouton_open.grid(row=0, column=0, padx=(5, 5), pady=(5, 2), columnspan=2, sticky=ttkbs.EW)

        self.frame_entry = ttkbs.LabelFrame(self.frame_win, text=" Les mesures de l'image : ")
        self.frame_entry.grid(row=1, column=0, padx=(5, 2), pady=(3, 2), sticky=ttkbs.EW)

        self.text_h = ttkbs.Label(self.frame_entry, text="Hauteur : (en pixel)")
        self.text_h.grid(row=0, column=0, padx=(5, 5), pady=(5, 2), sticky=ttkbs.EW)

        self.val_entry_h = ttkbs.StringVar()
        self.entry_hauteur = ttkbs.Entry(self.frame_entry, textvariable=self.val_entry_h)
        self.entry_hauteur.grid(row=0, column=1, padx=(5, 5), pady=(5, 2), sticky=ttkbs.EW)
        
        self.text_l = ttkbs.Label(self.frame_entry, text="Largeur : (en pixel)")
        self.text_l.grid(row=1, column=0, padx=(5, 5), pady=(5, 2), sticky=ttkbs.EW)

        self.val_entry_l = ttkbs.StringVar()
        self.entry_largeur = ttkbs.Entry(self.frame_entry, textvariable=self.val_entry_l)
        self.entry_largeur.grid(row=1, column=1, padx=(5, 5), pady=(3, 5), sticky=ttkbs.EW)

        self.bouton_resize = ttkbs.Button(self.frame_win, text="Synchroniser les valeurs :", command=lambda:self.resize_img())
        self.bouton_resize.grid(row=1, column=1, padx=(5, 5), pady=(5, 2), sticky=ttkbs.NSEW)

        self.bouton_save = ttkbs.Button(self.frame_win, text="Enregistrer l'image :", command=lambda:self.save_img())
        self.bouton_save.grid(row=2, column=0, padx=(5, 5), pady=(3, 5), columnspan=2, sticky=ttkbs.EW)

        ToolTip(self.bouton_save, text="Il faut ouvrir une IMAGE avant d'appuyer sur ce bouton.", bootstyle=(DANGER, INVERSE))

        self.fenetre.update()

    def save_tag(self):
        infinity_module.edit_tag.save(self=self.audio_self, audiofile=self.audio_filename, titre=self.entry_titre, album=self.entry_album, annee=self.entry_annee, artiste=self.entry_artist)

    def info_audio(self):
        self.tag_audio = infinity_module.edit_tag.tag_file(self=self.audio_self, audio_file=self.audio_filename)
        self.tag_audio_sha = infinity_module.edit_tag.tag_shazam(self=self.audio_self, chanson=self.shazam_file)

        print(self.tag_audio_sha)
        
        print(self.tag_audio['titre'][0])

        self.entry_titre.configure(state="normal")
        self.entry_artist.configure(state="normal")
        self.entry_album.configure(state="normal")
        self.entry_annee.configure(state="normal")
        self.entry_num_track.configure(state="normal")

        self.entry_titre.delete(0, ttkbs.END)
        self.entry_artist.delete(0, ttkbs.END)
        self.entry_album.delete(0, ttkbs.END)
        self.entry_annee.delete(0, ttkbs.END)
        self.entry_num_track.delete(0, ttkbs.END)


        self.entry_titre.insert(0, string=str(self.tag_audio["titre"][0]))
        self.entry_artist.insert(0, string=str(self.tag_audio["artiste"][0]))
        self.entry_album.insert(0, string=str(self.tag_audio["album"][0]))
        self.entry_annee.insert(0, string=str(self.tag_audio["annee"][0]))
        self.entry_num_track.insert(0, string=str(self.tag_audio["num album"][0]))


        self.entry_titre_sha.configure(state="normal")
        self.entry_artist_sha.configure(state="normal")
        self.entry_album_sha.configure(state="normal")
        self.entry_annee_sha.configure(state="normal")
        self.entry_num_track_sha.configure(state="normal")

        self.entry_titre_sha.delete(0, ttkbs.END)
        self.entry_artist_sha.delete(0, ttkbs.END)
        self.entry_album_sha.delete(0, ttkbs.END)
        self.entry_annee_sha.delete(0, ttkbs.END)
        self.entry_num_track_sha.delete(0, ttkbs.END)


        self.entry_titre_sha.insert(0, string=str(self.tag_audio_sha["titre"]))
        self.entry_artist_sha.insert(0, string=str(self.tag_audio_sha["artiste"]))
        self.entry_album_sha.insert(0, string=str(self.tag_audio_sha["album"]))
        self.entry_annee_sha.insert(0, string=str(self.tag_audio_sha["annee"]))
        self.entry_num_track_sha.insert(0, string=str(self.tag_audio_sha["num album"]))

    def ouvrir_audio(self):
        self.filename = filedialog.askopenfilename(title="Ouvrir l'audio :",filetypes=(("fichier audio","*mp3; *.flac; *.wav"),("mp3","*.mp3"),("flac","*.flac"),("wav","*.wav"),("all files","*.*")))
        print(f"/{self.filename}/")

        if self.filename: 
            self.nom_win = str(self.debut_nom_win) + " - Audio : " + str(self.filename)
            self.fenetre.title(str(self.nom_win))
            self.audio_self = infinity_module.edit_tag
            self.audio_filename = infinity_module.edit_tag.open(self.img, self.filename)
            self.shazam_file = infinity_module.edit_tag.open_shazam(self.img, self.filename)
            self.info_audio()

    def win_edit_tag(self):
        self.debut_nom_win = "Infinity Pack - Éditeur de tag "
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        self.img = infinity_module.edit_tag()
        self.audio_filename = None
        self.shazam_file = None

        self.bouton_ouvrir_audio = ttkbs.Button(self.frame_win, text="Ouvrir l'audio :", command=lambda:self.ouvrir_audio())
        self.bouton_ouvrir_audio.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), columnspan=2, sticky=ttkbs.EW)

        #fichier
        self.frame_audio = ttkbs.Labelframe(self.frame_win, text="Tag du fichier : ")
        self.frame_audio.grid(row=1, column=0, padx=(5, 5), pady=(2, 3), sticky=ttkbs.NSEW)

        self.label_titre = ttkbs.Label(self.frame_audio, text="Titre : ")
        self.label_titre.grid(row=0, column=0, padx=(5, 5), pady=(5, 3), sticky=ttkbs.E)

        self.entry_titre = ttkbs.Entry(self.frame_audio, state="disabled")
        self.entry_titre.grid(row=0, column=1, padx=(5, 5), pady=(5, 3), sticky=ttkbs.EW)

        self.label_artist = ttkbs.Label(self.frame_audio, text="Artiste : ")
        self.label_artist.grid(row=1, column=0, padx=(5, 5), pady=(2, 3), sticky=ttkbs.E)

        self.entry_artist = ttkbs.Entry(self.frame_audio, state="disabled")
        self.entry_artist.grid(row=1, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_album = ttkbs.Label(self.frame_audio, text="Album : ")
        self.label_album.grid(row=2, column=0, padx=(5, 5), pady=(2, 3), sticky=ttkbs.E)

        self.entry_album = ttkbs.Entry(self.frame_audio, state="disabled")
        self.entry_album.grid(row=2, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_annee = ttkbs.Label(self.frame_audio, text="Année : ")
        self.label_annee.grid(row=3, column=0, padx=(5, 5), pady=(2, 3), sticky=ttkbs.E)

        self.entry_annee = ttkbs.Entry(self.frame_audio, state="disabled")
        self.entry_annee.grid(row=3, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_num_track = ttkbs.Label(self.frame_audio, text="N° album : ")
        self.label_num_track.grid(row=4, column=0, padx=(5, 5), pady=(2, 5), sticky=ttkbs.E)

        self.entry_num_track = ttkbs.Entry(self.frame_audio, state="disabled")
        self.entry_num_track.grid(row=4, column=1, padx=(5, 5), pady=(2, 5), sticky=ttkbs.EW)


        #shazam
        self.frame_shazam = ttkbs.Labelframe(self.frame_win, text="Tag du shazam : ")
        self.frame_shazam.grid(row=1, column=1, padx=(5, 3), pady=(2, 3), sticky=ttkbs.NSEW)

        ToolTip(widget=self.frame_shazam, text="""Attention : si Shazam est bloqué ou que vous êtes hors-ligne alors ces cases resteront vide MAIS vous pouvez quand même éditer les tags.""")

        self.label_titre_sha = ttkbs.Label(self.frame_shazam, text="Titre : ")
        self.label_titre_sha.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.E)
        self.entry_titre_sha = ttkbs.Entry(self.frame_shazam, state="disabled")
        self.entry_titre_sha.grid(row=0, column=1, padx=(5, 5), pady=(5, 3), sticky=ttkbs.EW)

        self.label_artist_sha = ttkbs.Label(self.frame_shazam, text="Artiste : ")
        self.label_artist_sha.grid(row=1, column=0, padx=(5, 3), pady=(2, 3), sticky=ttkbs.E)
        self.entry_artist_sha = ttkbs.Entry(self.frame_shazam, state="disabled")
        self.entry_artist_sha.grid(row=1, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_album_sha = ttkbs.Label(self.frame_shazam, text="Album : ")
        self.label_album_sha.grid(row=2, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.E)
        self.entry_album_sha = ttkbs.Entry(self.frame_shazam, state="disabled")
        self.entry_album_sha.grid(row=2, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_annee_sha = ttkbs.Label(self.frame_shazam, text="Année : ")
        self.label_annee_sha.grid(row=3, column=0, padx=(5, 3), pady=(2, 3), sticky=ttkbs.E)
        self.entry_annee_sha = ttkbs.Entry(self.frame_shazam, state="disabled")
        self.entry_annee_sha.grid(row=3, column=1, padx=(5, 5), pady=(2, 3), sticky=ttkbs.EW)

        self.label_num_track_sha = ttkbs.Label(self.frame_shazam, text="N° album : ")
        self.label_num_track_sha.grid(row=4, column=0, padx=(5, 3), pady=(2, 3), sticky=ttkbs.E)
        self.entry_num_track_sha = ttkbs.Entry(self.frame_shazam, state="disabled")
        self.entry_num_track_sha.grid(row=4, column=1, padx=(5, 5), pady=(2, 5), sticky=ttkbs.EW)

        self.bouton_save_audio = ttkbs.Button(self.frame_win, text="Enregistrer les tags : ", command=lambda:self.save_tag())
        self.bouton_save_audio.grid(row=2, column=0, padx=(5, 5), pady=(2, 5), columnspan=2, sticky=ttkbs.EW)
        
        ToolTip(self.bouton_save_audio, text="Il faut ouvrir une MUSIQUE avant d'appuyer sur ce bouton.", bootstyle=(DANGER, INVERSE))

        self.fenetre.update()

    def trad(self):
        edit = infinity_module.traduction()

        self.traduit = infinity_module.traduction.trad_auto(self=edit, texte=self.entry_text.get("0.0", "end"), langue_f=self.select_langue.get())

        #print(self.traduit)
        self.label_text_trad.delete("0.0", "end")
        self.label_text_trad.insert("0.0", self.traduit)

    def win_trad(self):
        self.debut_nom_win = "Infinity Pack - Traduction "
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        self.entry_text = ScrolledText(self.frame_win, height=15, hbar=True, vbar=True, autohide=True, width=50)
        self.entry_text.grid(row=0, column=0, padx=(5, 3), pady=(5, 5), rowspan=3, sticky=NS)

        self.select_langue = ttkbs.Combobox(self.frame_win, state="readonly", values=list(LANGUAGES.values()))
        self.select_langue.grid(row=0, column=1, padx=(2, 3), pady=(5, 3))
        self.select_langue.current(list(LANGUAGES.values()).index(self.set_app_dic["langue"]))

        self.btn_trad = ttkbs.Button(self.frame_win, text="Traduire :", command=lambda:self.trad())
        self.btn_trad.grid(row=1, column=1, padx=(2, 3), pady=(2, 5), sticky=EW)

        self.label_text_trad = ScrolledText(self.frame_win, height=15, hbar=True, vbar=True, autohide=True, width=50)
        self.label_text_trad.grid(row=0, column=2, padx=(2, 5), pady=(5, 5), rowspan=3, sticky=NS)

        ToolTip(self.btn_trad, text="""La traduction ne fonctionne pas toujours correctement ....""")

    def update_setting(self):
        self.set_app_dic["theme"] = self.list_theme.get()
        self.set_app_dic["langue"] = self.list_langue.get()
        self.set_app_dic["citation"] = int(self.list_citation.get())
        self.set_app_dic["on off citation"] = self.on_off_citation.get()
        self.fenetre.update()

        with open(self.chemin_set_app, "w") as f:
            json.dump(self.set_app_dic, f)

        self.up_set_notif = ToastNotification(
            title="Infinity Pack",
            message="""Vos paramètres ont bien été mis à jour. Pour qu'ils soient tous appliquer veuiller redémarrer cette application.
                                                                            Merci.""",
            duration=6543,
            alert=True,
            position=(0, 50, 'ne')
        )
        self.up_set_notif.show_toast()

    def add_cit(self):
        result = dialog.Querybox.get_string(title="Infinity Pack - Ajouter une citation ", parent=self.fenetre)

        self.set_app_dic["liste citation"].append(result)
        print(self.set_app_dic["liste citation"])

    def win_modif_set(self):        
        self.debut_nom_win = "Infinity Pack - Modification des paramètres "
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        #selection du theme
        self.frame_theme = ttkbs.Labelframe(self.frame_win, text="Thème de l'application : ")
        self.frame_theme.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)
        
        self.list_theme = ttkbs.Combobox(self.frame_theme, state="readonly", values=self.liste_theme)
        self.list_theme.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)
        self.list_theme.current(self.liste_theme.index(self.set_app_dic["theme"]))

        #selection de la langue de traduction par defaut
        self.frame_langue = ttkbs.Labelframe(self.frame_win, text="Langue de traduction par défaut : ")
        self.frame_langue.grid(row=1, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)
        
        self.list_langue = ttkbs.Combobox(self.frame_langue, state="readonly", values=list(LANGUAGES.values()))
        self.list_langue.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)
        self.list_langue.current(list(LANGUAGES.values()).index(self.set_app_dic["langue"]))

        #selection de la citation par defaut
        self.frame_citation = ttkbs.Labelframe(self.frame_win, text="Citation : ")
        self.frame_citation.grid(row=1, column=1, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)

        self.list_num_cit = []

        for num in range(len(self.citations)):
            self.list_num_cit.append(num+1)
        
        self.label_cit = ttkbs.Label(self.frame_citation, text="Citation affichée : ")
        self.label_cit.grid(row=1, column=0, padx=(5, 3), pady=(2, 5), sticky=ttkbs.E)

        self.list_citation = ttkbs.Spinbox(self.frame_citation, state="readonly", values=self.list_num_cit)
        self.list_citation.grid(row=1, column=1, padx=(2, 5), pady=(2, 5), sticky=ttkbs.NSEW)
        self.list_citation.set(value=self.set_app_dic["citation"])

        self.label_on_off_cit = ttkbs.Label(self.frame_citation, text="Afficher la citation au démarrage de l'application : ")
        self.label_on_off_cit.grid(row=0, column=0, padx=(5, 3), pady=(5, 3), sticky=ttkbs.NSEW)

        self.on_off_citation = ttkbs.IntVar(value=self.set_app_dic["on off citation"])
        self.activ_citation = ttkbs.Checkbutton(self.frame_citation, bootstyle="round-toggle", variable=self.on_off_citation)
        self.activ_citation.grid(row=0, column=1, padx=(2, 5), pady=(5, 3), sticky=ttkbs.NSEW)

        self.btn_ajout_cit = ttkbs.Button(self.frame_citation, text="Ajouter une citation :", command=lambda:self.add_cit())
        self.btn_ajout_cit.grid(row=2, column=0, padx=(2, 5), pady=(5, 3), columnspan=2, sticky=ttkbs.NSEW)

        ToolTip(widget=self.btn_ajout_cit, text="""Ouvre une boite de dialogue.""")

        #mettre a jour les parametre
        self.btn_appliquer_set = ttkbs.Button(self.frame_win, text="Mettre à jour les paramètres ", command=lambda:self.update_setting())
        self.btn_appliquer_set.grid(row=0, column=2, padx=(2, 3), pady=(2, 3), sticky=ttkbs.EW)

        ToolTip(self.btn_appliquer_set, text="""Pour que les paramètres soit appliqués :
il faudra redémarrer cette application.""", bootstyle=(DANGER, INVERSE))
        
        #mise a jour de l'application
        self.frame_ver = ttkbs.Labelframe(self.frame_win, text="Mise à jour de l'application : ")
        self.frame_ver.grid(row=0, column=1, padx=(5, 3), pady=(2, 3), sticky=ttkbs.NSEW)

        ToolTip(self.frame_ver, text="Le système de mise à jour n'est pas disponible pour votre version de l'application.")

        self.label_ver = ttkbs.Label(self.frame_ver, text=f"Version installé : {self.set_app_dic["version"]}")
        self.label_ver.grid(row=0, column=0, padx=(5, 5), pady=(5, 3), sticky=ttkbs.EW)

    def open_site(self):
        webbrowser.open('https://myinfinityapp.wordpress.com/')

    def win_about(self):
        self.debut_nom_win = "Infinity Pack - Information de l'application"
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        self.label_info = ttkbs.Label(self.frame_win, text="""Cette application est créée par : Lilien T
Créé en : 2024""")
        self.label_info.grid(row=0, column=0, padx=(5, 5), pady=(5, 3), sticky=ttkbs.EW)

        self.link_btn = ttkbs.Button(self.frame_win, text="Ouvrir le site :", command=lambda:self.open_site())
        self.link_btn.grid(row=1, column=0, padx=(5, 5), pady=(5, 3), sticky=ttkbs.EW)

        ToolTip(widget=self.link_btn, text="""Ouvre le site : https://myinfinityapp.wordpress.com/ dans votre navigateur.""")

    def win_accueil(self):
        self.debut_nom_win = "Infinity Pack - Accueil"
        self.fenetre.title(self.debut_nom_win)

        self.frame_win = ttkbs.Frame(self.fenetre)
        self.frame_win.grid(row=0, column=0, sticky=ttkbs.NSEW)

        label = ttkbs.Label(self.frame_win, text="""Bienvenue sur Infinity Pack :

    Vous pouvez avec cette application :
        - redimensionner vos image
        - changer le theme de cette application
        - éditer des tags
        - et c'est tout pour le moment
        - et bientot traduire du texte""")
        label.grid(row=0, column=0, padx=(5, 5), pady=(5, 2))

    def cit(self, etat):
        if self.set_app_dic["on off citation"] == 1 or etat == 1:
            self.citations = list(self.set_app_dic["liste citation"])
            self.citation = self.citations[int(self.set_app_dic["citation"])-1]
            self.fen_cit = dialog.MessageDialog(parent=self.fenetre, message=str(self.citation), title=f"Infinity Pack - Citation n°{int(self.set_app_dic["citation"])}", buttons=["OK"])
            self.fen_cit.show()

    def openaudio(self):
        self.win_edit_tag()
        self.ouvrir_audio()

    def openimage(self):
        self.win_img_resizer()
        self.ouvrir_img()

    def __init__(self):
        # Le chemin absolu du fichier python
        absolute_path = os.path.abspath(__file__)
        # Le chemin absolu du répertoire contenant le fichier python
        self.directory_path = os.path.dirname(absolute_path)
        
        self.chemin_set_app = str(self.directory_path) + str("/setting.json")
        
        self.set_app_dic = {}

        with open(self.chemin_set_app, "r") as f:
            self.set_app_dic = json.load(f)

        print(self.set_app_dic)
        self.liste_theme = self.set_app_dic["liste des themes"]

        self.citations = list(self.set_app_dic["liste citation"])
        self.citation = self.citations[int(self.set_app_dic["citation"])-1]

        self.debut_nom_win = "Infinity Pack - accueil"
        self.fenetre = ttkbs.Window(title=self.debut_nom_win, themename=self.set_app_dic["theme"])
        self.fenetre.geometry("400x250")

        #self.ico = tk.PhotoImage(file=self.chemin_ico, master=self.fenetre)
        
        self.menubar = ttkbs.Menu(self.fenetre)

        self.file_sub_menu = ttkbs.Menu(self.menubar, tearoff=1)

        self.file_sub_menu.add_command(label="Image", command=lambda:self.openimage())
        self.file_sub_menu.add_command(label="Audio", command=lambda:self.openaudio())

        self.fenetre.config(menu=self.menubar)

        self.file_menu = ttkbs.Menu(self.menubar, tearoff=1)
        self.file_menu.add_command(label="Accueil", command=lambda:self.win_accueil())
        self.file_menu.add_cascade(label="Fichier", menu=self.file_sub_menu)
        self.file_menu.add_command(label="Traduire", command=lambda:self.win_trad())
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=lambda:self.close())

        self.app_menu = ttkbs.Menu(self.menubar)
        self.app_menu.add_command(label="Citations", command=lambda:self.cit(etat=1))
        self.app_menu.add_command(label="Éditeur de tag", command=lambda:self.win_edit_tag())
        self.app_menu.add_command(label="Image Resizer", command=lambda:self.win_img_resizer())
        self.app_menu.add_command(label="Traduction", command=lambda:self.win_trad())

        self.set_menu = ttkbs.Menu(self.menubar)
        self.set_menu.add_command(label="Modifier les paramètres", command=lambda:self.win_modif_set())
        self.set_menu.add_command(label="Information de l'application", command=lambda:self.win_about())
        
        self.menubar.add_cascade(label="Fichier", menu=self.file_menu)
        self.menubar.add_cascade(label="Application", menu=self.app_menu)
        self.menubar.add_cascade(label="Aide", menu=self.set_menu)

        self.win_accueil()

        self.cit(etat=0)

        self.fenetre.mainloop()

app = App()