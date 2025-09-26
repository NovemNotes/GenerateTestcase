import random
import os

def generate_random_file(filename, low, high):
    with open(filename, 'w') as file:
        file.write(f"{low} {high}")
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (low = {low}, high = {high})")

def main():
    a = 1
    b = 20
    # กรณีขอบ: [low, high] pairs โดยที่ 0 <= low <= high <= 10^9
    limit_cases = [
        [0, 0],                    # low=high=0 (กรณีต่ำสุด)
        [0, 10**9],               # low=0, high=max (กรณีห่างที่สุด)
        [10**9, 10**9]            # low=high=max (กรณีสูงสุด)
    ]
    
    used_pairs = set()
    
    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        
        if i-1 < len(limit_cases):
            low, high = limit_cases[i-1]
        else:
            while True:
                low = random.randint(0, 10**9)
                high = random.randint(low, 10**9)  # high >= low
                if (low, high) not in used_pairs:
                    break
        
        used_pairs.add((low, high))
        generate_random_file(filename, low, high)
    
    print(f"สร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
