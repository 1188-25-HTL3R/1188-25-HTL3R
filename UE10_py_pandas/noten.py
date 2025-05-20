__author__ = "Luka Pacar"
__version__ = "1.0"

import argparse
import sys
from typing import List

import pandas as pd
import re
import xml.etree.ElementTree as ET
import os

def read_xml(filename: str) -> pd.DataFrame:
    """
    List eine xml-datei mit Schuelerinfo ein und wandelt diese in ein DataFrame um.
    """

    # Interpretiert die XML Datei.
    tree = ET.parse(filename)
    root = tree.getroot()

    data = []
    for schueler in root.findall("Schueler"):
        eintrag = {elem.tag: elem.text for elem in schueler}
        data.append(eintrag)

    df = pd.DataFrame(data)

    # Versuche Zahlen wirklich als Zahlen zu speichern. z.B. Nummer-Spalte
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="noten.py by Luka Pacar")

    parser.add_argument("outfile", type=str, help="Ausgabedatei (z.B. result.csv)")

    parser.add_argument("-n", type=str, help="csv-Datei mit den Noten")
    parser.add_argument("-s", type=str, help="xml-Datei mit den Schülerdaten")
    parser.add_argument("-m", type=str, help="Name der Spalte, die zu verknüpfen ist (default = Nummer)", default="Nummer")
    parser.add_argument("-f", type=str, help="Name des zu filternden Gegenstandes (z.B. SEW)")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus")
    group.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")

    args = parser.parse_args()

    outfile = args.outfile
    noten_datei = args.n
    schueler_datei = args.s
    verknuepfte_spalte = args.m
    gegenstaende = args.f
    verbose = args.verbose
    quiet = args.quiet

    def print_err(text: str):
        if not quiet:
            print(text, file=sys.stderr)

    outfile_dir = os.path.dirname(outfile)
    if len(outfile_dir) and not os.path.isdir(os.path.dirname(outfile)):
        print_err("Output Ordner existiert nicht.")
        sys.exit(1)

    if not os.path.exists(noten_datei):
        print_err("Die angegebene Noten-Datei existiert nicht.")
        sys.exit(2)


    if not os.path.exists(schueler_datei):
        print_err("Die angegebene Schueler-Datei existiert nicht.")
        sys.exit(3)

    if gegenstaende is None:
        print_err("Gegenstand nicht angegeben")
        sys.exit(4)
    gegenstaende = re.split(r",",gegenstaende)


    if verbose:
        print("csv-Datei mit den Noten : " + str(noten_datei))

    if verbose:
        print("xml-Datei mit den Schülerdaten : " + str(schueler_datei))

    if not verknuepfte_spalte:
        print_err("Zu verknüpfende Spalte nicht angegeben.")
        sys.exit(5)

    df_noten = pd.read_csv(noten_datei, delimiter=";")
    df_schueler = read_xml(schueler_datei)

    if verknuepfte_spalte not in df_noten.columns or verknuepfte_spalte not in df_schueler.columns:
        print_err("Zu verknüpfende Spalte nicht in beiden Dateien aufzufinden.")
        sys.exit(6)

    # Gegenstände
    for gegenstand in gegenstaende:
        if gegenstand not in df_noten.columns:
            print_err("Gegenstand " + str(gegenstand) + " nicht gefunden.")
            sys.exit(7)

    # Tabellen verknüpfen
    column_filter: List[str] = [verknuepfte_spalte]
    column_filter.extend(gegenstaende)
    df_combined = df_schueler.merge(df_noten[column_filter], on=verknuepfte_spalte, how="left")

    if len(gegenstaende) > 1:
        df_combined["Schnitt"] = sum([df_combined[subject] for subject in gegenstaende]) / len(gegenstaende)

    try:
        df_combined.to_csv(outfile, index=False)
    except Exception as e:
        print_err("Fehler während dem Schreiben der Datei.")
        print_err(e.__str__())
        sys.exit(8)



