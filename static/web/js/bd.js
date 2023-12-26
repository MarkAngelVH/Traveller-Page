// const express = require('express');
// const bodyParser = require('body-parser');
// const cors = require('cors');
// const pool = require('./db');

// const app = express();

// // Middleware para procesar datos del formulario
// app.use(bodyParser.urlencoded({ extended: true }));

// // Configuración de CORS
// const corsOptions = {
//     origin: 'https://certuspruebas.uc.r.appspot.com/contactanos',
//     optionsSuccessStatus: 200,
// };

// app.use(cors(corsOptions));

// // Ruta para manejar la solicitud del formulario
// app.post('/guardar-datos', (req, res) => {
//     const { nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje } = req.body;

//     // Inserta los datos en la base de datos
//     pool.query('INSERT INTO contactanos (nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje) VALUES ($1, $2, $3, $4, $5, $6, $7)',
//         [nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje],
//         (error, results) => {
//             if (error) {
//                 console.error('Error al insertar en la base de datos:', error);
//                 res.status(500).send('Error al procesar la solicitud');
//             } else {
//                 res.status(200).send('Datos guardados correctamente');
//             }
//         }
//     );
// });

// // Inicia el servidor
// const PORT = 3000;
// app.listen(PORT, () => {
//     console.log(`Servidor iniciado en http://localhost:${PORT}`);
// });
