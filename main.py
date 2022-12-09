# $ sudo pip3 install experta
# $ sudo pip3 install networkx
# $ sudo pip3 install matplotlib

from experta import *
import ast


class MedicalExpert(KnowledgeEngine):
    username = ("",)

    @DefFacts()
    def needed_data(self):
        """
        Método que es llamado cada vez que engine.reset() is llamado.
        Funciona como constructor de esta clase.
        """
        yield Fact(findDisease="true")
        print(
            "Bienvenido al sistema experto de enfermedades en aves ponedoras\n\nA continuación te haré unas cuantas preguntas:\n\n"
        )

    @Rule(Fact(findDisease="true"), NOT(Fact(name=W())), salience=1000)
    def ask_name(self):
        self.username = input("Introduzca el nombre del usuario:\n")
        self.declare(Fact(name=self.username))

    # Encontrar sintoma secrecion_nasal
    
    @Rule(Fact(findDisease="true"), NOT(Fact(secrecion_nasal=W())), salience=995)
    def tienesecrecion_nasal(self):
        self.secrecion_nasal = input("\nDo you have secrecion_nasal?\nPor favor introduzca si/no\n")
        self.secrecion_nasal = self.secrecion_nasal.lower()
        self.declare(Fact(secrecion_nasal=self.secrecion_nasal.strip().lower()))

    # Encontrar sintoma secrecion_ocular
    @Rule(Fact(findDisease="true"), NOT(Fact(secrecion_ocular=W())), salience=985)
    def tienesecrecion_ocular(self):
        self.secrecion_ocular = input("\nDo you have secrecion_ocular?\nPor favor introduzca si/no\n")
        self.secrecion_ocular = self.secrecion_ocular.lower()
        self.declare(Fact(secrecion_ocular=self.secrecion_ocular.strip().lower()))

    # Encontrar sintoma jadeo
    @Rule(Fact(findDisease="true"), NOT(Fact(jadeo=W())), salience=975)
    def tienejadeo(self):
        self.jadeo = input("\nDo you jadeo?\nPor favor introduzca si/no\n")
        self.jadeo = self.jadeo.lower()
        self.declare(Fact(jadeo=self.jadeo.strip().lower()))
    
    # Encontrar sintoma espasmos
    @Rule(Fact(findDisease="true"), NOT(Fact(espasmos=W())), salience=970)
    def tieneespasmos(self):
        self.espasmos = input("\nDo you experience espasmos occasionally?\nPor favor introduzca si/no\n")
        self.espasmos = self.espasmos.lower()
        self.declare(Fact(espasmos=self.espasmos.strip().lower()))

    @Rule(Fact(findDisease="true"), NOT(Fact(rigidez=W())), salience=965)
    def tienerigidez(self):
        self.rigidez = input("\nDo you experience rigidez?\nPor favor introduzca si/no\n")
        self.rigidez = self.rigidez.lower()
        self.declare(Fact(rigidez=self.rigidez.strip().lower()))


    @Rule(Fact(findDisease="true"), NOT(Fact(tos=W())), salience=955)
    def tienetos(self):
        self.tos = input("\nDo you experience tos?\nPor favor introduzca si/no\n")
        self.tos = self.tos.lower()
        self.declare(Fact(tos=self.tos.strip().lower()))

    @Rule(Fact(findDisease="true"), NOT(Fact(estornudos=W())), salience=950)
    def tieneestornudos(self):
        self.estornudos = input("\nDo you experience estornudos?\nPor favor introduzca si/no\n")
        self.estornudos = self.estornudos.lower()
        self.declare(Fact(estornudos=self.estornudos.strip().lower()))

    @Rule(Fact(findDisease="true"), NOT(Fact(plumas_erizadas=W())), salience=945)
    def tieneplumas_erizadas(self):
        self.plumas_erizadas = input("\nDo you experience plumas_erizadas?\nPor favor introduzca si/no\n")
        self.plumas_erizadas = self.plumas_erizadas.lower()
        self.declare(Fact(plumas_erizadas=self.plumas_erizadas.strip().lower()))

    @Rule(Fact(findDisease="true"), NOT(Fact(fiebre=W())), salience=940)
    def tienefiebre(self):
        self.fiebre = input(
            "\nDo you experience sore fiebre?\nPor favor introduzca si/no\n")
        self.fiebre = self.fiebre.lower()
        self.declare(Fact(fiebre=self.fiebre.strip().lower()))

    @Rule(Fact(findDisease="true"), NOT(Fact(diarrea=W())), salience=935)
    def tienediarrea(self):
        self.diarrea = input(
            "\nDo you experience diarrea?\nPor favor introduzca si/no\n")
        self.diarrea = self.diarrea.lower()
        self.declare(Fact(diarrea=self.diarrea.strip().lower()))
        
    @Rule(Fact(findDisease="true"), NOT(Fact(infeccion_bolsa_fabricio=W())), salience=930)
    def tieneinfeccion_bolsa_fabricio(self):
        self.infeccion_bolsa_fabricio = input(
            "\nDo you experience infeccion_bolsa_fabricio?\nPor favor introduzca si/no\n")
        self.infeccion_bolsa_fabricio = self.infeccion_bolsa_fabricio.lower()
        self.declare(Fact(infeccion_bolsa_fabricio=self.infeccion_bolsa_fabricio.strip().lower()))
        
    @Rule(Fact(findDisease="true"), NOT(Fact(contracciones_cuello=W())), salience=925)
    def tienecontracciones_cuello(self):
        self.contracciones_cuello = input(
            "\nDo you experience contracciones_cuello?\nPor favor introduzca si/no\n")
        self.contracciones_cuello = self.contracciones_cuello.lower()
        self.declare(Fact(contracciones_cuello=self.contracciones_cuello.strip().lower()))
        
    @Rule(Fact(findDisease="true"), NOT(Fact(falta_apetito=W())), salience=920)
    def tienefalta_apetito(self):
        self.falta_apetito = input(
            "\nDo you experience falta_apetito?\nPor favor introduzca si/no\n")
        self.falta_apetito = self.falta_apetito.lower()
        self.declare(Fact(falta_apetito=self.falta_apetito.strip().lower()))
        
    @Rule(Fact(findDisease="true"), NOT(Fact(inflamacion_cara=W())), salience=915)
    def tieneinflamacion_cara(self):
        self.inflamacion_cara = input(
            "\nDo you experience inflamacion_cara?\nPor favor introduzca si/no\n")
        self.inflamacion_cara = self.inflamacion_cara.lower()
        self.declare(Fact(inflamacion_cara=self.inflamacion_cara.strip().lower()))
        
    @Rule(Fact(findDisease="true"), NOT(Fact(sensibilidad_luz=W())), salience=910)
    def tienesensibilidad_luz(self):
        self.sensibilidad_luz = input(
            "\nDo you experience sensibilidad_luz?\nPor favor introduzca si/no\n")
        self.sensibilidad_luz = self.sensibilidad_luz.lower()
        self.declare(Fact(sensibilidad_luz=self.sensibilidad_luz.strip().lower()))

    # Encontrar enfermedad 0
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="si"),
        Fact(secrecion_ocular="si"),
        Fact(jadeo="si"),
        Fact(espasmos="no"),
        Fact(headche="no"),
        Fact(tos="si"),
        Fact(estornudos="no"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="no"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def disease_0(self):
        self.declare(Fact(disease="Bronquitis Infecciosa"))

    # Encontrar enfermedad 1
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="si"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="si"),
        Fact(rigidez="si"),
        Fact(tos="si"),
        Fact(estornudos="si"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="si"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="si"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def disease_1(self):
        self.declare(Fact(disease="New Castle"))
        
    # Encontrar enfermedad 2
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="si"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="si"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="no"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def disease_2(self):
        self.declare(Fact(disease="Influenza Aviar"))

    # Encontrar enfermedad 3
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="si"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="no"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="si"),
    )
    def disease_3(self):
        self.declare(Fact(disease="Gumboro"))

    # Encontrar enfermedad 4
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
        Fact(rigidez="si"),
        Fact(tos="no"),
        Fact(estornudos="si"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="no"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def disease_4(self):
        self.declare(Fact(disease="Coriza Infecciosa"))

    # Encontrar enfermedad 5
    @Rule(
        Fact(findDisease="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="si"),
        Fact(plumas_erizadas="si"),
        Fact(fiebre="si"),
        Fact(diarrea="no"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def disease_5(self):
        self.declare(Fact(disease="Colera Aviar"))


    #reglas
    @Rule(Fact(findDisease="true"), NOT(Fact(disease=W())), salience=-1)
    def unmatched(self):
        self.declare(Fact(disease="unknown"))

    @Rule(Fact(findDisease="true"), Fact(disease=MATCH.disease), salience=1)
    def getDisease(self, disease):

        if disease == "unknown":
            mapDisease = []
            # agregar sintomas al map
            mapDisease.append("tos")#sintoma1
            mapDisease.append("secrecion_nasal")#sintoma2
            mapDisease.append("secrecion_ocular")#sintoma3
            mapDisease.append("jadeo")#sintoma4
            mapDisease.append("espasmos")#sintoma5
            mapDisease.append("plumas_erizadas")#sintoma6
            mapDisease.append("rigidez")#sintoma7
            mapDisease.append("fiebre")#sintoma8
            mapDisease.append("diarrea")#sintoma9
            mapDisease.append("estornudos")#sintoma10
            mapDisease.append("infeccion_bolsa_fabricio")#sintoma11
            mapDisease.append("contracciones_cuello")#sintoma12
            mapDisease.append("falta_apetito")#sintoma13
            mapDisease.append("inflamacion_cara")#sintoma14
            mapDisease.append("sensibilidad_luz")#sintoma15
            print("\n\nRevisamos los siguientes sintomas:", mapDisease)
            mapDisease_val = [
                self.tos,#sintoma1
                self.secrecion_nasal,#sintoma2
                self.secrecion_ocular,#sintoma3
                self.jadeo,#sintoma4
                self.espasmos,#sintoma5
                self.plumas_erizadas,#sintoma6
                self.rigidez,#sintoma7
                self.fiebre,#sintoma8
                self.diarrea,#sintoma9
                self.estornudos,#sintoma10
                self.infeccion_bolsa_fabricio,#sintoma11
                self.contracciones_cuello,#sintoma12
                self.falta_apetito,#sintoma13
                self.inflamacion_cara,#sintoma14
                self.sensibilidad_luz,#sintoma15
            ]
            print("\n\nLos sintomas en el ave son:", mapDisease_val)

            # Abrir el archivo que relaciona las enfermedades con los sintomas
            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()

            yes_symptoms = []
            for i in range(0, len(mapDisease_val)):
                if mapDisease_val[i] == "si":
                    yes_symptoms.append(mapDisease[i])

            max_val = 0
            print("\n\nLos sintomas encontrados son : ", yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key, ":", val)
                for x in val:
                    if x in yes_symptoms:
                        count += 1
                # print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_dis = key

            if max_val == 0:
                print("No se han encontrado enfermedades. El ave está sana.")
            else:
                print(
                    "\n\nNo podemos decirle con certeza cuál es la enfermedad exacta, pero creemos que padece...",
                    pred_dis,
                )

                print(
                    "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
                )

                print("\n\nInformación sobre la enfermedad:", pred_dis)

                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r")
                print(f.read())
                print(
                    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
                )
                print(
                    "\n\nNo se preocupe",
                    self.username,
                    ". Tenemos algunas sugerencias para usted\n",
                )
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r")
                print(f.read())
                print(
                    "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
                )
        else:
            print("La enfermedad más probable que padezca es:", disease)
            print("\n\n")
            print(
                "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
            )
            print("Información sobre la enfermedad:\n")
            print(disease)
            f = open("disease/disease_descriptions/" + disease + ".txt", "r")
            print(f.read())
            print(
                "\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
            )
            print(
                "\n\nNo se preocupe",
                self.username,
                ". Tenemos algunas sugerencias para usted\n",
            )
            f = open("disease/disease_treatments/" + disease + ".txt", "r")
            print(f.read())

    # @Rule(Fact(findDisease = 'true'),
    # Fact(name=MATCH.name))
    # def greet(self, name):
    #     print("Hi!",name, "How is the weather?")


if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print("Impresión de datos del motor de inferencia", engine.facts)
