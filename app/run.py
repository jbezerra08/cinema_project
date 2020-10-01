from main import create_app

app = create_app('config.ConfigTest')

if __name__ == '__main__':
    app.run()
