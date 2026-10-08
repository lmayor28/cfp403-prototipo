# Prototipo CFP 403

Prototipo de inicio del Centro de Formación Profesional N° 403 de Mercedes.

La página principal `index.html` es la versión independiente de Inicio A, con sus recursos integrados. El archivo editable es `Inicio A - Institucional.dc.html`.

Incluye las variantes B y C como referencias. Para regenerar la página principal tras editar el HTML independiente, copiar `CFP 403 - Inicio A.html` a `index.html`.

## Vista local

```sh
python -m http.server 8043 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8043/.

Los enlaces de acceso e inscripción son marcadores del prototipo.

## Prototipos conservados

- `index.html`: variante celeste, estela opaca y animaciones más livianas en móvil.
- `original.html`: copia exacta de la versión publicada en el commit `9c82839`, con su diseño y estela translúcida originales. Accesible desde «Prototipo original» en el navbar de la variante actual.

La estela original permanece dentro del HTML independiente de `original.html`; no se modifica al actualizar la nueva variante.
