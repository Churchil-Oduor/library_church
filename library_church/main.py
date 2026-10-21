import os
from fastapi import FastAPI
#from fastapi.templates import Jinja2Templates
from supabase import create_client, Client
from postgrest import APIError
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
supabase: Client = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_KEY"))


@app.get("/")
def main():
    try:
        response = supabase.table("associates").select("*").execute()
    except APIError as error:
        return "Error encountered"

    users = response.data

    return {"data": users}


if __name__ == "__main__":
    main()
