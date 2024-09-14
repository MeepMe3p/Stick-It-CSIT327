import mysql.connector
from secret import get_decrypted_password
def create_database()->None:
    data_base = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = get_decrypted_password()
    )
    cursor_object = data_base.cursor()
    cursor_object.execute(
        "CREATE DATABASE IF NOT EXISTS `Stick-It-Database`"
    )
    print("""L = {w ∈ {<3}* | w contains FURINA!🪼 }""")