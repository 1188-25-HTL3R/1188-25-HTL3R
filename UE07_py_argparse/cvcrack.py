import argparse
import sys
from UE05_Kasiski import caeser, kasiski

parser = argparse.ArgumentParser(description="cvcrack - Caesar & Vigenere key cracker by PAC / HTL Rennweg")
parser.add_argument("infile", help="Zu knackende Datei", type=str)
parser.add_argument("-c","--cipher", help="zu verwendende Chiffre", choices=["caesar","c","vigenere","v"])

group_verbose_or_quiet = parser.add_mutually_exclusive_group()
group_verbose_or_quiet.add_argument("-v","--verbose", help="Zeigt Infos an (siehe Beispiele in der Angabe)", action="store_true")
group_verbose_or_quiet.add_argument("-q","--quiet", help="Liefert nur den wahrscheinlichsten Key zurück", action="store_true")

args = parser.parse_args()

# Input auslesen
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

if args.cipher == "caesar" or args.cipher == "c":
    key = caeser.Caesar().crack(input_file_content)[0]
else:
    key = kasiski.Kasiski(input_file_content).crack_key(4)[0] # Möglicherweise Kasiski falsch implementiert? Verstehe length parameter nicht? TODO ZAI nachfragen

if args.verbose:
    print(f'Cracking {("Caesar" if args.cipher == "caesar" or args.cipher == "c" else "Vigenere")}-encrypted file {args.infile}: Key = {key}')
else:
    print(key)