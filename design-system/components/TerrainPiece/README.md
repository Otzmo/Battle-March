# TerrainPiece

Ein platziertes Geländestück auf dem Brett: Textur, Name, Maße, Dreh- und Löschknopf, Koordinate.

- Größe = Zoll × `scale` (13px). Form `radius-6`, `border-piece` in `ink-edge`, `shadow-piece`; beim Ziehen `shadow-piece-drag` und `z-drag`.
- Texturen nur aus CSS-Verläufen: `tex-forest` (Kronenpunkte), `tex-brick` (Fugen alle 2/3 Zoll; `.ruine`, `.turm` grau), `tex-hill` (Schatten zum Fuß), `tex-field` (Furchen), `tex-water` (Wellen).
- Name `piece-name` + Maße `piece-dims` weiß; auf dem hellen Feld `is-dark` → `text`.
- Mini-Buttons ⟳/× oben rechts (18px Kreise), Koordinaten-Etikett `coord` unten links.
- Roter `bm-coord-dot` sitzt mit seiner Mitte genau auf der Ecke, auf die die Koordinate zeigt.
- Kontrast: Weiß auf Wald (3.3:1), Hügel (3.5:1) und See (3.9:1) liegt unter 4.5:1 – Quellwerte, bewusst beibehalten.
