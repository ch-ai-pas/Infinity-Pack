import PIL as pil

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
