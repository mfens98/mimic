"""
Neutron API Plugin
"""
from __future__ import absolute_import, division, unicode_literals

import json
from uuid import uuid4
from six import text_type
from zope.interface import implementer
from twisted.plugin import IPlugin
from mimic.rest.mimicapp import MimicApp
from mimic.catalog import Entry
from mimic.catalog import Endpoint
from mimic.imimic import IAPIMock
from mimic.canned_responses.neutron import get_networks, get_network_by_key


@implementer(IAPIMock, IPlugin)
class NeutronApi(object):
    """
    Rest endpoints for mocked Neutron Api.
    """
    def __init__(self, regions=["ORD", "DFW", "IAD"]):
        """
        Create a NeutronApi.
        """
        self._regions = regions

    def catalog_entries(self, tenant_id):
        """
        List catalog entries for the Neutron API.
        """
        return [
            Entry(
                tenant_id, "network", "cloudNetworks",
                [
                    Endpoint(tenant_id, region, text_type(uuid4()), prefix="v2")
                    for region in self._regions
                ]
            )
        ]

    def resource_for_region(self, region, uri_prefix, session_store):
        """
        Get an :obj:`twisted.web.iweb.IResource` for the given URI prefix;
        implement :obj:`IAPIMock`.
        """
        return NeutronMock(self, uri_prefix, session_store, region).app.resource()


class NeutronMock(object):
    """
    Klein routes for the Neturon API.
    """
    def __init__(self, api_mock, uri_prefix, session_store, name):
        """
        Create a networks region with a given URI prefix
        """
        self.uri_prefix = uri_prefix
        self._api_mock = api_mock
        self._session_store = session_store
        self._name = name

    app = MimicApp()

    @app.route('/v2/<string:tenant_id>/networks', methods=['GET'])
    def network_list(self, request, tenant_id):
        """
        Gets network list
        """
        request.setResponseCode(200)
        return json.dumps({'networks' : []})


    @app.route('/v2/<string:tenant_id>/v2.0/networks', methods=['GET'])
    def list_networks(self, request, tenant_id):
        """
        Retrieves list of networks to which the specified tenant has access.
        http://developer.openstack.org/api-ref-networking-v2.html#listNetworks
        """
        #if doing a name request get name
        argName = (request.args.get(b'name', [None])[0])
        if argName is not None:
            argName = argName.decode("utf-8")
            response, network_info = get_network_by_key(argName)
            request.setResponseCode(response)
            if response == 200:
                return json.dumps(network_info)
            else:
                return ''

        request.setResponseCode(200)
        return json.dumps(get_networks())

    @app.route('/v2/<string:tenant_id>/v2.0/networks/<string:network_id>', methods=['GET'])
    def get_network_id(self, request, tenant_id, network_id):
        """
        Retrieves a specific networks to which the specified tenant has access.
        http://developer.openstack.org/api-ref-networking-v2.html#listNetworks
        """
        
        response, network_info = get_network_by_id(network_id)

        request.setResponseCode(response)
        if response == 200:
            return json.dumps(network_info)
        else:
            return ''

    @app.route('/v2/<string:tenant_id>/v2.0/security-groups', methods=['GET'])
    def get_security_groups(self, request, tenant_id):
        """
        Retrieves list of security-groups to which the specified tenant has access.
        http://developer.openstack.org/api-ref-networking-v2.html#security-groups-security-groups
        """
        request.setResponseCode(200)
        return json.dumps({'security_groups': []})
