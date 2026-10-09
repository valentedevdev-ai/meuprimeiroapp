from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MeuApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        titulo = Label(
            text="Meu Primeiro Aplicativo",
            font_size=28
        )

        self.nome = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            font_size=20
        )

        botao = Button(
            text="Entrar",
            font_size=20
        )

        self.mensagem = Label(
            text="",
            font_size=22
        )

        botao.bind(on_press=self.entrar)

        layout.add_widget(titulo)
        layout.add_widget(self.nome)
        layout.add_widget(botao)
        layout.add_widget(self.mensagem)

        return layout

    def entrar(self, instance):
        nome = self.nome.text

        if nome:
            self.mensagem.text = f"Olá, {nome}! 👋"
        else:
            self.mensagem.text = "Digite seu nome."


MeuApp().run()