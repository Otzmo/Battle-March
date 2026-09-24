# FormField

Beschriftete Eingabe mit Bereichsangabe, dazu Checkbox und eine kompakte Variante.

- Label in `maroon` .95rem über dem Feld; Feld `surface`, `control-border`, `radius-3`, 1rem.
- Bereich darunter in `bm-range` (.72rem, `ink-soft`), z. B. „20–200 mm“.
- Ungültig (`is-invalid`): Rahmen `maroon` + `shadow-invalid`; Fehlermeldung als fetter `maroon`-Text.
- Kompakt (`bm-field--compact`, Kartenbau-Palette): Label .72rem in `ink-muted`, Feld .8rem.
- Einheiten immer im Label: „(Zoll)“, „(mm)“.
