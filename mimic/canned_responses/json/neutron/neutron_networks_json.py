"""
Neutron Networks
"""

from __future__ import absolute_import, division, unicode_literals

networks = {
    "networks":
        [{
              "admin_state_up" : True,
              "id" : "71c1e68c-171a-4aa2-aca5-50ea153a3718",
              "name" : "network_1",
              "provider:network_type" : "vlan",
              "provider:physical_network" : "physnet1",
              "provider:segmentation_id" : "1000",
              "router:external" : False,
              "shared" : False,
              "status" : "ACTIVE",
              "subnets" : [],
              "tenant_id": "20bd52ff3e1b40039c312395b04683cf",
              "project_id": "20bd52ff3e1b40039c312395b04683cf"
         },
         {
              "admin_state_up": True,
              "id" : "396f12f8-521e-4b91-8e21-2e003500433a",
              "name" : "network_2",
              "provider:network_type" : "vlan",
              "provider:physical_network" : "physnet1",
              "provider:segmentation_id" : "1001",
              "router:external" : False,
              "shared" : False,
              "status" : "ACTIVE",
              "subnets" : [],
              "tenant_id": "20bd52ff3e1b40039c312395b04683cf",
              "project_id": "20bd52ff3e1b40039c312395b04683cf"
         },
         {
              "admin_state_up" : True,
              "id" : "71c1e68c-171a-4aa2-aca5-50ea153a4829",
              "name" : "duplicate_network",
              "provider:network_type" : "vlan",
              "provider:physical_network" : "physnet1",
              "provider:segmentation_id" : "1000",
              "router:external" : False,
              "shared" : False,
              "status" : "ACTIVE",
              "subnets" : [],
              "tenant_id": "20bd52ff3e1b40039c312395b04683cf",
              "project_id": "20bd52ff3e1b40039c312395b04683cf"
        
         },
         {
              "admin_state_up" : True,
              "id" : "82d2e68c-171a-4aa2-aca5-50ea153a4829",
              "name" : "duplicate_network",
              "provider:network_type" : "vlan",
              "provider:physical_network" : "physnet1",
              "provider:segmentation_id" : "1000",
              "router:external" : False,
              "shared" : False,
              "status" : "ACTIVE",
              "subnets" : [],
              "tenant_id": "20bd52ff3e1b40039c312395b04683cf",
              "project_id": "20bd52ff3e1b40039c312395b04683cf"
        
         }]
}
