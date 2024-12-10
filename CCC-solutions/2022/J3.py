#  Harp Tuning
if __name__ == '__main__':
    stringslabels = "ABCDEFGHIJKLMNOPQRST"          # labels of strings
    str = input()                                   # get the sequence of instructions
    instructions = []                               # list of instructions
    instruction = ''                                # an instruction, e.g., ABC+4
    for pos, c in enumerate(str[:-1]):
        if c not in stringslabels and str[pos + 1] in stringslabels:
            instruction += c
            instructions.append(instruction)
            instruction = ''
        else:
            instruction += c

    instruction += str[-1]
    instructions.append(instruction)

    for instruction in instructions:
        if '+' in instruction:
            instruction = instruction.split('+')
            print(instruction[0], "tighten", instruction[1])
        elif '-' in instruction:
            instruction = instruction.split('-')
            print(instruction[0], "loosen", instruction[1])
