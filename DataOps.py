
import pandas as pd
from urllib.parse import quote_plus
import pyodbc 



######################################  Get Data  ##################################################################
def get_data(sql_query,Server,Database,Driver = '{ODBC Driver 17 for SQL Server}'):

  
    """
    Description: Above function fetches the data for specified parameters from SSMS.

    Args:
        sql_query (String): Pass the Actual query to want to fetch
        Server (String): Server name
        Database (String): Database name
        Driver (String): Driver name for SQL Server. Default value is set to 'ODBC Driver 17 for SQL Server'
        

    Returns:
        return_type: data in the form of dataframe from sqlserver
    """

    try:
        pyodbc_conn = f"Driver={Driver};Server={Server};DATABASE={DATABASE};Trusted_Connection=yes;"
        conn_sql_server = pyodbc.connect(pyodbc_conn)
        df = pd.read_sql(sql_query, conn_sql_server)
        return df
    finally:
        conn_sql_server.close()


##################################  Convert Date Columns  ###########################################################


def convert_date_columns(df):
    
    """
    Avove function detects the columnname that contains date and convert it to datetime[64]

    Args:
        df: Pass the dataframe
        

    Returns:
        return_type: data in the form of dataframe from sqlserver
    """

    for col in df.columns:
        if 'date' in col.lower():  # Check if 'date' is in the column name 
            df[col] = pd.to_datetime(df[col], errors='coerce')  # Convert to datetime
            print(f"Converted {col} to datetime")
    return df


##################################  calculate_missing_proportions  ###########################################################

def calculate_missing_proportions(df):
    """
    Calculate the proportion of missing values for each column in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.Series: A Series with the proportion of missing values for each column.
    """
    missing_proportions = {}  # Initialize an empty dictionary

    for col in df.columns:
        # Calculate the proportion of missing values for the current column
        missing_proportions[col] = df[col].isna().sum() / df.shape[0]

    return pd.Series(missing_proportions)  # Convert the dictionary to a Series and return it



##################################  calculate_date_missing_proportions  ###########################################################


def calculate_date_missing_proportions(df):
    """
    Calculate the proportion of missing values for columns containing 'date'.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        dict: A dictionary with column names as keys and their proportion of missing values as values.
    """
    datecol = [col for col in df.columns if 'date' in col.lower()]  # Identify columns with 'date'
    missing_proportions = {}  # Initialize an empty dictionary to store results

    for d in datecol:  # Loop over the list of date column names
        # Calculate the proportion of missing values for the current column
        proportion_missing = round(df[d].isna().sum() / df.shape[0],3)
        missing_proportions[d] = proportion_missing  # Store the result in the dictionary

    return missing_proportions  # Return the dictionary of missing proportions

