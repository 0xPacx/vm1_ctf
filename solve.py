# MalwareTech VM1 Challenge - Custom Bytecode Emulator & Flag Extractor

# 507-byte (0x1fb) memory dump extracted from DAT_140003100
virtual_ram = bytearray.fromhex(
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "de 7e 7d 55 1e 05 e6 9f e4 a6 47 50 02 01 c7 fc cb 60 09 c6 0e 2e 41 65 a4 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 1d bd 01 05 "
    "53 01 12 48 01 10 e6 01 13 8a 01 0d 47 01 16 13 01 0a 15 01 00 98 01 02 3c 01 18 d9 01 1a 57 01 "
    "06 ab 01 1b c6 01 01 32 01 17 20 01 15 6f 01 11 2d 01 08 c9 01 09 e7 01 03 12 01 0c 2f 01 0e 88 "
    "01 19 6c 01 04 65 01 1e ae 01 14 59 01 1f 91 01 1c 5d 01 0f ae 01 0b 15 01 07 cc 02 20 00 03 "
    "00 00 02 21 00 03 01 00 02 22 00 03 02 00 02 23 00 03 03 00 02 24 00 03 04 00 02 25 00 03 05 00 "
    "02 26 00 03 06 00 02 27 00 03 07 00 02 28 00 03 08 00 02 29 00 03 09 00 02 2a 00 03 0a 00 02 2b "
    "00 03 0b 00 02 2c 00 03 0c 00 02 2d 00 03 0d 00 02 2e 00 03 0e 00 02 2f 00 03 0f 00 02 30 00 03 "
    "10 00 02 31 00 03 11 00 02 32 00 03 12 00 02 33 00 03 13 00 02 34 00 03 14 00 02 35 00 03 15 00 "
    "02 36 00 03 16 00 02 37 00 03 17 00 02 38 00 03 18 00 01 19 00 04 00 00"
)

# Locate the start of bytecode instructions (index 251 / 0xfb)
bytecode_start = virtual_ram.index(0x01, 200)
ip = 0  # Instruction Pointer
reg = 0  # Virtual Register

# Fetch-Decode-Execute loop (3 bytes per instruction)
while (bytecode_start + ip + 2) < len(virtual_ram):
    opcode = virtual_ram[bytecode_start + ip]
    operand1 = virtual_ram[bytecode_start + ip + 1]
    operand2 = virtual_ram[bytecode_start + ip + 2]

    if opcode == 0x01:  # MOV: Write immediate value to virtual RAM
        virtual_ram[operand1] = operand2
    elif opcode == 0x02:  # LOAD: Load byte from virtual RAM into register
        reg = virtual_ram[operand1]
    elif opcode == 0x03:  # XOR: XOR virtual RAM byte with register
        virtual_ram[operand1] ^= reg
    else:  # HALT: Stop execution
        break

    ip += 3

print(
    "********************************************\n"
    "Flag:", virtual_ram[:26].decode("ascii", errors="ignore"), "\n"
    "********************************************"
)