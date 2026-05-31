from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    
    projects = [
    {
        "title": "🌤 Weather App",
        "description": "A GUI desktop app built with Python and Tkinter that fetches real-time weather data using the OpenWeatherMap API. Features a dark theme UI with city search and Sri Lankan cities dropdown.",
        "tech": ["Python", "Tkinter", "REST API", "python-dotenv"],
        "github": "https://github.com/sudheera-hash/SriLankaWeatherApp"
    },
    {
        "title": "📚 Book Web Scraper",
        "description": "A Python web scraper that extracts book titles and prices from books.toscrape.com and exports the data to a CSV file. Follows ethical scraping practices.",
        "tech": ["Python", "BeautifulSoup4", "Requests", "CSV"],
        "github": "https://github.com/sudheera-hash/web-scraper"
    },
    {
        "title": "📚 BookStore — E-Commerce Web Application",
        "description": "A full-stack e-commerce bookstore built with Flask and SQLite featuring pure SQL queries, user authentication, shopping cart, wishlist, and admin inventory management. Demonstrates CRUD operations, database design, and role-based access control.",
        "tech": ["Python", "Flask", "SQLite", "SQL", "HTML", "CSS", "Flask-Login"],
        "features": [
            "User authentication (register/login)",
            "Browse & search books by title/genre",
            "Shopping cart & wishlist management",
            "Order checkout & order history",
            "Admin dashboard with inventory management",
            "Order tracking (pending/shipped status)"
        ],
        "github": "https://github.com/sudheera-hash/bookstore",
        "live": "https://bookstore-production-569e.up.railway.app"
    }
]
    skills = [
        {"name": "Python", "icon": "🐍"},
        {"name": "HTML & CSS", "icon": "🌐"},
        {"name": "Git & GitHub", "icon": "🔧"},
        {"name": "Machine Learning", "icon": "🤖"},
        {"name": "Data Science", "icon": "📊"},
        {"name": "Flask", "icon": "⚡"},
    ]

    return render_template("index.html", projects=projects, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)