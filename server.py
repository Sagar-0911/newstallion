from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'v18km7ds'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"
# initialize the app with the extension
db.init_app(app)

#login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Category(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    disc = db.Column(db.String(3000), nullable=False)
    catimg = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

class Product(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    disc = db.Column(db.String(3000), nullable=False)
    meterial_info = db.Column(db.String(3000), nullable=False)
    cat_id = db.Column(db.Integer)
    pw = db.Column(db.Integer)
    pd = db.Column(db.Integer)
    ph = db.Column(db.Integer)
    sd = db.Column(db.Integer)
    sh = db.Column(db.Integer)
    sw = db.Column(db.Integer)
    ah = db.Column(db.Integer)
    bh = db.Column(db.Integer)
    lh = db.Column(db.Integer)
    price = db.Column(db.Integer)
    img1 = db.Column(db.String(150), nullable=False)
    img2 = db.Column(db.String(150), nullable=False)
    img3 = db.Column(db.String(150), nullable=False)
    img4 = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), unique=True, nullable=False)
    passward = db.Column(db.String(3000), nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def home_red():
    return redirect(url_for("home"))

@app.route("/category")
def category():
    categories = Category.query.all()
    return render_template("category.html", categories=categories)

@app.route("/product")
def product():
    return render_template("product.html")


@app.route('/products/<int:id>')
def product_display(id):
    all_products = Product.query.filter_by(cat_id=id)
    cat = Category.query.filter_by(id=id).first().name
    # print(cat)

    return render_template("new_product_list.html", all_products=all_products, cat=cat)

@app.route("/addcart")
def addcart():

    return render_template("indexc.html")

@app.route('/product/view/<int:id>')
def show_product(id):
    product = Product.query.filter_by(id=id).first()
    # print(product.id)

    return render_template("product.html", product=product)

# admin
@app.route("/admin/login", methods=['GET', 'POST'])
def adminlogin():
    if request.method == "POST":
        uname = request.form["uname"]
        passward = request.form["pass"]
        user = Admin.query.filter_by(uname=uname).first()


        # devlop test admin add 
        # hash_and_salted_password = generate_password_hash(
        #         passward,
        #         method='pbkdf2:sha256',
        #         salt_length=8
        #     )
        # new_admin = Admin(uname=uname, passward=hash_and_salted_password)
        # db.session.add(new_admin)
        # db.session.commit()


        if not user:
                # flash("this username does not exist, Please Register")
                return redirect(url_for('adminlogin'))
        elif not check_password_hash(user.passward, passward):
                # flash("Password incorrect, PLease Try Again")
                return redirect(url_for('adminlogin'))
        else:
                login_user(user)
                return redirect(url_for('adminland'))

    return render_template("admin/adminlogin.html")


@app.route("/admin")
@login_required
def adminland():
     return render_template("admin/admin_landing.html")

@app.route('/admin/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    if request.method == "POST":
        category_name = request.form["category"]
        cat_disc = request.form["disc"]

        img_1 = request.files['catimg']
        ext1 = os.path.splitext(img_1.filename)[1]
        img_1_name = category_name + ext1
        img_1.save(os.path.join('static/img/catimg', img_1_name))

        # check if category already exist
        if Category.query.filter_by(name=category_name).first():
            # flash("category already exist")
            return redirect(url_for('addcategory'))
        
        new_category = Category(name = category_name,
                                disc = cat_disc,
                                catimg = img_1_name)
        db.session.add(new_category)
        db.session.commit()
        # flash("category added sucessfully")


    return render_template("admin/add_category.html")

@app.route("/admin/addproduct", methods=['GET', 'POST'])
@login_required
def add_product():
    categories = Category.query.all()

    if request.method == "POST":
        product_name = request.form["product_name"]
        product_disc = request.form["discription"]
        meterial_info = request.form["meterial_info"]
        cat_id = request.form["category"]
        pw = request.form["pw"]
        pd = request.form["pd"]
        ph = request.form["ph"]
        sd = request.form["sd"]
        sh = request.form["sh"]
        sw = request.form["sw"]
        ah = request.form["ah"]
        bh = request.form["bh"]
        lh = request.form["lh"]
        price = request.form["price"]
        # imges
        img_1 = request.files['img1']
        ext1 = os.path.splitext(img_1.filename)[1]
        img_1_name = product_name + "1" + ext1
        img_1.save(os.path.join('static/img/productimg', img_1_name))

        img_2 = request.files['img2']
        ext2 = os.path.splitext(img_2.filename)[1]
        img_2_name = product_name + "2" + ext2
        img_2.save(os.path.join('static/img/productimg', img_2_name))

        img_3 = request.files['img3']
        ext3 = os.path.splitext(img_3.filename)[1]
        img_3_name = product_name + "3" + ext3
        img_3.save(os.path.join('static/img/productimg', img_3_name))

        img_4 = request.files['img4']
        ext4 = os.path.splitext(img_4.filename)[1]
        img_4_name = product_name + "4" + ext4
        img_4.save(os.path.join('static/img/productimg', img_4_name))



        new_product = Product(    
            name = product_name,
            disc = product_disc,
            meterial_info = meterial_info,
            cat_id = cat_id,
            pw = pw,
            pd = pd,
            ph = ph,
            sd = sd,
            sh = sh,
            sw = sw,
            ah = ah,
            bh = bh,
            lh = lh,
            price = price,
            img1 = img_1_name,
            img2 = img_2_name,
            img3 = img_3_name,
            img4 = img_4_name,
        )
        db.session.add(new_product)
        db.session.commit()


    return render_template("admin/addproduct.html", categories=categories)


@app.route("/admin/editcategory", methods=['GET', 'POST'])
@login_required
def edit_category_list():
    categories = Category.query.all()
    return render_template("admin/edit_category_list.html", categories=categories)

@app.route('/admin/editcategory/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    curr_cat = Category.query.filter_by(id=id).first()
    # print(curr_cat.id)
    if request.method == "POST":

        # delete
        if 'delete' in request.form:
            # print("delete")
            db.session.delete(curr_cat)
            db.session.commit() 
            return redirect(url_for('adminland'))


        category_name = request.form["category"]
        cat_disc = request.form["disc"]

        img_1 = request.files['catimg']
        if img_1:
            ext1 = os.path.splitext(img_1.filename)[1]
            img_1_name = category_name + ext1
            img_1.save(os.path.join('static/img/catimg', img_1_name))
            curr_cat.catimg = img_1_name

        curr_cat.name = category_name
        curr_cat.disc = cat_disc
        db.session.commit()
        # flash("category added sucessfully")
    

    return render_template("admin/editcategory.html", curr_cat=curr_cat)

@app.route("/admin/editproduct/selectcat")
@login_required
def selectcategory():
    categories = Category.query.all()
    return render_template("admin/ep_catsel.html", categories=categories)


@app.route("/admin/editproduct/list/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_product_list(id):
    all_products = Product.query.filter_by(cat_id=id)
    return render_template("admin/edit_product_list.html", all_products=all_products)

@app.route('/admin/editproduct/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = Product.query.filter_by(id=id).first()

    if request.method == "POST":

        # delete
        if 'delete' in request.form:
            # print("delete")
            db.session.delete(product)
            db.session.commit() 
            return redirect(url_for('adminland'))

        product_name = request.form["product_name"]
        product_disc = request.form["discription"]
        meterial_info = request.form["meterial_info"]
        # cat_id = request.form["category"]
        pw = request.form["pw"]
        pd = request.form["pd"]
        ph = request.form["ph"]
        sd = request.form["sd"]
        sh = request.form["sh"]
        sw = request.form["sw"]
        ah = request.form["ah"]
        bh = request.form["bh"]
        lh = request.form["lh"]
        price = request.form["price"]
        # imges
        img_1 = request.files['img1']
        if img_1:
            ext1 = os.path.splitext(img_1.filename)[1]
            img_1_name = product_name + "1" + ext1
            img_1.save(os.path.join('static/img/productimg', img_1_name))
            product.img1 = img_1_name

        img_2 = request.files['img2']
        if img_2:
            ext2 = os.path.splitext(img_2.filename)[1]
            img_2_name = product_name + "2" + ext2
            img_2.save(os.path.join('static/img/productimg', img_2_name))
            product.img2 = img_2_name

        img_3 = request.files['img3']
        if img_3:
            ext3 = os.path.splitext(img_3.filename)[1]
            img_3_name = product_name + "3" + ext3
            img_3.save(os.path.join('static/img/productimg', img_3_name))
            product.img3 = img_3_name

        img_4 = request.files['img4']
        if img_4:
            ext4 = os.path.splitext(img_4.filename)[1]
            img_4_name = product_name + "4" + ext4
            img_4.save(os.path.join('static/img/productimg', img_4_name))
            product.img4 = img_4_name
        
        product.name = product_name
        product.disc = product_disc
        product.meterial_info = meterial_info
        # product.cat_id = cat_id
        product.pw = pw
        product.pd = pd
        product.ph = ph
        product.sd = sd
        product.sh = sh
        product.sw = sw
        product.ah = ah
        product.bh = bh
        product.lh = lh
        product.price = price

        db.session.commit()


    return render_template("admin/edit_product.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)

