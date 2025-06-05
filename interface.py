import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import socket
import os

# ---------- Configurações ----------
TCP_IP = '127.0.0.1'  # Coloque aqui o IP da Raspberry se for remoto
TCP_PORT = 8080
LOG_FILE = 'automonitor.log'  # Caminho do log, pode ser absoluto

# ---------- Comunicação TCP ----------
def send_tcp_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((TCP_IP, TCP_PORT))
            s.sendall(command.encode())
            return True
    except Exception as e:
        messagebox.showerror("Erro de conexão", f"Falha ao enviar comando TCP:\n{e}")
        return False

# ---------- Ações dos botões ----------
def verificar_status():
    messagebox.showinfo("🌿 Status", "Sistema funcionando normalmente!")

def ativar_rega():
    if send_tcp_command("activate"):
        messagebox.showinfo("💧 Rega", "Comando de ativação enviado com sucesso!")

def exibir_logs():
    if not os.path.exists(LOG_FILE):
        messagebox.showwarning("📜 Logs", "Arquivo de log não encontrado.")
        return

    with open(LOG_FILE, 'r') as f:
        conteudo = f.read()

    log_window = tk.Toplevel()
    log_window.title("📜 Logs do Sistema")
    log_window.configure(bg='#f0f0f0')
    log_window.geometry("700x500")

    text_area = scrolledtext.ScrolledText(log_window, wrap=tk.WORD, font=('Consolas', 11))
    text_area.insert(tk.END, conteudo)
    text_area.pack(expand=True, fill='both')
    text_area.config(state='disabled')

# ---------- Criando Interface ----------
def criar_interface():
    root = tk.Tk()
    root.title("🌿 Sistema de Monitoramento de Plantas")
    root.geometry("450x500")
    root.configure(bg="#e6f2e6")  # Fundo verde-claro
    root.resizable(False, False)

    # Estilo moderno
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TButton",
                    font=("Segoe UI", 14, "bold"),
                    padding=10,
                    foreground="#ffffff",
                    background="#4CAF50")
    style.map("TButton",
              foreground=[('active', '#ffffff')],
              background=[('active', '#45a049')])

    # Título
    title = tk.Label(root,
                     text="🌱 Sistema de Irrigação Inteligente",
                     font=("Segoe UI", 18, "bold"),
                     bg="#e6f2e6",
                     fg="#2e7d32")
    title.pack(pady=30)

    # Botões
    btn_verificar = ttk.Button(root, text="✅ Verificar Status", command=verificar_status)
    btn_verificar.pack(pady=15, ipadx=10, ipady=5)

    btn_regar = ttk.Button(root, text="💧 Ativar Rega", command=ativar_rega)
    btn_regar.pack(pady=15, ipadx=10, ipady=5)

    btn_logs = ttk.Button(root, text="📜 Ver Logs", command=exibir_logs)
    btn_logs.pack(pady=15, ipadx=10, ipady=5)

    # Rodapé
    footer = tk.Label(root,
                      text="🌿 Projeto de Engenharia - v1.0",
                      font=("Segoe UI", 10),
                      bg="#e6f2e6",
                      fg="gray")
    footer.pack(side="bottom", pady=20)

    root.mainloop()

# ---------- Execução ----------
if __name__ == "__main__":
    criar_interface()
