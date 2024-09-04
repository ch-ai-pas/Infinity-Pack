import PIL as pil
import requests
from ShazamAPI import Shazam
from mutagen.easyid3 import EasyID3
import mutagen
from googletrans import Translator
from googletrans import LANGUAGES

class imgresizer():
    def openning(self, img_file):
        print(img_file)
        self.filename_pil = pil.Image.open(img_file)
        print(self.filename_pil)

        return self.filename_pil
    
    def resize(self, filename, hauteur, entry_h, largeur, entry_l, type_val):
        self.filename = filename
        self.hauteur = hauteur
        self.entry = entry_h
        print(self.entry.get())
        self.largeur = largeur
        self.entry1 = entry_l

        # Ouvrir l'image avec PIL
        self.image = pil.Image.open(self.filename)
        
        print("-------------------------")
        print(f"/{self.entry.get()}/")
        print(self.largeur)
        print("+")
        print(f"/{self.entry1.get()}/")
        print(self.hauteur)

        if self.entry.get() != "":
            if int(self.entry.get()) != int(self.largeur):
                # Définir la largeur souhaitée
                self.largeur = int(self.entry.get())
                print(self.largeur)

                # Calculer la hauteur correspondante tout en conservant le rapport d'aspect
                self.hauteur = int((float(self.image.size[1]) * float(self.largeur / float(self.image.size[0]))))
                print("Hauteur de l'image " + str(self.hauteur))
            
            elif int(self.entry1.get()) != int(self.hauteur):
                # Définir la largeur souhaitée
                self.hauteur = int(self.entry1.get())
                print(self.hauteur)

                # Calculer la hauteur correspondante tout en conservant le rapport d'aspect
                self.largeur = int((float(self.image.size[0]) * float(self.hauteur / float(self.image.size[1]))))
                print("Largeur de l'image " + str(self.largeur))
            
        self.entry.set(self.largeur)
        self.entry1.set(self.hauteur)

        if type_val == "hauteur":
            return self.hauteur
        if type_val == "largeur":
            return self.largeur
        if type_val == "entry_h":
            return self.entry
        if type_val == "entry_l":
            return self.entry1
        
class update():
    def verif_update(self, info_app):
        print("cette fonctionnalité n'est pas disponible dans pour version")

class edit_tag():
    def open(self, filename):
        self.filename = filename

        #partie fichier
        self.audiofile = EasyID3(self.filename)

        return self.audiofile
    
    def open_shazam(self, filename):
        self.filename = filename

        with open(self.filename, "rb") as f:
            self.mp3 = f.read()

        #partie shazam
        self.shazam = Shazam(self.mp3)
        self.titre = self.shazam.recognizeSong()
        self.chanson = next(self.titre)

        #print(f"{self.chanson[1]['track']}")

        return self.chanson

    def tag_file(self, audio_file):
        self.dic_tag = {"titre":audio_file['title'],
                        "artiste":audio_file['artist'],
                        "album":audio_file['album'],
                        "annee":audio_file['date'],
                        "num album":audio_file['tracknumber'],
                        "genre":audio_file['genre']}

        return self.dic_tag
    
    def tag_shazam(self, chanson):
        self.dict_tag_sha = {"titre":chanson[1]['track']['title'],
                        "artiste":chanson[1]['track']['subtitle'],
                        "album":chanson[1]['track']['sections'][0]['metadata'][0]['text'],
                        "annee":chanson[1]['track']['sections'][0]['metadata'][2]['text'],
                        "num album":chanson[1]['track']['layout']} #, "artiste_album":chanson.tag.album_artist, "numero":chanson.tag.track_num, "image":chanson.tag.images}

        return self.dict_tag_sha
    
    def save(self, audiofile, titre, artiste, album, annee):
        print(titre.get())
        audiofile['title'] = titre.get()
        audiofile['artist'] = artiste.get()
        audiofile['album'] = album.get()
        audiofile['date'] = annee.get()

        audiofile.save(v2_version=3)

class traduction():
    def trad_auto(self, texte, langue_f):
        def translate_text(text, target_language):
            translator1 = Translator()
            translated_text = translator1.translate(text, dest=target_language)
            return translated_text.text

        original_text = texte
        target_language = langue_f
        translated_result = translate_text(original_text, target_language)
        #print(f"Translated text: {translated_result}")

        return translated_result