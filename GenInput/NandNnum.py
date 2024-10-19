import random
import os
#โปรแกรมสร้างเทสเคส สุ่มตัวเลข n จากนั้นสุ่มเลขมาอีก n จำนวน
def generate_random_file(filename):
    # สุ่มค่า n ระหว่าง 1 และ 10^6
    n = random.randint(1, 10**6)

    # สร้างลิสต์เพื่อเก็บค่า x ที่สุ่มได้
    x_values = [random.randint(-10**6, 10**6) for _ in range(n)] #ลิมิตของ x คือแต่ละค่าภายใน n จำนวน

    # สร้างไฟล์ใหม่และเขียนข้อมูล
    with open(filename, 'w') as file:
        # เขียนค่า n ในบรรทัดแรก
        file.write(f"{n}\n")
        
        # เขียนค่า x แต่ละค่าในบรรทัดถัดไป
        for x in x_values:
            file.write(f"{x}\n")

    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (n = {n})")

def main():
    #จำนวนเทสเคสที่ต้องการให้สร้าง
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
