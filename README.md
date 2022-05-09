# Caixa-REST-API

### Funcionamiento

1. Instalar los requisitos de **[requirements.txt]("https://github.com/albert-marquine/Caixa-REST-API/blob/main/requirements.txt")**:

```bash
 pur -r requirements.txt
```

2. Ejecutar el script **[caixa-rest-api-requests.py]("https://github.com/albert-marquine/Caixa-REST-API/blob/main/caixa-rest-api.py")** con los siguiente parámetros:

    * -a <<put|post|get>>
    * -endpoint <<endpoint_name>>
    * -file_path <<request.json>>

### Ejemplo de uso

```python
python3 caixa-api-requests.py -a post -endpoint payments -file_path request.json
```
