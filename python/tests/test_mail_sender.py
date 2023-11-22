from mail_sender import Request, MailSender

def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    class User :
        def __init__(self, name, email):
            self.name = name
            self.email = email
            
    class HttpClient :
        
        def __init__(self):
            self.last_request = None
        def post(self, url, request):
            self.last_request = request
              
            
    user = User("Jean", "jeand@gmail.com")
    hc = HttpClient()
    mail = MailSender(hc)

    mail.send_v1(user, "New message")
    

    expected_request = Request("Jean", "jean@email.com", "New notification", "New message") 
    assert hc.last_request == expected_request

    


def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    class User :
        def __init__(self, name, email):
            self.name = name
            self.email = email

    class HttpClient:
        def __init__(self):
            self.requests = []
            
        def post(self, url, request):
            self.requests.append(request)
            if len(self.requests) == 1:
                return Response(503)
            else:
                return Response(200)

    class Response:
        def __init__(self, code):
            self.code = code


    http_client = HttpClient()
    mail_sender = MailSender(http_client)
    user = User("Jean", "jean@gmail.com")

    mail_sender.send_v2(user, "message")
    expected_request = Request("Jean", "jean@gmail.com", "New notification", "message") 

    assert len(http_client.requests) == 2
    assert http_client.requests[0] == expected_request
    assert http_client.requests[1] == expected_request