from tkinter import *
import tkinter as tk
from tkinter import messagebox

def page_in():
    global ram_pages, storage_pages
    if len(ram_pages) < 4:  # Verifica se a estante tem menos de 4 livros
        if storage_pages:
            page = storage_pages.pop(0)
            ram_pages.append(page)
            update_canvas()
    else:
        messagebox.showinfo("Aviso", "A estante está cheia!")

def page_out():
    global ram_pages, storage_pages
    if ram_pages:
        page = ram_pages.pop(0)
        storage_pages.append(page)
        update_canvas()
    else:
        messagebox.showinfo("Aviso", "A estante está vazia!")


def update_canvas():
    canvas.delete("all")
    
    # Título e labels
    canvas.create_text(300, 30, text="Estante (Memória RAM)", font=("Arial", 16, "bold"))
    canvas.create_text(900, 30, text="Depósito (Armazenamento Secundário)", font=("Arial", 16, "bold"))
    
    # Ilustração da estante
    for i, page in enumerate(ram_pages):
        x1 = 50
        y1 = 50 + i*60
        x2 = 550
        y2 = 100 + i*60
        
        # Atribuir cores aos livros na estante
        if i == len(ram_pages) - 1:  # Último livro adicionado
            fill_color = "lightcoral"
        elif i == 0:  # Primeiro livro adicionado
            fill_color = "lightgreen"
        else:
            fill_color = "lightblue"
        
        canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
        canvas.create_text(300, 75 + i*60, text=page, font=("Arial", 12))
    
    # Ilustração do depósito
    for i, page in enumerate(storage_pages):
        canvas.create_rectangle(650, 50 + i*60, 1150, 100 + i*60, fill="lightgreen")
        canvas.create_text(900, 75 + i*60, text=page, font=("Arial", 12))
    
    # Ilustração do bibliotecário
    draw_librarian(1200, 150)
    
    # Ilustração dos alunos
    draw_student(50, 450)
    draw_super_mario(300, 450)
    
    # Setas representando o movimento dos livros
    canvas.create_line(570, 75, 630, 75, arrow=LAST, width=2)
    canvas.create_text(600, 60, text="PG-OUT", font=("Arial", 10, "bold"))
    
    canvas.create_line(630, 135, 570, 135, arrow=LAST, width=2)
    canvas.create_text(600, 150, text="PG-IN", font=("Arial", 10, "bold"))


def draw_librarian(x, y):
    # Cabeça
    canvas.create_oval(x, y, x + 70, y + 70, fill="peachpuff")
    # Corpo
    canvas.create_rectangle(x + 15, y + 70, x + 55, y + 150, fill="blue")
    
    # Braços
    if librarian_animation_state:
        canvas.create_line(x - 10, y + 75, x + 15, y + 100, width=5)
        canvas.create_line(x + 80, y + 75, x + 55, y + 100, width=5)
    else:
        canvas.create_line(x - 10, y + 85, x + 15, y + 110, width=5)
        canvas.create_line(x + 80, y + 85, x + 55, y + 110, width=5)
    
    # Pernas
    if librarian_animation_state:
        canvas.create_line(x + 25, y + 150, x + 25, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 45, y + 200, width=5)
    else:
        canvas.create_line(x + 25, y + 150, x + 30, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 40, y + 200, width=5)
    
    # Sapatos
    canvas.create_line(x + 10, y + 200, x + 30, y + 200, width=7)
    canvas.create_line(x + 40, y + 200, x + 60, y + 200, width=7)
    
    # Chapéu
    canvas.create_polygon(x + 5, y, x + 65, y, x + 35, y - 30, fill="brown")
    
    # Rosto (olhos e boca)
    canvas.create_oval(x + 20, y + 30, x + 30, y + 40, fill="black")
    canvas.create_oval(x + 40, y + 30, x + 50, y + 40, fill="black")
    canvas.create_line(x + 30, y + 50, x + 40, y + 50, fill="red", width=2)
    
    # Descrição do bibliotecário
    canvas.create_text(x + 35, y + 220, text="Bibliotecário", font=("Arial", 12, "bold"))
    canvas.create_text(x + 35, y + 240, text="(sistema operacional)", font=("Arial", 9, "italic"))

