from django.core.wsgi import get_wsgi_application
from django.test import TestCase
from django.test.client import RequestFactory


class WSGITest(TestCase):
    urls = "regressiontests.wsgi.urls"

    def test_get_wsgi_application(self):
        """
        Verify that ``get_wsgi_application`` returns a functioning WSGI
        callable.

        """
        application = get_wsgi_application()

        environ = RequestFactory()._base_environ(
            PATH_INFO="/",
            CONTENT_TYPE="text/html; charset=utf-8",
            REQUEST_METHOD="GET"
            )

        response_data = {}

        def start_response(status, headers):
            response_data["status"] = status
            response_data["headers"] = headers

        response = application(environ, start_response)

        self.assertEqual(response_data["status"], "200 OK")
        self.assertEqual(
            response_data["headers"],
            [('Content-Type', 'text/html; charset=utf-8')])
        self.assertEqual(
            unicode(response),
            u"Content-Type: text/html; charset=utf-8\n\nHello World!")
