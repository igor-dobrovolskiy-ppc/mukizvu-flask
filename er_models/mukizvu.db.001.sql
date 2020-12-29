BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "m3vu_person" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(255) NOT NULL,
	"surname"	VARCHAR(255) NOT NULL,
	"date_of_birth"	DATE,
	"gender"	VARCHAR(255),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_opus" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_performer_role" (
	"id"	INTEGER NOT NULL,
	"is_main_cast"	BOOLEAN NOT NULL,
	CHECK("is_main_cast" IN (0, 1)),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_performer_activity" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(255) NOT NULL,
	"desc"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_author" (
	"id"	INTEGER NOT NULL,
	"person_id"	INTEGER,
	FOREIGN KEY("person_id") REFERENCES "m3vu_person"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_performer" (
	"id"	INTEGER NOT NULL,
	"person_id"	INTEGER,
	FOREIGN KEY("person_id") REFERENCES "m3vu_person"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_role_activity" (
	"performer_id"	INTEGER,
	"personnel_id"	INTEGER,
	FOREIGN KEY("performer_id") REFERENCES "m3vu_performer_role"("id"),
	FOREIGN KEY("personnel_id") REFERENCES "m3vu_performer_activity"("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_opus_author" (
	"opus_id"	INTEGER,
	"author_id"	INTEGER,
	FOREIGN KEY("opus_id") REFERENCES "m3vu_opus"("id"),
	FOREIGN KEY("author_id") REFERENCES "m3vu_author"("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_band" (
	"id"	INTEGER NOT NULL,
	"performer_id"	INTEGER NOT NULL,
	"name"	VARCHAR(255) NOT NULL,
	FOREIGN KEY("performer_id") REFERENCES "m3vu_performer"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_personnel" (
	"id"	INTEGER NOT NULL,
	"band_id"	INTEGER NOT NULL,
	"start_date"	DATE NOT NULL,
	"end_date"	DATE,
	FOREIGN KEY("band_id") REFERENCES "m3vu_band"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_personnel_performer_role" (
	"performer_id"	INTEGER,
	"personnel_id"	INTEGER,
	"performer_role_id"	INTEGER,
	FOREIGN KEY("performer_id") REFERENCES "m3vu_performer"("id"),
	FOREIGN KEY("personnel_id") REFERENCES "m3vu_personnel"("id"),
	FOREIGN KEY("performer_role_id") REFERENCES "m3vu_performer_role"("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_performance_place" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(255) NOT NULL,
	"longitude"	FLOAT,
	"latitude"	FLOAT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "m3vu_performance_event" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(255),
	"perf_place_id"	INTEGER NOT NULL,
	"personnel_id"	INTEGER NOT NULL,
	"date"	DATE NOT NULL,
	FOREIGN KEY("perf_place_id") REFERENCES "m3vu_performance_place"("id"),
	FOREIGN KEY("personnel_id") REFERENCES "m3vu_personnel"("id"),
	PRIMARY KEY("id")
);
INSERT INTO "m3vu_person" VALUES (1,'Sergii','aka ''Platon'' aka ''Beard'' Distriyanov',NULL,NULL);
INSERT INTO "m3vu_person" VALUES (2,'Vitalii','Melnik',NULL,NULL);
INSERT INTO "m3vu_person" VALUES (3,'Ihor','aka ''INgW4R'' Dobrovolskyi',NULL,NULL);
INSERT INTO "m3vu_person" VALUES (4,'Maxim','Voronko',NULL,NULL);
INSERT INTO "m3vu_person" VALUES (5,'Alex','aka ''Travis''',NULL,NULL);
INSERT INTO "m3vu_person" VALUES (6,'Valentina','Taisija (Mamchyna)',NULL,NULL);
INSERT INTO "m3vu_opus" VALUES (1,'Mole');
INSERT INTO "m3vu_opus" VALUES (2,'Sharik');
INSERT INTO "m3vu_performer_role" VALUES (1,1);
INSERT INTO "m3vu_performer_role" VALUES (2,1);
INSERT INTO "m3vu_performer_role" VALUES (3,1);
INSERT INTO "m3vu_performer_role" VALUES (4,1);
INSERT INTO "m3vu_performer_role" VALUES (5,1);
INSERT INTO "m3vu_performer_role" VALUES (6,1);
INSERT INTO "m3vu_performer_activity" VALUES (1,'Rhythm Guitar',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (2,'Bass Guitar',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (3,'Solo Guitar',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (4,'Acoustic Guitar',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (5,'Drums',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (6,'Leading Vocal',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (7,'Back Vocal',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (8,'Percussion',NULL);
INSERT INTO "m3vu_performer_activity" VALUES (9,'Keyboards',NULL);
INSERT INTO "m3vu_author" VALUES (1,1);
INSERT INTO "m3vu_author" VALUES (2,2);
INSERT INTO "m3vu_performer" VALUES (1,1);
INSERT INTO "m3vu_performer" VALUES (2,2);
INSERT INTO "m3vu_performer" VALUES (3,3);
INSERT INTO "m3vu_performer" VALUES (4,4);
INSERT INTO "m3vu_performer" VALUES (5,5);
INSERT INTO "m3vu_performer" VALUES (6,6);
INSERT INTO "m3vu_performer" VALUES (7,NULL);
INSERT INTO "m3vu_role_activity" VALUES (1,5);
INSERT INTO "m3vu_role_activity" VALUES (1,8);
INSERT INTO "m3vu_role_activity" VALUES (2,1);
INSERT INTO "m3vu_role_activity" VALUES (2,3);
INSERT INTO "m3vu_role_activity" VALUES (2,4);
INSERT INTO "m3vu_role_activity" VALUES (2,6);
INSERT INTO "m3vu_role_activity" VALUES (3,2);
INSERT INTO "m3vu_role_activity" VALUES (4,1);
INSERT INTO "m3vu_role_activity" VALUES (4,3);
INSERT INTO "m3vu_role_activity" VALUES (5,6);
INSERT INTO "m3vu_role_activity" VALUES (5,4);
INSERT INTO "m3vu_role_activity" VALUES (5,8);
INSERT INTO "m3vu_role_activity" VALUES (6,9);
INSERT INTO "m3vu_role_activity" VALUES (6,6);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (3,3);
INSERT INTO "m3vu_opus_author" VALUES (4,3);
INSERT INTO "m3vu_opus_author" VALUES (4,4);
INSERT INTO "m3vu_opus_author" VALUES (6,5);
INSERT INTO "m3vu_opus_author" VALUES (6,6);
INSERT INTO "m3vu_opus_author" VALUES (5,5);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_opus_author" VALUES (1,1);
INSERT INTO "m3vu_opus_author" VALUES (2,1);
INSERT INTO "m3vu_opus_author" VALUES (2,2);
INSERT INTO "m3vu_band" VALUES (1,7,'Muki Zvu');
INSERT INTO "m3vu_personnel" VALUES (1,1,'2005-06-05','2008-10-23');
INSERT INTO "m3vu_personnel" VALUES (2,1,'2010-06-01',NULL);
INSERT INTO "m3vu_personnel_performer_role" VALUES (1,1,1);
INSERT INTO "m3vu_personnel_performer_role" VALUES (2,1,2);
INSERT INTO "m3vu_personnel_performer_role" VALUES (3,1,3);
INSERT INTO "m3vu_personnel_performer_role" VALUES (1,2,1);
INSERT INTO "m3vu_personnel_performer_role" VALUES (3,2,3);
INSERT INTO "m3vu_personnel_performer_role" VALUES (4,2,4);
INSERT INTO "m3vu_personnel_performer_role" VALUES (5,2,5);
INSERT INTO "m3vu_personnel_performer_role" VALUES (6,2,6);
INSERT INTO "m3vu_performance_place" VALUES (1,'NIPIASUtransgas',NULL,NULL);
INSERT INTO "m3vu_performance_event" VALUES (1,'8th of March Celebration, 2008',1,1,'2008-03-08');
CREATE UNIQUE INDEX IF NOT EXISTS "ix_m3vu_band_performer_id" ON "m3vu_band" (
	"performer_id"
);
CREATE INDEX IF NOT EXISTS "ix_m3vu_personnel_band_id" ON "m3vu_personnel" (
	"band_id"
);
CREATE INDEX IF NOT EXISTS "ix_m3vu_performance_event_personnel_id" ON "m3vu_performance_event" (
	"personnel_id"
);
CREATE INDEX IF NOT EXISTS "ix_m3vu_performance_event_perf_place_id" ON "m3vu_performance_event" (
	"perf_place_id"
);
COMMIT;
