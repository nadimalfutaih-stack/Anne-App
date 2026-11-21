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
- Angezeigt werden nur Annes Kalender: Kalender, Privat, Arbeit, Nadim, Unbenannter Kalender (Nadims Standardkalender, mit Anne geteilt; dorthin gehen neue Einträge von seinem iPhone).

## Festgelegtes Design

- Farbe „Salbei“, immer hell, kein Dunkelmodus, kein Sonnenlicht-Verlauf.
- Kompakter Kopf (Heute + roter Tageskreis + Datum in einer Zeile), hellgelbe Karte „Als Nächstes“.
- Neun Listen-Kacheln (3 × 3): Einkauf, Geschenke, Kinder, Unterlagen, Arzt, Haushalt, Treffen, Für mich, Sonstiges. Antippen zeigt nur diese Einträge des gewählten Tages, abhakbar.
- „Heute“, „Morgen“ und „Danach“: zuerst nur die Kacheln, Einträge erst nach Antippen einer Kachel.
- Kategorie kommt NUR aus dem Titel, nie aus der Uhrzeit (Anne trägt Zeiten willkürlich ein). Ein Eintrag kann in MEHRERE Kästchen (Abhaken gilt überall). Schlagwörter in `HINTS`: `words` = Teilwort, `whole` = nur ganzes Wort, `except` = hebt das Kästchen auf, `weak` = zählt nur, wenn sonst nichts passt. Ohne Treffer: Sonstiges.
- Kindernamen Hermine und Wim zählen als Kinder.
- **Fragefeld statt Sprachknopf** (seit 21.11.2026): unter den Kacheln ein Schreibfeld „Frag mich … z. B. Was muss ich morgen kaufen?“ + Knopf „Los“. Anne tippt oder diktiert über die iPhone-Tastatur (🎤 der Tastatur oder Wispr Flow). „Los“/Eingabetaste → `verstehen()` öffnet Tag/Kästchen oder sucht das Wort; sonst „Das habe ich nicht verstanden …“. Kein eigenes Mikrofon und keine Safari-Spracherkennung mehr. Eingabefeld mind. 16 px Schrift (sonst zoomt das iPhone).
- **Eintragen ohne Siri** (seit 21.11.2026, Nadim will kein Siri): Text im Fragefeld, der keine Frage ist (nicht mit Was/Wann/Wo/Zeig … beginnt), öffnet die Karte „Eintragen“ (Text, Tag Heute/Morgen/Übermorgen/Wochentag). Großer Knopf „✓ Eintragen“: speichert NUR in der App (localStorage `meintag-eigene`, nur auf diesem iPhone), steht sofort im passenden Kästchen, KEIN Apple-Fenster (das Fenster störte Nadim). Kleiner Knopf „📅 Auch in den Apple-Kalender“: speichert genauso und öffnet zusätzlich eine Kalender-Datei (.ics, ganztägig) → Apple-Fenster „Hinzufügen“. Dazu „Nur suchen“ / „Abbrechen“. Kommt derselbe Eintrag (gleicher Titel + Tag) später aus dem Kalender, wird die eigene Kopie entfernt; vergangene eigene Einträge verschwinden. Eine Webseite kann NICHT still in den Apple-Kalender schreiben. Kurzbefehl „Eintragen“ ist aufgegeben – Nadim nicht wieder damit belasten.
- **Listen aufteilen** (`teile()`, seit 21.11.2026): Ein Eintrag mit mehreren Dingen wird in einzelne Einträge zerlegt (je eigenes Kästchen, einzeln abhakbar). Kalender-Einträge: nur Spiegelstrich-Listen (beginnt mit „-“ oder ≥ 3 Teile; „Arzt - Wim“ bleibt ganz), Kennung `Titel@Start#n`. Im Fragefeld zusätzlich bei Komma/Semikolon und bei „und“ – außer bei Personen/Verabredungen (mit/bei/von …, Kinder- oder Treffen-Wörter: „Hermine und Wim abholen“ bleibt ganz). Die Karte zeigt vorab „N einzelne Einträge: …“.
- Abhaken: abgehakte Einträge bleiben an ihrem Platz stehen (durchgestrichen), damit man mehrere hintereinander abhaken kann; erst beim nächsten Öffnen des Kästchens stehen sie unten bei „Erledigt“ (Nadims Wunsch 21.11.2026).
- Löschen: einen ERLEDIGTEN Eintrag nach links wischen – sowohl frisch abgehakte (die noch an ihrem Platz stehen) als auch die in der Liste „Erledigt“ (weit = gelöscht, ein Stück = roter Knopf „Löschen“; Touch-Ereignisse, weil Zeiger-Ereignisse auf Nadims iPhone nicht reagierten), danach „Gelöscht · Rückgängig“. Eigene Einträge werden wirklich gelöscht; Kalender-Einträge nur in „Mein Tag“ ausgeblendet (localStorage `meintag-weg`), im Apple-Kalender bleiben sie. Offene Einträge sind nicht wischbar.
- Safari-Adresszeile zeigt „nadimalfutaih-stack.github.io“: bleibt so (Nadims Entscheidung 21.11.2026).
- Neue Einträge: localStorage `meintag-gesehen` merkt gesehene Einträge (Kennung Titel@Start, geänderte gelten als neu). Hinweis NUR im Kästchen: gelber Rand + „N NEU“; in der Liste oben, gelb hinterlegt, „NEU“-Schild. Kein gelber Streifen oben, keine Punkte auf Morgen/Danach (seit 21.11.2026 auf Nadims Wunsch). Kästchen öffnen = gesehen. Erstes Öffnen: nichts neu.
- Testlisten für die Zuordnung liegen in `tests/` (Format `Titel | Kategorie1, Kategorie2`, `-` = Sonstiges). Nach Änderungen an `HINTS` alle Listen prüfen.

## Symbol

- Home-Bildschirm-Symbol: Tagebuch „Nadim / Anne“ in Bordeaux, `prototyp/symbole/tagebuch-bordeaux.png` (Kurzbefehl → „Zum Home-Bildschirm“ → Foto auswählen).

Projektnotizen liegen in Notion unter Notizen → „Nadim – Neue Apps“ → „Anne Kalender-App“.
