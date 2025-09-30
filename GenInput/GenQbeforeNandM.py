import random
import os

def generate_random_file(filename, q, n_min, n_max, m_min, m_max):
    with open(filename, 'w') as file:
        file.write(f"{q}\n")
        for _ in range(q):
            n = random.randint(n_min, n_max)
            m = random.randint(m_min, m_max)
            file.write(f"{n} {m}\n")
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (q = {q})")

def main():
    a = 1
    b = 10
    
    # กำหนด min และ max สำหรับ q, n และ m
    q_min, q_max = 1, 1000
    n_min, n_max = 0, 10000
    m_min, m_max = 30, 8 * 10**4
    
    # limit cases
    limit_cases = [
        q_min,    # test case 1: min q
        q_max,    # test case 2: max q
        q_min,    # test case 3: min q (with extreme n,m)
        q_max     # test case 4: max q (with extreme n,m)
    ]
    
    used_q = set()
    
    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        
        if i-1 < len(limit_cases):
            q = limit_cases[i-1]
        else:
            while True:
                q = random.randint(q_min, q_max)
                if q not in used_q:
                    break
        
        used_q.add(q)
        generate_random_file(filename, q, n_min, n_max, m_min, m_max)
    
    print(f"\nสร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
