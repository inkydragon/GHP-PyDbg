# -*- coding: utf-8 -*-
import ghp_pydbg
from gph_pydbg_defines import HW_EXECUTE

debugger = ghp_pydbg.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

print_address = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % print_address
debugger.bp_set_hw(print_address,1,HW_EXECUTE)

debugger.run()
