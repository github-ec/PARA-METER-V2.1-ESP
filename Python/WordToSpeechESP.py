import pyttsx3, time, re

# Stand 2026/03/02 - Anpassung für ESP32 Header (ohne PROGMEM)
##############################
WordListFile = r"WordLists.h"
mp3Path      = r'C:\temp\mp3\\' # Backslash am Ende für Windows-Pfad
##############################

engine = pyttsx3.init()
# Stimme einstellen (Index oder Name ggf. anpassen)
voices = engine.getProperty('voices')
for voice in voices:
    if "German" in voice.name or "Deutsch" in voice.name:
        engine.setProperty('voice', voice.id)
        break

def get_word_arrays_from_file(filepath):
    """
    Liest die neue WordLists.h ein. Sucht nach Zeilen, die mit 
    'static const char p' beginnen und extrahiert den Inhalt zwischen Anführungszeichen.
    """
    all_categories = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # Filter: Suche nach Zeilen wie 'static const char p0[] = "..."'
                if line.startswith("const char p") and '"' in line:
                    # Extrahiere alles zwischen den ersten und letzten Anführungszeichen
                    match = re.search(r'"([^"]*)"', line)
                    if match:
                        content = match.group(1)
                        # Splitten bei '/' und leere Einträge ignorieren
                        words = [w.strip() for w in content.split('/') if w.strip()]
                        if words:
                            all_categories.append(words)
                    
        return all_categories

    except FileNotFoundError:
        print(f"Fehler: {filepath} nicht gefunden.")
        return []

wort_sammlung = get_word_arrays_from_file(WordListFile)

if not wort_sammlung:
    print("Keine Kategorien gefunden! Prüfe das Dateiformat.")
else:
    total_count = sum(len(kat) for kat in wort_sammlung)
    print(f"Insgesamt {len(wort_sammlung)} Kategorien mit {total_count} Begriffen geladen.\n")

    start_zeit = time.time()

    for kat_idx, kategorie in enumerate(wort_sammlung):
        print(f"Verarbeite Kategorie {kat_idx} ({kategorie[0]}) mit {len(kategorie)} Begriffen...")
        
        for word_idx, entry in enumerate(kategorie):
            # Dateiname Format: KKWW_Begriff.mp3 (K=Kategorie, W=Wort-Index)
            name = "{:02d}{:02d}_{}.mp3".format(kat_idx, word_idx, entry)
            # Bereinigung des Dateinamens (entfernt Sonderzeichen, die Windows nicht mag)
            clean_name = "".join([c for c in name if c.isalnum() or c in (' ', '.', '_')]).rstrip()
            fname = mp3Path + clean_name
            
            print(f" Generiere: {clean_name}")
            engine.save_to_file(entry, fname)
            
    engine.runAndWait()
    print("\nFertig! Dauer: {:.2f} Sekunden".format(time.time() - start_zeit))
