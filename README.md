# prueba_tecnica_py
Prueba Tecnica

# 1.Creacion Entorno Virtual

Ejecutar el comando ```python -m venv``` en la carpeta raiz del proyecto

# 2. Activacion del Entorno Virtual

En la raiz ejecutar : ```.\venv\Scripts\activate.bat```

# 3. Instalacion de Librerias(Archivo requirements)

Ejecutar
```pip install -r requirements.txt```

# 4. Crear Base de Datos 

En el archivo app.py cambiar la cadena de conexion 

```postgresql://postgres:admin@localhost:5432/PruebaTecnica```

# 5. Creacion del Primer Usuario en el sistema

Ejecute el comando ```INSERT INTO public."Users"(
	id, email, password, name)
	VALUES (?, ?, ?, ?); ``` cambie los ```?``` por los datos deseados
  
 Utilice como password:  ```pbkdf2:sha256:260000$vyuPQU0NRZ3CdBVk$d325303463629879a1918f5648eff8c1a3c8c7884cac723df0cc61d4e2ce8c74``` ya que esta encriptada
 El password equivale a julian11
 
 

