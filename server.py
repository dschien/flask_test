import flask

from perimeta import xml
from services import ModelReader


__author__ = 'schien'
from flask import Flask

app = Flask(__name__, static_url_path='')

import os


# @app.route('/static/<path:path>')
# def static_proxy(path):
#     # send_static_file will guess the correct MIME type
#     return app.send_static_file(os.path.join('static', path))


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/model.json')
def model():


    file = open('./xml/A.xml').read()
    doc = xml.CreateFromDocument(file)
    json = ModelReader().to_json(doc)

    return json
    # return flask.jsonify(**f)

#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form action="" method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''

if __name__ == '__main__':
    port = 8000

    # Open a web browser pointing at the app.
    # os.system("open http://localhost:{0}/".format(port))

    app.debug = True
    app.run(port=port)
    # hello_world()
