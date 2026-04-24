from http import cookies
from io import BytesIO
import base64
import encodings
import errno
import gzip
import os
import re
import socket
import ssl
import sys
import zlib
import select

import brotli
from IPy import IP

from . import errors
from . import util


SOCKET_TIMEOUT = .3


class HttpResponse(object):
    def __init__(self, http_response, user_agent):
        self.response = util.ensure_binary(http_response)
        # For testing purposes HTTPResponse might be called OOL
        try:
            self.dest_addr = user_agent.request_object.dest_addr
        except AttributeError:
            self.dest_addr = '127.0.0.1'
        self.response_line = None
        self.status = None
        self.cookiejar = user_agent.cookiejar
        self.status_msg = None
        self.version = None
        self.headers = None
        self.data = None
        self.CRLF = b'\r\n'
        self.process_response()

    def parse_content_encoding(self, response_headers, response_data):
        """
        Parses a response that contains Content-Encoding to retrieve
        response_data
        """
        pass

    def check_for_cookie(self, cookie):
        # http://bayou.io/draft/cookie.domain.html
        # Check if our originDomain is an IP
        pass

    def process_response(self):
        """
        Parses an HTTP response after an HTTP request is sent
        """
        pass


class HttpUA(object):
    """
    Act as the User Agent for our regression testing
    """
    def __init__(self):
        """
        Initalize an HTTP object
        """
        self.request_object = None
        self.response_object = None
        self.request = None
        self.cookiejar = []
        self.sock = None
        self.CIPHERS = \
            'ADH-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256:' \
            'ECDHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES128-SHA256:HIGH:'
        self.CRLF = '\r\n'
        self.RECEIVE_BYTES = 8192
        self.SOCKET_TIMEOUT = 5

    def send_request(self, http_request):
        """
        Send a request and get response
        """
        pass

    def build_socket(self):
        """
        Generate either an HTTPS or HTTP socket
        """
        pass

    def find_cookie(self):
        """
        Find a list of all cookies for a given domain
        """
        pass

    def build_request(self):
        pass

    def get_response(self):
        """
        Get the response from the socket
        """
        pass

    def read_response_from_socket(self):
        # wait for socket to become ready
        pass
