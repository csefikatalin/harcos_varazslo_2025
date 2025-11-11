# Harcos és varázsló

### Python projekt osztályokkal

A játékban van egy harcos és egy varázsló, akik minden körben egy 3 elemű játéktéren léphetnek véletlenszerűen egy mezőre. 

Amennyiben ugyanarra a mezőre lépnek, akkor harcolnak.

Kezdetben mindkét játékos életerejét véletlenszerűen határozzuk meg egy 6 oldalú kocka dobásával. A minimális életerőpont 3 lehet, ehhez adjuk a kockadobás eredményét.

A játék során minden körben véletlenszerűen változik a játékosok pozíciója ([0,2] zárt intervallumban)

A harc azt jelenti, hogy az életerejük 0-val, vagy 1-gyel csökken.

<img src="uml.png" alt="uml">