from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
import os
import json
import pyodbc
from dotenv import load_dotenv

# server connection details, get from environment variables
load_dotenv()
SQL_DRIVER = os.getenv("SQL_DRIVER")
SQL_SERVER_NAME = os.getenv("SQL_SERVER_NAME")
DATABASE_NAME = os.getenv("DATABASE_NAME")
IMAGES_PATH = os.getenv("IMAGES_PATH")  

# APP
#
# The purpose of this file is to render the built frontend found in
# sounds_classic_website/frontend/dist/, offer this rendering to the user when this
# flask server is accessed

# Select dist/ folder from frontend that contains the built Vue frontend
# dist/static/ contains all JS, CSS, and image assets of the Vue build
app = Flask(__name__, static_folder = "../frontend/dist/static", template_folder = "../frontend/dist")

# Enable CORS
CORS(app)

# Uncomment if working locally
@app.route("/")
def index():
    return render_template("index.html")

# catch all routes and serve the index.html in case
# the user accesses routes not explicitly defined, like
# dynamic routes (i.e., products, categories, etc.)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

def get_product(product_id):
    query = "SELECT * FROM dbo.invt WHERE webitem=1 AND Status_='Active'"
    if product_id is not None:
        query += f" AND id_={product_id}"

    try:
        cnxn = connect_to_sql()
        cursor = cnxn.cursor()
        cursor.execute(query)
        product = None
        for row in cursor:
            product = {
                "id": str(row.id_).strip(),
                "item_number": str(row.item).strip(),
                "manufacturer": str(row.brand).strip(),
                "model": str(row.model).strip(),
                "price": float(str(row.cost).strip()),
                "condition": str(row.Condition).strip(),
                "image": [str(row.picture1).strip(), str(row.picture2).strip()],
                "description": str(row.Notes).strip().replace("<div>", "").replace("</div>", "")
            }
        cursor.close()
        cnxn.close()
        return jsonify(product) if product else jsonify({})
    except Exception as e:
        return jsonify({})

def list_categories():
    try:
        cnxn = connect_to_sql()
        cursor = cnxn.cursor()
        # get distinct categories from the Categories table for dropdown menu
        cursor.execute("SELECT DISTINCT Category FROM dbo.Categories")
        categories = []
        index = 1
        for row in cursor:
            categories.append(str(row.Category).strip())
            index += 1
        cursor.close()
        cnxn.close()
        return jsonify(categories)
    except Exception as e:
        return jsonify([])
    
def get_category(category_requested):
    try:
        cnxn = connect_to_sql()
        cursor = cnxn.cursor()
        cursor.execute(f"SELECT * FROM dbo.invt WHERE webitem=1 AND Status_='Active' AND category='{category_requested}'")
        products = []
        for row in cursor:
            product = {
                "id": str(row.id_).strip(),
                "item_number": str(row.item).strip(),
                "manufacturer": str(row.brand).strip(),
                "model": str(row.model).strip(),
                "price": float(str(row.cost).strip()),
                "condition": str(row.Condition).strip(),
                "image": [str(row.picture1).strip(), str(row.picture2).strip()],
                "description": str(row.Notes).strip().replace("<div>", "").replace("</div>", "")
            }
            products.append(product)
        cursor.close()
        cnxn.close()
        return jsonify(products)
    except Exception as e:
        return []

# query database to list product categories available or actually get a product category if provided an argument
@app.route("/api/categories", methods=["GET"])
def get_categories():
    category_requested = (str)(request.args.get("category")).strip() if request.args.get("category") else None

    if category_requested == None:
        return list_categories()
    else:
        return get_category(category_requested)
    
@app.route("/api/products", methods=["GET"])
def get_products():
    product_id = (str)(request.args.get("id")).strip() if request.args.get("id") else None
    return get_product(product_id)

@app.route("/api/product/image", methods=["GET"])
def get_product_image():
    img = (str)(request.args.get("img")).strip() if request.args.get("img") else None
    if img is None:
        return jsonify({"error": "Product image file name is required"}), 400
    
    if not os.path.exists(f"{IMAGES_PATH}/{img}"):
        return jsonify({"error": "Images path does not exist"}), 404
    
    return send_from_directory(IMAGES_PATH, img, as_attachment=False)

@app.route("/api/product/image/main-carousel", methods=["GET"])
def get_main_carousel_image():
    # get the nth image from the product images and use that as the
    # nth image in the main carousel
    img_num = int((str)(request.args.get("n")).strip()) if request.args.get("n") else None

    if img_num is None:
        return jsonify({"error": "Image number is required"}), 400
    
    if not os.path.exists(f"{IMAGES_PATH}"):
        return jsonify({"error": "Images path does not exist"}), 404
    
    imgs = os.listdir(IMAGES_PATH)
    num_imgs = len(imgs)
    img_num = img_num % num_imgs  # wrap around if n exceeds number of images
    img = imgs[img_num]

    return send_from_directory(IMAGES_PATH, img, as_attachment=False)



# connect to sql server using pyodbc
def connect_to_sql():
    try:
        cnxn = pyodbc.connect(
            f"DRIVER={SQL_DRIVER};SERVER={SQL_SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;"
        )
        return cnxn
    except Exception as e:
        raise Exception(f"Error connecting to SQL Server: {e}")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int(os.getenv("PORT")))