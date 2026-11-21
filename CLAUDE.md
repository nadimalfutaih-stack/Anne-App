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
- Kategorie kommt NUR aus dem Titel, nie aus der Uhrzeit (Anne trägt Zeiten willkürlich ein). Ein Eintrag kann in MEHRERE Kästchen (Abhaken gilt überall). Schlagwörter in `HINTS`: `words` = Teilwort, `whole` = nur ganzes Wort, `except` = hebt das Kästchen auf, `weak` = zählt nur, wenn sonst nichts passt. Ohne Treffer: Sonstiges.
- Kindernamen Hermine und Wim zählen als Kinder.
- **Fragefeld statt Sprachknopf** (seit 21.11.2026): unter den Kacheln ein Schreibfeld „Frag mich … z. B. Was muss ich morgen kaufen?“ + Knopf „Los“. Anne tippt oder diktiert über die iPhone-Tastatur (🎤 der Tastatur oder Wispr Flow). „Los“/Eingabetaste → `verstehen()` öffnet Tag/Kästchen oder sucht das Wort; sonst „Das habe ich nicht verstanden …“. Kein eigenes Mikrofon und keine Safari-Spracherkennung mehr. Eingabefeld mind. 16 px Schrift (sonst zoomt das iPhone).
- Eintragen in den Kalender läuft über Siri („Hey Siri, erstelle einen Termin morgen: Milch kaufen“). Kurzbefehl „Eintragen“ ist aufgegeben (scheiterte an „Datum anpassen: Keine Konvertierung von Text in Zahl“). Nadim nicht wieder damit belasten, außer er fragt selbst. Standardkalender auf Annes iPhone sollte „Kalender“ sein.
- Neue Einträge: localStorage `meintag-gesehen` merkt gesehene Einträge (Kennung Titel@Start, geänderte gelten als neu). Hinweis NUR im Kästchen: gelber Rand + „N NEU“; in der Liste oben, gelb hinterlegt, „NEU“-Schild. Kein gelber Streifen oben, keine Punkte auf Morgen/Danach (seit 21.11.2026 auf Nadims Wunsch). Kästchen öffnen = gesehen. Erstes Öffnen: nichts neu.
- Testlisten für die Zuordnung liegen in `tests/` (Format `Titel | Kategorie1, Kategorie2`, `-` = Sonstiges). Nach Änderungen an `HINTS` alle Listen prüfen.

## Symbol

- Home-Bildschirm-Symbol: Tagebuch „Nadim / Anne“ in Bordeaux, `prototyp/symbole/tagebuch-bordeaux.png` (Kurzbefehl → „Zum Home-Bildschirm“ → Foto auswählen).

Projektnotizen liegen in Notion unter Notizen → „Nadim – Neue Apps“ → „Anne Kalender-App“.
