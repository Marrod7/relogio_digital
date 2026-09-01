import time
import tkinter as tk

def atualizar_relogio():
    hora_atual = time.strftime("%H:%M:%S")
    label_relogio.config(text=hora_atual)
    label_relogio.after(1000, atualizar_relogio)

janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("350x150")
janela.configure(bg="black")
janela.resizable(False, False)

label_relogio = tk.Label(
    janela,
    font=("Roboto", 48, "bold"),
    fg="white",
    bg="black"
)

label_relogio.pack(expand=True)

atualizar_relogio()
janela.mainloop()

