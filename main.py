"""
 sudo pip3 install networkx
 sudo pip3 install experta
 sudo pip3 install matplotlib
 
 La libreria 'experta'  está hecha para hacer sistemas expertos, está inspirado en el lenguaje CLIPS creado por la NASA.
 
 Funciona con únicamente con las versiones 3.5, 3.6, 3.7, 3.8
 
 Experta is a Python library for building expert systems strongly inspired by CLIPS.
"""


from experta import *
import ast


class MedicalExpert(KnowledgeEngine):
    nombre_usuario = ("",)

    @DefFacts()
    def needed_data(self):
        """
        Método que es llamado cada vez que engine.reset() es llamado.
        Funciona como constructor de esta clase.
        """
        yield Fact(findEnfermedad="true")
        print(
            """
Bienvenido al sistema experto de enfermedades en aves ponedoras
A continuación te haré unas cuantas preguntas:
"""
        )

    # Regla que guarda el como hecho el nombre del usuario del sistema
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(nombre=W())), salience=1000)
    def preguntar_nombre(self):
        self.nombre_usuario = input("Introduzca el nombre del usuario:\n")
        self.declare(Fact(nombre=self.nombre_usuario))

    # Encontrar sintoma secrecion_nasal
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(secrecion_nasal=W())), salience=995)
    def tienesecrecion_nasal(self):
        self.secrecion_nasal = input(
            "\nTiene secrecion nasal?\nPor favor introduzca si/no\n"
        )
        self.secrecion_nasal = self.secrecion_nasal.lower()
        self.declare(Fact(secrecion_nasal=self.secrecion_nasal.strip().lower()))

    # Encontrar sintoma secrecion_ocular
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(secrecion_ocular=W())), salience=985)
    def tienesecrecion_ocular(self):
        self.secrecion_ocular = input(
            "\nTiene secrecion ocular?\nPor favor introduzca si/no\n"
        )
        self.secrecion_ocular = self.secrecion_ocular.lower()
        self.declare(Fact(secrecion_ocular=self.secrecion_ocular.strip().lower()))

    # Encontrar sintoma jadeo
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(jadeo=W())), salience=975)
    def tienejadeo(self):
        self.jadeo = input("\nTiene jadeo?\nPor favor introduzca si/no\n")
        self.jadeo = self.jadeo.lower()
        self.declare(Fact(jadeo=self.jadeo.strip().lower()))

    # Encontrar sintoma espasmos
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(espasmos=W())), salience=970)
    def tieneespasmos(self):
        self.espasmos = input("\nTiene espasmos?\nPor favor introduzca si/no\n")
        self.espasmos = self.espasmos.lower()
        self.declare(Fact(espasmos=self.espasmos.strip().lower()))

    # Encontrar sintoma rigidez
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(rigidez=W())), salience=965)
    def tienerigidez(self):
        self.rigidez = input("\nTiene rigidez?\nPor favor introduzca si/no\n")
        self.rigidez = self.rigidez.lower()
        self.declare(Fact(rigidez=self.rigidez.strip().lower()))

    # Encontrar sintoma tos
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(tos=W())), salience=955)
    def tienetos(self):
        self.tos = input("\nTiene tos?\nPor favor introduzca si/no\n")
        self.tos = self.tos.lower()
        self.declare(Fact(tos=self.tos.strip().lower()))

    # Encontrar sintoma estornudos
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(estornudos=W())), salience=950)
    def tieneestornudos(self):
        self.estornudos = input("\nDetecta estornudos?\nPor favor introduzca si/no\n")
        self.estornudos = self.estornudos.lower()
        self.declare(Fact(estornudos=self.estornudos.strip().lower()))

    # Encontrar sintoma plumas_erizadas
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(plumas_erizadas=W())), salience=945)
    def tieneplumas_erizadas(self):
        self.plumas_erizadas = input(
            "\nTiene plumas erizadas?\nPor favor introduzca si/no\n"
        )
        self.plumas_erizadas = self.plumas_erizadas.lower()
        self.declare(Fact(plumas_erizadas=self.plumas_erizadas.strip().lower()))

    # Encontrar sintoma fiebre
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(fiebre=W())), salience=940)
    def tienefiebre(self):
        self.fiebre = input("\nTiene  fiebre?\nPor favor introduzca si/no\n")
        self.fiebre = self.fiebre.lower()
        self.declare(Fact(fiebre=self.fiebre.strip().lower()))

    # Encontrar sintoma diarrea
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(diarrea=W())), salience=935)
    def tienediarrea(self):
        self.diarrea = input("\nTiene diarrea?\nPor favor introduzca si/no\n")
        self.diarrea = self.diarrea.lower()
        self.declare(Fact(diarrea=self.diarrea.strip().lower()))

    # Encontrar sintoma infección bolsa fabricio
    @Rule(
        Fact(findEnfermedad="true"), NOT(Fact(infeccion_bolsa_fabricio=W())), salience=930
    )
    def tieneinfeccion_bolsa_fabricio(self):
        self.infeccion_bolsa_fabricio = input(
            "\nTiene infeccion en la bolsa de fabricio?\nPor favor introduzca si/no\n"
        )
        self.infeccion_bolsa_fabricio = self.infeccion_bolsa_fabricio.lower()
        self.declare(
            Fact(infeccion_bolsa_fabricio=self.infeccion_bolsa_fabricio.strip().lower())
        )

    # Encontrar sintoma contracciones cuello
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(contracciones_cuello=W())), salience=925)
    def tienecontracciones_cuello(self):
        self.contracciones_cuello = input(
            "\nTiene contracciones en el cuello?\nPor favor introduzca si/no\n"
        )
        self.contracciones_cuello = self.contracciones_cuello.lower()
        self.declare(
            Fact(contracciones_cuello=self.contracciones_cuello.strip().lower())
        )

    # Encontrar sintoma falta apetito
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(falta_apetito=W())), salience=920)
    def tienefalta_apetito(self):
        self.falta_apetito = input(
            "\nTiene falta de apetito?\nPor favor introduzca si/no\n"
        )
        self.falta_apetito = self.falta_apetito.lower()
        self.declare(Fact(falta_apetito=self.falta_apetito.strip().lower()))

    # Encontrar sintoma inflamación cara
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(inflamacion_cara=W())), salience=915)
    def tieneinflamacion_cara(self):
        self.inflamacion_cara = input(
            "\nTiene inflamacion en la cara?\nPor favor introduzca si/no\n"
        )
        self.inflamacion_cara = self.inflamacion_cara.lower()
        self.declare(Fact(inflamacion_cara=self.inflamacion_cara.strip().lower()))

    # Encontrar sintoma sensibilidad luz
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(sensibilidad_luz=W())), salience=910)
    def tienesensibilidad_luz(self):
        self.sensibilidad_luz = input(
            "\nTiene sensibilidad a la luz?\nPor favor introduzca si/no\n"
        )
        self.sensibilidad_luz = self.sensibilidad_luz.lower()
        self.declare(Fact(sensibilidad_luz=self.sensibilidad_luz.strip().lower()))

    """
    Encontrar enfermedad 0, Bronquitis Infecciosa
    Sintomas: 
    secrecion_nasal,secrecion_ocular,jadeo,tos    
    
    
        {"Bronquitis Infecciosa": "secrecion_nasal,secrecion_ocular,jadeo,tos", "New Castle": "secrecion_nasal,espasmos,rigidez,tos,estornudos,diarrea,contracciones_cuello", "Influenza Aviar": "secrecion_nasal,secrecion_ocular,estornudos", "Gumboro": "plumas_erizadas,diarrea,infeccion_bolsa_fabricio,falta_apetito", "Coriza Infecciosa": "inflamacion_cara,secrecion_ocular,sensibilidad_luz", "Colera Aviar": "secrecion_nasal,plumas_erizadas,fiebre,diarrea,contracciones_cuello,falta_apetito"}
    """

    @Rule(
        Fact(findEnfermedad="true"),
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
    def Enfermedad_0(self):
        self.declare(Fact(Enfermedad="Bronquitis Infecciosa"))

    """ 
        Encontrar enfermedad 1 New Castle
        Sintomas:
        secrecion_nasal,espasmos,rigidez,tos,
        estornudos,diarrea,contracciones_cuello
        
    """

    @Rule(
        Fact(findEnfermedad="true"),
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
    def Enfermedad_1(self):
        self.declare(Fact(Enfermedad="New Castle"))

    """ 
        Encontrar enfermedad 2 Influenza Aviar": 
        Sintomas:
        secrecion_nasal,secrecion_ocular,estornudos
        
    """
    @Rule(
        Fact(findEnfermedad="true"),
        Fact(secrecion_nasal="si"),
        Fact(secrecion_ocular="si"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
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
    def Enfermedad_2(self):
        self.declare(Fact(Enfermedad="Influenza Aviar"))

    """ 
        Encontrar enfermedad 3, Gumboro": 
        Sintomas:
        plumas_erizadas,diarrea,infeccion_bolsa_fabricio,falta_apetito
        
    """
    @Rule(
        Fact(findEnfermedad="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="no"),
        Fact(plumas_erizadas="si"),
        Fact(fiebre="no"),
        Fact(diarrea="si"),
        Fact(infeccion_bolsa_fabricio="si"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="si"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def Enfermedad_3(self):
        self.declare(Fact(Enfermedad="Gumboro"))

    """ 
        Encontrar enfermedad 4 Coriza Infecciosa:
        Sintomas: 
        inflamacion_cara,secrecion_ocular,sensibilidad_luz
        
    """
    @Rule(
        Fact(findEnfermedad="true"),
        Fact(secrecion_nasal="no"),
        Fact(secrecion_ocular="si"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="no"),
        Fact(plumas_erizadas="no"),
        Fact(fiebre="no"),
        Fact(diarrea="no"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="no"),
        Fact(falta_apetito="no"),
        Fact(inflamacion_cara="si"),
        Fact(sensibilidad_luz="si"),
    )
    def Enfermedad_4(self):
        self.declare(Fact(Enfermedad="Coriza Infecciosa"))

    """ 
        Encontrar enfermedad 5 Colera Aviar:
        Sintomas: 
        secrecion_nasal,plumas_erizadas,fiebre,diarrea,contracciones_cuello,falta_apetito
        
    """
    @Rule(
        Fact(findEnfermedad="true"),
        Fact(secrecion_nasal="si"),
        Fact(secrecion_ocular="no"),
        Fact(jadeo="no"),
        Fact(espasmos="no"),
        Fact(rigidez="no"),
        Fact(tos="no"),
        Fact(estornudos="no"),
        Fact(plumas_erizadas="si"),
        Fact(fiebre="si"),
        Fact(diarrea="si"),
        Fact(infeccion_bolsa_fabricio="no"),
        Fact(contracciones_cuello="si"),
        Fact(falta_apetito="si"),
        Fact(inflamacion_cara="no"),
        Fact(sensibilidad_luz="no"),
    )
    def Enfermedad_5(self):
        self.declare(Fact(Enfermedad="Colera Aviar"))

    # En caso de que no se encuentre una enfermedad a partir de
    # los sintomas, entonces es deconocida
    # posteriormente se le asigna una nueva a partir de
    # la importancia de los sintomas encontrados 
    # (en caso de haber sintomas)
    @Rule(Fact(findEnfermedad="true"), NOT(Fact(Enfermedad=W())), salience=-1)
    def unmatched(self):
        self.declare(Fact(Enfermedad="unknown"))

    @Rule(Fact(findEnfermedad="true"), Fact(Enfermedad=MATCH.Enfermedad), salience=1)
    def getEnfermedad(self, Enfermedad):

        if Enfermedad == "unknown":
            mapEnfermedad = []
            # agregar sintomas al diccionario
            mapEnfermedad.append("tos")  # sintoma1
            mapEnfermedad.append("secrecion_nasal")  # sintoma2
            mapEnfermedad.append("secrecion_ocular")  # sintoma3
            mapEnfermedad.append("jadeo")  # sintoma4
            mapEnfermedad.append("espasmos")  # sintoma5
            mapEnfermedad.append("plumas_erizadas")  # sintoma6
            mapEnfermedad.append("rigidez")  # sintoma7
            mapEnfermedad.append("fiebre")  # sintoma8
            mapEnfermedad.append("diarrea")  # sintoma9
            mapEnfermedad.append("estornudos")  # sintoma10
            mapEnfermedad.append("infeccion_bolsa_fabricio")  # sintoma11
            mapEnfermedad.append("contracciones_cuello")  # sintoma12
            mapEnfermedad.append("falta_apetito")  # sintoma13
            mapEnfermedad.append("inflamacion_cara")  # sintoma14
            mapEnfermedad.append("sensibilidad_luz")  # sintoma15
            print("\n\nRevisamos los siguientes sintomas:", mapEnfermedad)
            mapEnfermedad_val = [
                self.tos,  # sintoma1
                self.secrecion_nasal,  # sintoma2
                self.secrecion_ocular,  # sintoma3
                self.jadeo,  # sintoma4
                self.espasmos,  # sintoma5
                self.plumas_erizadas,  # sintoma6
                self.rigidez,  # sintoma7
                self.fiebre,  # sintoma8
                self.diarrea,  # sintoma9
                self.estornudos,  # sintoma10
                self.infeccion_bolsa_fabricio,  # sintoma11
                self.contracciones_cuello,  # sintoma12
                self.falta_apetito,  # sintoma13
                self.inflamacion_cara,  # sintoma14
                self.sensibilidad_luz,  # sintoma15
            ]
            print("\n\nLos sintomas en el ave son:", mapEnfermedad_val)

            # Abrir el archivo que relaciona las enfermedades con los sintomas
            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            #utiliza la libreria ast para manejar el texto 
            # (Abstract Syntax Trees)
            dictionary = ast.literal_eval(contents)
            file.close()

            # guarda los sintomas con 'si' en una nueva lista
            sintomasEncontrados = []
            for i in range(0, len(mapEnfermedad_val)):
                if mapEnfermedad_val[i] == "si":
                    sintomasEncontrados.append(mapEnfermedad[i])

            max_val = 0
            print("\n\nLos sintomas encontrados son : ", sintomasEncontrados)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key, ":", val)
                for x in val:
                    if x in sintomasEncontrados:
                        count += 1
                # print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_enf = key
            # si no encuentra sintomas con 'si' entonces está sano
            if max_val == 0:
                print("No se han encontrado enfermedades. El ave está sana.")
            else:
                # Al haber sintomas, entonces el ave tiene una enfermedad
                # Pero en esta situación, no hizo match con ninguna enfermedad
                print(
                    "\n\nNo podemos decirle con certeza cuál es la enfermedad exacta, pero creemos que padece...",
                    pred_enf,
                )

                print('''
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                     
                      ''')

                print("\n\nInformación sobre la enfermedad:", pred_enf)
                # abre el archivo txt correpondiente a la enfermedad
                # donde obtendrá su descripción
                f = open("disease/disease_descriptions/" + pred_enf + ".txt", "r")
                print(f.read())
                print('''
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                     
                      ''')
                print(
                    "\n\nNo se preocupe",
                    self.nombre_usuario,
                    ". Tenemos algunas sugerencias para usted\n",
                )
                # abre el archivo txt correpondiente a la enfermedad
                # donde obtendrá su tratamiento
                f = open("disease/disease_treatments/" + pred_enf + ".txt", "r")
                print(f.read())
                print('''
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                     
                      ''')
        else:
            # Los sintomas son exactos a los de X enfermedad
            print("La enfermedad más probable que padezca es:", Enfermedad)
            print("\n\n")
            print('''
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                     
                      ''')
            print("Información sobre la enfermedad:\n")
            print(Enfermedad)
            
            # abre el archivo txt correpondiente a la enfermedad
            # donde obtendrá su descripción
            f = open("disease/disease_descriptions/" + Enfermedad + ".txt", "r")
            print(f.read())
            print('''
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                     
                      ''')
            print(
                "\n\nNo se preocupe",
                self.nombre_usuario,
                ". Tenemos algunas sugerencias para usted\n",
            )
            # abre el archivo txt correpondiente a la enfermedad
            # donde obtendrá su tratamiento
            f = open("disease/disease_treatments/" + Enfermedad + ".txt", "r")
            print(f.read())


if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print("Impresión de datos del motor de inferencia", engine.facts)
