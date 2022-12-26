# Caixa-REST-API

## Descripción

Libreria de python para gestionar la cuenta de Caixab y/o realizar transacciones internas.

## Instalación

### Utiliznado pip

Si usted usa `pip`, puede instalar la libreria `caixa-rest-api` ejecutando:

`pip install -i https://test.pypi.org/simple/ caixab_rest_apii`

### Desde GitHub

   1. Clone el repositorio: `git clone https://github.com/albert-marquine/Caixa-REST-API.git`
   2. Installe el paquete: `pip install ./`

## Funcionamiento

### Desde la línea de comandos

   1. Si desea realizar un cambio (POST o PUT) deberá de crear un JSON que contenga los parámetros del atributo `DATA`
      
        ```json
        {
            "endpoint":"",
            "user":"user-example",
            "IBAN":"ES6821004855170193613279",
            "concept":"this is an example."
        }
        ```

   2. Ejecute el siguiente comando:

        ```bash
        caixab_rest_api-cli --api_key 'jasdfo23c03jdafa' --secret_key 'asdf838duju30' --action 'POST' --endpoint 'paiments' --file_path '/home/albert-marquine/proyectos/Caixa-REST-API/request.json'
        ```

### Importando la librería en tu código

   1. Importe le módulo en su código: `import caixab_api`
   2. Pásale los argumentos de tu consulta en una variable de tipo Namespace:

        ```pyhton
        def caixab_queries()
            """
            Caixab make queries function
            """
            import caixab_rest_api
            from argparse import Namespace
            
            caixab_arguments = Namespace()
            caixab_arguments.api_key = 
            caixab_arguments.secret_key = 
            caixab_arguments.action = 
            caixab_arguments.endpoint = 
            caixab_arguments.data = {
                "endpoint":"",
                "user":"user-example",
                "IBAN":"ES6821004855170193613279",
                "concept":"this is an example."
            }
            caixab_rest_api.run(arguments)
        ```