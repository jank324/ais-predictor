# AIS-Predictor

Did you ever want to know when and where your ship arrives? Worry no more ...

## Starten der App - Online Version

Die Online-Version der App, wie wir sie präsentiert haben, ist auf Heroku
gehostet. Der Broker und die Agents laufen auf je einem sogenannten Dyno, einer
eigenen Maschine. Die App ist erreichbar unter 'ais-predictor.herokuapp.com'.
Zu beachtet ist dabei, dass die Dynos nach 30 Minuten Inaktivität in einen
Schlafmodus wechseln. Für den Broker bedeutet das, dass es einfach nur ein
wenig länger dauert, bis die Webseite lädt. Für die Agents bedeutet der
Schlafmodus aber, dass man ein paar mal Predictions anstoßen muss, bis sie alle
aufwachen. Dazu öffnen Sie einfach die Webapp, laden eine .arff-Datei und
führen für ein paar Predictions auf beiden Strecken aus. Führen Sie die
Predictions auf möglichst frühen Datenpunkten aus, damit alle Agents aufgeweckt
werden.

Wenn jemand das System selber aufsetzen möchte, dann muss nur der Ordner des
jeweiligen Agents bzw. des Brokers auf die Maschine kopiert werden, auf der der
jeweilige Teil des Programms laufen soll. Sofern Docker installiert ist, kann
man dann einfach das Docker Image builden und starten. Im Source Code des
Brokers müssen ggfs. die URLs der Agents eingetragen werden.

Ebenso lässt sich das Programm einfach um Agents und Routen erweitern, indem
man einen Agent kopiert, die Konfigurationsdatei anpasst und die Machine
Learning Modelle austauscht. Der neue Agent muss dann beim Broker unter der
entsprechenden Route mit seiner URL / IP-Adresse registriert werden.

## Preprocessing der Daten
Die Daten wurden in Jupyter Notebooks (.ipynb Dateien) bereinigt. Die Notebooks
finden Sie im ordner 'data'. Damit Sie die Notebooks ansehen können, ohne
Jupyter Notebook zu installieren, haben wir zu jedem Notebook eine HTML-Datei
mit dem gleichen Namen generiert.
Die Notebooks mit 'filter' im Namen wurden zum bereinigen benutzt. Aus ihnen
wurden die gereinigten Daten dann als .pkl Dateien exportiert, damit Sie von
den 'learning' Notebooks für das Training benutzt werden können.