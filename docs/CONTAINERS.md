## Sobre os Containers

### Payloads mínimos para criação de Containers
#### Method: POST, URL: /api/containers
- Campo `name` ...
- Campo `internal_port` ...
- Campo `external_port` ...
- Campo `image` ...
- Campo `memory` aceita APENAS a unidade megabytes (m)
- Campo `cpus` ...

```json
{
  "name": "myContainer",
  "internal_port": 80,
  "external_port": 8080,
  "image": "nginx:latest",
  "memory": 512, 
  "cpus": 0.5
}
```
