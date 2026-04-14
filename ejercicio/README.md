# Ejercicio

En este ejercicio los alumnos deben aplicar `Adapter` y `Facade` en un escenario de tienda en línea.

## Contexto

El sistema de compra depende de tres áreas:

- inventario,
- pagos,
- envíos.

Además, la pasarela de pago disponible es `StripeLegacy`, cuya interfaz no coincide con la interfaz estándar de pagos de la tienda.

## Objetivo

Completar el archivo `tienda_online_base.py` para:

1. crear un `StripeAdapter` que implemente `InterfazPago`,
2. adaptar la llamada hacia `StripeLegacy`,
3. crear una `CompraFacade` que coordine inventario, pago y envío,
4. ejecutar el flujo completo de compra desde un único punto de entrada.

## Qué se espera del alumno

- identificar dónde aplicar `Adapter`,
- identificar dónde aplicar `Facade`,
- completar los métodos marcados con `TODO`,
- probar la ejecución final del flujo.

## Ejecución

Desde la raíz del repositorio:

```bash
python .\ejercicio\tienda_online_base.py
```

Al inicio el archivo lanza `NotImplementedError`. La meta es reemplazar esas partes con la implementación del alumno.
