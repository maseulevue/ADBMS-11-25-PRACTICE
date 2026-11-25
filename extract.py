import duckdb

duckdb.sql("""
    COPY (
        SELECT *
        FROM read_csv_auto('website_sessions.csv')
    )
    TO 'bronze_website_sessions.parquet'
    (FORMAT PARQUET);
""")
