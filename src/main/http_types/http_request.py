from typing import Dict, Optional


class HttpRequest:
    def __init__(
        self,
        body: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        params: Optional[Dict] = None,
        query: Optional[Dict] = None,
    ):
        self.body = body
        self.headers = headers
        self.params = params
        self.query = query
