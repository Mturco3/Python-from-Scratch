# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:09:24 2023

@author: miche
"""

import pandas as pd
df_results=pd.read_csv(r"C:\Users\miche\Documenti\Csv files\Data_Stack_2019\survey_results_public.csv", index_col="Respondent")
df_questions=pd.read_csv(r"C:\Users\miche\Documenti\Csv files\Data_Stack_2019\survey_results_schema.csv", index_col="Column")
#Creation of a dataframe, a two dimensional data structure with rows and columns. It is similar to a 
#dictionary in which we have a list of values(rows) for each key(columns). There are more functionality.
#We can also specify index_col when reading a file
#To visualize the entire data structure, we use the method:
pd.set_option("display.max_rows",85)
pd.set_option("display.max_columns",4)
#A dataframe has different attributes and methods:
    #1) df.shape      -> Numbers of rows and columns (ATTRIBUTE)
    #2) df.info()     -> Numbers of rows and columns + names and datatypes of each column
    #3) df.head(int)  -> Shows the first n rows of the dataframe
    #4) df.tail(int)  -> Shows the last n rows of the dataframe
    #5) df.columns    -> Shows the name of each column
    #6) df.index      -> Shows the name of each label
    #7) df.sort_index -> Sorts the indexes

#A dataframe can also be instanciated from scratch with: 
    #1) pd.DataFrame(datastructure)
dic={"first":["Michele", "Gabriele", "Raffaele"], 
     "last": ["Capitollo", "Turco", "Turco"], 
     "pokemon": ["OSHAWOTT", "SNIVY", "TEPIG"],
     "email": ["michele@mail.it","gabriele@mail.it","raffaele@mail.it"]}
df_people=pd.DataFrame(dic)

#We can access a single column in the same way we access the value associated to a specific key in 
#a dictionary: however the return type will be a series, a one dimensional array:
    #1) df[column_to_access]
first_names=df_people["first"] 
#We can also access multiple columns and the return type will be another dataframe:
    #1) df[[list_of_columns]]
emails_names=df_people[["first","email"]]

#Series have different methods and attributes too:
    #1) serie.value_counts()  -> returns the name of the values in a series and it counts them
    #2) serie.min             -> returns the smallest element of the serie
    #3) serie.sum()           -> returns the sum of the elements in the series
hobby_or_not=df_results[["Hobbyist", "MainBranch"]].value_counts()

#To access also rows we need to use the following methods:
    #1) df.iloc[[list of rows],[list of columns]]  -> Shows the nth row and the nth column
    #   (Integer location, the rows are accessed by index).
    #2) df.loc[[list of rows],[list of columns]]   -> Shows the nth row and the nth column
    #   (The label of columns and rows need to be passed to access them)
    #   (We can also pass a bool serie)
int_first_people=df_people.iloc[[0,2],[0,2]]
first_people=df_people.loc[[0,2],["first","email"]]
hobby_or_not=df_results[["Hobbyist", "MainBranch"]]
reduced_data=df_results.loc[1:2,"Hobbyist":"Employment"] #Slicing is inclusive 

#As we have seen, the rows can be represented by labels: to create a label, we need to use the method:
    #1) df.set_index("column_to_set_as_index") (It does not change the df, unless we specify Inplace)
    #2) df.reset_index() it resets the index of the dataframe
df_people.set_index("email", inplace=True)
first_people=df_people.loc[["michele@mail.it","raffaele@mail.it"],["first","last"]]
#We can also specify index_col when reading a file
df_questions.sort_index(inplace=True, ascending=True)




#FILTERING

#When we compare the column series to a specific value, we get another series of bool values:
#We can then pass that serie to the dataframe to get the matching values
#Logic operators can also be applied for advanced filtering: 
    # | = or and & = and
filt= (df_people["first"]=="Michele") &  (df_people["last"]=="Turco")
michele=df_people[filt]
#To get the opposite boolean series, we can add a tilde before the filter to negate it
gabriele=df_people[~filt]
high_salary=(df_results["ConvertedComp"]>70000)
filtered=(df_results[high_salary])[["ConvertedComp","Employment","EdLevel","LanguageWorkedWith"]]
list_of_countries=["United States","India", "United Kingdom", "Germany"]
#To check for multiple values in a column, we can firstly create a list and then use the isin function.
filt_country=df_results["Country"].isin(list_of_countries)
#We can also consider the filter created as selector for rows in the loc function
country=df_results.loc[filt_country,["Country","Employment"]]

#Strings method can also be used for filtering data in a dataframe

filt_programming_language=df_results["LanguageWorkedWith"].str.contains("Python", na=False)
#filt_programming_language= "Python" in df_results["LanguageWorkedWith"].str
programming_languages=df_results.loc[filt_programming_language,["LanguageWorkedWith"]]



#UPTADING ROWS AND COLUMNS

#Update a column name:
#1) Assignment: changes every column name (not really useful)
#2) List comprehension: changes a particoular feature of column names
#3) Using strings methods after calling the str method on the columns
#4) Changing a single column with rename method
df_people.columns=["first_name","last_name","pokemon"]
df_people.columns=[x.upper() for x in df_people.columns]
df_people.columns=df_people.columns.str.replace("_"," ")
df_people.rename(columns={"FIRST NAME": "First_name"}, inplace=True)
#Uptade a single value:
#1) Assignment: changes every values if loc selects the entire rows
#2) Assignment: changes the values in the columns considered
df_people.loc["raffaele@mail.it"]=["Raffaele", "Amicelli", "TEPIG"]
df_people.loc["raffaele@mail.it","LAST NAME"]="Gigio"
df_people.at["raffaele@mail.it","LAST NAME"]="Lollo" #Alternative
#Update values in a column:
#1) String method
#2) Apply: it works with dataframes as long as with series: a function is passed 
#          as a parameter. When this method is used on a dataframe, the function is
#          applied to the series (columns) of the dataframe. It also works with lambda
#          functions
#3) Applymap: it only works on dataframes and it applies the function on every value
#             in the two dimensional array
#4) Map: it only works with series and it is used to substitute each value in a serie with
#        another value. The unchanged values will be represented as Nan
#5) Replace: similar to map, the unchanged values will stay the same. Both of them do not 
#            change the dataframe, so to keep them we have to assign the serie to a column
df_people["POKEMON"]=df_people["POKEMON"].str.upper()
df_people["POKEMON"]=df_people["POKEMON"].str.lower()
df_people["POKEMON"]=df_people["POKEMON"].apply(lambda x: x.upper())
#df_people["POKEMON"]=df_people["POKEMON"].apply(len)
#print(df_people.apply(pd.Series.max, axis="rows"))
df_len_people=df_people.applymap(len)
print(df_people["POKEMON"].replace({"TEPIG": "INFERNAPE", "OSHAWOTT": "PIPLUP"}))

df_results.rename(columns={"ConvertedComp":"USD salary"}, inplace=True)
def yesorno(string):
    if string=="Yes":
        return True
    else:
        return False
df_results["Hobbyist"]=df_results["Hobbyist"].apply(yesorno)


#ADD/REMOVE COLUMNS AND ROWS
df_people.columns=df_people.columns.str.lower()
df_people.columns=df_people.columns.str.replace(" ", "_")
df_people["full_name"]=df_people["first_name"]+" "+ df_people["last_name"]
#The method to delete a column or a row is drop
df_people.drop(columns=["first_name", "last_name"], inplace=True)
#To revert the process, we use the split method with expand keyword
df_people[["first_name", "last_name"]]=df_people["full_name"].str.split(" ", expand=True)
new_row=pd.DataFrame({"first_name":["Giulio"], "email": ["giulio@mail.com"], 
                      "cibo":["Pasta al sugo"]})
new_row.set_index("email", inplace=True)
df_people=pd.concat([df_people,new_row], ignore_index=False)
#df_people.drop(index="gabriele@mail.it", inplace=True)
filt=df_people["last_name"]=="Turco"
#We can also drop rows using conditions, as shown in the following line
#df_people.drop(index=df_people[filt].index, inplace=True)

print("lol".find("h"))
