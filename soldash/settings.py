HOSTS = [
                 {'hostname': 'localhost', 
                  'port': 8983, 
                  'auth': {}},
                 {'hostname': '33.33.33.10', 
                  'port': 8983,
                  'auth': {'username': 'test', 'password': 'test'}},
                 {'hostname': '33.33.33.11', 
                  'port': 8983,
                  'auth': {'username': 'test', 'password': 'test'}},
                 {'hostname': '33.33.33.12', 
                  'port': 8983,
                  'auth': {'username': 'test', 'password': 'test'}}
             ]
INDEXES = [None, 'asdf']

c = {}
c['responseHeaders'] = {0: 'ok'}
c['commands'] = [
                    {'command': 'fetchindex', 'title': 'Fetch Index'},
                    {'command': 'abortfetch', 'title': 'Abort Fetch'},
                    {'command': 'enablepoll', 'title': 'Enable Polling'},
                    {'command': 'disablepoll', 'title': 'Disable Polling'}, 
                    {'command': 'enablereplication', 'title': 'Enable Replication'}, 
                    {'command': 'disablereplication', 'title': 'Disable Replication'},
                    {'command': 'details', 'title': False}, 
                    {'command': 'filelist', 'title': 'File List'},
                    {'command': 'backup', 'title': 'Backup'} 
                ]