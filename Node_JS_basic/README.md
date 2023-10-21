# Habilidades de Node.js

En este proyecto, se espera que al final puedas explicar a cualquiera sin la ayuda de Google cómo:

## 1. Ejecutar JavaScript con Node.js
   - Para ejecutar JavaScript con Node.js, utiliza el comando `node` seguido del nombre de tu archivo JavaScript:
     ```sh
     node miarchivo.js
     ```

## 2. Uso de Módulos en Node.js
   - Los módulos en Node.js se utilizan mediante la función `require` para importarlos en tu código. Ejemplo:
     ```javascript
     const fs = require('fs');
     ```

## 3. Lectura de Archivos con un Módulo Específico de Node.js
   - Para leer archivos en Node.js, puedes utilizar el módulo `fs`. Aquí tienes un ejemplo de lectura de un archivo:
     ```javascript
     const fs = require('fs');
     fs.readFile('miarchivo.txt', 'utf8', (err, data) => {
       if (err) {
         console.error(err);
         return;
       }
       console.log(data);
     });
     ```

## 4. Acceso a Argumentos de Línea de Comandos y Variables de Entorno con `process`
   - Los argumentos de línea de comandos se acceden a través de `process.argv`, y las variables de entorno se acceden a través de `process.env`. Ejemplo de argumentos de línea de comandos:
     ```javascript
     const args = process.argv.slice(2);
     console.log(args);
     ```
     Ejemplo de variables de entorno:
     ```javascript
     const port = process.env.PORT;
     console.log(`El servidor se está ejecutando en el puerto ${port}`);
     ```

## 5. Creación de un Pequeño Servidor HTTP con Node.js
   - Puedes crear un servidor HTTP en Node.js utilizando el módulo integrado `http`. Aquí tienes un ejemplo básico:
     ```javascript
     const http = require('http');

     const server = http.createServer((req, res) => {
       res.writeHead(200, { 'Content-Type': 'text/plain' });
       res.end('¡Hola, Mundo!\n');
     });

     server.listen(8080, 'localhost', () => {
       console.log('Servidor escuchando en el puerto 8080');
     });
     ```

## 6. Creación de un Pequeño Servidor HTTP con Express.js
   - Primero, debes instalar Express.js usando `npm install express`. Luego, puedes crear un servidor básico de la siguiente manera:
     ```javascript
     const express = require('express');
     const app = express();
     const port = 3000;

     app.get('/', (req, res) => {
       // Tu lógica aquí
     });

     app.listen(port, () => {
       console.log(`Servidor Express escuchando en el puerto ${port}`);
     });
     ```
