import sys

rows = int(input("Enter number of rows : "))
print(f"{rows} rows will be printed with *")

for i in range(1, rows + 1):
    # Print spaces
    print(' ' * (rows - i), end='')
    # Print stars
    print('*' * (1 * i))