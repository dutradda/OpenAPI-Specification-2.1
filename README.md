# An Unofficial OpenAPI 2.1 Specification

## Introductions
This specification is an unofficial update of the OpenAPI 2.0 Specification.

## Validation
To validate yours 2.1 specifications you can use the [command-line validator](https://github.com/dutradda/openapi21-python) tool.

## Updates over version 2.0

### 1. 
Enabled the use of the [`allof`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#schema-object) directive on the root of the [`Paths Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#pathsObject) object. Example:

```json
"paths": {
    "allOf": [{
        "$ref": "test1/swagger.json"
    },{
        "$ref": "test2/swagger.json"
    }]
}
```


### 2.
Enabled the use of the [`allof`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#schema-object) directive on the root of the [`Definitions Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#definitionsObject) object. Example:

```json
"definitions": {
    "allOf": [{
        "$ref": "definitions1.json"
    },{
        "$ref": "definitions2.json"
    }]
}
```


### 3.
Added the `controllerId` property to the [`Paths Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#pathsObject). This property is required. Example:

```json
"post": {
    "controllerId": "test_controller",
    "operationId": "post_test",
    "responses": {
        "201": {
            "description": "Created"
        }
    }
}
```


### 4.
The [`operationId`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#operation-object) property of the [`Paths Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#pathsObject) is mandatory now.


### 5.
Enabled the use of the [`anyOf`](https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.5.4) directive on the [`Schema Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#schema-object). Example:

```json
"responses": {
    "200": {
        "description": "OK",
        "schema": {
            "anyOf": [{
                "type": "object"
            },{
                "type": "array"
            }]
        }
    }
}
```


### 6.
Enabled the use of the [`oneOf`](https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.5.5) directive on the [`Schema Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#schema-object) object. Example:

```json
"responses": {
    "200": {
        "description": "OK",
        "schema": {
            "oneOf": [{
                "type": "object"
            },{
                "type": "array"
            }]
        }
    }
}
```


### 7.
Enabled the use of the [`patternProperties`](https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.4.4) directive on the [`Schema Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#schema-object) object. Example:

```json
"responses": {
    "200": {
        "description": "OK",
        "schema": {
            "type": "object",
            "patternProperties": {
                "test.*": {"type": "string"}
            }
        }
    }
}
```


### 8.
Enabled [`object`](https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.4) type for any parameter, not just for body anymore. Example:

```json
"parameters": [{
    "name": "test",
    "in": "query",
    "type": "object",
    "schema": {
        "$ref": "../definitions1.json#/query"
    }
}]
```


### 9.
The [`items`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#parameterObject) directive of the `array` type now accepts objects and any directive of the original [json-schema draft4](https://tools.ietf.org/html/draft-fge-json-schema-validation-00#section-5.3). Example:

```json
"parameters": [{
    "name": "test",
    "in": "header",
    "type": "array",
    "items": {
        "type": "object",
        "patternProperties": {
            "test.*": {
                "oneOf": [{
                    "type": "object"
                }, {
                    "type": "array"
                }]
            }
        }
    }
}]
```


### 10.
The [`Example Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md#exampleObject) and [`examples`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md#fixed-fields-10) directive of the [`OAS 3`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md) [`Parameter Object`](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md#parameterObject) is now available. Example:

```json
"parameters": [{
    "name": "test1",
    "in": "query",
    "type": "object",
    "schema": {
        "properties": {
            "test": {"type": "boolean"}
        }
    },
    "example": {
        "test": true
    }
},{
    "name": "test2",
    "in": "header",
    "type": "integer",
    "examples": {
        "test1": 1,
        "test2": 2
    }
}]
```
