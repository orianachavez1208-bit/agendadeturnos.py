CREATE DATABASE agenda_turnos;
USE agenda_turnos;
CREATE TABLE clientes (
  id_cliente INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR (100)
  telefono VARCHAR (20)
  email VARCHAR (100)
  );
CREATE TABLE turnos (
  id_turno INT PRIMARY KEY AUTO-INCREMENT,
  id_cliente INT,
  fecha DATE
  hora TIME
  servicio VARCHAR (100),
  estado VARCHAR (20),
  FOREIGN KEY (id_cliente)
  REFERENCES clientes (id_cliente)
  );
