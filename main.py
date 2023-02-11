from website import create_app
from website import models as store

app = create_app()

#store.create_account()
store.read_account()


if __name__== "__main__":
    app.run(debug=True)