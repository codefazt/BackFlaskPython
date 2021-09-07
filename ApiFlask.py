import flask
from flask import request, jsonify
from collections import OrderedDict
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.

typeahead = json.load(open('names.json',))

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
    <p>A prototype API for distant Names and Times. remeber to put Host:Port/typeahead</p>'''

@app.route('/typeahead/', methods=['GET'])
@app.route('/typeahead/<id>', methods=['GET'])
def api_all(id='10'):

    if(id.isnumeric()):

        data_inicial = list(typeahead.items())[:int(id)]
        data_final = sorted(data_inicial, key=lambda x: x[1], reverse=True)
        return json.dumps(data_final)
    else:
        newDict = dict(filter(lambda elem: str(id).lower() in elem[0].lower(), typeahead.items()))
        sort_orders =sorted(newDict.items(), key=lambda x: x[1], reverse=True)

        sort_dict = OrderedDict()

        for item in sort_orders:
            sort_dict[item[0]] = item[1]
        
        verify = False
        for elem in sort_dict:

            if str(elem).lower() == str(id).lower():
                verify = True
                
        if verify == True and sort_dict is not None: 
            print(str(id))
            sort_dict.move_to_end(str(id).capitalize(), last=False)

        return json.dumps([sort_dict])

@app.route('/typeahead', methods=['POST'])
def change_times():


    try:
        for item in typeahead:
            if item == request.json['name']:
                typeahead[item] = request.json['times']
                print(typeahead[item])
        
        return F''' Success you change the Time for the name selected. { request.json }'''
    except:
        return ''' <h1> Sorry worn format, Do it in this wey {"name":"Joanna","times":500} </h1> '''
        

app.run(host='0.0.0.0', port=65432, debug=True)