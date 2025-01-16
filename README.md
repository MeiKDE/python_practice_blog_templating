# Flask Blog Application

This is a simple Flask-based blog application that fetches posts from an external API, displays all blog posts on the home page, and shows individual posts on separate pages. The app uses Jinja templates for dynamic content rendering.

---

## Features

### 1. Fetch Blog Posts
- **Source**: Posts are fetched from an external API at `https://api.npoint.io/48e6ee09c985b1f9c133`.
- **Data Structure**: Each post includes the following attributes:
  - `id`: Unique identifier for the post
  - `title`: Title of the post
  - `subtitle`: Subtitle of the post
  - `body`: Content of the post

### 2. Display All Posts
- **Route**: `/`
- **Functionality**: Displays a list of all blog posts with titles, subtitles, and a link to read each post.
- **Template**: `index.html` uses a loop to render all posts dynamically.

### 3. Display Individual Post
- **Route**: `/post/<int:index>`
- **Functionality**: Displays the details of a single post identified by its `id`.
- **Template**: `post.html` renders the content of the selected post.

---

## Project Structure

```
project-folder/
├── app.py                # Main Flask application
├── post.py               # Post class definition
├── templates/
│   ├── index.html        # Template for the home page
│   ├── post.html         # Template for individual blog posts
├── static/
│   └── css/
│       └── styles.css    # CSS styles for the application
```

