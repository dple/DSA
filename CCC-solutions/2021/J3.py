# Secret Instructions

if __name__ == '__main__':
    instruction = input()
    instructions = []
    while instruction != '99999':
        instructions.append(instruction)
        instruction = input()

    for instruction in instructions:
        code = int(instruction[0]) + int(instruction[1])
        if code % 2 == 0 and code != 0:
            direction = 'right'
        elif code %2 == 1:
            direction = 'left'
        steps = instruction[2:]
        print(direction, steps)