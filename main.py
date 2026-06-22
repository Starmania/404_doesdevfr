from flask import Flask, request
from cloudflare_error_page import render as render_cf_error_page

app = Flask(__name__)
port = 5000

# Define a route for GET requests to the root URL
@app.route("/")
def index():
    # Render the error page and send to client
    return render_cf_error_page({
        "title": "Skill issue (Page not found)",
        "error_code": "Nahhh",
        "more_information": {
            "hidden": False,
            "text": "cloudflare.com",
            "link": "",
            "for": "more information"
        },
        "browser_status": {
            "status": "error",
            "location": "You",
            "name": "Browser",
            "status_text": "Skill issue"
        },
        "cloudflare_status": {
            "status": "ok",
            "location": "Marseilles",
            "name": "Cloudflare",
            "status_text": "Sometimes Working"
        },
        "host_status": {
            "status": "ok",
            "location": "Website",
            "name": "Host",
            "status_text": "Always Working"
        },
        "error_source": "browser",
        "what_happened": "You tried to access my website but you have no skills. Too bad for you.",
        "what_can_i_do": "Get better.",
        "perf_sec_by": {
            "text": "Geofront",
            "link": "https://doesdev.fr"
        },
        "html_title": "Skill issue (Page not found)",
        "ray_id": request.headers.get("Cf-Ray", "")[:16],
        "client_ip": request.headers.get("X-Forwarded-For") or request.remote_addr
    }), 404

if __name__ == "__main__":
    # Start the server and listen on the specified port
    app.run(debug=True, port=port)
