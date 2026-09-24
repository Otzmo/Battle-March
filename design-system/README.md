Battle March ist ein Regel-Leitfaden und Werkzeugkasten für Tabletop-Gefechte: Regeltext auf Pergament, Werkzeuge im selben Rahmen. Alles wirkt wie ein gedrucktes Regelheft mit Siegelwachs-Rot – ruhig, lesbar, ohne Effekte.

## Inhalt und Ton

- **Sprache**: Deutsch als Standard; der GermanComp-Reiter folgt dem englischen Original. Keine Mischsätze.
- **Ansprache**: sachlich-imperativ, Du-Form in Bedienhinweisen („Ziehe ein Stück auf das Raster“), unpersönlich im Regeltext („Die Aufstellungszone ist 10 Zoll tief.“).
- **Spielbegriffe** exakt wie im Regelwerk: W3, W6, 2W6, S4, DS -1, Einheitenstärke, Unterphase „Beginn des Zuges“. Maße in Zoll mit `"` (12"), Basen in mm (60×100 mm).
- **Gliederung**: Kapitel nummeriert („1. Spielablauf“, GermanComp römisch „I. Restriction Pack“), Missionen „Mission 1 – Schätze“ mit Halbgeviertstrich.
- **Aufzählungen in einer Zeile** mit Mittelpunkt: „Schweres Gelände · Deckung (treffen −1) · natürliches Gelände“.
- Keine Emojis. Symbole nur funktional: `▸` (Akkordeon), `⟳` und `×` (Stück drehen/löschen), `↗` (externer Link).

## Farbe

- `maroon` ist die einzige Akzentfarbe: Rahmen, Überschriften, aktive Tabs, gefüllte Buttons. Hover und „an“-Zustand: `maroon-dark`.
- Flächen in drei Stufen: Seite `page-bg` → Blatt/Panel `beige` → Einlage `surface` (Statbox, Akkordeon-Körper, Eingaben). Kopfzeilen `tan`.
- Text: `text` für Fließtext, `ink-muted` für Untertitel und Labels, `ink-soft` für Hinweise, `ink-caption` für Bildunterschriften.
- Spielbrett-Farben sind Daten, keine Dekoration: `zone-p1`/`zone-p2`/`zone-nml` nur für Aufstellungszonen, `terrain-*` nur für Gelände, `treasure` nur für Schätze, `objective` nur für Zielpunkte in Diagrammen.
- `earth` ausschließlich für die Leeren-/Zurücksetzen-Aktion. `note-bg`/`note-border` ausschließlich für Geltungsbereich-Hinweise.
- Kontrast: Alle Textpaare erfüllen 4.5:1, außer weißer Beschriftung auf `terrain-forest`, `terrain-hill`, `terrain-water` und dem Fokusring `focus` (siehe deren Notizen) – Quellwerte, nicht verändert.

## Typografie

- Eine Familie: `serif` (Georgia, DejaVu Serif). Keine Webfonts, keine zweite Schrift.
- Hierarchie über Größe, Fettung und `maroon`, nicht über Schriftwechsel: `page-title` → `section-title` → `guide-h1` (mit 3px-Unterstrich) → `guide-h2` → `guide-h3`.
- Fließtext `body` 16px/1.5. Kursiv trägt Bedeutung: Regelzitate, Aufstellungshinweise, Untertitel (`subtitle`), Hinweise (`hint`), Bildunterschriften (`caption`).
- Versalien nur für Zonen-Etiketten („SPIELER 1“) und Ansichts-Beschriftungen (`eyebrow`, +.08em).
- Zahlen in Tabellen und Reglern tabellarisch (`font-variant-numeric: tabular-nums`).

## Abstände, Rahmen, Radien

- Werte stammen 1:1 aus dem Code und sind nicht auf ein Raster gerundet: `space-4` … `space-26`, dazu `scale` = 1 Zoll auf dem Brett (13px).
- Rahmen statt Schatten: Panels `border-panel`, Akkordeon `border-piece`, Callouts `border-callout` mit 4–5px linker `maroon`-Kante (`border-accent`, `border-accent-wide`).
- Radien klein: `radius-4` für Flächen und Buttons, `radius-3` für Eingaben, `radius-6` für Geländestücke und Tab-Oberkanten, `radius-round` für Kreise.
- Schatten nur auf dem Brett: `shadow-piece`, `shadow-piece-drag`, `shadow-treasure`.

## Layout

- Kopf, Tab-Leiste und Reiter max. `content-max` (1320px), zentriert; Leitfaden und BASE als Blatt max. `sheet-max` (900px).
- Kartenbau: Palette (210px) links, Brett rechts, Lücke `space-22`.
- Unter `bp-mobile` (720px): Seitenrand `space-12`, Tabs gleich breit, Palette als Raster, Zonen-Legende unter dem Brett, Tabellen und Brett scrollen in sich.

## Zustände

- Fokus: 3px `focus`-Umriss mit 2px Abstand (Akkordeon-Kopf: innen, -3px).
- Hover füllt: umrandete Elemente (Tab, Preset, Link-Button) werden `maroon` mit weißem Text.
- Aktiver Pinsel: `maroon`-Rahmen + `shadow-brush-active`. Ungültige Eingabe: `maroon`-Rahmen + `shadow-invalid`.
- Deaktiviert: `disabled-bg` mit `disabled-ink`, Cursor `not-allowed`.
- Bewegung: nur die Akkordeon-Pfeildrehung (.18s).

## Ikonografie und Bilder

- Kein Logo und kein Icon-Set: der Name „Battle March“ steht in `page-title`.
- Diagramme (Missionen, Aufstellungszonen) sind schlichte Inline-SVGs: Grund `diagram-bg`, Hilfslinien `diagram-line`, Messlinien `diagram-stroke`, Ziele als Kreise in `objective` mit weißem Rand, Beschriftung 10–11px.
- Gelände-Texturen entstehen nur aus CSS-Verläufen (siehe TerrainPiece), nie aus Bildern.

## Nicht übernommen

- Kein dunkles Theme – die Quelle hat nur das helle Pergament-Theme.
- Keine Schriftdateien – die Quelle nutzt Systemschriften.
- Komponenten als statische Vorschauen mit `components/bundle.css`; die Quelle ist eine einzelne HTML-Datei ohne Komponentenbibliothek, daher gibt es kein JS-Bundle.

---

Live-Version: https://claude.ai/artifact/9JaG42wXX42K3M8rcf6VYW
