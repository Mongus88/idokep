
# Teszt feladat

## A feladat leírása:
- Az idokep.hu oldalról szedje össze, hogy milyen ruhát javasol a mai napra, az eredményt mentse le egy szöveges file-ba
- Az idokep.hu oldalról szedje össze, hogy a következő négy napban fog-e esni az eső, az eredményt mentse el csv-be
- Az idokep.hu oldalról mentse le az elmúlt 24 óra csapadéktérképét és az aktuális hőmérséklet térképet
## Eszközök
python : programozási nyelv  
behave keretrendszer : BDD fejlesztést segíti  
playwright : böngésző automatizálás
## Leírás
A feladat megoldása során törekedtem arra, hogy egy olyan megoldást hozzak létre ami:
- bővíthető
- struktúrált
- stabilan működik

### Bővíthető
A POM-nak és a modulokból felépített fájlstruktúrának köszönhetően minimális ráfordítással lehet új funkciókat, teszteket hozzáadni a projekthez.
### Struktúrált
A BDD elveket szem előtt tartva elkülönítettem a forgatókönyveket (.feature) és a lépéseket (steps könyvtár), külön könyvtárat kaptak a segédfüggvények (utils).
### Stabilan működik
A biztos működést a modern és stabil szelektorok használata és a playwright automatikus várakozása adja.

## Futtatás
### local:
Töltsd le az összes mappát és fájlt és a terminálba írd be: behave features. A local futtatáshoz szükséges a .env fájl amiben a base url van.

### GitAction
Válaszd ki a Run Behave Playwright Tests workflows-t és kattints a run workflows-ra

## Összegzés
A feladat megoldásával szemben támasztott elvárásaim teljesültek.

Tovább fejleszthető a projekt a következőkkel:
* landing_page létrehozása, hogy ne minden városnka külön legyen egy page oldala
* a playwright akciókat expect-el bővíteni ami segíti a hibakeresést
* a feature fájlok gherkin leírásait átfogalmazni
