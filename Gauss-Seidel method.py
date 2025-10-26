import numpy as np

# Nathaphoom Create Function Gauss-Seidel Method with Auto Pivoting 
# Phongthorn Create Function Show steps

#! Start Nathapoom AI
def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    x = np.zeros(n)

    print("=== เริ่มคำนวณวิธีเกาส์-ไซเดล ===\n")

    for k in range(1, max_iter+1):
        print(f"ครั้งที่ {k}:")
        x_old = x.copy()

        for i in range(n):
            # Show steps
            x_number = 0
            #! End Nathapoom AI

            #! Start Phongsathorn
            move_to_divide = 0
            print("x{} = ( {}".format(i+1, b[i]), end=" ") # x1 = (b
            for j in range(n):
                if j != i:
                    if A[i][j] != 0:
                        print(f"+{abs(A[i][j])}" if A[i][j]<0 else -A[i][j], end="")
                        print(f"({x[x_number]:.4f})", end=" ") # x1 = (b x2 x3 x4)
                else: move_to_divide = A[i][j]
                x_number+=1
            print(f")/{move_to_divide}", end=" ")
            #! End Phongsathorn

            #! Start Nathapoom AI
            sum_ = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - sum_) / A[i, i]
            #! End Nathapoom AI

            #! Start Phongsathorn
            print(f"= {x[i]:.4f}")
            #! End Phongsathorn

        #! Start Nathapoom AI
        econ = abs((x[2]-x_old[2])/x[2])
        print(f"Econ = {econ:.5f} {'>' if econ>tol else '<'} {tol}\n")
        if econ < tol:
            print(f"\nสิ้นสุดการคำนวณหลัง {k} ครั้ง (ถึงค่าความคลาดเคลื่อนที่กำหนด)\n")
            break
        
    print("\nคำตอบประมาณคือ:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.4f}")

    return x


# ===========================
# 🔹 ส่วนรับค่าจากผู้ใช้
# ===========================
print("=== โปรแกรมคำนวณระบบสมการเชิงเส้นด้วยวิธีเกาส์-ไซเดล ===\n")

n = int(input("กรุณาระบุขนาดเมทริกซ์ (n x n): "))

print("\nกรุณาป้อนค่าของเมทริกซ์ A (แต่ละแถวคั่นด้วยช่องว่าง):")
A = np.zeros((n, n))
for i in range(n):
    A[i] = list(map(float, input(f"แถวที่ {i+1}: ").split()))

print("\nกรุณาป้อนค่าของเวกเตอร์ b (คั่นด้วยช่องว่าง):")
b = np.array(list(map(float, input().split())))
#! End Nathapoom AI

#! Start Phongsathorn
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("ตารางเมทริกซ์")
for i in range(n):
    print("[", end=" ")
    for j in range(n):
        print(A[i][j], end=" ")
    print("] =",b[i])

print("\nขั้นตอนที่ 1 จัดรูปแบบทำซ้ำ")
# === ตรวจสอบศูนย์บนแนวทแยง แล้วสลับแถวอัตโนมัติ ===
for i in range(n):
    if A[i, i] == 0:
        for k in range(i+1, n):
            if A[k, i] != 0:
                A[[i, k]] = A[[k, i]]
                b[[i, k]] = b[[k, i]]
                break
        else:
            raise ZeroDivisionError(f"ไม่สามารถทำ Pivot ที่แถว {i+1} ได้ (A[{i},{i}] = 0)")
# === จัดรูปแบบ ===
for i in range(n): 
    x_number = 1
    move_to_divide = 0
    print("x{} = ( {}".format(i+1, b[i]), end=" ") # x1 = (b

    for j in range(n):
        if j != i:
            if A[i][j] != 0:
                print(f"+{abs(A[i][j])}" if A[i][j]<0 else -A[i][j], end="")
                print(f"(x{x_number})", end=" ") # x1 = (b x2 x3 x4)
        else: move_to_divide = A[i][j]
        x_number+=1
    print(f")/{move_to_divide}")
#! End Phongsathorn

#! Start Nathapoom AI
print("\nขั้นตอนที 2 การกำหนดค่าเริ่มต้นและเกณฑ์ค่าความคลาดเคลื่อน")
tol = float(input("\nกรุณาป้อนค่าความคลาดเคลื่อน (ε): "))

# เรียกใช้ฟังก์ชัน
print("\nขั้นตอนที 3 การคำนวณทำซ้ำตรวจสอบความคลาดเคลื่อน")
gauss_seidel(A, b, tol=tol)
#! End Nathapoom AI