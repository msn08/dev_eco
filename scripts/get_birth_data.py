import pandas as pd
import os
import pyreadstat
import unidecode
import time


# JUST TO MAKE SURE THE DIRECTORY IS CORRECT, DOESN'T RUN NORMALLY
def set_working_directory():
    print("Current working directory - before")
    print(os.getcwd())
    print()
    os.chdir('../')
    os.chdir('/Users/msotonov/Nextcloud/Master_s3/DevEconomics/data')
    print("Current working directory - after")
    print(os.getcwd())

### ****** ********** ****** ###
### ****** VARIABLES  ****** ###
### ****** ********** ****** ###

list_data_csv = ["Nac_2016.csv","Nac_2017.csv","Nac_2018.csv","Nac_2019.csv"]
list_data_sav = ["Nac_2008.sav","Nac_2009.sav","Nac_2010.sav","Nac_2011.sav",
"Nac_2012.sav","Nac_2013.sav","Nac_2014.sav","Nac_2015.sav"]
data_code = pd.read_csv("data_code.csv") #ALLOWS US TO TRANSLATE NAME REGION TO NUMBER OF THE REGION
data_month = pd.read_csv("data_month.csv") #ALLOWS US TO TRANSLATE NAME REGION TO NUMBER OF THE REGION

### ****** **************************************** ****** ###
### ****** FUNCTIONS TO CLEAN THE NAMES OF THE DATA ****** ###
### ****** **************************************** ****** ###

def clean_municipality(region,muni):
    muni_str = str(muni)
    if len(muni_str) == 1:
        good_muni = region + "00" + muni_str
    elif len(muni_str) == 2:
        good_muni = region + "0" + muni_str
    else:
        good_muni = region + muni_str
    return good_muni

def clean_region(region):
    reg_str = str(region)
    if len(reg_str) == 1:
        good_reg = "0" + reg_str
    else:
        good_reg = reg_str
    return good_reg


### ****** **************************  ****** ###
### ****** FUNCTIONS FOR READING DATA  ****** ###
### ****** **************************  ****** ###

def reading_csv(list_tables):
    data_final = pd.DataFrame()
    for element in list_tables:
        print("######## READING: ",element)
        if "2017" in element or "2018" in element:
            print("Problematics one")
            data = pd.read_csv(element,encoding="Latin-1", delimiter=";")
            data=data.rename(columns = {"ï»¿COD_DPTO" : "COD_DPTO"})
        else:
            data = pd.read_csv(element,encoding="Latin-1")
        data_temp = get_data_year(data)
        name = "Month_" + str(element)
        print("######## SAVING: ",name)
        data_temp.to_csv(name,index=True)
        data_final = data_final.append(data_temp)
    return data_final

def reading_sav(list_tables,df_codes):
    data_final = pd.DataFrame()
    for element in list_tables:
        print("######## READING: ",element)
        data, metadata = pyreadstat.read_sav(element, encoding="latin1",apply_value_formats=True) 
        names = list(data.columns)
        new_names = []
        for i in names:
            new_names.append(i.upper())
        data.columns=new_names
        data_temp = get_data_year_sav(data,df_codes)
        name = "Month_" + str(element) +".csv"
        print("######## SAVING: ",name)
        data_temp.to_csv(name,index=True)
        data_final = data_final.append(data_temp)
    return data_final

### ****** **************************  ****** ###
### ****** FUNCTIONS FOR GETTING DATA  ****** ###
### ****** **************************  ****** ###

# ONCE IT GETS THE CORRECT REGION, MUNICIPALITY, MONTH AND YEAR, IT WRITE THE CORRECT FORMAT OF DATAFRAME
#OUTPUT: DATAFRAME FOR ONE REGION AND ONE MUNICIPALITIES AND ONE MONTH IN CORRECT FORMAT
def birth_per_month(df_big,region,municipality,month,year):
    df_small = df_big[df_big["MES"] == month]
    num_birth = df_small.shape[0]
    reg = str(region)
    muni = str(municipality)
    if len(str(month)) > 3:
            month = get_num_reg(month,data_month)
    data_format = {
        "Region" : [reg],
        "Municipality" : [muni],
        "Births" : [num_birth],
        "Month" : [month],
        "Year" : [year]
    }
    final_data = pd.DataFrame(data_format)
    return final_data

