#!/usr/bin/env python3
"""
BasicAuth module for the API authentication.
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the
        Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        elif isinstance(authorization_header, str) is False:
            return None
        elif authorization_header.startswith("Basic") and authorization_header.endswith(" "):
            return None
        else:
            return authorization_header.split("Basic ", 1)[1]
