from flask import Flask
import requests
import os
 
app = Flask(__name__)
 
@app.route('/')
def get_order():
    # url=os.environ.get('INV_SVC_URL')
    # response = requests.get(url)
    ver="2.0"
    # res='{"Service":"Invoice", "Version":' + ver + '}\n'
    res='{"Service":"Tax", "Version":' + ver + '}'
    # res=res + response.content.decode('utf-8')
    return res
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)