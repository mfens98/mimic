"""
Canned responses for neutron networks 
"""
from __future__ import absolute_import, division, unicode_literals
from mimic.canned_responses.json.neutron.neutron_networks_json import networks

def get_networks():
    """
    Canned response for neutron get networks call
    """
    return networks

def get_network_by_key(network_key):
    """
    Get network by its network_id
    """

    network_dict = get_networks()
    for network in network_dict['networks']:
        if network['id'] == network_key:
            response = 200
            return (response, network)
        elif network['name'] == network_key:
            response = 200
            output_dict = {"networks" : [network]}
            return (response, output_dict)

    # network id not in networks return 404 not found
    response = 404
    return(response, '')
