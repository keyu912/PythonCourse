import json
import csv

inp_file = "input.csv"
outp_file = "output.json"

def task() -> None:
    
    a = open(inp_file, "r")
    b = open(outp_file, "w")

    reader = csv.DictReader(a)
    c = []
    for i in reader:
        c.append(i)


    json.dump(c, b, indent = 4)
    b.close()
    a.close()


if __name__ == '__main__':
    
    task()

    with open(outp_file) as output_f:
        for line in output_f:
            print(line, end="")
