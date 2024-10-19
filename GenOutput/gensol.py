import os
import subprocess
import glob

def process_input_files(exe_path):
    # หาไฟล์ .in ทั้งหมดในโฟลเดอร์ปัจจุบัน
    input_files = glob.glob('*.in')
    
    if not input_files:
        print("ไม่พบไฟล์ .in ในโฟลเดอร์นี้")
        return

    for input_file in input_files:
        # สร้างชื่อไฟล์ output
        output_file = input_file.replace('.in', '.sol')
        
        print(f"กำลังประมวลผล {input_file}...")
        
        try:
            # เปิดไฟล์ input และ output
            with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
                # รัน .exe file และส่งข้อมูลจาก input ไปยัง .exe
                # จากนั้นบันทึกผลลัพธ์ลงในไฟล์ output
                subprocess.run([exe_path], stdin=infile, stdout=outfile, text=True, check=True)
            
            print(f"สร้างไฟล์ {output_file} เสร็จสิ้น")
        
        except subprocess.CalledProcessError as e:
            print(f"เกิดข้อผิดพลาดในการประมวลผล {input_file}: {e}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")

def main():
    # ขอ path ของไฟล์ .exe จากผู้ใช้
    exe_path = input("กรุณาใส่ path ของไฟล์ .exe (เช่น C:\\path\\to\\your\\program.exe): ")
    
    # ตรวจสอบว่าไฟล์ .exe มีอยู่จริง
    if not os.path.exists(exe_path):
        print("ไม่พบไฟล์ .exe ตาม path ที่ระบุ")
        return

    process_input_files(exe_path)
    print("การประมวลผลเสร็จสิ้น")

if __name__ == "__main__":
    main()
