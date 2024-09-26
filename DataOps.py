
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

