# Paginación en API REST 📖

![Paginación](pagination.png)

¡Bienvenido a la documentación sobre cómo implementar la paginación en tus API REST! La paginación es una técnica clave para gestionar grandes conjuntos de datos y proporcionar una experiencia de usuario eficiente.

## Paginación Simple con Parámetros 📑

La paginación con parámetros simples utiliza dos parámetros principales en las solicitudes GET:
- `page`: Indica el número de página que deseas ver.
- `page_size`: Establece cuántos elementos se muestran por página.

Ejemplo de solicitud: `GET /api/resource?page=2&page_size=10`

## Paginación con Metadatos Hipermedia 🌐

La paginación con metadatos hipermedia enriquece las respuestas de tu API con información adicional sobre cómo navegar entre páginas. Esto se hace comúnmente mediante enlaces en la respuesta.

Ejemplo de respuesta:
```json
{
    "data": [ ... ],
    "links": {
        "self": "/api/resource?page=2",
        "next": "/api/resource?page=3",
        "prev": "/api/resource?page=1",
        "first": "/api/resource?page=1",
        "last": "/api/resource?page=5"
    }
}

