import platform
import psutil
import datetime

class Sysinfo:

    def __init__(self):
        self.uname = platform.uname()
        self.psutil = psutil
        pass

    def getSystem(self):
        return "Betriebssystem: " + self.uname.system

    def getNodeName(self):
        return "PC Name: " + self.uname.node

    def getRelease(self):
        return "Betriebssystem Release: " + self.uname.release

    def getVersion(self):
        return "Betriebssystem Version: " + self.uname.version

    def getMachine(self):
        return "Machine: " + self.uname.machine

    def getProcessor(self):
        return "Prozessor: " + self.uname.processor

    def getBootTime(self):
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
        boot_time_string = f"Boot Time: {bt.day}.{bt.month}.{bt.year} {bt.hour}:{bt.minute}:{bt.second}"
        return boot_time_string

    def getCPUCores(self, locical):
        if locical == True:
            return "Physische Kerne: " + str(self.psutil.cpu_count(locical))
        elif(locical == False):
            return "Logische Kerne: " + str(self.psutil.cpu_count(locical))

    def getCPUFrequency(self, status):
        if status == "current":
            return "Aktuelle Frequenz: " + str(self.psutil.cpu_freq().current) + "Mhz"
        elif status == "max":
            return "Max Frequenz: " + str(self.psutil.cpu_freq().max) + "Mhz"

    def getCPUUsage(self):
        return "CPU Usage: " + str(self.psutil.cpu_percent()) + "%"

