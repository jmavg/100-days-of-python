import sys

levels = int(sys.argv[1])
spaces_amount = levels - 1
buffer = " "
leaf = "*"
log = " " * spaces_amount + "*"

for i in range(1, levels+1):
    print(buffer*spaces_amount + leaf*(2*i-1))
    spaces_amount -= 1
print(log)