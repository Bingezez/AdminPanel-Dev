import psutil

from adminpanel.lib.utils import serialize


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size


class Ram:
    def __init__(self) -> None:
        self.used = convert_bytes(psutil.virtual_memory().used)
        self.free = convert_bytes(psutil.virtual_memory().free)
        self.total = convert_bytes(psutil.virtual_memory().total)
        self.percent = psutil.virtual_memory().percent


class Cpu:
    def __init__(self) -> None:
        self.cores = psutil.cpu_count(logical=False)
        self.logical_processors = psutil.cpu_count()
        self.percent = psutil.cpu_percent()


class Perfomance:
    @property
    def json_perfomance(self):
        ram = Ram()
        cpu = Cpu()
    
        return serialize({
            "ram": {
                "total": ram.total,
                "free": ram.free,
                "used": ram.used,
                "percent": ram.percent},
            "cpu": {
                "cores": cpu.cores,
                "logical_processors": cpu.logical_processors,
                "percent": cpu.percent}
        })


if __name__ == "__main__":
    pass
