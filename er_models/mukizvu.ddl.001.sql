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
-- CREATE UNIQUE INDEX IF NOT EXISTS "ix_m3vu_band_performer_id" ON "m3vu_band" (
-- 	"performer_id"
-- );
-- CREATE INDEX IF NOT EXISTS "ix_m3vu_personnel_band_id" ON "m3vu_personnel" (
-- 	"band_id"
-- );
-- CREATE INDEX IF NOT EXISTS "ix_m3vu_performance_event_personnel_id" ON "m3vu_performance_event" (
-- 	"personnel_id"
-- );
-- CREATE INDEX IF NOT EXISTS "ix_m3vu_performance_event_perf_place_id" ON "m3vu_performance_event" (
-- 	"perf_place_id"
-- );
COMMIT;
