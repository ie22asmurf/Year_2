# Schulprojekt Raspberry Pi
If you don't know how to handle markdown, go to:  
https://markdownlivepreview.com/  
and copy/paste this file's content into the online editor
## Einrichten des Raspis
### Download des [Raspberry Pi Imager Installer](https://www.raspberrypi.com/software/)
- [Windows](https://downloads.raspberrypi.org/imager/imager_latest.exe)
- [MacOS](https://downloads.raspberrypi.org/imager/imager_latest.dmg)
- [Ubuntu](https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb)
- Installationsprozess mit der Datei starten

### Boot-SD-Karte erstellen
- Micro-SD an den Computer anschließen
- Raspberry Pi Imager starten
    - Konfiguration:
        - |Feld|Eingabe|
            |--------------|-------------|
            | Choose Device  | Entsprechendes Raspi-Modell       |
            | Choose OS      | Raspberry Pi OS (oder anderes)    |
            | Choose Storage | SD-Karte auswählen                |
            |----------------|---------------------------------------------|
            | Konfiguration  | Hostname, Nutzername, Passwort, Netzwerk einrichten  |
    - Installationsprozess starten
    - Auf Abschluss warten

### Raspi booten
- Micro-SD in Raspi stecken
- Raspi an Strom anschließen
    - Erfolg erkennbar durch rote Lampe: Stromversorgung
- Boot läuft automatisch durch 
    - Prozess erkennbar an grüner Lampe: Datenaktivität

### Zugriff auf Raspi
<details>
<summary>
Via SSH
</summary>

Voraussetzungen:
- Computer im gleichen Netzwerk
- Hostname, Benutzername und Passwort des Raspis bekannt

Prozess auf dem Computer:
- Powershell öffnen
```PowerShell
ssh <hostname>@<nutzername>
<Passwort>
```

Nun ist die Verbindung mit dem Raspi auf der Konsole hergestellt

</details>
<details>
<summary>
Via Capture Card
</summary>

Voraussetzungen:
- Hardware:
    - Capture-Card
    - MikroHDMI- auf HDMI-Kabel (statt HDMI gewünschter Capture-Card-Input möglich)
    - Maus/Tastatur für Raspi
- Software:
    - Kamera-App o.ä.

Prozess:
- Verkabeln:
    - Maus, Tastatur an Raspi anschließen
    - Capture-Card an Computer anschließen
    - MicroHDMI-Kabel an Raspi anschließen
    - Anderes Kabelende an Capture-Card anschließen
- Kamera-App starten, Capture-Card als Input auswählen
- Raspi ist nun bedienbar, Kamera-App fungiert als "Bildschirm" des Raspis
</details>
Die Dokumentation geht ab hier von der Verbindung via Capture-Card aus

### Raspi einrichten
#### Hardware
- Dokumentationen erarbeiten
    - [Raspi-GPIO-Pins](https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm)
    - [Breadboards](https://www.smarthome-tricks.de/esp8266/das-breadboard/)

- Raspi entsprechend der Projektvorgabe verkabeln

#### Software
- Terminal aufrufen (strg + alt + t)
- Updaten des Raspis
    ```shell
    sudo apt update
    sudo apt upgrade
    ```
- Installieren erforderlicher Programme
    ```shell
    sudo apt install python3 -y
    sudo apt install i2c-tools -y
    ```


    



