BEGIN;
CREATE TABLE "fichas_tipo_programa" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombres" varchar(140) NOT NULL UNIQUE
)
;
CREATE TABLE "fichas_jornada" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombre" varchar(140) NOT NULL
)
;
CREATE TABLE "fichas_programa" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombre" varchar(140) NOT NULL UNIQUE,
    "tipo_id" integer NOT NULL REFERENCES "fichas_tipo_programa" ("id")
)
;
CREATE TABLE "fichas_competencia_programa" (
    "id" integer NOT NULL PRIMARY KEY,
    "competencia_id" integer NOT NULL,
    "programa_id" integer NOT NULL REFERENCES "fichas_programa" ("id"),
    UNIQUE ("competencia_id", "programa_id")
)
;
CREATE TABLE "fichas_competencia" (
    "id" integer NOT NULL PRIMARY KEY,
    "codigo" varchar(140) NOT NULL,
    "nombre" varchar(140) NOT NULL,
    "fase" varchar(140) NOT NULL
)
;
CREATE TABLE "fichas_resultados" (
    "id" integer NOT NULL PRIMARY KEY,
    "codigo" varchar(140) NOT NULL,
    "nombre" varchar(140) NOT NULL,
    "competencia_id" integer NOT NULL REFERENCES "fichas_competencia" ("id")
)
;
CREATE TABLE "fichas_ficha" (
    "id" integer NOT NULL PRIMARY KEY,
    "identificador" varchar(140) NOT NULL UNIQUE,
    "jornada" varchar(140) NOT NULL,
    "programa_id" integer NOT NULL REFERENCES "fichas_programa" ("id")
)
;
CREATE TABLE "fichas_aprendiz" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombres" varchar(140) NOT NULL,
    "apellidos" varchar(140) NOT NULL,
    "estado" bool NOT NULL,
    "ficha_id" integer NOT NULL REFERENCES "fichas_ficha" ("id")
)
;
CREATE TABLE "fichas_instructor_fichas" (
    "id" integer NOT NULL PRIMARY KEY,
    "instructor_id" integer NOT NULL,
    "ficha_id" integer NOT NULL REFERENCES "fichas_ficha" ("id"),
    UNIQUE ("instructor_id", "ficha_id")
)
;
CREATE TABLE "fichas_instructor" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombres" varchar(140) NOT NULL,
    "apellidos" varchar(140) NOT NULL,
    "estado" bool NOT NULL
)
;
CREATE TABLE "fichas_horario" (
    "id" integer NOT NULL PRIMARY KEY,
    "fecha" date NOT NULL,
    "ficha_id" integer NOT NULL REFERENCES "fichas_ficha" ("id")
)
;
CREATE TABLE "fichas_franja" (
    "id" integer NOT NULL PRIMARY KEY,
    "nombre" varchar(140) NOT NULL UNIQUE,
    "jornada" varchar(140) NOT NULL
)
;
CREATE TABLE "fichas_evento_franja" (
    "id" integer NOT NULL PRIMARY KEY,
    "evento_id" integer NOT NULL,
    "franja_id" integer NOT NULL REFERENCES "fichas_franja" ("id"),
    UNIQUE ("evento_id", "franja_id")
)
;
CREATE TABLE "fichas_evento" (
    "id" integer NOT NULL PRIMARY KEY,
    "dias" varchar(20) NOT NULL,
    "instructor_id" integer NOT NULL REFERENCES "fichas_instructor" ("id"),
    "horario_id" integer NOT NULL REFERENCES "fichas_horario" ("id"),
    "competencia_id" integer NOT NULL REFERENCES "fichas_competencia" ("id")
)
;
CREATE INDEX "fichas_programa_acf1eac4" ON "fichas_programa" ("tipo_id");
CREATE INDEX "fichas_resultados_9bb7c9ec" ON "fichas_resultados" ("competencia_id");
CREATE INDEX "fichas_ficha_23fb0883" ON "fichas_ficha" ("programa_id");
CREATE INDEX "fichas_aprendiz_8a0765e7" ON "fichas_aprendiz" ("ficha_id");
CREATE INDEX "fichas_horario_8a0765e7" ON "fichas_horario" ("ficha_id");
CREATE INDEX "fichas_evento_fdb8591a" ON "fichas_evento" ("instructor_id");
CREATE INDEX "fichas_evento_6e64cd21" ON "fichas_evento" ("horario_id");
CREATE INDEX "fichas_evento_9bb7c9ec" ON "fichas_evento" ("competencia_id");

COMMIT;
