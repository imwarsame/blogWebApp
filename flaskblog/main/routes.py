from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint("main", __name__)


@main.route("/home")
@main.route("/")
def home():
    page = request.args.get("page", 1, type=int)
    # each page will have just 5 posts, helps load site faster
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # pass in posts=posts variable here to use in home.html template
    return render_template("home.html", posts=posts)
    # render_template
    # loads our html page by fetching it from our templates directory
    # saves us the trouble of typing entire html files here
    # making it v v messy v v quickly


@main.route("/about")
def about():
    return render_template("about.html", title="About")
