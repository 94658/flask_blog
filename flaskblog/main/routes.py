from flask import request, render_template, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


# default route
# for home page
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


# route for about page
@main.route("/about")
def about():
    return render_template('about.html', title='About')
