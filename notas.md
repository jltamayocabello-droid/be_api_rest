
# REST

## Representación

usuario
id = 10, nombre=Ana, password=1234

{
    "id": 10,
    "nombre": "Ana"
}

## Ejemplo de SOAP

<sopa:Envelope>
    <sopa:Body>
        <getUserResponse>
            <id>1</id>
            <name>Ana</name>
        </getUserResponse>
    </sopa:Body>
</sopa:Envelope>