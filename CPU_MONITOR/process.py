import psutil as pt 

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical = False)
        self.cpu_count_logical = pt.cpu_count()
    
    def cpu_percent_return(self):
        return pt.cpu_percent(percpu = True)

    def cpu_one_return(self):
        return pt.cpu_percent()

    def ram_usage(self):
        return pt.virtual_memory()
