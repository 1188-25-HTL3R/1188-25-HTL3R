import subprocess

print("Output 1:")
# 1
subprocess.run([
    "python", "cvcrypt.py",
    "--verbose",
    "--cipher", "caesar",
    "--encrypt",
    "--key", "b",
    "rk.txt", "test_output_dir/rk_ceb.txt"
])

print("Output 2:")
# 2
subprocess.run([
    "python", "cvcrypt.py",
    "--cipher", "caesar",
    "--encrypt",
    "--key", "b",
    "rk.txt", "test_output_dir/rk_ceb.txt"
])

print("Output 3:")
# 3
subprocess.run([
    "python", "cvcrypt.py",
    "--verbose",
    "--cipher", "vigenere",
    "--encrypt",
    "--key", "hugo",
    "rk.txt", "test_output_dir/rk_vdhugo.txt"
])

print("Output 4:")
# 4
subprocess.run([
    "python", "cvcrypt.py",
    "--verbose",
    "--cipher", "v",
    "--decrypt",
    "--key", "hugo",
    "rk_vehugo.txt", "test_output_dir/rk_vdhugo.txt"
])

print("Output 5:")
# 5
subprocess.run([
    "python", "cvcrypt.py",
    "--cipher", "v",
    "--decrypt",
    "--key", "hugo",
    "mich_gibts_nicht.txt", "test_output_dir/rk_vdhugo.txt"
])

print("Output 6:")
# 6
subprocess.run([
    "python", "cvcrypt.py"
])

print("Output 7:")
# 7
subprocess.run([
    "python", "cvcrypt.py",
    "--help"
])