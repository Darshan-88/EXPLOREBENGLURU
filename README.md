# Top 10 Places to Visit in Bengaluru

A modern travel-guide website built with Python, Flask, HTML, CSS and JavaScript.

## Features

- Fixed glass-style navigation bar
- Navigation options: Food, Temples, Hills, Party, Shopping
- Full-screen hero section
- Hero automatically changes through 5 Bengaluru destinations
- Hero manual slide controls
- Top 10 destination cards
- Category filtering
- Exact-place Google Maps iframe in every card
- Responsive mobile layout
- No database required for this first version

## 1. Open the project

Open this folder in VS Code:

`bengaluru_top10_travel`

## 2. Create a virtual environment

Windows CMD:

```bash
python -m venv venv
venv\Scripts\activate
```

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

## 3. Install Flask

```bash
pip install -r requirements.txt
```

## 4. Run

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## 5. Edit the places

All place information is currently stored in `app.py` inside `PLACES`.

## 6. Change the hero slides

Hero images/text are in `app.py` inside `HEROES`.

## Image note

The Bengaluru landmark photographs in this starter are loaded from Wikimedia Commons using Special:FilePath URLs. Several selected files are listed by their Commons pages as Creative Commons licensed. Before publishing the website commercially, keep proper photographer/license attribution and verify each image's current license. Some lifestyle images use Unsplash URLs.

## Next development stages

1. Add search
2. Add separate Food / Temples / Hills / Party / Shopping pages
3. Add destination detail pages
4. Add a database
5. Add admin panel
6. Add user login
7. Add wishlist
8. Add itinerary planner
9. Add weather information
10. Deploy the website
