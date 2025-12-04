import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
