# Solana Tracker Using FAST API and SQLLITE

### Start the Applications



### Access

You can access the api at http://localhost:8000/ .You can acces the API docs at http://localhost:8000/docs. 

### Use Case 

We have a Solana API. It should be able to do the following.

- User should be able to create an account
- User should be able to place a buy order on any date.
- User should be able to place a sell order on any date.
- User should be able to retriev their account information.
- User should be able to view the difference in prices between two dates.


### User Post Requset.

If you navigate to the docs. You can use the json below ot generate the following CURL request.

```json
{
  "user_name": "kavisek",
  "first_name": "kavi",
  "last_name": "sek"
}
```


```bash 
curl -X 'POST' \
  'http://localhost:8000/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_name": "kavisek",
  "first_name": "kavi",
  "last_name": "sek"
}'
```