def draw_student(x, y):
    # Cabeça
    canvas.create_oval(x, y, x + 70, y + 70, fill="peachpuff")
    # Corpo
    canvas.create_rectangle(x + 15, y + 70, x + 55, y + 150, fill="green")
    
    # Braços
    if student_animation_state:
        canvas.create_line(x - 10, y + 75, x + 15, y + 100, width=5)
        canvas.create_line(x + 80, y + 75, x + 55, y + 100, width=5)
    else:
        canvas.create_line(x - 10, y + 85, x + 15, y + 110, width=5)
        canvas.create_line(x + 80, y + 85, x + 55, y + 110, width=5)
    
    # Pernas
    if student_animation_state:
        canvas.create_line(x + 25, y + 150, x + 25, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 45, y + 200, width=5)
    else:
        canvas.create_line(x + 25, y + 150, x + 30, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 40, y + 200, width=5)
    
    # Sapatos
    canvas.create_line(x + 10, y + 200, x + 30, y + 200, width=7)
    canvas.create_line(x + 40, y + 200, x + 60, y + 200, width=7)
    
    # Chapéu
    canvas.create_polygon(x + 5, y, x + 65, y, x + 35, y - 30, fill="red")
    
    # Rosto (olhos e boca)
    canvas.create_oval(x + 20, y + 30, x + 30, y + 40, fill="black")
    canvas.create_oval(x + 40, y + 30, x + 50, y + 40, fill="black")
    canvas.create_line(x + 30, y + 50, x + 40, y + 50, fill="red", width=2)
    
    # Descrição do aluno
    canvas.create_text(x + 35, y + 220, text="Aluno", font=("Arial", 12, "bold"))

def draw_super_mario(x, y):
    # Cabeça
    canvas.create_oval(x, y, x + 70, y + 70, fill="peachpuff")
    # Chapéu
    canvas.create_polygon(x + 10, y + 5, x + 60, y + 5, x + 35, y - 20, fill="red")
    canvas.create_text(x + 35, y - 10, text="M", font=("Arial", 10, "bold"), fill="white")
    
    # Corpo
    canvas.create_rectangle(x + 15, y + 70, x + 55, y + 150, fill="blue")
    # Botões do macacão
    canvas.create_oval(x + 20, y + 100, x + 30, y + 110, fill="yellow")
    canvas.create_oval(x + 40, y + 100, x + 50, y + 110, fill="yellow")
    
    # Braços
    if mario_animation_state:
        canvas.create_line(x - 10, y + 75, x + 15, y + 100, width=5)
        canvas.create_line(x + 80, y + 75, x + 55, y + 100, width=5)
    else:
        canvas.create_line(x - 10, y + 85, x + 15, y + 110, width=5)
        canvas.create_line(x + 80, y + 85, x + 55, y + 110, width=5)
    
    # Pernas
    if mario_animation_state:
        canvas.create_line(x + 25, y + 150, x + 25, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 45, y + 200, width=5)
    else:
        canvas.create_line(x + 25, y + 150, x + 30, y + 200, width=5)
        canvas.create_line(x + 45, y + 150, x + 40, y + 200, width=5)
    
    # Sapatos
    canvas.create_line(x + 10, y + 200, x + 30, y + 200, width=7)
    canvas.create_line(x + 40, y + 200, x + 60, y + 200, width=7)
    
    # Rosto (olhos, nariz e boca)
    canvas.create_oval(x + 20, y + 30, x + 30, y + 40, fill="black")
    canvas.create_oval(x + 40, y + 30, x + 50, y + 40, fill="black")
    canvas.create_oval(x + 30, y + 40, x + 40, y + 50, fill="orange")
    canvas.create_line(x + 25, y + 50, x + 45, y + 50, fill="red", width=2)
    
    # Descrição do Super Mario
    canvas.create_text(x + 35, y + 220, text="Super Mario", font=("Arial", 12, "bold"))

def animate():
    global librarian_animation_state, student_animation_state, mario_animation_state
    librarian_animation_state = not librarian_animation_state
    student_animation_state = not student_animation_state
    mario_animation_state = not mario_animation_state
    update_canvas()
    root.after(500, animate)

# Lista de páginas na memória RAM e no armazenamento secundário
ram_pages = ["Livro 1", "Livro 2", "Livro 3", "Livro 4"]
storage_pages = ["Livro 5", "Livro 6"]

# Configuração da janela principal
root = Tk()
root.title("Simulação de Biblioteca")

# Canvas para desenho
canvas = Canvas(root, width=1300, height=800)
canvas.pack()

# Botões para Page-In e Page-Out
button_in = tk.Button(root, text="PG-IN", command=page_in, width=10, bg="lightblue")
button_in.place(relx=0.3, rely=1.0, y=-50)

button_out = tk.Button(root, text="PG-OUT", command=page_out, width=10, bg="lightgreen")
button_out.place(relx=0.7, rely=1.0, y=-55)

# Estados de animação
librarian_animation_state = False
student_animation_state = False
mario_animation_state = False

# Atualização inicial do canvas
update_canvas()

# Iniciar animação
root.after(500, animate)

# Loop principal da interface
root.mainloop()
