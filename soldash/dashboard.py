import urllib
import urllib2
import simplejson

from flask import Flask, render_template, request, jsonify

from settings import c

app = Flask(__name__)

@app.route('/')
def homepage():
    initialise()
    return render_template('homepage.html', c=c)

@app.route('/execute/<command>', methods=['POST'])
def execute(command):
    hostname = request.form['host']
    port = request.form['port']
    auth = {}
    try:
        username = request.form['username']
        password = request.form['password']
        auth = {'username': username,
                'password': password}
    except KeyError:
        pass
    host = {'hostname': hostname,
            'port': port,
            'auth': auth}
    return jsonify(query_solr(host, command))

def initialise():
    for host in c['hosts']:
        details = query_solr(host, 'details')
        if details['status'] == 'ok':
            host['details'] = details['data']
        elif details['status'] == 'error':
            host['details'] = None
            host['error'] = details['data']

def parse_address(address):
    return address.split('%3A')

def query_solr(host, command, params=None):
    url = 'http://%s:%s/solr/replication?command=%s&wt=json' % (host['hostname'], 
                                                                host['port'], 
                                                                command)
    if params:
        for key in params:
            url += '&%s=%s' % (key, params[key])
    if host['auth']:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, 
                             host['auth']['username'], 
                             host['auth']['password'])
        auth_handler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
    try:
        conn = urllib2.urlopen(url)
        retval = {'status': 'ok', 
                  'data': simplejson.load(conn)}
    except urllib2.HTTPError, e:
        retval = {'status': 'error',
                'data': 'auth'}
    except urllib2.URLError, e:
        retval = {'status': 'error', 
                'data': 'down'}
    print str(retval)
    return retval

if __name__ == '__main__':
    app.run(debug=True)