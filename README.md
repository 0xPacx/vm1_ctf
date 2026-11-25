## MalwareTech VM1 - Bytecode Emulator

A lightweight Python emulator written to solve the **MalwareTech VM1** reverse engineering challenge by replicating its custom virtual machine architecture and decrypting the flag from the extracted memory dump.

### VM Architecture Summary

- **Virtual RAM:** `507 bytes` (`0x1fb`) copied from `DAT_140003100`.
- **Encrypted Data:** Stored at the beginning of the buffer (`0x00` - `0x18`).
- **Bytecode:** Starts at offset `0xff` (index `255`), fetched in 3-byte chunks (`opcode`, `operand1`, `operand2`).

| Opcode | Mnemonic | Description |
| :--- | :--- | :--- |
| `0x01` | `MOV` | Writes `operand2` into `virtual_ram[operand1]` |
| `0x02` | `LOAD` | Loads `virtual_ram[operand1]` into the virtual register |
| `0x03` | `XOR` | XORs `virtual_ram[operand1]` with the virtual register |
| `else` | `HALT` | Terminates the VM execution loop |

### Full Write-Up

For the complete reverse engineering walkthrough in Ghidra, check out the blog post:

[TR](https://0xpacx.github.io/posts/vm1/)


[EN](https://0xpacx.github.io/en/posts/vm1/)
