from flask import render_template,request, redirect, url_for, flash, abort
from . import main
from app.models import User,Blog,Comment,Subscriber
from ..requests import get_quotes
from flask_login import login_required, current_user
from .forms import CreateBlog
from ..email import mail_message
from .forms import UpdateProfile
from .. import db, photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    quotes = get_quotes()
    post=Blog.query.all()
    blogs = Blog.query.all()
    return render_template('index.html', quotes=quotes, post=post, blogs=blogs)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object()
        blog = Blog(title=title,content=content,user=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("New Blog Post","email/subscriber",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        flash('You Posted a new Blog', )
    return render_template('newblog.html', form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog.query.get(id)
    return render_template('blogs.html',blog=blog,comments=comments)
    

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Nicky's Blogging site","email/subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))


@main.route('/blog/<blog_id>', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))