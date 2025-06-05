import tkinter as tk
from tkinter import ttk, messagebox

class ConversorBinarioDecimal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor Binário-Decimal")
        self.geometry("400x300")
        self.configure(padx=20, pady=20)
        
        self.criar_componentes()
        
    def criar_componentes(self):
        titulo_label = ttk.Label(self, text="Conversor Binário-Decimal", font=("Arial", 16))
        titulo_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        quadro_entrada = ttk.LabelFrame(self, text="Entrada")
        quadro_entrada.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        
        self.tipo_conversao = tk.StringVar(value="bin_para_dec")
        ttk.Radiobutton(quadro_entrada, text="Binário para Decimal", 
                        variable=self.tipo_conversao, value="bin_para_dec").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(quadro_entrada, text="Decimal para Binário", 
                        variable=self.tipo_conversao, value="dec_para_bin").grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(quadro_entrada, text="Digite o valor:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entrada_valor = ttk.Entry(quadro_entrada, width=20)
        self.entrada_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        botao_converter = ttk.Button(self, text="Converter", command=self.converter)
        botao_converter.grid(row=2, column=0, columnspan=3, pady=10)
        
        quadro_resultado = ttk.LabelFrame(self, text="Resultado")
        quadro_resultado.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        
        self.resultado_var = tk.StringVar(value="")
        resultado_label = ttk.Label(quadro_resultado, textvariable=self.resultado_var, font=("Arial", 12))
        resultado_label.grid(row=0, column=0, padx=10, pady=10)
        
    def converter(self):
        valor_entrada = self.entrada_valor.get().strip()
        
        if not valor_entrada:
            messagebox.showerror("Erro", "Por favor, digite um valor.")
            return
        
        tipo = self.tipo_conversao.get()
        
        try:
            if tipo == "bin_para_dec":
                if not all(bit in '01' for bit in valor_entrada):
                    raise ValueError("Números binários só podem conter 0 ou 1.")
                
                valor_decimal = int(valor_entrada, 2)
                self.resultado_var.set(f"Decimal: {valor_decimal}")
                
            else:
                valor_decimal = int(valor_entrada)
                if valor_decimal < 0:
                    raise ValueError("Por favor, insira um número positivo.")
                
                valor_binario = bin(valor_decimal)[2:]
                self.resultado_var.set(f"Binário: {valor_binario}")
                
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

if __name__ == "__main__":
    app = ConversorBinarioDecimal()
    app.mainloop()
