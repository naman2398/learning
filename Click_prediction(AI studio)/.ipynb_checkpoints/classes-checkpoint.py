from sklearn.base import BaseEstimator, TransformerMixin
import pycountry_convert as pc
import pandas as pd




class CountrytoContinent(BaseEstimator, TransformerMixin):
    def __init__(self,country):
        self.country = country
    
    def fit(self,X,y=None):
        return self
      
    def continent_country(self,country_name):
    
        try:
            country_alpha2 = pc.country_name_to_country_alpha2(country_name)
            country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
            country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
            return country_continent_name

        except:
            return "Others"
    
    def transform(self,X,y=None):
        X["Continent"]=X[self.country].apply(self.continent_country)
        return X
        
class MonthHour(BaseEstimator, TransformerMixin):
    def __init__(self,timestamp):
        self.timestamp = timestamp
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        X['Month'] = [int(val[5:7]) for val in X[self.timestamp]]
        X['Hour'] = [int(val[11:13]) for val in X[self.timestamp]]
        return X

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self,columns):
        self.columns = columns
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        X.drop(X[self.columns],axis=1,inplace=True)
        return X

class Encoding(BaseEstimator, TransformerMixin):
    def __init__(self,col):
        self.col = col
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        X=pd.get_dummies(X,columns=self.col)
        return X