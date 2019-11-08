import mysql.connector as connector


def run_query(query, params, select=False):
    cnx = connector.connect(**params)
    cursor = cnx.cursor()
    cursor.execute(query)
    if select:
        data = cursor.fetchall()
    else:
        cnx.commit()
        data = None
    cnx.close()
    return data


def select(columns, table, where=''):
    if where != '':
        query = 'SELECT {} FROM {} WHERE {}'.format(columns, table, where)
    else:
        query = 'SELECT {} FROM {}'.format(columns, table)
    return query


def insert(data, table, columns):
    return 'INSERT INTO {} {} VALUES ({})'.format(table, columns, data)


def update(table, field, data, where):
    return 'UPDATE {} SET {} = {} WHERE {}'.format(table, field, data, where)


def initialize_db(params):
    query1 = "CREATE TABLE category (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name TEXT NOT NULL)"
    query2 = "CREATE TABLE note (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, cat_id INT NOT NULL references category(id), title TEXT NOT NULL, data TEXT NOT NULL, deleted BOOL NOT NULL)"
    query3 = "INSERT INTO category (name) VALUES ('Sem Categoria')"

    queries = [query1, query2, query3]

    for query in queries:
        cnx = connector.connect(**params)
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cnx.close()

    return ""


def is_initialized(params):
    initialized = True
    cnx = connector.connect(**params)
    cursor = cnx.cursor()
    query = 'SELECT * FROM note'
    try:
        cursor.execute(query)
    except:
        initialized = False
    cnx.close()
    return initialized