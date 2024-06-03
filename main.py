import tkinter as tk

# Definir cores
cor_memoria_principal = "lightblue"
cor_memoria_secundaria = "gray"
cor_pagina_carregada = "green"
cor_pagina_descarregada = "white"

# Definir tamanho da tela
largura = 800
altura = 600

# Criar janela principal
janela = tk.Tk()
janela.title("Animação Page-in Page-out")
janela.geometry(f"{largura}x{altura}")

# Criar frames para memória principal e secundária
frame_memoria_principal = tk.Frame(janela, bg=cor_memoria_principal, width=largura // 2, height=altura)
frame_memoria_principal.pack_propagate(0)
frame_memoria_secundaria = tk.Frame(janela, bg=cor_memoria_secundaria, width=largura // 2, height=altura)
frame_memoria_secundaria.pack_propagate(0)

# Função para criar e posicionar páginas
def criar_pagina(frame, cor, texto, x, y):
    pagina = tk.Frame(frame, bg=cor, width=100, height=50)
    pagina.pack_propagate(0)
    pagina.place(x=x, y=y)
    label = tk.Label(pagina, text=texto, font=("Arial", 12))
    label.pack()
    return pagina

# Criar páginas de exemplo
pagina_1 = criar_pagina(frame_memoria_principal, cor_pagina_carregada, "Página 1", 20, 20)
pagina_2 = criar_pagina(frame_memoria_principal, cor_pagina_carregada, "Página 2", 150, 20)
pagina_3 = criar_pagina(frame_memoria_secundaria, cor_pagina_descarregada, "Página 3", 20, 150)
pagina_4 = criar_pagina(frame_memoria_secundaria, cor_pagina_descarregada, "Página 4", 150, 150)

# Função para simular Page-in
def page_in(pagina_origem, pagina_destino):
    # Mover página da memória secundária para a principal
    pagina_destino.place(x=pagina_origem.winfo_x(), y=pagina_origem.winfo_y())
    pagina_origem.config(bg=cor_pagina_descarregada)
    pagina_destino.config(bg=cor_pagina_carregada)

# Função para simular Page-out
def page_out(pagina_origem, pagina_destino):
    # Mover página da memória principal para a secundária
    pagina_destino.place(x=pagina_origem.winfo_x(), y=pagina_origem.winfo_y())
    pagina_origem.config(bg=cor_pagina_carregada)
    pagina_destino.config(bg=cor_pagina_descarregada)

# Função para simular o processo de page-in e page-out
def simular():
    page_in(pagina_3, pagina_1)  # Carregar Página 3 na Memória Principal
    janela.after(1000, lambda: page_out(pagina_2, pagina_4))  # Descarregar Página 2 para a Memória Secundária
    janela.after(2000, lambda: page_in(pagina_4, pagina_2))  # Carregar Página 4 na Memória Principal
    janela.after(3000, lambda: page_out(pagina_1, pagina_3))  # Descarregar Página 1 para a Memória Secundária

# Posicionar frames de memória
frame_memoria_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame_memoria_secundaria.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Simular o processo de page-in e page-out
janela.after(1000, simular)

# Executar janela principal
janela.mainloop()
