
def fetch_pomiary_by_date(start_date, end_date):
    cur.execute(
        "SELECT * FROM pomiary WHERE data BETWEEN %s AND %s;", (start_date, end_date))
    return cur.fetchall()