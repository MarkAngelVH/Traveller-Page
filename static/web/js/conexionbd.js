// const express = require('express');
// const { Pool } = require('pg');
// const bodyParser = require('body-parser');

// const app = express();
// const port = 3000; // Puedes cambiar el puerto según tu configuración

// // Configuración de la conexión a PostgreSQL
// const pool = new Pool({
//   user: 'postgres',
//   host: '34.29.69.18',
//   database: 'postgres',
//   password: 'lambo123456',
//   port: 5432, // Puerto por defecto de PostgreSQL
// });

// // Middleware para parsear los datos del formulario
// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(bodyParser.json());

// // Ruta para manejar la solicitud POST del formulario
// app.post('/guardar-datos', (req, res) => {
//   const {
//     nombredecontacto,
//     calle,
//     ciudad,
//     postocode,
//     telefono,
//     email,
//     mensaje,
//   } = req.body;

//   // Consulta SQL para insertar datos en la tabla contactanos
//   const query = `
//     INSERT INTO contactanos
//       (nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje)
//     VALUES
//       ($1, $2, $3, $4, $5, $6, $7)
//   `;

//   const values = [
//     nombredecontacto,
//     calle,
//     ciudad,
//     postocode,
//     telefono,
//     email,
//     mensaje,
//   ];

//   // Ejecutar la consulta
//   pool.query(query, values, (error, results) => {
//     if (error) {
//       console.error(error);
//       res.status(500).json({ error: 'Error al guardar datos en la base de datos' });
//     } else {
//       res.status(200).json({ message: 'Datos guardados exitosamente' });
//     }
//   });
// });

// // Iniciar el servidor
// app.listen(port, () => {
//   console.log(`Servidor escuchando en http://localhost:${port}`);
// });
