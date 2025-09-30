import random
import os

def generate_random_file(filename, n, m):
    with open(filename, 'w') as file:
        file.write(f"{n} {m}")
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (n = {n}, m = {m})")

def main():
    a = 1
    b = 10
    
    # กำหนด min และ max สำหรับ n และ m
    n_min, n_max = 0, 10000
    m_min, m_max = 30, 8 * 10**4
    
    # limit cases ครบทั้ง 4 แบบ
    limit_cases = [
        (n_min, m_min),    # test case 1: min n, min m (0, 30)
        (n_min, m_max),    # test case 2: min n, max m (0, 80000)
        (n_max, m_min),    # test case 3: max n, min m (10000, 30)
        (n_max, m_max)     # test case 4: max n, max m (10000, 80000)
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
