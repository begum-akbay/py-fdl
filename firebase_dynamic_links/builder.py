from urllib.parse import urlencode

from .client import FirebaseClient


def generate_short_link(client, app_code, query_params, is_partial_link):
    long_dynamic_link = generate_long_link(app_code=app_code, is_partial_link=is_partial_link, query_params=query_params)

    return client.shorten_link(long_link=long_dynamic_link)


def generate_long_link(app_code, query_params, is_partial_link):
    query_string = urlencode(query_params)
    domain = 'https://{app_code}.page.link'.format(app_code=app_code) if is_partial_link else app_code
    
    link = '{domain}/?{query_string}'.format(domain=domain, query_string=query_string)

    return link



class DynamicLinkBuilder:
    def __init__(self, client):
        self.client = client

    def generate_long_link(self, app_code, is_partial_link=True, **kwargs):
        return generate_long_link(app_code=app_code, query_params=kwargs, is_partial_link=is_partial_link)

    def generate_short_link(self, app_code, is_partial_link=True, **kwargs):
        return generate_short_link(client=self.client, app_code=app_code, query_params=kwargs, is_partial_link=is_partial_link)


def dynamic_link_builder(api_key):
    return DynamicLinkBuilder(client=FirebaseClient(api_key=api_key))
