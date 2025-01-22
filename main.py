from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog_url = "https://api.npoint.io/1ee82c6ce9e5d3efc2bf"
response = requests.get(blog_url)
posts = response.json()

print(f"print posts: {posts}")


post_objects = [
    Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts
]

print(f"print post_objects: {post_objects}")


# Print post objects
for post_obj in post_objects:
    print(post_obj.id, post_obj.title, post_obj.subtitle)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
