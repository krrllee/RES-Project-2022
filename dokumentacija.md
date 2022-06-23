Projektni zadatak 3 - Load Balancer

Projekat se sastoji od komponente Writer koja šalje podatke Load
Balancer komponenti. Korisnik ima mogućnost pa pali i gasi Worker
komponente. Podaci koje Writer šalje su string vrijednost CODE, koji
moze biti: CODE_ANALOG, CODE_DIGITAL , CODE_CUSTOM , CODE_LIMITSET,
CODE_SINGLENODE, CODE_MULTIPLENODE, CODE_CONSUMER i CODE_SOURCE, kao i
integer vrijednost VALUE. Komponenta Load Balancer prima podatke sa
Writer komponente, čuva ih u lokalnom baferu, a zatim prosljeđuje na
obradu upaljenim Workerima. Unutar Workera prima se poruka sa Load
Balancera, potom se generiše integer vrijednost koja prestavlja ID. Na
osnovu koda koji dobijemo sa Load Balancera, određujemo vrijednost
DataSet-a: za CODE_ANALOG i CODE_DIGITAL je 1, za CODE_CUSTOM i
CODE_LIMITSET je 2, za CODE_SINGLENODE i CODE_MULTIPLENOD je 3 i za
CODE_CONSUMER i CODE_SOURCE je 4. Za svaki DataSet postoji odgovarajuća
tabela u bazi podataka u koju se upisuju podaci:
ID,CODE,VALUE,DATASET,DATE (generisani timestamp koji predstavlja
vrijeme upisa podatka u bazu). Prije samog upisa u bazu neophodno je
ispitati koja je vrijednost DataSeta, a zatim i uslov da li vrijednost
VALUE razlicita od 2% od do sada upisanih vrijednosti u bazi. Ako je
vrijednost veća, upisuje se u bazu. U suprotnom se zanemaruje. Jedini
izuzetak koji ne podleže ovom uslovu je podatak čiji je kod
CODE_DIGITAL, koji se direktno upisuje u bazu.

Raspored kodova I DataSet-ova :

DataSet1 : CODE_ANALOG

CODE_DIGITAL

DataSet2 : CODE_CUSTOM

CODE_LIMITSET

DataSet3 : CODE_SINGLENODE

CODE_MULTIPLENOD

DataSet4 : CODE_CONSUMER

CODE_SOURCE

Reader komponenta ima zadatak da, prema zahtjevu korisnika, iščita
podatke iz tabele na osnovu zadatog koda ili na osnovu zadatog
vremenskog intervala u kome u podaci upisani.

UML Dijagram (dijagram komponenti) :

![](vertopal_7fcf7a8e5a5d4b349215d8a4813dad6e/media/image1.wmf){width="6.0in"
height="4.158333333333333in"}

Dijagrami aktivnosti:

![](vertopal_7fcf7a8e5a5d4b349215d8a4813dad6e/media/image2.wmf){width="5.016666666666667in"
height="5.641666666666667in"}

![](vertopal_7fcf7a8e5a5d4b349215d8a4813dad6e/media/image3.wmf){width="6.0in"
height="5.391666666666667in"}
