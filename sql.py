import psycopg2

conn = psycopg2.connect(database = "sql_from_python", user = "postgres", password ="86380029")
with conn.cursor() as  cur:
    cur.execute("""
        create table if not exists course(
            id serial primary key not null,
            last_name text not null,
            first_name text not null,
            email varchar(100) not null,
            phone  integer
        );
        """)
    conn.commit()


def create_db(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        create table if not exists course(
           # прописываем поля таблицы и их ограничения
        );
        """)
    conn.commit()




def add_client(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        insert into sql_from_python(last_name, first_name, email, phone=None) values ();
        """)
    conn.commit()
            
    
def add_phone(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        insert into sql_from_python(id, phone) values ();
        """)
    conn.commit()


def change_client(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        update sql_from_python set # прописываем знчения,которые нужно изменить
        where id = ;
        """)
    conn.commit()


def delete_phone(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        delete from sql_from_python
        where client_id = , phone = none;
        """)
    conn.commit()

def delete_client(conn):
    with conn.cursor() as  cur:
    cur.execute("""
        delete from sql_from_python
        where id = ;
        """)
    conn.commit()


def find_client(conn):
    with conn.cursor() as  cur:
    cur.execute("""
       select last_name = , first_name =, email = , phone=None from sql_from_python;
        """)
    conn.commit()


with psycopg2.connect(database="sql_from_python", user="postgres", password="86380029") as conn:
    add_client()
    add_phone()
    change_client()
    delete_phone()
    delete_client()
    find_client()

conn.close()


  