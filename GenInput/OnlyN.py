import random
import os
#โปรแกรมสุ่มเทสเคสที่ในเทสเคสมีเฉพาะ n เพียงตัวเดียว
def generate_random_file(filename):
    # สุ่มจำนวนเต็ม n 
    n = random.randint(1, 10**6) #ลิมิตของ n
    num = f"{n:02d}"
    with open(filename, 'w') as file:
        file.write(num)
       
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (number = {n})")

def main():
    #จำนวนเทสเคสที่ต้องการสร้างตั้งแต่ a ถึง b
    a = 1
    b = 20
    
    # สร้างไฟล์ตั้งแต่ a ถึง b
    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        generate_random_file(filename)
    
    print(f"สร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
