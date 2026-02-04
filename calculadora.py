import tkinter as tk
import math
import ast
import operator

# ================= CONFIGURAÇÕES =================
BG = "#121212"
BTN = "#2A2A2A"
BTN_SCI = "#1F1F1F"
TXT = "#EAEAEA"
EQUAL = "#FF9800"

root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("420x620")
root.resizable(False, False)
root.configure(bg=BG)

# ================= VISOR =================
entrada = tk.Entry(
    root,
    font=("Arial", 24),
    bg=BG,
    fg=TXT,
    bd=0,
    justify="right",
    insertbackground=TXT
)
entrada.grid(row=0, column=0, columnspan=5, padx=15, pady=(20, 5), sticky="we")

# ================= HISTÓRICO =================
historico = []

lista_historico = tk.Listbox(
    root,
    bg="#1C1C1C",
    fg=TXT,
    font=("Arial", 10),
    height=6
)
lista_historico.grid(row=1, column=0, columnspan=5, padx=15, pady=5, sticky="we")

# ================= PARSER SEGURO =================
OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def avaliar(expressao):
    def _avaliar(no):
        if isinstance(no, ast.Num):
            return no.n
        elif isinstance(no, ast.BinOp):
            return OPERADORES[type(no.op)](
                _avaliar(no.left),
                _avaliar(no.right)
            )
        elif isinstance(no, ast.UnaryOp):
            return OPERADORES[type(no.op)](_avaliar(no.operand))
        else:
            raise ValueError("Expressão inválida")

    arvore = ast.parse(expressao, mode="eval")
    return _avaliar(arvore.body)

# ================= FUNÇÕES =================
def inserir(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def apagar():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto[:-1])

def calcular():
    try:
        expr = entrada.get()
        if not expr:
            return

        expr_tratada = expr.replace("×", "*").replace("÷", "/").replace("%", "/100")
        resultado = avaliar(expr_tratada)

        historico.append(f"{expr} = {resultado}")
        lista_historico.insert(tk.END, historico[-1])

        limpar()
        entrada.insert(0, resultado)

    except ZeroDivisionError:
        limpar()
        entrada.insert(0, "Erro: divisão por zero")
    except ValueError:
        limpar()
        entrada.insert(0, "Erro: expressão inválida")
    except:
        limpar()
        entrada.insert(0, "Erro")

def cientifica(func):
    try:
        x = float(entrada.get())
        if func == "sin": r = math.sin(math.radians(x))
        elif func == "cos": r = math.cos(math.radians(x))
        elif func == "tan": r = math.tan(math.radians(x))
        elif func == "sqrt":
            if x < 0:
                raise ValueError
            r = math.sqrt(x)
        elif func == "log":
            if x <= 0:
                raise ValueError
            r = math.log10(x)
        elif func == "ln":
            if x <= 0:
                raise ValueError
            r = math.log(x)

        historico.append(f"{func}({x}) = {r}")
        lista_historico.insert(tk.END, historico[-1])

        limpar()
        entrada.insert(0, r)

    except ValueError:
        limpar()
        entrada.insert(0, "Erro matemático")

# ================= FRAME CIENTÍFICO =================
frame_sci = tk.Frame(root, bg=BG)
frame_sci.grid(row=2, column=0, columnspan=5, pady=5)

cientificos = [
    ("sin", lambda: cientifica("sin")),
    ("cos", lambda: cientifica("cos")),
    ("tan", lambda: cientifica("tan")),
    ("xʸ",  lambda: inserir("**")),
    ("ln",  lambda: cientifica("ln")),
    ("log", lambda: cientifica("log")),
    ("√x",  lambda: cientifica("sqrt")),
    ("π",   lambda: inserir(str(math.pi))),
    ("e",   lambda: inserir(str(math.e))),
    ("%",   lambda: inserir("%")),
]

for i, (txt, cmd) in enumerate(cientificos):
    tk.Button(
        frame_sci,
        text=txt,
        command=cmd,
        bg=BTN_SCI,
        fg=TXT,
        font=("Arial", 11),
        width=5,
        height=2,
        bd=0
    ).grid(row=i//5, column=i%5, padx=4, pady=4)

# ================= FRAME NUMÉRICO =================
frame_num = tk.Frame(root, bg=BG)
frame_num.grid(row=3, column=0, columnspan=5, pady=10)

botoes = [
    ("7", "8", "9", "÷", "DEL"),
    ("4", "5", "6", "×", "("),
    ("1", "2", "3", "-", ")"),
    ("0", ".", "C", "+", "="),
]

for r, linha in enumerate(botoes):
    for c, txt in enumerate(linha):
        if txt == "C":
            cmd = limpar
        elif txt == "DEL":
            cmd = apagar
        elif txt == "=":
            cmd = calcular
        else:
            cmd = lambda t=txt: inserir(t)

        cor = EQUAL if txt == "=" else BTN

        tk.Button(
            frame_num,
            text=txt,
            command=cmd,
            bg=cor,
            fg="black" if txt == "=" else TXT,
            font=("Arial", 15),
            width=5,
            height=2,
            bd=0
        ).grid(row=r, column=c, padx=4, pady=4)

# ================= INICIAR =================
root.mainloop()