# Prueba_Tecnica_py
Prueba Tecnica

# 1.Creacion Entorno Virtual y Archivo .env

Ejecutar el comando ```python -m venv venv``` en la carpeta raiz del proyecto

cree un nuevo archivo con la extension .env en la carpeta raiz y coloque la llaver secreta en el
```
SECRET_KEY=VWdsubvgYzQxTCbUwfSO7c8WUO7pAj7K
```

# 2. Activacion del Entorno Virtual

En la raiz ejecutar : 
```
.\venv\Scripts\activate.bat
```

# 3. Instalacion de Librerias(Archivo requirements)

Ejecutar
```
pip install -r requirements.txt
```

# 4. Crear Base de Datos 
Cree una nueva base de datos en postgres y cambien la cadena de conexion en el archivo ```app.py```

```
postgresql://postgres:admin@localhost:5432/PruebaTecnica
```

Ejecute en la carpeta raiz del proyecto para iniciar la aplicacion y que se creen las tablas

```
python .\app.py
```

# 5. Creacion del Primer Usuario en el sistema

Ejecute el comando de inserción en la tabla de usuarios
```
INSERT INTO public."Users"(
	id, email, password, name)
	VALUES (
	'c22d7936-81ce-4e0b-80a2-045ef54aaaa9', 
	'root@gmail.com', 																		'pbkdf2:sha256:260000$vyuPQU0NRZ3CdBVk$d325303463629879a1918f5648eff8c1a3c8c7884cac723df0cc61d4e2ce8c74', 
	'root');
```
	
 Utilice como password:  
 ```pbkdf2:sha256:260000$vyuPQU0NRZ3CdBVk$d325303463629879a1918f5648eff8c1a3c8c7884cac723df0cc61d4e2ce8c74``` 
 ya que esta encriptada. El password equivale a ```julian11```
 
 
 # Docs Api en Postman
 https://documenter.getpostman.com/view/20043771/Uz5NiD7n
 
 Para ejecutar las Apis seleccione Run in Postman en la parte superior derecha

 ![image](https://user-images.githubusercontent.com/80919045/173138671-b6e12772-43fe-4ce0-b94e-45f6af0140bc.png)
 
 Importe la configuracion en su workspace de Postman(Escritorio) 
 
 Listo!!!


