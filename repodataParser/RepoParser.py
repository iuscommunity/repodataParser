from urllib2 import urlopen
from StringIO import StringIO
from gzip import GzipFile
from xml.dom import minidom


class Parser:
    'A class for reading a Yum repos primary.xml.gz and returning data'

    def __init__(self, *args, **kwargs):
        'Our initializer for the class'
        if kwargs.has_key('url'):
            self.url = kwargs.get('url')
            self.__open()
            self.__decompress()
            self.__dom()
            self.__elements()
            self.__todict()
        else:
            raise Exception('kwargs url missing')

    def __open(self):
        'Open a Yum Repodata XML File'
        self.res = urlopen('%s' % self.url).read()

    def __decompress(self):
        'Attempts to decompress a string as Gzip'
        buf = StringIO(self.res)
        f = GzipFile(fileobj=buf)
        try:
            self.content = f.read()
        except IOError:
            self.content = self.res

    def __dom(self):
        'get the XML dom object'
        self.dom = minidom.parse(StringIO(self.content))

    def __elements(self):
        'Get a Element by ID name'
        self.elements = self.dom.getElementsByTagName('package')

    def __node_get_attributes(self, node):
        if node.attributes.items():
            return dict(node.attributes.items())

    def __node_get_value(self, node):
        if node.firstChild:
            return node.firstChild.nodeValue

    def __todict(self):
        'create a dict from the XML data'
        data = []
        if self.elements:
            for item in self.elements:
                object = {}
                for node in item.childNodes:
                    if node.nodeName != '#text':
                        key = node.nodeName
                        attr = self.__node_get_attributes(node)
                        value = self.__node_get_value(node)
                        object[key] = (value, attr)
                data.append(object)
        self.data = data

    def getList(self):
        'returns a python list of dicts of the nodes in a XML files TagName'
        return self.data

    def getPackage(self, package):
        'return a python list of dicts for a package name'
        mypackages = []
        for pkg in self.data:
            if pkg['name'][0] == package:
                mypackages.append(pkg)
        return mypackages