# ONCE IT'S GET THE CORRECT REGION, AND MUNICIPALITIES, IT GETS THE MONTHS AND LAUNCHES THE ABOVE FUNCTION
#OUTPUT: DATAFRAME FOR ONE REGION AND ONE MUNICIPALITIES AND ALL MONTHS IN CORRECT FORMAT
def get_data_muni(df_region,region,muni,year):
    names = ["Region","Municipality","Births","Month","Year"]
    df_all = pd.DataFrame(columns=names)
    list_months = list(df_region["MES"].unique())
    for month in list_months:
        df_temp = birth_per_month(df_region,region,muni,month,year)
        df_all = df_all.append(df_temp)
    return df_all


# ONCE IT'S GET THE CORRECT REGION AND YEAR, IT GETS THE MUNICIPALITIES AND LAUNCHES THE ABOVE FUNCTION
#OUTPUT: DATAFRAME FOR ONE REGION AND ALL MUNICIPALITIES AND ALL MONTHS IN CORRECT FORMAT
def get_data_region(df_reg,reg,year):
    data_muni05 = pd.DataFrame()
    list_muni = list(df_reg["COD_MUNIC"].unique())
    for m in list_muni:
        muni = clean_municipality(reg,m)
        data_muni = get_data_muni(df_reg,reg,muni,year)
        data_muni05 = data_muni05.append(data_muni)
    return data_muni05


# ONCE IT'S GET THE CORRECT DATASET, IT GETS THE YEAR, REGIONS AND LAUNCHES THE ABOVE FUNCTIONS
#OUTPUT: DATAFRAME WITH ALL REGIONS AND ALL MONTHS IN CORRECT FORMAT
def get_data_year(df_year):
    data_all_year = pd.DataFrame()
    list_reg = list(df_year["COD_DPTO"].unique())
    year = df_year["ANO"].unique()[0]
    for r in list_reg:
        data_reg = df_year[df_year["COD_DPTO"] == r]
        reg = clean_region(r)
        print("Reading region:",reg)
        data_year_temp = get_data_region(data_reg,reg,year)
        data_all_year = data_all_year.append(data_year_temp)
    return data_all_year

def get_data_year_sav(df_year,df_codes):
    data_all_year = pd.DataFrame()
    list_reg = list(df_year["COD_DPTO"].unique())
    year = df_year["ANO"].unique()[0]
    for r in list_reg:
        data_reg = df_year[df_year["COD_DPTO"] == r]
        r2 = get_num_reg(r,df_codes)
        reg = clean_region(r2)
        print("Reading region:",reg)
        data_year_temp = get_data_region(data_reg,reg,year)
        data_all_year = data_all_year.append(data_year_temp)
    return data_all_year

def get_num_reg(name_reg,df_codes):
    name_better = name_reg.lstrip()
    name_best = unidecode.unidecode(name_better).upper()
    for index, row in df_codes.iterrows():
        row_compare = row["Department"]
        row_best = unidecode.unidecode(row_compare).upper()
        if name_best in row_best:
            reg_code = df_codes.loc[index,"Code"]
        elif "ARCHI" in name_best:
            reg_code = 88
    return reg_code

if __name__ == "__main__":
    start_time = time.time()
    print("#### READING CSV DATA")
    csv_final = reading_csv(list_data_csv)
    print("#### SAVING CSV DATA")
    csv_final.to_csv("csv_final.csv",index=True)
    print("#### READING SAV DATA")
    sav_final = reading_sav(list_data_sav,data_code)
    print("#### SAVING SAV DATA")
    sav_final.to_csv("sav_final.csv",index=True)
    print("#### SAVING SAV DATA")
    csv_final = csv_final.append(sav_final)
    csv_final.reset_index(inplace=True, drop=True)
    csv_final.to_csv("birth_final.csv",index=True)
    print("--- %s seconds ---" % (time.time() - start_time))