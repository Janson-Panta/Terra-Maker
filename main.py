

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image




class Adm (ScreenManager):
    pass

class Principal (Screen):
    def mudar1(self):

        if self.ids.label1.text == "Dan":
            self.ids.label1.text = "Mon"

        elif self.ids.label1.text == "Mon":
            self.ids.label1.text = "Sen"

        elif self.ids.label1.text == "Sen":
            self.ids.label1.text = "Tar"

        elif self.ids.label1.text == "Tar":
            self.ids.label1.text = "Mid"

        elif self.ids.label1.text == "Mid":
            self.ids.label1.text = "Arc"

        elif self.ids.label1.text == "Arc":
            self.ids.label1.text = "Not"

        elif self.ids.label1.text == "Not":
            self.ids.label1.text = "Cit"

        elif self.ids.label1.text == "Cit":
            self.ids.label1.text = "Arm"

        elif self.ids.label1.text == "Arm":
            self.ids.label1.text = "Erin"

        elif self.ids.label1.text == "Erin":
            self.ids.label1.text = "Noa"

        elif self.ids.label1.text == "Noa":
            self.ids.label1.text = "Niff"

        elif self.ids.label1.text == "Niff":
            self.ids.label1.text = "Cra"

        elif self.ids.label1.text == "Cra":
            self.ids.label1.text = "Cri"

        elif self.ids.label1.text == "Cri":
            self.ids.label1.text = "Hid"

        elif self.ids.label1.text == "Hid":
            self.ids.label1.text = "Unt"

        elif self.ids.label1.text == "Unt":
            self.ids.label1.text = "Dan"





    def mudar2(self):
        if self.ids.label2.text == "gar":
            self.ids.label2.text = "dra"

        elif self.ids.label2.text == "dra":
            self.ids.label2.text = "lei"

        elif self.ids.label2.text == "lei":
            self.ids.label2.text = "dar"

        elif self.ids.label2.text == "dar":
            self.ids.label2.text = "tan"

        elif self.ids.label2.text == "tan":
            self.ids.label2.text = "irn"

        elif self.ids.label2.text == "irn":
            self.ids.label2.text = "tev"

        elif self.ids.label2.text == "tev":
            self.ids.label2.text = "dun"

        elif self.ids.label2.text == "dun":
            self.ids.label2.text = "kev"

        elif self.ids.label2.text == "kev":
            self.ids.label2.text = "tor"

        elif self.ids.label2.text == "tor":
            self.ids.label2.text = "zen"

        elif self.ids.label2.text == "zen":
            self.ids.label2.text = "zir"

        elif self.ids.label2.text == "zir":
            self.ids.label2.text = "nel"

        elif self.ids.label2.text == "nel":
            self.ids.label2.text = "ton"

        elif self.ids.label2.text == "ton":
            self.ids.label2.text = "zar"

        elif self.ids.label2.text == "zar":
            self.ids.label2.text = "ent"

        elif self.ids.label2.text == "ent":
            self.ids.label2.text = "dub"

        elif self.ids.label2.text == "dub":
            self.ids.label2.text = "gar"



    def mudar3 (self):


        if self.ids.label3.text == "ann":
            self.ids.label3.text = "don"

        elif self.ids.label3.text == "don":
            self.ids.label3.text = "dan"

        elif self.ids.label3.text == "dan":
            self.ids.label3.text = "vik"

        elif self.ids.label3.text == "vik":
            self.ids.label3.text = "eir"

        elif self.ids.label3.text == "eir":
            self.ids.label3.text = "zan"

        elif self.ids.label3.text == "zan":
            self.ids.label3.text = "ren"

        elif self.ids.label3.text == "ren":
            self.ids.label3.text = "gor"

        elif self.ids.label3.text == "gor":
            self.ids.label3.text = "tus"

        elif self.ids.label3.text == "tus":
            self.ids.label3.text = "tiv"

        elif self.ids.label3.text == "tiv":
            self.ids.label3.text = "zav"

        elif self.ids.label3.text == "zav":
            self.ids.label3.text = "rin"

        elif self.ids.label3.text == "rin":
            self.ids.label3.text = "tis"

        elif self.ids.label3.text == "tis":
            self.ids.label3.text = "ode"

        elif self.ids.label3.text == "ode":
            self.ids.label3.text = "can"

        elif self.ids.label3.text == "can":
            self.ids.label3.text = "eti"

        elif self.ids.label3.text == "eti":
            self.ids.label3.text = "osd"

    def forma(self):
        self.ids.label4.text = self.ids.label1.text + self.ids.label2.text + self.ids.label3.text

    def limpa(self):
        self.ids.label4.text = " "



class MainApp (MDApp):
    def fechar(self):
        self.stop()

    def build (self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        return Adm()




MainApp().run()
