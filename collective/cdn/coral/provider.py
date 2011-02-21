from zope.interface import implements
from collective.cdn.core.interfaces import ICDNProvider

class cdn(object):   
    
    implements(ICDNProvider)
    
    def __init__(self,hostname=[],port=80,path=''):
        ''' Initialize
        '''
        self.hostname = ['nyud.net',]
        self.port = 80
        self.path = ''
    
    def process_url(self,url,relative_path=''):
        '''Given a base url we return a coralized version of it
           >>> obj = cdn()
           >>> assert obj.process_url('http://nohost/plone/') == 'http://nohost.nyud.net/plone/'
           >>> assert obj.process_url('http://nohost:80/plone/') == 'http://nohost.nyud.net/plone/'
           >>> assert obj.process_url('http://nohost:8080/plone/') == 'http://nohost.8080.nyud.net/plone/'
       
        '''
        # splits url parts
        protocol,path = url.split('://')
        path = path.split('/')
        hostname = path[0]
        if hostname.find(':') > -1 :
            fqdn, port = hostname.split(':')
            if not (port == '80'):
                hostname = '%s.%s' % (fqdn, port)
            else:
                hostname = fqdn
        
        # append coralnetwork domain to our fqdn
        hostname = '%s.%s' % (hostname,self.hostname[0])
        path[0] = hostname
        
        # add path, if supplied
        if self.path:
            path.insert(1,self.path)
        
        # join everything
        path = '/'.join(path)
        url = '%s://%s' % (protocol, path)
        return url