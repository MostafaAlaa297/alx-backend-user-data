#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to authenticate"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the path requires authentication.
        :param path: The path to check.
        :param excluded_paths: A list of paths that
        are excluded from authentication.
        :return: False for now, as implementation will be added later.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        :param request: The Flask request object.
        :return: None, as the implementation will be added later.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.
        :param request: The Flask request object.
        :return: None, as the implementation will be added later.
        """
        return None
