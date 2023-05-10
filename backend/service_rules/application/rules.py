import pandas as pd
from numpy import NaN, empty, nan
from pandas import DataFrame, Series
from dateutil.parser import parse
from datetime import datetime, timedelta
from convertdate import islamic

class Rules(): 
    def __init__(self, df : DataFrame, dfRejected : DataFrame) :
        self.set_dfRejected(dfRejected)
        self.set_df(df)

    def get_dfRejected(self):
        return self.__dfRejected
    
    def set_dfRejected(self, dfRejected): 
        self.__dfRejected = dfRejected

    def get_df(self): 
        return self.__df
    
    def set_df(self, df): 
        self.__df = df
        
    #def concat_dfRejected(self, df_new_rejected_row) : 
    #    self.__dfRejected = pd.concat([self.__dfRejected, df_new_rejected_row])
        
    def create_rejected_rows(self, mask : Series, column_names_to_keep : list, rule : str, message : str,alert_type : str='rejected'):
        df_rejected_row = self.__df.loc[mask, column_names_to_keep].copy()
        df_rejected_row['Rule'] = rule
        df_rejected_row['Type'] = alert_type
        df_rejected_row['Message'] = message
        self.__dfRejected = pd.concat([self.__dfRejected, df_rejected_row])
        return df_rejected_row 

    #Temps en n2 parcourir toutes les colonnes des noms de colonne données et pour chacune de ces colonnes tester si elles sont inférieur à une
    #taille N 
    def v_lenght(self, number_length_limit: int, column_names_to_test: list, column_names_to_keep: list):
        #df_rejected_row = pd.DataFrame()
        for col in column_names_to_test : 
            mask = self.__df[col].apply(lambda x: len(str(x)) > number_length_limit)
            column_names_to_keep.append(col)
            self.create_rejected_rows(mask, column_names_to_keep, 'V-length' + str(number_length_limit), 'warning', f'La longueur ne doit pas dépasser {number_length_limit} caractères')
        #df_rejected_row = 
        #self.concat_dfRejected(df_rejected_row)

        
    #On utilise isalnum car elle est plus rapide en terme de complexite
    def alphaCharacter(self, column_names_to_test: list, column_names_to_keep: list, type_alert='rejected'):
        mask = self.__df[column_names_to_test].apply(lambda x: str(x).isalnum())
        df_rejected_row = pd.DataFrame()
        if type_alert == 'rejected' : 
            df_rejected_row = self.create_rejected_rows(mask, column_names_to_keep, 'V-Alpha-1','Alpha characters only',type_alert)
        elif type_alert == 'warning':
            df_rejected_row = self.create_rejected_rows(mask, column_names_to_keep, 'V-Alpha-2', 'Alpha characters only',type_alert)
        self.concat_dfRejected(df_rejected_row)

    def remove_leading_zero(self):
        
        def treatment_leading_zero(val):
            str_val = str(val)
            if str_val.startswith('0'):
                return str_val.lstrip('0') or nan
            return val

        self.__df = self.__df.applymap(treatment_leading_zero)
        
    def date_hijri(self, columns_names_to_test : str, date_format : str, dayfirst : bool, yearfirst : bool=None) :
        
        # Use vectorized string methods to parse the 'BIRTHDATE' column into datetime objects
        #'%Y-%m-%d %H:%M:%S'
        df = self.__df.dropna(subset=columns_names_to_test)
        not_parsed_dates = pd.to_datetime(df[columns_names_to_test], format=date_format, errors='coerce')

        # Filter the 'BIRTHDATE' column to only include date strings that are not in the specified format
        bad_dates = df.loc[not_parsed_dates.isnull(), columns_names_to_test]
        hijri_year = islamic.from_gregorian(datetime.now().year, datetime.now().month, datetime.now().day)[0]
        bad_dates = bad_dates.apply(lambda x: parse(x, fuzzy=True, dayfirst=dayfirst, yearfirst=yearfirst))
        hijri_date = bad_dates.loc[bad_dates.apply(lambda x: x.year <= hijri_year) == True]
        hijri_date = hijri_date.apply(lambda x: islamic.to_gregorian(x.year, x.month, x.day))
        hijri_date = hijri_date.apply(lambda x : f"{x[0]:04d}-{x[1]:02d}-{x[2]:02d} 00:00:00")

        self.__df.loc[hijri_date.index, columns_names_to_test] = hijri_date

    def v_date(self, columns_names_to_test : str, columns_to_keep : list, name_column_date_of_birth : str = None, date_of_death : bool=False) : 
        
        gregorian_today = datetime.now()
        gregorian_date_limit = gregorian_today - timedelta(days=125*365)
        df = pd.to_datetime(self.__df[columns_names_to_test]).copy()
        
        if date_of_death : 
            mask_v_date_of_death = df.apply(lambda x : x if x >= name_column_date_of_birth else None)
            if len(mask_v_date_of_death) > 0 : 
                self.create_rejected_rows(mask_v_date_of_death, columns_to_keep, 'V-DateofDeath', 'Date must be greater than or equal to DateOfBirth')
            
            
        mask_v_today_1 = df.apply(lambda x: x if x <= datetime.now() else None)
        if len(mask_v_today_1) > 0 : 
            self.create_rejected_rows(mask_v_today_1, columns_to_keep, 'V-Today-1', 'Value must be less than or equal to today')

        mask_v_date_of_birth_1 = df.apply(lambda x: x if x >= gregorian_date_limit else None)
        if len(mask_v_date_of_birth_1) > 0 : 
            df_rejected_row_3 = self.create_rejected_rows(mask_v_date_of_birth_1, columns_to_keep, 'V-DateOfBirth-1', 'Patient older than 125 years')
        
        mask_v_format_date_1 = pd.to_datetime(self.__df[columns_names_to_test], errors='coerce', format='%Y-%m-%d %H:%M:%S')
        if len(mask_v_format_date_1) > 0 : 
            self.create_rejected_rows(mask_v_format_date_1, columns_to_keep, 'V-FormatDate-1','Invalid date format. Must be YYYY-MM-DD HH: MM: SS')
            
    def patient_deceased(self, column_names_to_test : str, name_column_to_fill) :
        
        def testing_column(row) : 
            if pd.notna(row[column_names_to_test]):
                return 'Oui'
            else:
                return row[name_column_to_fill]

        self.__df[column_names_to_test] = self.__df.apply(testing_column, axis=1)
        
        
 

