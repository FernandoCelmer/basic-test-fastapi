## Collections

HOST: http://127.0.0.1:8000

## URL: /items/ | <b>GET</b>
```cURL
curl --location --request GET '{{HOST}}/items/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Teste",
    "description": "API de Teste"
}
'
```

## URL: /items/ | <b>POST</b>
```cURL
curl --location --request POST '{{HOST}}/items/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Teste",
    "description": "API de Teste"
}
'
```