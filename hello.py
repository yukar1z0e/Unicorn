from unicorn import *
from unicorn.arm_const import *

ARM_CODE = b"\x37\x00\xa0\xe3\x03\x10\x42\xe0"
# mov r0, #0x37;
# sub r1, r2, r3

# Test ARM

def test_arm():
    print("Emulate ARM code")
    try:
        # Initialize emulator in ARM mode
        mu=Uc(UC_ARCH_ARM,UC_MODE_ARM)
    except UcError as e:
        print("ERROR:%s"% e)
