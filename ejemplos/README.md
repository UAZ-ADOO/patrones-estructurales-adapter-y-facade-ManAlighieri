# Ejemplos

Esta carpeta contiene dos ejemplos pequeños en Python para mostrar cómo se aplican los patrones `Adapter` y `Facade`.

## adapter_ejemplo.py

Este ejemplo modela un cargador americano que necesita conectarse a una toma europea.

### Cómo funciona

- `EnchufeEuropeo` representa la interfaz que el cliente espera usar.
- `CargadorAmericano` es la clase existente con una interfaz incompatible.
- `AdaptadorCorriente` recibe un `CargadorAmericano` y traduce la llamada del cliente hacia el método disponible en la clase incompatible.

### Qué observar

- El cliente no habla directamente con `CargadorAmericano`.
- El adaptador mantiene la compatibilidad sin modificar la clase legacy.
- La responsabilidad del adaptador es traducir la interfaz.

## facade_ejemplo.py

Este ejemplo modela un cine en casa con varios componentes.

### Cómo funciona

- `ReproductorDVD`, `Proyector` y `Luces` son subsistemas independientes.
- `CineEnCasaFacade` coordina esos objetos y expone un solo método de alto nivel: `ver_pelicula`.
- El cliente usa la fachada sin preocuparse por el orden ni por los detalles internos.

### Qué observar

- El cliente no necesita conocer todos los pasos de preparación.
- La fachada centraliza la orquestación.
- La responsabilidad principal de la fachada es simplificar el uso del sistema.

## Ejecución

Desde la raíz del repositorio:

```bash
python .\ejemplos\adapter_ejemplo.py
python .\ejemplos\facade_ejemplo.py
```
