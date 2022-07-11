file = open("program.txt", "r")
prog = file.read()
file.close()

depth = 0
for c in prog:
    if c == '(':
        depth += 1
    elif c == ')':
        depth -= 1

print(f"Depth: {depth}")