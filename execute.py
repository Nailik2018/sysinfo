# -*- coding: utf-8 -*-

from sysinfo import Sysinfo

sysinfo = Sysinfo()

print("-" * 40, " System Info ", "-" * 40)
print(sysinfo.getSystem())
print(sysinfo.getNodeName())
print(sysinfo.getRelease())
print(sysinfo.getVersion())
print(sysinfo.getMachine())
print(sysinfo.getProcessor())

print("-" * 40, " Boot Time Info ", "-" * 40)
print(sysinfo.getBootTime())

print("-" * 40, " CPU Info ", "-" * 40)
print(sysinfo.getCPUCores(False))
print(sysinfo.getCPUCores(True))
print(sysinfo.getCPUFrequency("max"))
print(sysinfo.getCPUFrequency("current"))
print(sysinfo.getCPUUsage())
print(sysinfo.getCPUTemperature())
print(sysinfo.getSingleWorkloadOfCPUs(True, 1))

print("-" * 40, " RAM Info ", "-" * 40)
print(sysinfo.getTotalRAM())
print(sysinfo.getAvailableRAM())
print(sysinfo.getUsedRAM())
print(sysinfo.getRAMWorkloadPrecent())

print("-" * 40, " SWAP Info ", "-" * 40)
print(sysinfo.getTotalSWAP())
print(sysinfo.getAvailableSWAP())
print(sysinfo.getUsedSWAP())
print(sysinfo.getSWAPWorkloadPrecent())

print("-" * 40, " Laufwerke Info ", "-" * 40)
print(sysinfo.getDiskInformations())
print(sysinfo.getDiskIORead())
print(sysinfo.getDiskIOWrite())

print("-" * 40, " GPU Info ", "-" * 40)
print(sysinfo.getGPUInformations())

print("-" * 40, " Netzwerk Info ", "-" * 40)
print(sysinfo.getNetworkInformations())
