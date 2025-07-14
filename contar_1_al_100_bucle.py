print("=== 10 números por línea ===")
for i in range(1, 101):
    print(f"{i:3d}", end=" ")  # :3d formatea con 3 espacios
    if i % 10 == 0:  # Salto de línea cada 10 números
        print()  # Nueva línea