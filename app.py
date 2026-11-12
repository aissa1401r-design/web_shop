from flask import Flask, render_template
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

#===الاتصال بقاعدة البيانات supabase====
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    """الصفحة الرئيسية: عرض جميع المنتجات"""
    #جلب المنتجات من ال supabase
    response = supabase.table("products").select("*").execute()
    products = response.data

    #تمرير المنتجات الى قالب HTML
    return render_template("index.html", products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)