from application import app
from config.config import ServerConfig

@app.route('/')
def aa():
    print('hahahah')
    return "aa"


if __name__ == '__main__':
    voice_welcome = ' '.join(['a','b','c'])
    app.run(host='127.0.0.1', port=5000, debug=True)
