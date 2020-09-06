from main import create_app, db

app = create_app('config')

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[+] Database created')
