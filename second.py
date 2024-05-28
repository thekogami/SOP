import time

class MemoryVisualizationApp:
    def __init__(self):
        self.virtual_memory = ["Página 1", "Página 2", "Página 3", "Página 4"]
        self.frames = ["Moldura 1", "Moldura 2", "Moldura 3"]
        self.page_frame_map = {}
        self.mapping_table = [""] * len(self.frames)

    def draw_memory_pagination(self):
        print("\nMemória Virtual por Paginação:")
        print("Virtual Memory:")
        for page in self.virtual_memory:
            print(f"| {page} |", end=" ")
        print("\n" + "-" * 50)
        print("Physical Memory (Frames):")
        for frame in self.frames:
            print(f"| {frame} |", end=" ")
        print("\n" + "-" * 50)

    def draw_mapping_table(self):
        print("\nTabela de Mapeamento:")
        for entry in self.mapping_table:
            if entry:
                print(entry)
            else:
                print("| Empty |")

    def update_mapping_table(self, page, frame, release=False):
        if release:
            for i in range(len(self.mapping_table)):
                if self.mapping_table[i].startswith(page):
                    self.mapping_table[i] = ""
                    break
        else:
            for i in range(len(self.mapping_table)):
                if not self.mapping_table[i]:
                    self.mapping_table[i] = f"| {page} -> {frame} |"
                    break

    def simulate_pagination_algorithm(self):
        self.draw_memory_pagination()
        for i, page in enumerate(self.virtual_memory):
            print("\nInserindo:", page)
            if i < len(self.frames):
                self.page_frame_map[page] = self.frames[i]
            else:
                page_out = list(self.page_frame_map.keys())[0]
                frame_released = self.page_frame_map.pop(page_out)
                self.page_frame_map[page] = frame_released
                self.update_mapping_table(page_out, "", release=True)
                print(f"Page-out: {page_out}")
                time.sleep(1)
                self.update_mapping_table(page, frame_released)
                print(f"Page-in: {page}")
                time.sleep(1)

            self.update_mapping_table(page, self.page_frame_map[page])
            self.draw_memory_pagination()
            self.draw_mapping_table()
            time.sleep(1)

    def show_message(self):
        print("Função ainda não implementada!")

if __name__ == "__main__":
    app = MemoryVisualizationApp()
    app.simulate_pagination_algorithm()
