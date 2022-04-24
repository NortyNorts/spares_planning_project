from flask import Flask, render_template

from controllers.customers_controller import customers_blueprint
from controllers.parts_controller import parts_blueprint
from controllers.units_controller import units_blueprint

app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(parts_blueprint)
app.register_blueprint(units_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
