import random
import os

def generate_random_file(filename, n):
    with open(filename, 'w') as file:
        file.write(f"{n}")
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (number = {n})")

def main():
    a = 1
    b = 20
    limit_cases = [1, 10**4]
    used_numbers = set()

    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        if i-1 < len(limit_cases):
            n = limit_cases[i-1]
        else:
            while True:
                n = random.randint(1, 10000)
                if n not in used_numbers:
                    break
        used_numbers.add(n)
        generate_random_file(filename, n)
    
    print(f"สร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
