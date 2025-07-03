1. Modul MySql.Data.MySqlClient importieren
2. Connection mittels MySqlConnection erstellen
3. Connection öffnen
4.1. Select:
4.1.1. SQL Befel als String anlegen
4.1.2. Einen neuen Command erstellen
4.1.3. Command.ExecuteReader() ausführen und Ergebnis speichern
4.1.3. Mit einer Schleife das Ergebnis durchgehen
4.2. Insert:
4.2.1. Neuen Command erstellen
4.2.2. Command.CommandText mit Insertbefehl füllen
4.2.3. Mit den Befehl Command.ExecuteNonQuery() den Inserbefehl ausführen
5. Connection schließen

Was hat gut funktioniert:
* Das komplette anlegen und abfragen lief reibungslos

Was lief stockend:
* Nichts

Welche Unterschiede sind Ihnen zwischen Python und C# aufgefallen:
* Die befehle heißen anderst
* Die Befüllung des CommandText gibt es in Python nicht
* Ansonsten sind sie sich ähnlich