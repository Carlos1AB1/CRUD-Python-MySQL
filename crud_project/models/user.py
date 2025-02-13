# models/user.py
from typing import List, Optional
from mysql.connector.connection import MySQLConnection
from db.connection import get_connection

class User:
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id: int = id
        self.name: str = name
        self.email: str = email

class UserDAO:
    @staticmethod
    def create_table() -> None:
        """Crea la tabla 'users' si no existe."""
        connection: MySQLConnection = get_connection()  # Se asume que get_connection() devuelve un MySQLConnection
        cursor = connection.cursor()
        query: str = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def create_user(name: str, email: str) -> None:
        """Inserta un nuevo usuario en la base de datos."""
        connection: MySQLConnection = get_connection()
        cursor = connection.cursor()
        query: str = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values: tuple[str, str] = (name, email)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all_users() -> List[User]:
        """Retorna una lista con todos los usuarios."""
        connection: MySQLConnection = get_connection()
        cursor = connection.cursor()
        query: str = "SELECT id, name, email FROM users"
        cursor.execute(query)
        result: List[tuple] = cursor.fetchall()
        users: List[User] = [User(id=row[0], name=row[1], email=row[2]) for row in result]
        cursor.close()
        connection.close()
        return users

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Retorna un usuario según su ID."""
        connection: MySQLConnection = get_connection()
        cursor = connection.cursor()
        query: str = "SELECT id, name, email FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        row: Optional[tuple] = cursor.fetchone()
        user: Optional[User] = User(id=row[0], name=row[1], email=row[2]) if row else None
        cursor.close()
        connection.close()
        return user

    @staticmethod
    def update_user(user_id: int, name: str, email: str) -> None:
        """Actualiza los datos de un usuario."""
        connection: MySQLConnection = get_connection()
        cursor = connection.cursor()
        query: str = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        values: tuple[str, str, int] = (name, email, user_id)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete_user(user_id: int) -> None:
        """Elimina un usuario de la base de datos."""
        connection: MySQLConnection = get_connection()
        cursor = connection.cursor()
        query: str = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        cursor.close()
        connection.close()
