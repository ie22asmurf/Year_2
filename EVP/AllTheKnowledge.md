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




_____________________________

## Netzwerke
### DHCP
Dynamic Host Configuration Protocol

### DORA
Discover    | Offer     | Response  | Acknowledge
Client      | Server    | Client    | Server

### Relay (Agent)
Ein Relay-Agent ist eine Netzwerkkomponente, die in einem Computernetzwerk dazu dient, DHCP (Dynamic Host Configuration Protocol) Nachrichten zwischen Client-Geräten und DHCP-Servern zu vermitteln. DHCP ist ein Protokoll, das dazu dient, IP-Adressen und andere Netzwerkkonfigurationseinstellungen automatisch an Geräte in einem Netzwerk zu verteilen.

Hier sind die grundlegenden Funktionen eines Relay-Agents:

1. Weiterleitung von DHCP-Nachrichten:
Der Relay-Agent empfängt DHCP-Anforderungen von Client-Geräten, die im Netzwerk keine zugewiesene IP-Adresse haben. Anschließend leitet er diese Anforderungen an einen oder mehrere DHCP-Server weiter.

2. Unterstützung in verschiedenen Subnetzen:
Wenn sich Client-Geräte und DHCP-Server in verschiedenen Subnetzen befinden, ist der Relay-Agent notwendig. Er trägt dazu bei, DHCP-Anforderungen über Subnetzgrenzen hinweg zu vermitteln, indem er die Anforderungen an die DHCP-Server weiterleitet und sicherstellt, dass die Antworten wieder an die entsprechenden Subnetze zurückgehen.

3. Hinzufügen von Informationen:
Der Relay-Agent kann zusätzliche Informationen zu den DHCP-Nachrichten hinzufügen. Dies kann beispielsweise die Identifikation des Relay-Agents selbst oder andere Informationen sein, die für die korrekte IP-Adresszuweisung relevant sind.

4. Broadcast-Umgebung überwinden:
DHCP verwendet normalerweise Broadcast-Nachrichten für die IP-Konfiguration. In Umgebungen, in denen Broadcasts nicht über Subnetze hinweg weitergeleitet werden, spielt der Relay-Agent eine entscheidende Rolle, indem er DHCP-Nachrichten anstelle von Broadcasts verwendet.

Insgesamt ermöglicht der Relay-Agent eine effiziente und reibungslose IP-Adresszuweisung in Netzwerken mit mehreren Subnetzen, indem er DHCP-Anforderungen übermittelt und die Antworten an die entsprechenden Clients zurückleitet.

### VLAN
Ein VLAN (Virtual Local Area Network) ist eine Technologie, die es ermöglicht, ein physisches Netzwerk in mehrere virtuelle Netzwerke zu segmentieren. Diese Segmentierung erfolgt auf der Data-Link-Schicht (Layer 2) des OSI-Modells. Hier sind die grundlegenden Punkte, die VLANs charakterisieren:

1. Logische Gruppierung:
VLANs ermöglichen die logische Gruppierung von Geräten in einem Netzwerk, unabhängig von ihrer physischen Position. Geräte, die sich in verschiedenen Teilen des Netzwerks befinden, können denselben VLAN-Zugehörigkeitsstatus haben.

2. Isolierung und Broadcast-Domänen:
Geräte innerhalb desselben VLANs können direkt miteinander kommunizieren, als ob sie sich im selben physischen Netzwerk befinden würden. Gleichzeitig sind VLANs so konzipiert, dass sie den Broadcast-Verkehr innerhalb des VLANs begrenzen, was die Effizienz des Netzwerks verbessert.

3. Flexibilität und Skalierbarkeit:
Durch die Verwendung von VLANs können Netzwerkadministratoren Netzwerke leicht anpassen und skalieren, ohne physische Änderungen vornehmen zu müssen. Neue logische Gruppen können einfach durch die Konfiguration von VLANs erstellt werden.

4. Sicherheit:
VLANs ermöglichen es, den Datenverkehr zwischen verschiedenen logischen Gruppen zu isolieren. Dies trägt zur Netzwerksicherheit bei, da Geräte in einem VLAN normalerweise keinen direkten Zugriff auf Geräte in anderen VLANs haben.

