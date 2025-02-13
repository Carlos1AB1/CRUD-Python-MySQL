# main.py
from models.user import UserDAO
from views.crud_interface import menu

def main() -> None:
    """
    Función principal del programa.
    
    Crea la tabla 'users' si no existe y muestra el menú de opciones.
    """
    UserDAO.create_table()
    menu()

if __name__ == "__main__":
    main()
