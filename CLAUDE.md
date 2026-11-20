# Anne-App („Mein Tag“)

Eigenständiges Projekt von Nadim für seine Frau Anne. Hat nichts mit der Wein-App oder „Meine Expedition“ zu tun.

## Arbeitsregel (wichtig)

- Vor jeder Änderung kurz auf Deutsch schreiben, **was** gemacht wird (was sich auf dem Bildschirm ändert und wo).
- Bei Design-Änderungen vorher ein Muster zeigen.
- **Erst nach Nadims „ja“ umsetzen.** Rückfragen und Erklärungen dürfen direkt beantwortet werden.
- Einfach und Schritt für Schritt erklären; Nadim ist kein Techniker.

## Was die App ist

- `prototyp/index.html`: die Web-App „Mein Tag“ (Tagesübersicht aus Annes Apple-Kalender).
- `docs/index.html`: daraus erzeugt mit `python3 scripts/build-pages.py`; wird über GitHub Pages ausgeliefert: https://nadimalfutaih-stack.github.io/Anne-App/ (Branch `claude/serene-hopper-pbi0tg`, Ordner `/docs`). Nach jeder Änderung an `prototyp/index.html` neu erzeugen.
- Daten kommen vom iPhone-Kurzbefehl „Mein Tag“ über `#d=<Base64>`; eine Zeile pro Termin: `Titel;Start;Ende;Ganztägig;Kalender`. Datumsformat vom iPhone z. B. `20/11/2026, 06:00`. Der Teil nach `#` geht nicht an den Server.
- Angezeigt werden nur Annes Kalender: Kalender, Privat, Arbeit, Nadim.

## Festgelegtes Design

- Farbe „Salbei“, immer hell, kein Dunkelmodus, kein Sonnenlicht-Verlauf.
- Kompakter Kopf (Heute + roter Tageskreis + Datum in einer Zeile), hellgelbe Karte „Als Nächstes“.
- Neun Listen-Kacheln (3 × 3): Einkauf, Geschenke, Kinder, Unterlagen, Arzt, Haushalt, Treffen, Für mich, Sonstiges. Antippen zeigt nur diese Einträge des gewählten Tages, abhakbar.
- „Heute“, „Morgen“ und „Danach“: zuerst nur die Kacheln, Einträge erst nach Antippen einer Kachel.
- Kategorie kommt NUR aus dem Titel, nie aus der Uhrzeit (Anne trägt Zeiten willkürlich ein). Schlagwörter in `HINTS`: `words` = Teilwort, `whole` = nur ganzes Wort. Vorrang: Unterlagen → Arzt → Geschenke → Kinder → Treffen → Für mich → Einkauf → Haushalt, sonst Sonstiges.

## Symbol

- Home-Bildschirm-Symbol: Tagebuch „Nadim / Anne“ in Bordeaux, `prototyp/symbole/tagebuch-bordeaux.png` (Kurzbefehl → „Zum Home-Bildschirm“ → Foto auswählen).

Projektnotizen liegen in Notion unter Notizen → „Nadim – Neue Apps“ → „Anne Kalender-App“.
