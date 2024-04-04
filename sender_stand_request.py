import configuration
import requests
import data
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
def auth_token():
    user = post_new_user(data.user_body)
    user_json = user.json()

    return user_json["authToken"]
def post_new_client_kit(kit_body_key):
    token = auth_token()
    headers = data.headers.copy()
    headers["Authorization"] = f'Bearer {token}'
    kit_body = kit_body_key
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)