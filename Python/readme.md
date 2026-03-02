Basis for the following scripts are

* worte.ods: A LibreOffice calc sheet containing categories (column headers) and words in the row below a category column
* worte.csv: The csv export of worte.ods. Make sure to use the colon ; as a separator!

The script

* csvToESPHeaderFile.py reads the CSV file "worte.csv" and creates the header file "WordLists.h" for use with the wordStorage class
* WordToSpeechESP.py reads the header file "WordLists.h" and creates voice files for each word found in the .h file
* changeOriginalToGhost.py scans the folder "original_mp3s", adds a "Ghost" effect to the voice and stores the changed file to the folder "geister_mp3s".

