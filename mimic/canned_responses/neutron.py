"""
Canned responses for neutron networks 
"""
from __future__ import absolute_import, division, unicode_literals
from mimic.canned_responses.json.neutron.neutron_networks_json import networks

def get_networks():
    """
    Canned response for neutron get networks call
    """
    print("Called networks function")
    return networks

def get_network_by_id(network_id):
    """
    Get network by its network_id
    """

    network_dict = get_networks()
    for network in network_dict['networks']:
        if network['id'] == network_id:
            response = 200
            return (response, image)

    # network id not in networks return 404 not found
    response = 404
    return(response, '')
