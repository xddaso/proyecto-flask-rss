# Bootstrap 5

Primers passos amb bootstrap 5.

## Estructura inicial

Revisa [l'exemple 00](./src/00-estructura-inicial.html).

## Containers 

Revisa [l'exemple 01](./src/01-containers.html).

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_containers.php
* Referència completa: https://getbootstrap.com/docs/5.3/layout/containers/

La classe `container` proporciona un contenidor d'amplada fixa responsive.

La classe `.container-fluid` proporciona un contenidor d'amplada completa, que ocupa tota l'amplada disponible.

## Colors

Seguim amb l'exemple anterior.

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_colors.php
* Referència completa: https://getbootstrap.com/docs/5.3/utilities/colors/

Modifica el primer contenidor:

```html
<div class="container-fluid text-white bg-primary">
```

I el segon:

```html
<div class="container bg-secondary text-bg-secondary">
```

## Padding & Margin

Seguim amb l'exemple anterior.

* Referència completa: https://getbootstrap.com/docs/5.3/utilities/spacing/

Afegim padding al primer contenidor:

```html
<div class="container-fluid text-white bg-primary p-5">
```

I margin i padding al segon contenidor:

```html
<div class="container bg-secondary text-bg-secondary mt-5 p-2">
```

## Text

Seguim amb l'exemple anterior.

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_typography.php
* Referència completa: https://getbootstrap.com/docs/5.3/content/typography/

Afegeix les classe `text-center` al primer container, `lead`a un paràgraf i el tag `<mark>` a una paraula.

## Borders

Seguim amb l'exemple anterior.

* Referència completa: https://getbootstrap.com/docs/5.3/utilities/borders/

Afegeix les classes `border`, `border-danger` i `rounded` al segon container.

## Grid

Revisa [l'exemple 02](./src/02-grid.html).

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_grid_basic.php
* Referència completa: https://getbootstrap.com/docs/5.3/layout/grid/

Cada fila es definiex amb la classe `row` i el contingut amb la classe `col`. L'amplada disponible es divideix en 12 i pots assignar a una cel·la en concret un espai fix, de manera que les altres és reparteixen l'espai disponible.

Al segon grid es fan servir les classes específiques segons la mida de la pantalla:

* `.col-`: dispositius molt petits: amplada de pantalla inferior a 576 píxels
* `.col-sm-`: dispositius petits: amplada de la pantalla igual o superior a 576 píxels
* `.col-md-`: dispositius mitjans: amplada de la pantalla igual o superior a 768 píxels
* `.col-lg-`: dispositius grans: amplada de la pantalla igual o superior a 992 píxels
* `.col-xl-`: dispositius xl - amplada de la pantalla igual o superior a 1200 píxels
* `.col-xxl-`: dispositius xxl - amplada de la pantalla igual o superior a 1400 px

Atenció! Cada classe augmenta, de manera que si vols possar les mateixes amplades per a `sm` i `md`, només cal que ho facis per `sm`.

## Navbar

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_navbar.php
* Referència completa: https://getbootstrap.com/docs/5.3/components/navbar/

## Tables

* Referència bàsica: https://www.w3schools.com/bootstrap5/bootstrap_tables.php
* Referència completa: https://getbootstrap.com/docs/5.3/content/tables/
