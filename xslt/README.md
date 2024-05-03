# XSLT

Per a poder fer servir **chrome** com a processador de XSLT de manera local, has d'iniciar-lo amb el flag `--allow-file-access-from-files`:

    google-chrome --allow-file-access-from-files

En el cas de **firefox**, cal entrar a `about:config` i canviar el valor de `security.fileuri.strict_origin_policy` a `false`.

Aquestes limitacions són pel fet d'obrir l'XML com a fitxer local. Si es fa servir [l'extensió de Visual Code de Live Server per obrir l'XML](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer), funciona en qualsevol navegador.