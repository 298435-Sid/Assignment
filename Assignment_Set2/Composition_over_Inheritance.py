class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self, cpu_model, ram_size):
        self.cpu = CPU(cpu_model)   
        self.ram = RAM(ram_size)    

    def display_specs(self):
        print(f"Computer with {self.cpu.model} CPU and {self.ram.size} RAM.")

my_comp = Computer("Intel i7", "16GB")
my_comp.display_specs()