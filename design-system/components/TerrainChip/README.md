# TerrainChip

Ziehbarer Eintrag der Gelände-Palette: Farbfeld, Name, Maße in Zoll.

- Weiß, `border-chip` in `ink-edge`, `radius-5`; Cursor `grab`/`grabbing`, `touch-action:none`.
- Farbfeld 26×20 in der Terrain-Farbe (`terrain-*`), Name fett .82rem, Maße `B x T"`.
- Standardsatz: Wald 6x10, Gebäude 6x8, Hügel 8x6, Ruine 7x7, Feld 6x8, See 6x10, Turm 8x8.
- Palette ist 210px breit; mobil ein Raster mit `minmax(140px,1fr)`.
