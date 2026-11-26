import os
from cryptography.fernet import Fernet


def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()


def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados = f.decrypt(dados_encriptados)

    with open(arquivo, "wb") as file:
        file.write(dados)


def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome not in {"ransomware.py", "descriptografar.py", "chave.key", "Leia isso.txt"} and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Arquivos em 'test_files' restaurados com sucesso!")


if __name__ == "__main__":
    main()