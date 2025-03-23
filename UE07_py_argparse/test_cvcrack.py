import subprocess

print("Output 1:")
# 1
subprocess.run([
    "python", "cvcrack.py",
    "--cipher", "caesar",
    "--verbose",
    "rk_ceb.txt"
])

print("Output 2:")
# 2
subprocess.run([
    "python", "cvcrack.py",
    "--cipher", "caesar",
    "rk_ceb.txt"
])

print("Output 3:")
# 3
subprocess.run([
    "python", "cvcrack.py",
    "--cipher", "vigenere",
    "rk_vehugo.txt"
])

print("Output 4:")
# 4
subprocess.run([
    "python", "cvcrack.py",
    "-v",
    "--cipher", "vigenere",
    "rk_vehugo.txt"
])

print("Output 5:")
# 5
subprocess.run([
    "python", "cvcrack.py",
    "mich_gibts_nicht.txt"
])

print("Output 6:")
# 6
subprocess.run([
    "python", "cvcrack.py"
])

print("Output 7:")
# 7
subprocess.run([
    "python", "cvcrack.py",
    "--help"
])