# Market Place Documentation

## Environment
1. Install the dotenv loader:
   pip install python-dotenv
2. Create a local env file:
   cp .env.example .env
   #### Edit `.env` and set a secure `SECRET_KEY` (do not commit .env)
3. Run the app normally; `market/__init__.py` will load values from `.env`.