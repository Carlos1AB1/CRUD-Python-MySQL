# views/crud_interface.py
from typing import List, Optional
from models.user import UserDAO, User

def menu() -> None:
    while True:
        print("\n=== CRUD de Usuarios  ===")
        print("1. Crear usuario ")
        print("2. Mostrar todos los usuarios  ")
        print("3. Mostrar usuario por ID  ")
        print("4. Actualizar usuario  ")
        print("5. Eliminar usuario  ")
        print("6. Salir ")
        
        opcion: str = input("Selecciona una opción: ")

        if opcion == "1":
            name: str = input("Ingrese el nombre: ")
            email: str = input("Ingrese el email: ")
            UserDAO.create_user(name, email)
            print("Usuario creado correctamente.")

        elif opcion == "2":
            users: List[User] = UserDAO.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user.id}, Nombre: {user.name}, Email: {user.email}")
            else:
                print("No hay usuarios registrados.")

        elif opcion == "3":
            user_id_input: str = input("Ingrese el ID del usuario: ")
            try:
                user_id: int = int(user_id_input)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
                continue

            user: Optional[User] = UserDAO.get_user_by_id(user_id)
            if user:
                print(f"ID: {user.id}, Nombre: {user.name}, Email: {user.email}")
            else:
                print("Usuario no encontrado.")

        elif opcion == "4":
            user_id_input: str = input("Ingrese el ID del usuario a actualizar: ")
            try:
                user_id: int = int(user_id_input)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
                continue

            name: str = input("Ingrese el nuevo nombre: ")
            email: str = input("Ingrese el nuevo email: ")
            UserDAO.update_user(user_id, name, email)
            print("Usuario actualizado correctamente.")

        elif opcion == "5":
            user_id_input: str = input("Ingrese el ID del usuario a eliminar: ")
            try:
                user_id: int = int(user_id_input)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
                continue

            UserDAO.delete_user(user_id)
            print("Usuario eliminado correctamente.")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
