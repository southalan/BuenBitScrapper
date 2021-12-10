# BuenBitScrapper

An offline scrapper for BuenBit tickets, a popular crypto exchange from Argentina. 

This was my first project automating the information that you could get from a transaction ticket with fixed structure

The objective was to capture the information from the fields that can be seen in the picture (taken from the .pdf ticket file, that BuenBit provides after each time you do a transaction)

![image](https://user-images.githubusercontent.com/80550822/145272358-8ecf153b-a453-447f-8729-c93ed9e8b849.png)

In turn, this information would be added to .csv file so you can later browse it more comfortably. The script will ignore the bottom of the .pdf where personal information is stored.

![image](https://user-images.githubusercontent.com/80550822/145273418-65c7f1c6-ed82-42db-b852-9115497ababb.png)

How to use:

1) Put all your BuenBit tickets in a folder.
2) Download the release .exe or compile from source to execute the script.
3) Point the "Source" folder to where your BuenBit tickets are.
4) Provide an "Output" folder to where you want the results. (.csv with default name "results" in UTF-8)
5) Enjoy the results!

Note: In the future, I hope to improve the release system to be compliant with the deterministic build philosophy (https://reproducible-builds.org/docs/deterministic-build-systems/) and to also provide better security and stability for the end user. 

If this was useful to you and want to help me keep developing this kind of stuff, you can always send me a donation!

![imagen](https://user-images.githubusercontent.com/80550822/145650828-95c3fe7e-368f-4740-a85e-fcf4ad76ed96.png)

ETH: 0x7c56d55cB972D28049f9202b3231e4cEa9A83510 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Un scrapper offline para tickets de BuenBit, un exchange popular de criptomonedas de Argentina.

Este fue mi primer proyecto automatizando la informacion que se puede obtener de un ticket de transacciones con estructura fija. 

El objetivo fue capturar la informacion de los campos que se pueden ver en la imagen (sacada de un ticket archivo .pdf, que Buenbit provee cada vez que haces una transaccion)

![image](https://user-images.githubusercontent.com/80550822/145272358-8ecf153b-a453-447f-8729-c93ed9e8b849.png)

A su vez, esta informacion se agrega a un archvio .csv que mas tarde podes navegar de manera mas comoda. El script va a ignorar la parte inferior del .pdf donde la informacion personal se guarda. 

![image](https://user-images.githubusercontent.com/80550822/145273418-65c7f1c6-ed82-42db-b852-9115497ababb.png)

Como usar: 

1) Poner todos los tickets de BuenBit en una carpeta.
2) Descargar el .exe publicado o compilar desde la fuente para ejecutar el script.
3) Apuntar a la carpeta "Fuente" a donde estan los tickets de BuenBit.
4) Proveer una carpeta "Salida" a donde van a ir los resultados. (.csv, con nombre por defecto "results" en UTF-8)
5) Disfrutar de los resultados!

Nota: En el futuro, espero mejorar el sistema de publicaciones para ser obediente con la filosofia de builds deterministas (https://reproducible-builds.org/docs/deterministic-build-systems/) y para darle mayor seguridad y estabilidad al usuario final. 

Si te ha resultado util y te gustaria ayudarme a seguir desarrollando este tipo de cosas, siempre podes enviarme una donacion!

![imagen](https://user-images.githubusercontent.com/80550822/145650840-c18b355d-c741-4e48-bd4c-f87b65ad6b78.png)

ETH: 0x7c56d55cB972D28049f9202b3231e4cEa9A83510 
