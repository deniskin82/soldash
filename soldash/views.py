from flask import render_template, request, jsonify

from soldash import app
from soldash.helpers import get_details, query_solr, get_solr_versions
from soldash.settings import (RESPONSEHEADERS, COMMANDS, JS_REFRESH, 
                              DEBUG, HIDE_STATUS_MSG_SUCCESS, HIDE_STATUS_MSG_ERROR)

@app.route('/')
def homepage():
    cores = get_details()
    solr_version = get_solr_version()
    return render_template('homepage.html', 
                           cores=cores, 
                           solr_version=solr_version)

@app.route('/execute/<command>', methods=['POST'])
def execute(command):
    hostname = request.form['host']
    port = request.form['port']
    
    core = request.form['core']
    if core in ['null', 'None', 'undefined']:
        core = None
    auth = {}
    params = {}
    try:
        auth = {'username': request.form['username'],
                'password': request.form['password']}
    except KeyError, e:
        pass
    try:
        params = {'indexversion': request.form['indexversion']}
    except KeyError, e:
        pass
    host = {'hostname': hostname,
            'port': port,
            'auth': auth}
    return jsonify(query_solr(host, command, core, params=params))

@app.route('/solr_versions', methods=['GET'])
def solr_versions():
    return jsonify({'data': get_solr_versions()})

@app.route('/details', methods=['GET'])
def details():
    retval = get_details()
    return jsonify({'data': retval,
                    'solr_response_headers': RESPONSEHEADERS,
                    'commands': COMMANDS,
                    'js_refresh': JS_REFRESH,
                    'debug': str(DEBUG).lower(),
                    'hide_status_msg_success': HIDE_STATUS_MSG_SUCCESS,
                    'hide_status_msg_error': HIDE_STATUS_MSG_ERROR})
