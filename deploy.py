import subprocess
import os

def set_heroku_config_var(app_name, key, value):
    subprocess.run(["heroku", "config:set", f"{key}={value}", "--app", app_name], check=True)

# Reemplaza 'goma-app' con el nombre de tu aplicación en Heroku
app_name = "goma-app"

# Asegúrate de reemplazar con tu clave de API de OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    print("Error: No se encontró la clave API de OpenAI en las variables de entorno.")
else:
    set_heroku_config_var(app_name, "OPENAI_API_KEY", openai_api_key)
