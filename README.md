# First API

The smallest possible backend: a Python server (stdlib only, no dependencies)
with two JSON endpoints.

## Run it

```
py server.py
```

Server starts on http://localhost:8000

## Endpoints

- `GET /hello` → `{"message": "Hello, world!"}`
- `GET /status` → `{"status": "ok", "time": "<current UTC time>"}`

## Test it

**curl:**
```
curl http://localhost:8000/hello
curl http://localhost:8000/status
```

**Browser:** just open http://localhost:8000/hello or http://localhost:8000/status
