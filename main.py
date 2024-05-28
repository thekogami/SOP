import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MemoryVisualizationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memória Virtual e Swapping")
        self.geometry("800x600")

        # Criar os frames para cada seção
        self.create_frames()

        # Desenhar os conceitos
        self.draw_memory_pagination(self.canvas1)
        self.draw_page_in_page_out(self.canvas2)
        self.draw_swapping(self.canvas3)

    def create_frames(self):
        self.frame1 = ttk.LabelFrame(self, text="Memória Virtual por Paginação", padding=(10, 10))
        self.frame1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.canvas1 = tk.Canvas(self.frame1, width=750, height=180, bg='white')
        self.canvas1.pack()

        self.frame2 = ttk.LabelFrame(self, text="Page-in Page-out", padding=(10, 10))
        self.frame2.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.canvas2 = tk.Canvas(self.frame2, width=750, height=180, bg='white')
        self.canvas2.pack()

        self.frame3 = ttk.LabelFrame(self, text="Swapping", padding=(10, 10))
        self.frame3.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.canvas3 = tk.Canvas(self.frame3, width=750, height=180, bg='white')
        self.canvas3.pack()

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def draw_memory_pagination(self, canvas):
        button1 = tk.Button(self.frame1, text='Memória Virtual por paginação', command=self.simulate_pagination_algorithm)
        button1.place(x=160, y=40, width=180, height=30)

        button2 = tk.Button(self.frame1, text='Page-in Page-out', command=self.show_message)
        button2.place(x=350, y=40, width=180, height=30)

        button3 = tk.Button(self.frame1, text='Swap-in Swap-out', command=self.show_message)
        button3.place(x=540, y=40, width=180, height=30)

        virtual_mem = [("Página 1", 50, 80), ("Página 2", 50, 120), ("Página 3", 50, 160)]
        for page, x, y in virtual_mem:
            canvas.create_rectangle(x, y, x + 80, y + 30, fill="lightblue")
            canvas.create_text(x + 40, y + 15, text=page)

        # Desenhar Tabela de Mapeamento
        self.mapping_table_coords = []
        x, y = 500, 80
        canvas.create_text(x + 50, y - 20, text="Tabela de Mapeamento", font=('Arial', 10, 'bold'))
        for _ in range(3):
            self.mapping_table_coords.append((x, y))
            y += 40

    def draw_page_in_page_out(self, canvas):
        # Desenhar Memória Física
        physical_mem = [("Moldura 1", 50, 40), ("Moldura 2", 50, 80), ("Moldura 3", 50, 120)]
        for frame, x, y in physical_mem:
            canvas.create_rectangle(x, y, x + 80, y + 30, fill="lightgreen")
            canvas.create_text(x + 40, y + 15, text=frame)

        # Desenhar Armazenamento Secundário
        secondary_storage = [("Bloco 1", 300, 40), ("Bloco 2", 300, 80), ("Bloco 3", 300, 120)]
        for block, x, y in secondary_storage:
            canvas.create_rectangle(x, y, x + 80, y + 30, fill="lightyellow")
            canvas.create_text(x + 40, y + 15, text=block)

        # Desenhar Setas de Page-in e Page-out
        canvas.create_line(130, 55, 300, 55, arrow=tk.LAST, dash=(4, 2))
        canvas.create_text(215, 35, text="Page-out", font=('Arial', 10, 'italic'))

        canvas.create_line(300, 95, 130, 95, arrow=tk.LAST, dash=(4, 2))
        canvas.create_text(215, 115, text="Page-in", font=('Arial', 10, 'italic'))

    def draw_swapping(self, canvas):
        # Desenhar Processos na Memória Principal
        processes_mem = [("Processo A", 50, 40), ("Processo B", 50, 80), ("Processo C", 50, 120)]
        for proc, x, y in processes_mem:
            canvas.create_rectangle(x, y, x + 120, y + 30, fill="lightcoral")
            canvas.create_text(x + 60, y + 15, text=proc)

        # Desenhar Processos no Disco
        processes_disk = [("Processo A", 300, 40), ("Processo B", 300, 80), ("Processo C", 300, 120)]
        for proc, x, y in processes_disk:
            canvas.create_rectangle(x, y, x + 120, y + 30, fill="lightgrey")
            canvas.create_text(x + 60, y + 15, text=proc)

        # Desenhar Setas de Swap-in e Swap-out
        canvas.create_line(170, 55, 300, 55, arrow=tk.LAST, dash=(4, 2))
        canvas.create_text(235, 35, text="Swap-out", font=('Arial', 10, 'italic'))

        canvas.create_line(300, 95, 170, 95, arrow=tk.LAST, dash=(4, 2))
        canvas.create_text(235, 115, text="Swap-in", font=('Arial', 10, 'italic'))

    def simulate_pagination_algorithm(self):
        pages = ["Página 1", "Página 2", "Página 3", "Página 4"]
        frames = ["Moldura 1", "Moldura 2", "Moldura 3"]
        page_frame_map = {}

        for i, page in enumerate(pages):
            if i < len(frames):
                page_frame_map[page] = frames[i]
            else:
                page_out = list(page_frame_map.keys())[0]
                frame_released = page_frame_map.pop(page_out)
                page_frame_map[page] = frame_released
                self.update_mapping_table(page_out, "", release=True)
                self.update_mapping_table(page, frame_released)
                self.update_page_in_page_out(page, page_out)

            self.update_mapping_table(page, page_frame_map[page])

    def update_mapping_table(self, page, frame, release=False):
        if release:
            for item in self.canvas1.find_withtag("map_table"):
                if self.canvas1.itemcget(item, 'text').startswith(page):
                    self.canvas1.delete(item)
            return

        for x, y in self.mapping_table_coords:
            if not self.canvas1.find_overlapping(x, y, x + 100, y + 30):
                self.canvas1.create_text(x, y, text=f"{page} -> {frame}", tags="map_table")
                break

    def update_page_in_page_out(self, page_in, page_out):
        self.canvas2.create_text(150, 100, text=f"{page_out} -> {page_in}", font=('Arial', 10, 'italic'))

    def show_message(self):
        messagebox.showinfo("Informação", "Função ainda não implementada!")

if __name__ == "__main__":
    app = MemoryVisualizationApp()
    app.mainloop()
