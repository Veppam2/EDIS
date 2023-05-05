BEGIN TRANSACTION;
DROP TABLE IF EXISTS "categoria";
CREATE TABLE IF NOT EXISTS "categoria" (
	"id_categoria"	INTEGER,
	"nombre"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id_categoria" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "helado";
CREATE TABLE IF NOT EXISTS "helado" (
	"id_helado"	INTEGER,
	"sabor"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id_helado" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "mesa";
CREATE TABLE IF NOT EXISTS "mesa" (
	"numero_mesa"	INTEGER,
	"ubicacion"	TEXT NOT NULL,
	PRIMARY KEY("numero_mesa")
);
DROP TABLE IF EXISTS "alimento";
CREATE TABLE IF NOT EXISTS "alimento" (
	"id_alimento"	INTEGER,
	"id_categoria"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL UNIQUE,
	"descripcion"	TEXT NOT NULL,
	"imagen"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	FOREIGN KEY("id_categoria") REFERENCES "categoria"("id_categoria"),
	PRIMARY KEY("id_alimento" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "votacion";
CREATE TABLE IF NOT EXISTS "votacion" (
	"numero_mesa"	INTEGER NOT NULL,
	"id_helado"	INTEGER NOT NULL,
	"nombre_votante"	TEXT NOT NULL,
	FOREIGN KEY("id_helado") REFERENCES "helado"("id_helado"),
	FOREIGN KEY("numero_mesa") REFERENCES "mesa"("numero_mesa")
);
DROP TABLE IF EXISTS "carrito";
CREATE TABLE IF NOT EXISTS "carrito" (
	"numero_mesa"	INTEGER NOT NULL,
	"id_alimento"	INTEGER NOT NULL,
	FOREIGN KEY("id_alimento") REFERENCES "alimento"("id_alimento"),
	FOREIGN KEY("numero_mesa") REFERENCES "mesa"("numero_mesa")
);
COMMIT;
