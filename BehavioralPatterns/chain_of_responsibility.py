class Handler:
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class ConcreteHandler1(Handler):  # Inherits from the abstract handler class
    """Concrete Handler 1"""

    def _handle(self, request):
        if 0 < request <= 10:  # provide condition for handling
            print(f'Request {request} handled in handler 1')
            return True


class DefaultHandler(Handler):  # Inherits from the abstract handler class
    """Default Handler"""

    def _handle(self, request):
        """If there is no handler is available"""
        # No condition checking as this the default handler
        print(f'End of chain, no handler for {request}')
        return True  # Indicates that request has been handled


class Client:   # Using handlers
    def __init__(self):
        # Create Handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))
        # Note that the default handler has no successor

    def delegate(self, requests):  # Send your requests one at a time for the handler to handle
        for request in requests:
            self.handler.handle(request)


if __name__ == "__main__":
    # Create a Client
    c = Client()

    # Create requests
    requests = [2, 5, 30]

    #Send the requests
    c.delegate(requests)