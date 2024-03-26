import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._lingua = None
        self._mode = None
        self._txt = None
        self._avvio = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        # row1
        self._lingua = ft.Dropdown(width=750,
                                   label="Lingua",
                                   hint_text="Scegli la lingua",
                                   options=[
                                       ft.dropdown.Option("Italian"),
                                       ft.dropdown.Option("English"),
                                       ft.dropdown.Option("Spanish")]
                                   )
        row1 = ft.Row([self._lingua])

        # row2
        self._mode = ft.Dropdown(width=150,
                                 label="Modalità",
                                 hint_text="Scegli la modalità di correzione",
                                 options=[ft.dropdown.Option("Default"),
                                          ft.dropdown.Option("Linear"),
                                          ft.dropdown.Option("Dichotomic")])

        self._txt = ft.TextField(label="Inserisci qua la frase da correggere", width=450, )

        self._avvio = ft.ElevatedButton(width=150, text="Correggi",
                                        on_click=self.__controller.checkBeforeRunning)

        row2 = ft.Row([self._mode, self._txt, self._avvio])

        self.page.add(row1, row2)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def start_checking(self, testo, lingua, mode):
        (parole_errate, tempo) = self.__controller.handleSentence(testo, lingua, mode)

        self._checked = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._checked.controls.append(ft.Text(f"Frase inserita: {self._txt}"))
        for i in range(parole_errate.lenght()):
            self._checked.controls.append(ft.Text(f"{parole_errate[i]}"))
        self._checked.controls.append(ft.Text(f"Tempo processo: {tempo}"))

        self.page.add(self._checked)
        self.page.update()
