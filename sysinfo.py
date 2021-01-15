import platform
import psutil
import datetime
import GPUtil
import clr

class Sysinfo:

    def __init__(self):
        self.uname = platform.uname()
        self.psutil = psutil
        self.virtual_memory = psutil.virtual_memory()
        self.swap = psutil.swap_memory()
        self.disks = psutil.disk_partitions()
        self.disk_io = psutil.disk_io_counters()
        self.gpus = GPUtil.getGPUs()
        self.net_address = psutil.net_if_addrs()
        self.net_io = psutil.net_io_counters()

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

    def getCPUTemperature(self):
        import os
        from time import sleep
        res = os.popen("vcgencmd measure_temp").readline()
        temp = (res.replace("temp=", "").replace("'C\n", ""))
        print("Die CPU-Temperatur liegt bei {0}°C.".format(temp))

    def getSingleWorkloadOfCPUs(self, percpu, interval):
        cpus = self.psutil.cpu_percent(percpu=percpu, interval=interval)
        cores = ''
        i = 1
        max_cpus = len(cpus)
        for cpu in cpus:
            if i == max_cpus:
                core_string = "Core " + str(i) + ": " + str(cpu)
            else:
                core_string = "Core " + str(i) + ": " + str(cpu) + "%\n"
            cores += core_string
            i += 1
        return cores

    def getTotalRAM(self):
        return "Totaler RAM: " + str(self.adjustSize(self.virtual_memory.total))

    def getAvailableRAM(self):
        return "Verfügbarer RAM: " + str(self.adjustSize(self.virtual_memory.available))

    def getUsedRAM(self):
        return "Benutzer RAM: " + str(self.adjustSize(self.virtual_memory.used))

    def getRAMWorkloadPrecent(self):
        return "Prozent: " + str(self.virtual_memory.percent) + "%"

    def getTotalSWAP(self):
        return "Total SWAP: " + str(self.adjustSize(self.swap.total))

    def getAvailableSWAP(self):
        return "Total SWAP: " + str(self.adjustSize(self.swap.free))

    def getUsedSWAP(self):
        return "Benutzer SWAP: " + str(self.adjustSize(self.swap.used))

    def getSWAPWorkloadPrecent(self):
        return "Prozent: " + str(self.swap.percent) + "%"

    def getDiskInformations(self):
        disks_informations = ""
        max_disks = len(self.disks)
        i = 1
        for disk in self.disks:
            disk_information = "Laufwerk: " + str(disk.device) + "\n"
            disk_information += "\tMountpoint: " + str(disk.mountpoint) + "\n"
            disk_information += "\tDateisystem: " + str(disk.fstype) + "\n"
            try:
                partition_usage = psutil.disk_usage(disk.mountpoint)
            except PermissionError:
                continue
            disk_information += "\t Speicherplatz Total: " + str(self.adjustSize(partition_usage.total)) + "\n"
            disk_information += "\t Speicherplatz Benutzt: " + str(self.adjustSize(partition_usage.used)) + "\n"
            disk_information += "\t Speicherplatz Frei: " + str(self.adjustSize(partition_usage.free)) + "\n"
            if i == max_disks:
                disk_information += "\t Speicherplatz Prozent: " + str(partition_usage.percent) + "%"
            else:
                disk_information += "\t Speicherplatz Prozent: " + str(partition_usage.percent) + "%\n"
            i += 1
            disks_informations += disk_information
        return disks_informations

    def getDiskIORead(self):
        return "Gelesen seit reboot:" + str(self.adjustSize(self.disk_io.read_bytes))

    def getDiskIOWrite(self):
        return "Geschrieben seit reboot:" + str(self.adjustSize(self.disk_io.write_bytes))

    def getGPUInformations(self):
        gpus_informations = ""
        for gpu in self.gpus:
            gpu_information = ""
            # print(gpu.name)
            gpu_information += "GPU Name: " + str(gpu.name) + "\n"
            gpu_information += "\tGPU Load: " + str(gpu.load + 100) + "\n"
            gpu_information += "\tTotaler GPU Speicher: " + str(gpu.memoryTotal) + "\n"
            gpu_information += "\tBenutzer GPU Speicher: " + str(gpu.memoryUsed) + "\n"
            gpu_information += "\tFreier GPU Speicher: " + str(gpu.memoryFree) + "\n"
            gpu_information += "\tGPU Temperatur: " + str(gpu.temperature) + "\n"
            gpus_informations += gpu_information
        return gpus_informations

    def getNetworkInformations(self):
        net_informations = ""
        for interface_name, interface_addresses in self.net_address.items():
            net_informations += "Interface: " + str(interface_name) + "\n"
            for address in interface_addresses:
                if str(address.family) == "AddressFamily.AF_INET6":
                    net_informations += "\tIP Adresse: " + str(address.address) + "\n"
                    net_informations += "\tIP Netmask: " + str(address.netmask) + "\n"
                    net_informations += "\tIP Broadcast IP: " + str(address.broadcast) + "\n"
                elif str(address.family) == "AddressFamily.AF_PACKET":
                    net_informations += "\t MAC Address: " + str(address.address) + "\n"
                    net_informations += "\t Netmask: " + str(address.netmask) + "\n"
                    net_informations += "\t Broadcast MAC: " + str(address.broadcast) + "\n"
        net_io = self.net_io
        net_informations += "Total Bytes Sent: " + str(self.adjustSize(net_io.bytes_sent)) + "\n"
        net_informations += "Total Bytes Received: " + str(self.adjustSize(net_io.bytes_recv)) + "\n"

        return net_informations

    @staticmethod
    def adjustSize(size):
        factor = 1024
        for i in ["B", "KB", "MB", "GB", "TB"]:
            if size > factor:
                size = size / factor
            else:
                return f"{size: 3f}{i}"
