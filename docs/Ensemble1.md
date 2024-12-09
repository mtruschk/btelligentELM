# Overview for Diagram **Ensemble1**:

![Diagram Ensemble1](../png/Ensemble1.png)
## recognized shapes from b.telligent ADAPT library:

|Shape ID|Shape Type|Label|
|--------|----------|-----|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-1|Hub|Hub|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-2|Satellite|Satellite|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-3|Link|Link|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-7|Hub|Client|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-8|Satellite|Adressdaten|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-9|Link|Link|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-13|Satellite|Finanzdaten|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-14|Hub|Location|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-15|Satellite|Adressdaten|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-20|Hub|Advice|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-21|Satellite|Ermittlung|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-22|Hub|Article|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-23|Satellite|Produktdaten|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-24|Link|Link|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-27|Satellite|Logistikdaten|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-28|Hub|Advice Line|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-29|Satellite|Default|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-33|Link|Link|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-38|Hub|Manufacturer|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-39|Satellite|Default|
|Ensemble1.NiGAJ-zjjn4dBykOqdRH-40|Link|Link|

## recognized connections from b.telligent ADAPT library:

|Source Type|Source Label|Connection Type|Label|Target Type|Target Label|Connection ID|Source ID|Target ID|
|-----------|------------|---------------|-----|-----------|------------|-------------|---------|---------|
|Satellite|Adressdaten|Hub-to-Sat||Hub|Location|Ensemble1.NiGAJ-zjjn4dBykOqdRH-10|Ensemble1.NiGAJ-zjjn4dBykOqdRH-15|Ensemble1.NiGAJ-zjjn4dBykOqdRH-14
|Hub|Location|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-11|Ensemble1.NiGAJ-zjjn4dBykOqdRH-14|Ensemble1.NiGAJ-zjjn4dBykOqdRH-9
|Hub|Advice|Hub-to-Link-1||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-12|Ensemble1.NiGAJ-zjjn4dBykOqdRH-20|Ensemble1.NiGAJ-zjjn4dBykOqdRH-9
|Satellite|Finanzdaten|Hub-to-Sat||Hub|Client|Ensemble1.NiGAJ-zjjn4dBykOqdRH-16|Ensemble1.NiGAJ-zjjn4dBykOqdRH-13|Ensemble1.NiGAJ-zjjn4dBykOqdRH-7
|Satellite|Adressdaten|Hub-to-Sat||Hub|Client|Ensemble1.NiGAJ-zjjn4dBykOqdRH-17|Ensemble1.NiGAJ-zjjn4dBykOqdRH-8|Ensemble1.NiGAJ-zjjn4dBykOqdRH-7
|Hub|Client|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-18|Ensemble1.NiGAJ-zjjn4dBykOqdRH-7|Ensemble1.NiGAJ-zjjn4dBykOqdRH-9
|Satellite|Ermittlung|Hub-to-Sat||Hub|Advice|Ensemble1.NiGAJ-zjjn4dBykOqdRH-19|Ensemble1.NiGAJ-zjjn4dBykOqdRH-21|Ensemble1.NiGAJ-zjjn4dBykOqdRH-20
|Satellite|Default|Hub-to-Sat||Hub|Advice Line|Ensemble1.NiGAJ-zjjn4dBykOqdRH-25|Ensemble1.NiGAJ-zjjn4dBykOqdRH-29|Ensemble1.NiGAJ-zjjn4dBykOqdRH-28
|Satellite|Logistikdaten|Hub-to-Sat||Hub|Article|Ensemble1.NiGAJ-zjjn4dBykOqdRH-30|Ensemble1.NiGAJ-zjjn4dBykOqdRH-27|Ensemble1.NiGAJ-zjjn4dBykOqdRH-22
|Satellite|Produktdaten|Hub-to-Sat||Hub|Article|Ensemble1.NiGAJ-zjjn4dBykOqdRH-31|Ensemble1.NiGAJ-zjjn4dBykOqdRH-23|Ensemble1.NiGAJ-zjjn4dBykOqdRH-22
|Hub|Article|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-32|Ensemble1.NiGAJ-zjjn4dBykOqdRH-22|Ensemble1.NiGAJ-zjjn4dBykOqdRH-24
|Hub|Advice Line|Hub-to-Link-1||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-34|Ensemble1.NiGAJ-zjjn4dBykOqdRH-28|Ensemble1.NiGAJ-zjjn4dBykOqdRH-33
|Hub|Advice|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-35|Ensemble1.NiGAJ-zjjn4dBykOqdRH-20|Ensemble1.NiGAJ-zjjn4dBykOqdRH-33
|Hub|Advice Line|Hub-to-Link-1||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-36|Ensemble1.NiGAJ-zjjn4dBykOqdRH-28|Ensemble1.NiGAJ-zjjn4dBykOqdRH-24
|Satellite|Default|Hub-to-Sat||Hub|Manufacturer|Ensemble1.NiGAJ-zjjn4dBykOqdRH-37|Ensemble1.NiGAJ-zjjn4dBykOqdRH-39|Ensemble1.NiGAJ-zjjn4dBykOqdRH-38
|Hub|Manufacturer|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-42|Ensemble1.NiGAJ-zjjn4dBykOqdRH-38|Ensemble1.NiGAJ-zjjn4dBykOqdRH-40
|Hub|Article|Hub-to-Link-N||Link|Link|Ensemble1.NiGAJ-zjjn4dBykOqdRH-43|Ensemble1.NiGAJ-zjjn4dBykOqdRH-22|Ensemble1.NiGAJ-zjjn4dBykOqdRH-40
