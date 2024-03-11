from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def half_adder(a, b):
  s = XOR_gate(a, b)
  c = AND_gate(a, b)
  return (s, c)

# print(half_adder(0, 0))
# print(half_adder(0, 1))
# print(half_adder(1, 0))
# print(half_adder(1, 1))

def full_adder(a, b, c):
  s = half_adder(half_adder(a, b)[0], c)[0]
  c_out = OR_gate(half_adder(a, b)[1], half_adder(half_adder(a, b)[0], c)[1])
  return (s, c_out)

# print(full_adder(0, 0, 0))
# print(full_adder(1, 1, 1))
# print(full_adder(0, 1, 1))
# print(full_adder(1, 1, 0))

def ALU(a, b, c, opcode):
  if opcode == 0:
    s, c_out = half_adder(a, b)
  elif opcode == 1:
    s, c_out = full_adder(a, b, c)
  return s, c_out

print(ALU(0, 0, 1, 0))
print(ALU(0, 0, 1, 1))
print(ALU(1, 1, 1, 0))
print(ALU(1, 1, 1, 1))