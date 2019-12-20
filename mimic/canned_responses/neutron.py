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
    Get network by its network_id or name
    Assumes network_id's are unique but not names
    """

    network_dict = get_networks()
    output_dict = {"networks" : []}
    for network in network_dict['networks']:
        if network['id'] == network_key:
            response = 200
            return (response, network)
        elif network['name'] == network_key:
            output_dict['networks'].append(network)
            
    if len(output_dict['networks']) > 0:
        #have a list of networks, return this
        response = 200
        return (response, output_dict)

    # network id not in networks return 404 not found
    response = 404
    return(response, '')
