# Flex

Tutorial sobre flex: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox

Podeu fer servir un generador: https://angrytools.com/css-flex/

Per habilitar flex a un contenidor:

    .contenidor-flex {
        display: flex;
    }

Flex opera en dos eixos: l'eix principal (main axis) i l'eix secundari (cross axis). L'eix principal és la direcció en què es disposen els elements flexibles.

    .contenidor-flex {
        flex-direction: row; /* o column, row-reverse, column-reverse */
    }

Els elements comencen des de la vora inicial de l'eix principal.
Els elements no s'estiren a la dimensió principal, però poden reduir-se.
Els elements s'estiraran per omplir la mida de l'eix transversal.

## Multilinea amb flex-wrap

`flex-wrap: wrap` per a permetre que els elements ocupin una nova linea/columna si no hi caben, o `flex-wrap: nowrap` per a no permetre-go.

## Propietats dels elements:

### flex-basis
Mida dels elements si no tenen una mida assignada. És el width o el height depenent del `flex-direction`

### flex-grow
Número positiu que indica, proporcionalment, com poden creixer els elements.

### flex-shrink
Número positiu que indica, proporcionalment, com poden decreixen els elements.

## Alineament o justificació dels elements

### align-items
La propietat `align-items` alinearà els elements a l'eix secundari. Els valors poden ser: `flex-start`, `flex-end`, `center` o `stretch`.

### justify-content
La propietat `justify-content` alinearà els elements a l'eix principal. Els valors poden ser:

* flex-start
* flex-end
* center
* space-around
* space-between
* space-evenly




