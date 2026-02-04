# Calculadora Científica em Python 🧮

Projeto de **calculadora científica com interface gráfica**, desenvolvido em **Python** utilizando a biblioteca **Tkinter**.  
O foco do projeto é praticar lógica de programação, construção de interfaces gráficas, tratamento de erros e empacotamento de aplicações desktop.

---

## 📌 Funcionalidades

### Operações básicas
- Soma
- Subtração
- Multiplicação
- Divisão
- Porcentagem (%)

### Operações científicas
- Seno (sin)
- Cosseno (cos)
- Tangente (tan)
- Logaritmo (log)
- Logaritmo natural (ln)
- Raiz quadrada (√x)
- Potência (xʸ)
- Constantes matemáticas (π e e)

### Recursos adicionais
- Botão **DEL** para apagar um dígito
- Histórico de cálculos exibido na interface
- Tratamento de erros matemáticos (divisão por zero, raiz inválida, etc.)
- Interface gráfica em tema escuro
- Layout inspirado na calculadora científica do Android

---

## 🔐 Segurança
O projeto **não utiliza `eval()`** para calcular expressões matemáticas.  
As expressões são avaliadas por um **parser seguro** baseado no módulo `ast`, permitindo apenas operações matemáticas válidas e evitando execução de código arbitrário.

---

## 🛠 Tecnologias utilizadas
- **Python 3.11**
- **Tkinter** (interface gráfica)
- **ast** e **operator** (avaliação segura de expressões)
- **PyInstaller** (geração de executável para Windows)

---

## ▶️ Como executar o projeto

### Executar pelo Python
1. Certifique-se de ter Python 3.11 instalado
2. Clone o repositório
3. No terminal, execute:
```bash
python calculadora.py
