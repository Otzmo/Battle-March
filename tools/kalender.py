"""Erzeugt termine.ics (und termine-2027.ics fuer alte Abos) aus den Terminen in Firebase.

Laeuft per GitHub Action alle 15 Minuten. Die Datei wird nur neu geschrieben, wenn sich
ein Termin geaendert hat; sonst bleibt sie (samt DTSTAMP) unveraendert und es gibt keinen Commit.
"""
import datetime
import json
import pathlib
import re
import sys
import urllib.request

QUELLE = "https://spieltageuebersicht-default-rtdb.europe-west1.firebasedatabase.app/termine.json"
DATEIEN = ["termine.ics", "termine-2027.ics"]
TERMIN = re.compile(r"^\d{4}-\d\d-\d\d$")
UHR = re.compile(r"^\d\d:\d\d$")

KOPF = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//OTZMO-TOW//Termine//DE
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Termine The Old World
X-WR-TIMEZONE:Europe/Berlin
REFRESH-INTERVAL;VALUE=DURATION:PT1H
X-PUBLISHED-TTL:PT1H
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""


def text(s):
    return s.replace(chr(92), chr(92) * 2).replace(";", chr(92) + ";").replace(",", chr(92) + ",").replace("\n", chr(92) + "n")


def uid(tid):
    # Die Ausgangstermine haben das Datum als ID; ihre UID bleibt wie in der ersten Kalenderdatei,
    # damit bestehende Abos keine doppelten Eintraege bekommen.
    if TERMIN.match(tid):
        return tid.replace("-", "") + "-spieltag@otzmo-tow"
    return re.sub(r"[^A-Za-z0-9_-]", "", tid) + "@otzmo-tow"


def kalender(termine, stempel):
    zeilen = KOPF.split("\n")
    gueltig = [(k, t) for k, t in termine.items()
               if isinstance(t, dict) and TERMIN.match(str(t.get("datum", "")))
               and UHR.match(str(t.get("beginn", ""))) and UHR.match(str(t.get("ende", "")))
               and isinstance(t.get("art"), str)]
    for k, t in sorted(gueltig, key=lambda x: (x[1]["datum"], x[1]["beginn"])):
        d = t["datum"].replace("-", "")
        titel = text(t["art"].strip()[:30] + " The Old World")
        zeilen += ["BEGIN:VEVENT", "UID:" + uid(k), "DTSTAMP:" + stempel,
                   "DTSTART;TZID=Europe/Berlin:%sT%s00" % (d, t["beginn"].replace(":", "")),
                   "DTEND;TZID=Europe/Berlin:%sT%s00" % (d, t["ende"].replace(":", "")),
                   "SUMMARY:" + titel,
                   "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + titel, "TRIGGER:-P2D", "END:VALARM",
                   "END:VEVENT"]
    zeilen.append("END:VCALENDAR")
    return "\r\n".join(zeilen) + "\r\n"


def ohne_stempel(s):
    return re.sub(r"DTSTAMP:\S+", "", s)


def main():
    with urllib.request.urlopen(QUELLE, timeout=30) as r:
        termine = json.load(r)
    if not termine:
        # Datenbank leer (noch nicht uebernommen): bestehende Datei nicht ueberschreiben
        print("Keine Termine in der Datenbank - nichts geaendert.")
        return 0
    stempel = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    neu = kalender(termine, stempel)
    for name in DATEIEN:
        pfad = pathlib.Path(name)
        alt = pfad.read_text(encoding="utf-8") if pfad.exists() else ""
        if ohne_stempel(alt.replace("\r\n", "\n")) != ohne_stempel(neu.replace("\r\n", "\n")):
            pfad.write_bytes(neu.encode("utf-8"))
            print(name + " aktualisiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
