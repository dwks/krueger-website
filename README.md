# 8 Facts About AI - Flask Application

A Flask web application that displays important facts about AI risks and safety concerns, with responsive design for mobile and desktop.

## Features

- **Responsive Design**: Different layouts for mobile/tablet and desktop
- **Interactive Cards**: Click to expand content on mobile, click to show details in sidebar on desktop
- **Social Media Sharing**: Share buttons for Twitter, Facebook, LinkedIn, and copy link
- **Bootstrap Styling**: Modern, responsive UI using Bootstrap 5
- **Jinja2 Templates**: Clean separation of logic and presentation

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Copy your static assets to the appropriate directories:
   - `static/img/x.png` - X/Twitter icon
   - `static/img/facebook.png` - Facebook icon  
   - `static/img/linkedin.png` - LinkedIn icon
   - `static/img/yoshua.jpg` - Profile image for empty column

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with navbar and layout
│   └── index.html        # Main page template
├── static/
│   ├── css/              # Custom CSS files
│   ├── js/               # JavaScript files
│   └── img/              # Images and icons
└── README.md             # This file
```

## Template Features

- **Base Template**: Common layout with navbar and social sharing
- **Responsive Cards**: Mobile cards expand inline, desktop cards show content in sidebar
- **Dynamic Content**: AI facts and desktop content loaded from Flask data
- **Social Sharing**: Integrated sharing functionality for major platforms

## Customization

### Adding New AI Facts
Edit the `ai_facts` list in `app.py` to add or modify facts.

### Adding Desktop Content
Edit the `desktop_content` dictionary in `app.py` to modify desktop-specific content.

### Styling
Customize the Bootstrap classes in the templates or add custom CSS to `static/css/`.

## Browser Support

- Modern browsers with ES6 support
- Bootstrap 5 responsive breakpoints
- Mobile-first responsive design
