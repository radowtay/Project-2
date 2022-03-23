from operator import and_
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_


#Set up Flask
app = Flask(__name__)

#create Flask Routes
@app.route("/")
def home():
    #set up database
    database_path = "Load/compiled_Data.db"

    engine = create_engine(f"sqlite:///{database_path}")
    metadata = sqlalchemy.MetaData()
    conn = engine.connect()

    #name the database tables for easier reference
    arrests_table = sqlalchemy.Table('.\\arrest_data_transformed', metadata, autoload=True, autoload_with=engine)
    offenders_table = sqlalchemy.Table('.\\Offender_totals_by_County', metadata, autoload=True, autoload_with=engine)
    counties_table = sqlalchemy.Table('.\\County_Codes', metadata, autoload=True, autoload_with=engine)
    offense_table = sqlalchemy.Table('.\\offense_code_names', metadata, autoload=True, autoload_with=engine)

    #get data from counties table using Bexar as default
    county_quer = sqlalchemy.select(counties_table).where(counties_table.columns.COUNTY_CODE == '15')
    county_out = conn.execute(county_quer)
    html_county = county_out.mappings().one().COUNTY_NAME

    #get registered offender count from offender data with Bexar as default
    reg_count_quer = sqlalchemy.select(offenders_table).where(offenders_table.columns.COUNTY_CODE == '15')
    county_out = conn.execute(reg_count_quer)
    html_reg_count = county_out.mappings().one().Registered_Offender_Count

    #get queries for offense counts from the last year
    stat_rape_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '3'))
    sex_asst_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '4'))
    obscene_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '8'))
    prom_pros_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '15'))
    pros_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '30'))
    peep_tom_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '33'))
    sod_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '43'))
    inc_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '55'))
    fond_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '56'))
    purch_pros_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '61'))
    rape_quer = sqlalchemy.select(arrests_table).where(and_(arrests_table.columns.COUNTY_CODE == '15', arrests_table.columns.OFFENSE_TYPE_ID == '36'))

    #execute queries
    stat_rape_res = conn.execute(stat_rape_quer)
    sex_asst_res = conn.execute(sex_asst_quer)
    obscene_res = conn.execute(obscene_quer)
    prom_pros_res = conn.execute(prom_pros_quer)
    pros_res = conn.execute(pros_quer)
    peep_tom_res = conn.execute(peep_tom_quer)
    sod_res = conn.execute(sod_quer)
    inc_res = conn.execute(inc_quer)
    fond_res = conn.execute(fond_quer)
    purch_pros_res = conn.execute(purch_pros_quer)
    rape_res = conn.execute(rape_quer)

    #store into mapped values
    try:
        html_stat_rape = stat_rape_res.mappings().first().INCIDENT_COUNT
    except:
        html_stat_rape = 0
    try:
        html_sex_asst = sex_asst_res.mappings().first().INCIDENT_COUNT
    except:
        html_sex_asst = 0
    try:
        html_obscene = obscene_res.mappings().first().INCIDENT_COUNT
    except:
        html_obscene = 0
    try:
        html_prom_pros = prom_pros_res.mappings().first().INCIDENT_COUNT
    except:
        html_prom_pros = 0
    try: 
        html_pros = pros_res.mappings().first().INCIDENT_COUNT
    except:
        html_pros = 0
    try:
        html_peep_tom = peep_tom_res.mappings().first().INCIDENT_COUNT
    except:
        html_peep_tom = 0
    try:
        html_sod = sod_res.mappings().first().INCIDENT_COUNT
    except:
        html_sod = 0
    try:
        html_inc = inc_res.mappings().first().INCIDENT_COUNT
    except:
        html_inc = 0
    try:
        html_fond = fond_res.mappings().first().INCIDENT_COUNT
    except:
        html_fond = 0
    try:
        html_purch_pros = purch_pros_res.mappings().first().INCIDENT_COUNT
    except:
        html_purch_pros = 0
    try:
        html_rape = rape_res.mappings().first().INCIDENT_COUNT
    except:
        html_rape
    
    html_totals = html_stat_rape + html_sex_asst + html_obscene +html_prom_pros+html_pros+html_sod+html_inc+html_fond+html_purch_pros+html_rape

    return render_template("index.html", 
        county=html_county, 
        registered_offender_count = html_reg_count,
        count_type_3 = html_stat_rape,
        count_type_4 = html_sex_asst,
        count_type_8 = html_obscene,
        count_type_15 = html_prom_pros,
        count_type_30 = html_pros,
        count_type_33 = html_peep_tom,
        count_type_43 = html_inc,
        count_type_55 = html_sod,
        count_type_56 = html_fond,
        count_type_61 = html_purch_pros,
        count_type_36 = html_rape,
        count_totals = html_totals)

@app.route("/scrape")
def scrape():
    #run the queries, ran out of time to finish this pieces to allow selection of different locations
    out = "hello"

if __name__ == "__main__":
    app.run(debug=True)