
# Log Microservice (Flask)

Microservice developed to be able to record and consult logs of all types of operations carried out in any type of application.

It is developed in Flask, a Python framework for lightweight applications and microservices. It uses a connection to MongoDB, optimal for managing Logs.


## API Reference

#### LOG Register

```http
  POST /log/<module_name>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `number` | **Required**. Id of your register logged |
| `prevStatus` | `object` | **Optional**. Previus register status if exist |
| `nextStatus` | `object` | **Optional**. New register status |
| `request` | `object` | **Optional**. Request from transaction success |
| `response` | `object` | **Optional**. Response of transaction |

#### Get LOG

```http
  GET /log/<module_name>/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `number` | **Required**. Id of item to fetch |

#### Get LOGs

```http
  GET /log/<module_name>
```

## Deployment

To deploy this project run

```bash
  python main.py
```


## Authors

- [@jon.snow](https://github.com/jhonlpjr)

