# Accordion

Aufklappbarer Block für lange Regelteile (Missionen, Zufallsereignisse, Zauberlehren).

- Rahmen `border-piece` in `maroon`, Körper `surface`, Kopf `tan` (Hover `tan-hover`), Text `maroon` fett 1.02rem.
- Pfeil `▸` rechts, dreht sich offen um 90° (.18s; bei reduzierter Bewegung ohne Übergang).
- Kopf ist ein `button` mit `aria-expanded` und `aria-controls`; Körper `role="region"`, geschlossen `hidden`.
- Titel: „Mission 1 – Schätze“, „Tabelle der Zufallsereignisse (2W6)“ – Nummer, Halbgeviertstrich, Name.
