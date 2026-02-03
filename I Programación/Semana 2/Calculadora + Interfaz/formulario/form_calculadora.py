import tkinter as tk
from tkinter import font
from util import util_ventana
from config import constantes as cons


class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.historial = []
        self.sidebar_visible = False
        self.sidebar_width = 260
        self.sidebar = None

        self.construir_botones()
        self.configurar_grid()
        self.config_window()
        self.construir_widget()
        self.construir_menu_hamburguesa()

    # ---------------- VENTANA ----------------
    def config_window(self):
        self.title('Python GUI Calculadora')
        self.resizable(True, True)
        self.configure(bg=cons.COLOR_DE_FONDO_DARK)
        self.attributes('-alpha', 0.96)

        w, h = 370, 570
        util_ventana.centrar_ventana(self, w, h)

    # ---------------- GRID ----------------
    def configurar_grid(self):
        for col in range(5):
            self.columnconfigure(col, weight=1)

        for row in range(8):
            self.rowconfigure(row, weight=1)

    # ---------------- PANTALLA ----------------
    def construir_widget(self):
        self.operation_label = tk.Label(
            self,
            text="",
            anchor="e",
            bg=cons.COLOR_DE_FONDO_DARK,
            fg=cons.COLOR_DE_TEXTO_DARK,
            font=("Arial", 12)
        )
        self.operation_label.grid(
            row=0, column=0, columnspan=4,
            sticky="nsew", padx=10
        )

        self.entry = tk.Entry(
            self,
            font=("Arial", 26),
            justify="right",
            bg=cons.COLOR_CAJA_TEXTO_DARK,
            fg=cons.COLOR_DE_TEXTO_DARK,
            bd=0,
            insertbackground=cons.COLOR_DE_TEXTO_DARK
        )
        self.entry.grid(
            row=1, column=0, columnspan=4,
            sticky="nsew", padx=10, pady=5
        )

    # ---------------- BOTONES ----------------
    def construir_botones(self):
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val, col_val = 2, 0
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                bg = cons.COLOR_BOTONES_ESPECIALES_DARK
                btn_font = font.Font(size=16, weight='bold')
            else:
                bg = cons.COLOR_BOTONES_DARK
                btn_font = roboto_font

            tk.Button(
                self,
                text=button,
                command=lambda b=button: self.on_button_click(b),
                bg=bg,
                fg=cons.COLOR_DE_TEXTO_DARK,
                relief=tk.FLAT,
                font=btn_font,
                bd=0,
                activebackground=cons.COLOR_BOTONES_ESPECIALES_DARK
            ).grid(
                row=row_val,
                column=col_val,
                columnspan=2 if button == '=' else 1,
                padx=5,
                pady=5,
                sticky="nsew"
            )

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    # ---------------- LÓGICA ----------------
    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)

                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))

                operation = f"{expression} = {result}"
                self.operation_label.config(text=operation)
                self.historial.append(operation)

            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")

        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")

        elif value == '<':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current[:-1])

        else:
            self.entry.insert(tk.END, value)

    # ---------------- MENÚ HAMBURGUESA ----------------
    def construir_menu_hamburguesa(self):
        self.menu_button = tk.Button(
            self,
            text="☰",
            font=("Arial", 20, "bold"),
            bg=cons.COLOR_BOTONES_DARK,
            fg=cons.COLOR_DE_TEXTO_DARK,
            bd=0,
            activebackground=cons.COLOR_BOTONES_ESPECIALES_DARK,
            command=self.mostrar_historial
        )
        self.menu_button.grid(
            row=0, column=4,
            sticky="ne", padx=8, pady=5
        )

    def mostrar_historial(self):
        if self.sidebar_visible:
            self.ocultar_sidebar()
        else:
            self.mostrar_sidebar()
    
    def mostrar_sidebar(self):
        self.sidebar_visible = True

        x = self.winfo_x() + self.winfo_width()
        y = self.winfo_y()
        h = self.winfo_height()

        self.sidebar = tk.Toplevel(self)
        self.sidebar.overrideredirect(True)
        self.sidebar.configure(bg=cons.COLOR_SIDEBAR_DARK)
        self.sidebar.geometry(f"{self.sidebar_width}x{h}+{x}+{y}")

        lista = tk.Listbox(
            self.sidebar,
            font=("Arial", 12),
            bg=cons.COLOR_SIDEBAR_DARK,
            fg=cons.COLOR_DE_TEXTO_DARK,
            bd=0,
            highlightthickness=0,
            selectbackground=cons.COLOR_BOTONES_ESPECIALES_DARK
        )
        lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for item in self.historial:
            lista.insert(tk.END, item)

        self.animar_sidebar(-self.sidebar_width)


    def ocultar_sidebar(self):
        if self.sidebar:
            self.animar_sidebar(0)


    def animar_sidebar(self, target_x):
        step = 20

        x = self.sidebar.winfo_x()
        y = self.sidebar.winfo_y()

        destino = self.winfo_x() + self.winfo_width() + target_x

        if (target_x < 0 and x > destino) or (target_x == 0 and x < destino):
            x += -step if target_x < 0 else step
            self.sidebar.geometry(f"+{x}+{y}")
            self.after(10, lambda: self.animar_sidebar(target_x))
        else:
            if target_x == 0:
                self.sidebar.destroy()
                self.sidebar = None
                self.sidebar_visible = False


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    app = FormularioCalculadora()
    app.mainloop()
