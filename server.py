from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"
# initialize the app with the extension
db.init_app(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Catgory %r>' % self.name

class Product(db.Model):
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

@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        category_name = request.form["category"]

        # check if category already exist
        if Category.query.filter_by(name=category_name).first():
            #User already exists
            # flash("category already exist")
            return redirect(url_for('addcategory'))
        
        new_category = Category(name = category_name)
        db.session.add(new_category)
        db.session.commit()
        # flash("category added sucessfully")


    return render_template("add_category.html")

@app.route("/addproduct", methods=['GET', 'POST'])
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
            lh = lh
        )
        db.session.add(new_product)
        db.session.commit()

    return render_template("addproduct.html", categories=categories)

@app.route('/products/<int:id>')
def product_display(id):
    all_products = Product.query.filter_by(cat_id=id)

    return render_template("product_display.html", all_products=all_products)

@app.route('/product/view/<int:id>')
def show_product(id):
    product = Product.query.filter_by(id=id).first()
    # print(product.id)

    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)

