#!/usr/bin/env python2
from arch import *
class ROPChain:
    def __init__(self, binary, gadgets):
        self.binary = binary
        self.gadgets = gadgets


    def parse_gadget(self):
	    if self.binary.getArch() == CS_ARCH_X86:
		    self.parser = ROPParserX86(self.gadgets, self.binary.getArchMode())
                    self.formulas = self.parser.parse()
