# renamed from flaskblog.py to run.py because now the only purpose of this script is to just run
from flaskblog import create_app


app = create_app()
"""
__name__ == __main__ is only true when we run flaskblog.py script directly.
"""
if __name__ == "__main__":
    app.run(debug=True)
