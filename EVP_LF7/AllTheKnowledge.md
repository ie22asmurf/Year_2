# EvP LF7
### Wiederholung (2023/8/9)
##### Einheiten
Kibi * 2^10 = Mebi
-> Gibi -> Tebi -> Pebi -> Exbi

Kibi * 2^30 = Tebi

#### RAID
* Datastryping
    - Daten werden nicht auf die erste, wenn sie voll ist auf die zweite Festplatte geladen,  
    sondern in Datenblöcken direkt auf die verschiedenen Festplatten verteilt
* Parity/Parität

____________
____________

## Backup
* Unterschied zu RAID 1:  
    System ("Frontend") erkennt 2 verschiedene Speicher, waehrend ein RAID als ganzes erkannt wird

### Strategien
* Full Backup
    - Kompletter Datenbestand wird gesichert
* Incremental Backup
    - Das Backup beinhaltet alle Aenderungen seit dem letzten Backup einer Art
    - In regelmaessigen Abstaenden wird ein zusaetzliches, sehr kleines Backup gemacht
* Differential Backup
    - Das Backup beinhaltet alle Aenderungen seit dem letzten Full Backup
    - In regelmaessigen Abstaenden wird ein zusaetzliches Backup gemacht
  

* On-Premise Backup
    - In-House Backup
* Off-Site Backup
    - Out-House Backup
* Cloud Backup
    - Backup wo auch immer, erreichbar ueber ein Internet
* Oft auf Magnetbändern:
    - Vorteil: Manipulation nicht ohne weiteres möglich

### Technologien
Unterscheiden sich abhängig vom Betriebssystem

#### Microsoft
Unter Microsoft wird ein __Archivbit__ als Attribut einer Datei festgelegt. Daran erkennt die Backup-Software, ob sich die Datei seit dem letzten Backup verändert hat.

#### Unix
Unter Unix wird der __Timestamp__ der Datei verglichen. Für Microsoft-Dateien gibt es Workarounds, beispielsweise das Executable-Bit (xbit) anstelle des Archivbits

#### Snapshots
* Kein richtiges Backup
* Nützlich bei VMs
* Aktueller Zustand eines Systems wird kopiert, ist nicht ohne weiteres auf anderes System übertragbar -> Kein Backup


## Vorsorge Stromausfall
#### USV
<!-- Muss wahrscheinlich ueberarbeitet werden, hatte nen Kater -->
Unterbrechungsfreie Stromversorgung
- Soll Systeme ueber einen gewissen Zeitraum (Minuten bis Stunden) mit Strom abdecken, beispielsweise ueber einen zusaetzlichen Generator
    * Systeme muessen nicht zwingend heruntergefahren werden, crashen erstmal nicht und sind arbeitsfaehig
- Auch Vorteile wie Ueberspannungsschutz uvm

Nach Norm EN 62040
| | |
|---------|-------|
| Klasse 1 | VFI (Voltage and Frequency Independent) |
| Klasse 2 | VI (Voltage Independent) |
| Klasse 3 | VFD (Voltage and Frequency Dependent) |



#### Füsik
- Aus den zwei Anschluessen der Steckdose kommen Wechselspannungen (Sinusförmig, gegeneinander um eine halbe Phase versetzt)
    * Durch diese zwei Wechselspannungen wird zu einer Gleichspannung transformiert
