# fastapi-project
Project uses fastAPI framework to build API endpoints.
1. The endpoint **/prime/{number}** checks if number is a prime number using Miller-Rabin primality test (number < 9223372036854775807).
2. The endpoint **/picture/invert** inverts colors of JPG image.
3. The endpint **/time** returns current time after authentication by OAuth 2.0.

## Getting started
1. Go to code folder.
2. Install dependencies.
```zsh
pip install -r requirements.txt
```
3. Start FastAPI process.
```zsh
uvicorn main:app --reload 
```
4. Open local API docs [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
