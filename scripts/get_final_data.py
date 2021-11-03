import pandas as pd
import time


### ****** **************************  ****** ###
### ****** FUNCTIONS FOR READING DATA  ****** ###
### ****** **************************  ****** ###

#NOTE: THIS CODE IS BASED ON get_birth_data.py BUT A SIMPLIFY VERSION
# WE COULD CONSIDER THIS AS VERSION 2.0

# ONCE IT GETS THE CORRECT REGION, MUNICIPALITY, MONTH AND YEAR, IT WRITE THE CORRECT FORMAT OF DATAFRAME
#OUTPUT: ROW WITH ALL THE VARIABLES EXECPT Treatment 
def get_data_month(df,muni,year):
    final_data = pd.DataFrame()
    list_month = df["Month"].unique()
    for month in list_month:
        new_month = df[df["Month"] == month]
        total_violence = new_month.shape[0]
        farc_violence = new_month[new_month["FARC Involvement"]=="Yes"].shape[0]
        ratio = farc_violence/total_violence
        birth = get_birth_number(muni,year,month)
        data_formated = {
            "Municipality" : [muni],
            "Births": [birth],
            "Farc Violence" : [farc_violence],
            "Total Violence" : [total_violence],
            "Ratio" : [ratio],
            "Treatment": ["test"],
            "Month" :[month],
            "Year" : [year]
            }
        month_data = pd.DataFrame(data_formated)
        final_data = final_data.append(month_data)
    return final_data

#ONCE WE GET THE CORRECT MUNICIPALITY, MONTH AND YEAR, IT GOES TO THE births DATASET TO GET THE CORRECT BIRTH NUMBER
#OUTPUT: INT WITH THE NUMBER OF BIRTHS. 
#NOTE: -1 IS BE ABLE TO CLEAN IT LATER
def get_birth_number (muni, year,month):
    df1 = birth_data.loc[(birth_data["Municipality"] == muni) & (birth_data["Month"] == month)&(birth_data["Year"] == year)]
    if len(df1) > 0:
        birth_numrer = birth_data.loc[df1.index[0],"Births"]
    else:
        birth_numrer = -1
    return birth_numrer

#ONCE IT GETS THE CORRECT YEAR, IT GIVES THE CORRECT MUNICIPALIES CORRESPONSIND TO THE YEAR
#OUTPUT: DATAFRAME WITH CORRECT YEAR AND MUNICIPALITY
def get_muni_data(df, year):
    list_muni = df["Municipality"].unique()
    muni_data = pd.DataFrame()
    for muni in list_muni:
        new_df = df[(df["Municipality"] == muni)]
        new_new = new_df[new_df["Year"]==year]
        new_new2 = get_data_month(new_new,muni,year)
        muni_data = muni_data.append(new_new2)
    return muni_data

#ONCE IT GETS THE CORRECT DATASET, IT GIVES THE YEARS. !!!!! THESE YEARS ARE NOT CORRECT, THEY ARE OUT OF THE CONCERNED PERIOD!!!
#OUTPUT: DATAGRAME WITH CORRECT YEAR
def get_year_data(df):
    list_year = df["Year"].unique()
    year_data = pd.DataFrame()
    for year in list_year:
        print("##### READING YEAR ",year)
        new_test = get_muni_data(df,year)
        year_data = year_data.append(new_test)
    return year_data

#ONCE THE CORRECT DATAFRAME IS GIVEN WITH THE YEAR, MONTH, MUNICIPALITY AND BIRTHS, IT ALLOWS TO REMOVE THE DATA OUT OF THE CONCENED PERIOD AND WRONG REGIONS
#OUTPUT: CORRECT DATAFRAME WITH THE ALL THE CORRECT DATA !!!!!EXCEPT TREATMENT THAT SHOULD BE DONE IN STATA!!!!!
def get_clean_data(df):
    new_df = get_year_data(df)
    clean_df = new_df[new_df["Births"] != -1]
    return clean_df


### ****** ********** ****** ###
### ****** VARIABLES  ****** ###
### ****** ********** ****** ###
birth_data = pd.read_csv("~/Nextcloud/Master_s3/DevEconomics/data/birth_final.csv")
violence_panel_data = pd.read_csv("/Users/msotonov/Downloads/violence_panel_data.csv")

if __name__ == "__main__":
    start_time = time.time()
    csv_final = get_clean_data(violence_panel_data)
    csv_final.to_csv("birth_violence_final.csv",index=True)
    print("--- %s seconds ---" % (time.time() - start_time))