import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

# Função para gerar o QR code
def gerar_qr():
    github_profile = entry_url.get()

    if github_profile:
        # Gera o QR code para o URL inserido
        qr = qrcode.make(github_profile)

        # Converte a imagem para BytesIO para não salvar localmente
        img_buffer = BytesIO()
        qr.save(img_buffer, format="PNG")
        img_buffer.seek(0)  # Volta para o início do buffer

        # Carrega e exibe a imagem na interface
        img = Image.open(img_buffer)
        img = img.resize((200, 200))  # Redimensiona a imagem para caber na interface
        img_tk = ImageTk.PhotoImage(img)

        # Atualiza o rótulo com a imagem gerada
        label_img.config(image=img_tk)
        label_img.image = img_tk  # Necessário para evitar que a imagem seja deletada pelo garbage collector

        messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, insira a URL do perfil do GitHub.")

# Cria a janela principal
root = tk.Tk()
root.title("Gerador de QR Code para qualquer link")
root.geometry("400x400")

# Texto explicativo
label_explicativo = tk.Label(root, text="Insira a URL para gerar o QR code:")
label_explicativo.pack(pady=10)

# Campo de entrada de texto para a URL
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=10)

# Botão para gerar o QR code
btn_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qr)
btn_gerar.pack(pady=10)

# Rótulo para exibir o QR code gerado
label_img = tk.Label(root)
label_img.pack(pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()