# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 02.12.12, 20:01 CET
    
    Copyright (c) 2012 apitrary

"""
import logging
import tornado
from tornado.httpclient import HTTPRequest
from deployrlib.config.event_reporter_config import EVENT_REPORTER_CONFIG
from deployrlib.config.logging_config import LOG_FORMAT
from deployrlib.services import deployr_config_service, logging_service
from tornado import httpclient

# Logger
logging.basicConfig(format=LOG_FORMAT)
logger = logging_service.get_logger()

class EventReporter(object):
    """
        Reports all events back to a defined API for later reference.
    """

    def __init__(self):
        """
            Initialize the EventReporter
        """
        super(EventReporter, self).__init__()

        # Load configuration
        self.config = deployr_config_service.load_configuration()
        self.env = EVENT_REPORTER_CONFIG[self.config['NAME']]
        self.deploy_url = '{}/deploys'.format(self.env['EVENT_REPORTER_URL'])

        # Setup the Async HTTP client for calling Riak asynchronously
        self.http_client = tornado.httpclient.HTTPClient()


    def send(self, message):
        """
            Send a message to API URL
        """
        request = HTTPRequest(url=self.deploy_url)
        request.method = 'POST'
        request.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        request.body = message

        try:
            #noinspection PyTypeChecker
            response = self.http_client.fetch(request=request)
            logger.debug("Response from Event Reporter: {}".format(response.body))
        except httpclient.HTTPError, e:
            logger.error("Error when trying to contact Event Reporter! Error: {}".format(e))

##############################################################################
#
# FOR DEBUGGING
#
##############################################################################

if __name__ == '__main__':
    event_reporter = EventReporter()
    event_reporter.send('test')
