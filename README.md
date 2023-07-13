Proyecto Oncoliq

Objetivo: Crear una plataforma que sirva como base de datos de la startup Oncoliq, permitiendo tener un registro de pacientes enroladas, medicos que dan seguimientos a estas pacientes y laboratorio/operarios donde estas pacientes se realizaran el test de Oncoliq.
En esta version actualizada se agrego la creacion y edicion de usuarios, un login, logout, la posibilidad de poner un avatar asociado a nuestro perfil, un blog donde se pueden dejar comentarios y por ultimo un apartado que habla acerca de mi.

Navbar:

El Navbar consta de las secciones: Laboratorio, Medico, Paciente, Perfil, Comentario, Blog, Logout y Acerca de mi.

Para agregar items a la base de datos se puede realizar desde las siguientes urls:

Laboratorio: http://127.0.0.1:8000/Oncoliq/setLaboratorio

Medico: http://127.0.0.1:8000/Oncoliq/setMedico

Paciente: http://127.0.0.1:8000/Oncoliq/setPaciente

Para buscar items de la base de datos se puede realizar desde las siguientes urls:

Laboratorio: http://127.0.0.1:8000/Oncoliq/getLaboratorio

Medico: http://127.0.0.1:8000/Oncoliq/getMedico

Paciente: http://127.0.0.1:8000/Oncoliq/getPaciente

Los Modelos de la BD son los siguientes:

Laboratorio: Contiene las columnas laboratorio, operario, email, equipo, fecha, resultado

Medico: Contiene las columnas nombre, apellido, email, institucion, informe, mamografia

Paciente: Contiene las columnas nombre, apellido, email

