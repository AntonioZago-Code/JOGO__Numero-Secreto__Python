import customtkinter as ctk

class Game(ctk.CTk):

    def __init__(self):
        super().__init__()

        self._set_appearance_mode("System")
        self.resizable(width=False, height=False)
        self.geometry("600x500")
        self.title("Número Secreto: O Jogo")


        self.header()
        self.main()
        self.footer()


    def header(self):

        self.titulo = ctk.CTkLabel(self, text="Número Secreto: O Jogo", text_color="#00f", font=('Arial bold', 32))
        self.titulo.pack(pady=15)

        self.descricao = ctk.CTkLabel(self, text="Será que você consegue acertar o número secreto com apenas 10 tentativas? Para poder ajudar lhe daremos uma dica ao clicar na lampada (Disponivel apenas uma vez por rodada e somente até a tentativa 5)", wraplength=500, text_color="#0ff", font=('Arial', 16))
        self.descricao.pack(pady=5)


    def main(self):

        self.input_area = ctk.CTkFrame(self, width=550, height=100, fg_color="transparent")
        self.input_area.pack(pady=5)

        self.label = ctk.CTkLabel(self.input_area, text="Digite seu palpite abaixo:", font=('Arial', 24))
        self.label.grid(row=0, column=0, columnspan=2, pady=15)

        self.user_number = ctk.CTkEntry(self.input_area, font=('Arial', 24), width=100, height=50, justify="center")
        self.user_number.grid(row=1, column=0, padx=10, pady=5)

        self.btn_enviar_palpite = ctk.CTkButton(self.input_area, text="Enviar Palpite", height=50, font=('Arial', 16))
        self.btn_enviar_palpite.grid(row=1, column=1, padx=10, pady=5) # Ao lado do self.user_number

        self.display_tentativas = ctk.CTkLabel(self.input_area, text="Tentativa restantes: 10", font=('Arial', 16))
        self.display_tentativas.grid(row=2, column=0, columnspan=2, pady=15)


    def footer(self):

        self.alerts_area = ctk.CTkFrame(self, width=550, height=150, fg_color="#333")
        self.alerts_area.pack(padx=0, pady=0)



if __name__ == "__main__":

    game = Game()
    game.mainloop()
