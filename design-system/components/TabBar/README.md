# TabBar

Die klebende Reiter-Leiste oben auf der Seite, die zwischen Leitfaden und Werkzeugen wechselt.

- Tabs sind Karteikarten: `border-strong` in `maroon`, oben `radius-6`, unten gerade.
- Aktiv (`aria-selected="true"`) und Hover: Fläche `maroon`, Text weiß. Inaktiv: `beige` mit `maroon`-Text.
- Die Leiste klebt (`position:sticky`, `z-tabbar`) und trägt `page-bg`, damit darunter scrollender Inhalt verschwindet.
- Unter `bp-mobile` teilen sich die Tabs die Breite gleichmäßig (`flex:1`, 10px 8px Innenabstand).
- Tastatur: Pfeiltasten wechseln, nur der aktive Tab hat `tabindex="0"`; Fokusring `focus`.

Der Verbraucher liefert: die Tab-Beschriftungen (kurz, ein bis zwei Wörter) und die zugehörigen `tabpanel`-Container.
