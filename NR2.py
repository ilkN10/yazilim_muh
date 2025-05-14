
x = 0.5  
tolerance = 1e-10
max_iterations = 100
iteration = 0

def f(x):
    return (x - 1) ** 2 * (x - 2) * (x - 3)

def f1(x):
    return 2 * (x - 1) * (x - 2) * (x - 3) + (x - 1) ** 2 * (2 * x - 5)

def f2(x):
    return (
        2 * (x - 2) * (x - 3)
        + 4 * (x - 1) * (2 * x - 5)
        + 2 * (x - 1) ** 2
    )


f_val = f(x)
f1_val = f1(x)
f2_val = f2(x)
dx = -f1_val / f2_val

print(f"-- {iteration}  x: {x:.6f}  f: {f_val:.6f}  f1: {f1_val:.6f}  f2: {f2_val:.6f}  dx: {dx:.6f}")


while abs(dx) > tolerance and iteration < max_iterations:
    x = x + dx
    iteration += 1

    f_val = f(x)
    f1_val = f1(x)
    f2_val = f2(x)

    if f2_val == 0:
        print("Sıfıra bölme hatası! f2 = 0 oldu.")
        break

    dx = -f1_val / f2_val

    print(f"-- {iteration}  x: {x:.6f}  f: {f_val:.6f}  f1: {f1_val:.6f}  f2: {f2_val:.6f}  dx: {dx:.6f}")

# Sonuç
print(f"\nYaklaşık kök: {x:.10f}  f(x): {f(x):.10f}  Toplam iterasyon: {iteration}")
