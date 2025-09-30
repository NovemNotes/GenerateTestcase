import random
import os

def generate_random_file(filename, n, m):
    with open(filename, 'w') as file:
        file.write(f"{n} {m}")
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (n = {n}, m = {m})")

def main():
    a = 1
    b = 20
    
    # กำหนดค่า limit cases สำหรับ (n, m)
    limit_cases = [
        (1, 1),           # test case 1
        (10**4, 10**4)    # test case 2
    ]
    
    used_pairs = set()
    
    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        
        if i-1 < len(limit_cases):
            n, m = limit_cases[i-1]
        else:
            while True:
                n = random.randint(n_min, n_max)
                m = random.randint(m_min, m_max)
                if (n, m) not in used_pairs:
                    break
        
        used_pairs.add((n, m))
        generate_random_file(filename, n, m)
    
    print(f"\nสร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
