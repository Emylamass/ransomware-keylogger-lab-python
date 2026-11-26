<div align="center">

# Simulação de Malwares em Python e Estratégias de Defesa

![Python](https://img.shields.io/badge/Python-3.10%2B-2ea44f?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-2ea44f?style=for-the-badge)
![Foco](https://img.shields.io/badge/Foco-Seguran%C3%A7a%20Ofensiva%20%26%20Defensiva-1f6feb?style=for-the-badge)

*Projeto prático desenvolvido para o desafio da DIO: implementação controlada de Ransomware e Keylogger simulados em Python, com foco na análise de funcionamento e medidas de mitigação.*

</div>

---

## ⚠️ Aviso Legal e Ético

Todas as implementações e testes documentados neste repositório foram desenvolvidos **exclusivamente em ambiente controlado e isolado**, com finalidade estritamente educacional. Os conceitos aqui apresentados visam compreender mecanismos de ataque para aprimorar a detecção, a prevenção e a resposta a incidentes no mundo real. Nunca execute scripts deste tipo em sistemas ou redes sem autorização explícita.

---

## 🎯 Objetivos do Projeto

- Compreender na prática o funcionamento interno de ameaças como **Ransomware** e **Keylogger**.
- Implementar simulações controladas em **Python** utilizando bibliotecas de criptografia simétrica (`cryptography.fernet`), monitoramento de eventos (`pynput`) e envio de e-mails (`smtplib`).
- Identificar brechas técnicas e comportamentais exploradas por essas ameaças.
- Documentar estratégias de defesa, prevenção e detecção aplicáveis a ambientes reais.

---

## 📂 Estrutura do Repositório

```text
.
├── README.md
├── ransomware/
│   ├── ransomware.py
│   ├── descriptografar.py
│   └── test_files/
│       └── exemplo.txt
├── keylogger/
│   └── keylogger.py
└── images/
