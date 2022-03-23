-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Ry9oSd
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "arrest_totals" (
    "AGENCY_ID" INT   NOT NULL,
    "OFFENSE_TYPE_ID" INT   NOT NULL,
    "UCR_AGENCY_NAME" VARCHAR   NOT NULL,
    "COUNTY_NAME" VARCHAR   NOT NULL,
    "OFFENSE_NAME" VARCHAR   NOT NULL,
    "INCIDENT_COUNT" INT   NOT NULL,
    "COUNTY_CODE" INT   NOT NULL,
    CONSTRAINT "pk_arrest_totals" PRIMARY KEY (
        "COUNTY_CODE"
     )
);

CREATE TABLE "Offender_totals_by_County" (
    "COUNTY_CODE" INT   NOT NULL,
    "COUNTY_NAME" VARCHAR   NOT NULL,
    "Registered_Offender_Count" INT   NOT NULL,
    CONSTRAINT "pk_Offender_totals_by_County" PRIMARY KEY (
        "COUNTY_CODE"
     )
);

ALTER TABLE "arrest_totals" ADD CONSTRAINT "fk_arrest_totals_COUNTY_CODE" FOREIGN KEY("COUNTY_CODE")
REFERENCES "Offender_totals_by_County" ("COUNTY_CODE");

