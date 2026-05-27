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