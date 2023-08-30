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

### Backup
* Unterschied zu RAID 1:  
    System ("Frontend") erkennt 2 verschiedene Speicher, waehrend ein RAID als ganzes erkannt wird

##### Strategien
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
