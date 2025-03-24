import sys
import argparse
from UE05_Kasiski import caeser, vigenere
"""
cvcrypt - Caesar & Vigenere Encrypter/Decrypter

Dieses Skript ermöglicht die Verschlüsselung und Entschlüsselung von Dateien mithilfe des Caesar- oder Vigenere-Algorithmus.
Der Benutzer kann den gewünschten Algorithmus auswählen und die Eingabe- sowie Ausgabedateien angeben.

Verwendung:
    python cvcrypt.py <infile> <outfile> -c <cipher> [-e | -d] -k <key> [-v | -q]

Argumente:
    infile    - Die zu verschlüsselnde oder zu entschlüsselnde Datei.
    outfile   - Die Zieldatei für das Ergebnis.
    -c, --cipher  - Der zu verwendende Verschlüsselungsalgorithmus ("caesar", "c", "vigenere", "v").
    -e, --encrypt - Verschlüsselung aktivieren.
    -d, --decrypt - Entschlüsselung aktivieren.
    -k, --key     - Der Schlüssel für die Verschlüsselung/Entschlüsselung.
    -v, --verbose - Detaillierte Ausgabe aktivieren.
    -q, --quiet   - Minimale Ausgabe aktivieren.

Autor:
    Luka Pacar
"""

__author__ = "Luka Pacar"

parser = argparse.ArgumentParser(description="cvcrypt - Caesar & Vigenere encrypter / decrypter by PAC / HTL Rennweg")
parser.add_argument("infile", help="Zu verschlüsselnde Datei", type=str)
parser.add_argument("outfile", help="Zieldatei", type=str)

parser.add_argument("-c","--cipher", help="zu verwendende Chiffre", choices=["caesar","c","vigenere","v"])

group_verbose_or_quiet = parser.add_mutually_exclusive_group()
group_verbose_or_quiet.add_argument("-v","--verbose", action="store_true")
group_verbose_or_quiet.add_argument("-q","--quiet", action="store_true")

group_decrypt_or_encrypt = parser.add_mutually_exclusive_group()
group_decrypt_or_encrypt.add_argument("-d","--decrypt", action="store_true")
group_decrypt_or_encrypt.add_argument("-e","--encrypt", action="store_true")

parser.add_argument("-k","--key", help="Encryption-Key")

args = parser.parse_args()


# Key speichern
if args.key:
    key = args.key
else:
    print("No Key given (--key KEY)", file=sys.stderr)
    exit(1)

# Input auslesen
try:
    input_file_content = open(args.infile).read()
except FileNotFoundError:
    print(args.infile + ": No such file or directory", file=sys.stderr)
    exit(1)
except PermissionError:
    print(args.infile + ": Permission denied", file=sys.stderr)
    exit(1)
except IsADirectoryError:
    print(args.infile + ": Is a directory", file=sys.stderr)
    exit(1)
except Exception:
    print("An error occurred while reading the input file", file=sys.stderr)
    exit(1)

# Encrypt/Decrypt ausführen und output speichern
if args.cipher == "vigenere" or args.cipher == "v":
    print("Vigenere")
    if args.encrypt:
        output = vigenere.Vigenere(key).encrypt(input_file_content)
    else:
        output = vigenere.Vigenere(key).decrypt(input_file_content)
else:
    if args.encrypt:
        output = caeser.Caesar(key).encrypt(input_file_content)
    else:
        output = caeser.Caesar(key).decrypt(input_file_content)

# Output speichern
try:
    with open(args.outfile, "w") as file:
        file.write(output)

    if args.verbose:
        print("Encrypting " + ("Caeser" if args.cipher == "caesar" or args.cipher == "c" else "Vigenere") + " with key = " + key + "from file " + args.infile + " to file " + args.outfile)
except FileNotFoundError:
    print(args.outfile + ": No such file or directory", file=sys.stderr)
    exit(1)
except PermissionError:
    print(args.outfile + ": Permission denied", file=sys.stderr)
    exit(1)
except IsADirectoryError:
    print(args.outfile + ": Is a directory", file=sys.stderr)
    exit(1)
except Exception:
    print("An error occurred while writing the output file", file=sys.stderr)
    exit(1)

