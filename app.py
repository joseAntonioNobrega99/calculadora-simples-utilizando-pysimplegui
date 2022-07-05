import PySimpleGUI as sg

sg.theme("random")

class Main():
    def __init__(self):

        tela = [
            [sg.Text("Calculadora Simples")],
            [sg.Text("Número1"),sg.Input("",key="numero1")],
            [sg.Text("Número2"),sg.Input("",key="numero2")],
            [sg.Button("Somar"),sg.Button("Subtrair"),sg.Button("Múltiplicar"),sg.Button("Dividir")],
            [sg.Text("",key="resultado")]
        ]

        self.janela = sg.Window("Calculadora Simples",tela)
    def Inicializar(self):

        while True:

            self.eventos,self.valores = self.janela.read()
            self.resultado = 0

            if self.eventos == sg.WINDOW_CLOSED:
                break
            if self.eventos == "Somar":
                self.resultado = float(self.valores["numero1"]) + float(self.valores["numero2"])
                self.janela["resultado"].update(f"O resultado é {self.resultado}")
            if self.eventos == "Subtrair":
                self.resultado = float(self.valores["numero1"]) - float(self.valores["numero2"])
                self.janela["resultado"].update(f"O resultado é {self.resultado}")
            if self.eventos == "Múltiplicar":
                self.resultado = float(self.valores["numero1"]) * float(self.valores["numero2"])
                self.janela["resultado"].update(f"O resultado é {self.resultado}")
            if self.eventos == "Dividir":
                self.resultado = float(self.valores["numero1"]) / float(self.valores["numero2"])
                self.janela["resultado"].update(f"O resultado é {self.resultado}")

app = Main()
app.Inicializar()