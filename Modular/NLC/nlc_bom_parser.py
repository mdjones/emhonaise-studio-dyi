#!/usr/bin/env python3

from pypdf import PdfReader
import pandas as pd
import csv
import re
import sys


def main():
    pdf_file = sys.argv[1]
    reader = PdfReader(pdf_file)

    page = reader.pages[1]
    lines = page.extract_text().split("\n")
    header = None
    desc_starts = ["Mouser", "similar", "Synthcube", "Modular Addict", "Tayda: ", "if you want.", 'four 10 pin sections.']
    valsWspace = [
        "TL072 or TL082",
        "TL074 or TL084",
        "100k pot",
        "20k trimpot",
        "toggle switch SPDT",
        "3.5MM SOCKET Kobiconn",
        "S1JL, Schottky, power",
        "Eurorack 10 pin power",
        "connector",
        "LL4148 diode",
        "rectifier or 10R",
        "10k pot",
        "100k pot",
        "5k trimpot",
        "10 Pin 2.54mm Single",
        "40 Pin 2.54mm Single",
        "Row Female Pin Header",
        "Row Pin Header Strip"
    ]

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.writer(csvfile)
        for l in lines:
            l = l.rstrip()
            l = re.sub(r"\s+", " ", l)


            toks = [t.strip() for t in l.split(" ", 2) if t.strip()]
            if len(toks) == 0:
                continue
            if toks == ["VALUE", "QUANTITY", "DETAILS"]:
                header = toks
                row = ["x = Soldered"] + toks + ["x = In Stock"]
                writer.writerow(row)
                continue

            for vws in valsWspace:
                if l.startswith(vws):
                    toks = [vws]
                    toks.extend(l.replace(vws, "").strip().split(" ", 1))
            if header:
                for s in desc_starts:
                    if toks[0].startswith(s):
                        toks = ["", ""]
                        toks.append(l)

                if len(toks) > 1:
                    row = [""] + toks
                    for i in range(1, 5-len(row)+1):
                        row.append("")
                    writer.writerow(row)
                elif len(toks) > 0:
                    found = False
                    if not found:
                        writer.writerow([l])

main()
