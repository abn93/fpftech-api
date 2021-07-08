# ecommerce-API

## Descrição

Essa é uma API para funcionar em conjunto com o frontendecommerce, onde é utilizado o sqlite como banco de dados.

## Configuração do projeto

### Inicialização do Ambiente virtual
```
python3 -m venv venv
. venv/bin/activate
```

### Instalar dependências
```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

### Iniciar o servidor

```
python3 run server
```
### API Endpoints

GET
`/produtos/` lista todos os produtos\
**Response**

```json
[
	{
		"id": "3c4356e7-d1d1-4ca8-858b-22b250a0a727",
		"nome": "GEFORCE GT 1030",
		"marca": "GALAX",
		"categoria": "Placas de vídeo",
		"preco": "730.00"
	},
	{
		"id": "3c4356e7-d1d1-4ca8-858b-22b25040a727",
		"categoria": "erwt",
		"marca": "123",
		"nome": "Linux",
		"preco": "12"
	}
]
```

GET
`/produtos/:id` lista um produto\
**Response**

```json
{
	"id": "3c4356e7-d1d1-4ca8-858b-22b250a0a727",
	"nome": "GEFORCE GT 1030",
	"marca": "GALAX",
	"categoria": "Placas de vídeo",
	"preco": "730.00"
}
```

POST
`/produtos/` adiciona um produto\
**Request body**

```json
{
	"categoria": "erwt",
	"marca": "123",
	"nome": "Linux",
	"preco": "12"
}
```

PUT
`/produtos/:id` atualiza um produto \
**Request body**

```json
{
	"categoria": "x",
	"marca": "12f3",
	"nome": "sa",
	"preco": "x"
}
```

DELETE
`/produtos/:id` deleta um produto\

### Dependências

- asgiref
- Django
- django-cors-headers
- djangorestframework
- pytz
- sqlparse