5. Effiziente Ressourcennutzung:
Durch die Möglichkeit, mehrere VLANs auf einem einzigen physischen Switch zu haben, kann die Hardware effizienter genutzt werden. Dies ist besonders nützlich in Umgebungen mit vielen logischen Gruppen, wie sie in großen Unternehmen oder Rechenzentren vorkommen.

Insgesamt bieten VLANs eine flexible und effiziente Möglichkeit, Netzwerke zu organisieren und zu verwalten, indem sie eine logische Trennung auf der Data-Link-Ebene ermöglichen.


### Trunk Connections
In Netzwerken bezieht sich eine "Trunk-Verbindung" auf eine Verbindung zwischen zwei Netzwerkgeräten, die so konfiguriert ist, dass sie den Verkehr mehrerer VLANs übertragen kann. Trunk-Verbindungen sind besonders relevant, wenn Sie VLANs in Ihrem Netzwerk verwenden. Hier sind die wichtigsten Punkte zur Trunk-Verbindung:

1. Übertragung von mehreren VLANs:
Eine Trunk-Verbindung ermöglicht die Übertragung von Datenverkehr mehrerer VLANs über dieselbe physische Verbindung. Das ist wichtig, wenn die Verbindung zwischen zwei Switches, Routern oder anderen Netzwerkgeräten den Datenverkehr für mehrere logische Gruppen (VLANs) übertragen soll.
2. Tagging der Datenpakete:
Damit die Trunk-Verbindung den Verkehr mehrerer VLANs erfolgreich übertragen kann, werden den Datenpaketen Tags hinzugefügt. Ein Tag ist eine Kennzeichnung im Datenpaket, die angibt, zu welchem VLAN das Paket gehört. Dieses Tagging ermöglicht es den Geräten am anderen Ende der Trunk-Verbindung, die Daten den entsprechenden VLANs zuzuordnen.
3. Verwendung von IEEE 802.1Q:
Der Standard, der am häufigsten für das Tagging von VLAN-Informationen in Trunk-Verbindungen verwendet wird, ist IEEE 802.1Q. Dieser Standard definiert, wie die VLAN-Informationen in den Ethernet-Frames eingebettet werden.
4. Effiziente Nutzung der Bandbreite:
Durch die Kombination des Datenverkehrs mehrerer VLANs auf einer einzigen physischen Verbindung ermöglicht eine Trunk-Verbindung eine effizientere Nutzung der Netzwerkbandbreite. Das ist besonders wichtig in Umgebungen mit vielen VLANs und großem Datenverkehr.
5. Konfiguration an den Endpunkten:
Beide Enden der Trunk-Verbindung müssen so konfiguriert sein, dass sie die gleichen VLAN-Informationen verstehen. Das schließt die richtige Konfiguration von Tagging und die Definition der erlaubten VLANs auf der Verbindung ein.

Zusammengefasst ermöglichen Trunk-Verbindungen die effiziente Übertragung von Datenverkehr mehrerer VLANs über eine einzelne physische Verbindung, indem sie Tagging-Mechanismen verwenden, um die VLAN-Informationen zu übermitteln. Dies ist besonders wichtig in Netzwerken, in denen die Segmentierung des Datenverkehrs nach logischen Gruppen (VLANs) erforderlich ist.


### Frames
Siehe TCP/IP:
über den Frame wird die Ziel-Macadresse verwendet.
Wenn alle Bits der MAC auf 1 sind, ist es ein Broadcast im gleichen LAN (bzw VLAN)


### Abgrenzung zwischen Abteilungsnetzen
- Nutzen von Switches:
    - Auf OSI-2
    - 3 ist möglich, aber quatsch:
        - Jede Abteilung bräuchte eigenen Router
    - Auf der Switchlayer kann man VLANs einrichten
    - Bei den Trunk-Verbindungen werden die Frameheader gekennzeichnet, dies nutzen VLANs um die Pakete zuzuordnen

    - Wenn der Switch den Frame auf den Trunk schaltet, wird der Frame getaggt (Tag enthält Informationen über das Urpsrungs-VLAN)
    - Der empfangende Switch braucht diesen Tag (Auch VLAN-ID), um Berechtigungen und Antwortadresse zuordnen zu können
        - Nur notwendig wenn man Trunkverbindungen nutzt!