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

