from .config import logger, DB_URI
from sqlalchemy import create_engine


def load_to_db(df, table_name):
    try:
        engine = create_engine(DB_URI)
        df.to_sql(
            name=table_name,    # Name of the SQL table
            con=engine,             # The SQLAlchemy engine
            if_exists='replace',    # Options: 'fail', 'replace', 'append'
            index=False             # Set to False if you don't want to save the pandas index as a column
        )
        logger.info('Successfully loaded the data to the database')
    except Exception as e:
        logger.error(f'Error loading data to database. Error Details /n {e}')



