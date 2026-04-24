import yaml


class Request():
    def __init__(self):
        self.input = {}
        self.output = {}
        self.data_start = 0

    def double_quote(self, mystr):
        pass

    def generate_yaml(self):
        pass

    def get_request_line(self, req):
        pass

    def get_headers(self, req):
        pass

    def get_data(self, req):
        pass

    def write_yaml(self, fname, yaml_out):
        pass

# Example Usage
# req = Request()
#
# request = '''GET / HTTP/1.1
# User-Agent: test:/data
#
# xyz
#
# '''
# request = request.replace('\n', '\r\n')
# req.get_request_line(request)
# req.get_headers(request)
# req.get_data(request)
# yaml_out = req.generate_yaml()
# write_yaml('out.yaml', yaml_out)
