from mondo import MondoClient
from random import choice
from string import ascii_uppercase
from urllib import parse
import requests
from mondo.exceptions import MondoApiException


class MondoClientStaging(MondoClient):
    BASE_API_URL = 'https://staging-api.gmon.io'


BASE_API_URL = 'https://staging-api.gmon.io'
BASE_AUTH_API_URL = 'https://staging-auth.getmondo.co.uk'


def generate_state_token(length=10):
    return ''.join(choice(ascii_uppercase) for _ in range(length))


def generate_mondo_auth_url(client_id, redirect_uri, state_token=None):
    """
    Generate a url to redirect the user to
    for the first step of the authorization flow
    :param client_id: the oauth_client
    :param redirect_uri: URL to which the user will be redirected
    :param state_token: random token to check the authenticity of the request
    :return: authorization url
    """
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
    }

    if state_token:
        params.update({
            'state': state_token
        })

    return BASE_AUTH_API_URL + '/?' + parse.urlencode(params)


def exchange_authorization_code_for_access_token(client_id, client_secret, authorization_code, redirect_uri):
    """
    Exchange the authorization token for an access token
    :param client_id: the oauth_client_id
    :param client_secret: the client secret
    :param authorization_code: the authorization code returned by the first lef
                               of the oauth process
    :param redirect_uri: the (mandatory) redirect uri
    :return: A tuple of an access token and a refresh token (if your app is
             a confidential one).
    """

    response = requests.post(
        url=BASE_API_URL + "/oauth2/token",
        data={
            'grant_type': 'authorization_code',
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'code': authorization_code
        }
    ).json()

    if 'error' in response:
        raise MondoApiException(response['error_description'])

    return response['access_token'], response.get('refresh_token'), response.get('user_id')


def refresh_access_token(client_id, client_secret, refresh_token):
    """
    Confidential app are allowed to refresh the access token
    in order to make new requests.
    :param client_id:
    :param client_secret:
    :param refresh_token:
    :return: a tuple with the new access token and the new refresh token
    """
    response = requests.post(
        url=BASE_API_URL + "/oauth2/token",
        data={
            'grant_type': 'refresh_token',
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token
        }
    ).json()

    if 'error' in response:
        raise MondoApiException(response['error_description'])

    return response['access_token'], response['refresh_token']
