# Pasos para realizar la instalación

1. Debe tener instalado Docker en el computador

2. Ejecutar en la terminal el comando

```
docker compose up --build -d
```

3. La documentación de los endpoint del api las podra encontrar en la siguiente [url](http://localhost:8000/swagger/)

4. Para poder obtener el token de acceso para crear personas debe enviar

```
{
  "username": "jeyfredc",
  "password": "jeyfredc"
}
```

5. Enviar `Bearer Token` con el access token obtenido

---

**Crear Persona**

- Método POST

- URL `api/persona/createPerson`

```
{
  "type_document": "TI",
  "document_number": "5550",
  "name": "Julian",
  "last_name": "Martinez",
  "hobbie": "Ver series de Tv"
}
```

- Respuesta Exito

```
{
  "id": 1,
  "document_number": "123456789",
  "first_name": "Jeyfred",
  "last_name": "Cruz",
  "hobby": "programar"
}
```

- Respuesta Error

```
{
  "error": true,
  "description": "No se encontró la persona con el número de documento 123456789"
}
```
---
**Obtener persona por Id**

- Método GET

- URL `api/persona/getPersonByID/{id}`

- Respuesta Exito

```
{
  "id": 1,
  "document_number": "123456789",
  "first_name": "Jeyfred",
  "last_name": "Cruz",
  "hobby": "programar"
}
```

- Respuesta Error

```
{
  "error": true,
  "description": "No se encontró la persona con el ID 1"
}
```
---
**Editar persona por Id**

- Método PUT

- URL `api/persona/editPersonById/{id}`

```
{
  "name": "julian",
  "last_name": "Perez",
  "hobbie": "Programar"
}
```

- Respuesta Exito

```
{
  "id": 1,
  "document_number": "123456789",
  "first_name": "Julian",
  "last_name": "Perez",
  "hobby": "Programar"
}
```

- Respuesta Error

```
{
  "error": true,
  "description": "No se encontró la persona con el ID 1"
}
```
**Borrar persona por Id**

- Método DELETE

- URL `api/persona/deletePersonById/{id}`

```
{
  "type_document": "TI",
  "document_number": "5550",
  "name": "Julian",
  "last_name": "Martinez",
  "hobbie": "Ver series de Tv"
}
```

- Respuesta Exito

```
204 No Content
```

- Respuesta Error

```
{
  "error": true,
  "description": "No se encontró la persona con el ID 1"
}
```
