# Board

Die Spielmatte im Kartenbau: 48×36 Zoll als Raster, ein Zoll = `scale`.

- Außen `bm-board-outer` (`beige`, `border-accent` in `maroon`), innen `bm-board` mit `border-strong`.
- Raster aus vier CSS-Verläufen: `grid-minor` je Zoll, `grid-major` alle 6 Zoll.
- Zonen werden als Zellen (1 Zoll) in `zone-p1`/`zone-p2`/`zone-nml` auf einem Canvas gemalt.
- Geländefreier 16"-Kreis (`bm-no-terrain`): `maroon`-Schraffur über `blush-veil`, kursive Beschriftung.
- Schätze (`bm-treasure`): goldene Münze aus `treasure-*`, `shadow-treasure`.
- Ebenen: Kreis `z-circle` < Stücke `z-piece` < Marker `z-marker` < Koordinatenpunkt `z-coord-dot`.
- Das Brett scrollt waagerecht in sich, nie die Seite.
