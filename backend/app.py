from flask import Flask, jsonify, render_template, request, send_file
from flask_cors import CORS
import os

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

# EXAMPLE BACKEND HTTP REQUEST AVAILABLE TO FRONTEND
#@app.route("/api/compilepdf", methods=["POST"])
#def compilepdf():
#    request_data = request.get_json()
#    # Send pdf created by createpdf
#    pdf = createpdf.compile(request_data)
#    pdf_response = send_file(pdf)
#
#    # Delete file created by pdf after it is sendable
#    createpdf.deleteFile(pdf)
#
#    return pdf_response

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int(os.getenv("PORT")))