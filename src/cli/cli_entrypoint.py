from time import sleep
from ..monitors.cpu_monitor import CpuMonitor

from blessed import Terminal

class Cli:
    def __init__(self) -> None:
        self.terminal = Terminal()
        self.monitor = CpuMonitor()
        self.monitor.install_new_values_callback(self._new_values)


    def run(self):
        with self.terminal.hidden_cursor():
            self.monitor.start()
            while True:
                sleep(10)


    def _new_values(self, graph_values, last_readable_value):
        print(self.terminal.clear)
        print("Monitorets CLI mode")
        print("")
        print(f"CPU: {last_readable_value}")
        print("")
        print("Press q to quit")
