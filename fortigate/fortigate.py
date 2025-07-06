#!/usr/bin/env python3
"""
Fortigate MCP Server using FastMCP
Manages multiple Fortigate devices and VDOMs
"""

import json
import logging
import requests
from typing import Dict, List, Optional, Any
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Logging configuration
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("fortigate-mcp")


class FortigateAPI:
    """Class to manage Fortigate REST APIs"""

    def __init__(self, host: str, token: str):
        self.host = host.rstrip('/')
        self.token = token
        self.base_url = f"https://{self.host}/api/v2"
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        })
        self.session.verify = False

    def _make_request(self, method: str, endpoint: str, vdom: str = 'root',
                      params: Dict = None, data: Dict = None) -> Dict:
        """Executes API request with VDOM handling"""
        url = f"{self.base_url}/{endpoint}"

        # Add VDOM parameter if not root
        if vdom != 'root':
            params = params or {}
            params['vdom'] = vdom

        try:
            logger.debug(f"making request to {url} with params {params}, data {data}, vdom {vdom}")
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            logger.debug(f"response: {response.text}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def get_system_status(self) -> Dict:
        """Get system status"""
        return self._make_request('GET', 'monitor/system/status')

    def get_vdoms(self) -> List[Dict]:
        """List all VDOMs"""
        result = self._make_request('GET', 'cmdb/system/vdom')
        return result.get('results', [])

### Policy
    def get_firewall_policies(self, vdom: str = 'root') -> List[Dict]:
        """Get firewall policy list"""
        result = self._make_request('GET', 'cmdb/firewall/policy', vdom=vdom)
        return result.get('results', [])

    def get_policy_by_id(self, policy_id: int, vdom: str = 'root') -> Dict:
        """Get specific firewall policy by ID"""
        result = self._make_request('GET', f'cmdb/firewall/policy/{policy_id}', vdom=vdom)
        return result.get('results', {})

    def create_firewall_policy(self, policy_data: Dict, vdom: str = 'root') -> Dict:
        """Create new firewall policy"""
        return self._make_request('POST', 'cmdb/firewall/policy', vdom=vdom, data=policy_data)

    def update_firewall_policy(self, policy_id: int, policy_data: Dict, vdom: str = 'root') -> Dict:
        """Update existing firewall policy"""
        return self._make_request('PUT', f'cmdb/firewall/policy/{policy_id}', vdom=vdom, data=policy_data)

    def delete_firewall_policy(self, policy_id: int, vdom: str = 'root') -> Dict:
        """Delete firewall policy"""
        return self._make_request('DELETE', f'cmdb/firewall/policy/{policy_id}', vdom=vdom)

    def lookup_firewall_policy(self, srcintf: str,source_ip: str,protocol: str,dest: str,source_port: int = 0,dest_port: int =0, vdom: str = 'root') -> Dict:
        """Lookup existing firewall policy, simulating a packet"""
        params = {
            'srcintf': srcintf,
            'sourceip': source_ip,
            'protocol': protocol,
            'dest': dest,
        }
        if source_port != 0:
            params['sourceport'] = source_port
        if dest_port != 0:
            params['destport'] = dest_port

        result = self._make_request('GET', f'monitor/firewall/policy-lookup', vdom=vdom,params=params )
        return result.get('results', {})

    def get_address_objects(self, vdom: str = 'root') -> List[Dict]:
        """Get address objects"""
        result = self._make_request('GET', 'cmdb/firewall/address', vdom=vdom)
        return result.get('results', [])

    def create_address_object(self, address_data: Dict, vdom: str = 'root') -> Dict:
        """Create address object"""
        return self._make_request('POST', 'cmdb/firewall/address', vdom=vdom, data=address_data)

    def get_service_objects(self, vdom: str = 'root') -> List[Dict]:
        """Get service objects"""
        result = self._make_request('GET', 'cmdb/firewall/service/custom', vdom=vdom)
        return result.get('results', [])

    def create_service_object(self, service_data: Dict, vdom: str = 'root') -> Dict:
        """Create service object"""
        return self._make_request('POST', 'cmdb/firewall/service/custom', vdom=vdom, data=service_data)

    def get_vip_addresses(self, vdom: str = 'root') -> List[Dict]:
        """Get firewall virtual ip list"""
        result = self._make_request('GET', 'cmdb/firewall/vip', vdom=vdom)
        return result.get('results', [])

    def delete_vip_address(self, vip_name: str, vdom: str = 'root') -> Dict:
        """Delete firewall virtual ip address"""
        result = self._make_request('DELETE', f'cmdb/firewall/vip/{vip_name}', vdom=vdom)
        return result.get('results', [])

    ### Network
    def get_interfaces(self, vdom: str = 'root') -> List[Dict]:
        """Get interface list"""
        result = self._make_request('GET', 'cmdb/system/interface', vdom=vdom)
        return result.get('results', [])

    def get_static_routes(self, vdom: str = 'root') -> List[Dict]:
        """Get static routes"""
        result = self._make_request('GET', 'cmdb/router/static', vdom=vdom)
        return result.get('results', [])

    def create_static_route(self, route_data: Dict, vdom: str = 'root') -> Dict:
        """Create static route"""
        return self._make_request('POST', 'cmdb/router/static', vdom=vdom, data=route_data)

    def get_policy_routes(self, vdom: str = 'root') -> List[Dict]:
        """Get policy routes"""
        result = self._make_request('GET', 'cmdb/router/policy', vdom=vdom)
        return result.get('results', [])

    def get_routing_table(self, vdom: str = 'root') -> List[Dict]:
        """
        Get the live routing table (like 'get router info routing-table all' in CLI)
        for the specified VDOM (default 'root').
        """
        endpoint = 'monitor/router/ipv4'
        result = self._make_request('GET', endpoint, vdom=vdom)
        return result.get('results', [])
### Routing dynamic
    def get_bgp_peers(self, vdom: str = 'root') -> List[Dict]:
        endpoint = 'monitor/router/bgp/neighbors'
        result = self._make_request('GET', endpoint, vdom=vdom)
        return result.get('results', [])

    def route_lookup(self, route: str, vdom: str = 'root' ) -> Dict:
        endpoint = 'monitor/router/lookup'
        result = self._make_request('GET', endpoint, vdom=vdom, params={"destination": route})
        return result.get('results',{})

### Security Profiles
    def get_av_profiles(self, vdom: str = 'root') -> List[Dict]:
        """Get antivirus profiles"""
        result = self._make_request('GET', 'cmdb/antivirus/profile', vdom=vdom)
        return result.get('results', [])

    def create_av_profile(self, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Create antivirus profile"""
        return self._make_request('POST', 'cmdb/antivirus/profile', vdom=vdom, data=profile_data)

    def update_av_profile(self, profile_name: str, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Update antivirus profile"""
        return self._make_request('PUT', f'cmdb/antivirus/profile/{profile_name}', vdom=vdom, data=profile_data)

    def delete_av_profile(self, profile_name: str, vdom: str = 'root') -> Dict:
        """Delete antivirus profile"""
        return self._make_request('DELETE', f'cmdb/antivirus/profile/{profile_name}', vdom=vdom)

    def get_webfilter_profiles(self, vdom: str = 'root') -> List[Dict]:
        """Get web filter profiles"""
        result = self._make_request('GET', 'cmdb/webfilter/profile', vdom=vdom)
        return result.get('results', [])

    def create_webfilter_profile(self, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Create web filter profile"""
        return self._make_request('POST', 'cmdb/webfilter/profile', vdom=vdom, data=profile_data)

    def update_webfilter_profile(self, profile_name: str, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Update web filter profile"""
        return self._make_request('PUT', f'cmdb/webfilter/profile/{profile_name}', vdom=vdom, data=profile_data)

    def delete_webfilter_profile(self, profile_name: str, vdom: str = 'root') -> Dict:
        """Delete web filter profile"""
        return self._make_request('DELETE', f'cmdb/webfilter/profile/{profile_name}', vdom=vdom)

    def get_ips_sensors(self, vdom: str = 'root') -> List[Dict]:
        """Get IPS sensors"""
        result = self._make_request('GET', 'cmdb/ips/sensor', vdom=vdom)
        return result.get('results', [])

    def create_ips_sensor(self, sensor_data: Dict, vdom: str = 'root') -> Dict:
        """Create IPS sensor"""
        return self._make_request('POST', 'cmdb/ips/sensor', vdom=vdom, data=sensor_data)

    def update_ips_sensor(self, sensor_name: str, sensor_data: Dict, vdom: str = 'root') -> Dict:
        """Update IPS sensor"""
        return self._make_request('PUT', f'cmdb/ips/sensor/{sensor_name}', vdom=vdom, data=sensor_data)

    def delete_ips_sensor(self, sensor_name: str, vdom: str = 'root') -> Dict:
        """Delete IPS sensor"""
        return self._make_request('DELETE', f'cmdb/ips/sensor/{sensor_name}', vdom=vdom)

    def get_ssl_ssh_profiles(self, vdom: str = 'root') -> List[Dict]:
        """Get SSL/SSH inspection profiles"""
        result = self._make_request('GET', 'cmdb/firewall/ssl-ssh-profile', vdom=vdom)
        return result.get('results', [])

    def create_ssl_ssh_profile(self, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Create SSL/SSH inspection profile"""
        return self._make_request('POST', 'cmdb/firewall/ssl-ssh-profile', vdom=vdom, data=profile_data)

    def update_ssl_ssh_profile(self, profile_name: str, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Update SSL/SSH inspection profile"""
        return self._make_request('PUT', f'cmdb/firewall/ssl-ssh-profile/{profile_name}', vdom=vdom, data=profile_data)

    def delete_ssl_ssh_profile(self, profile_name: str, vdom: str = 'root') -> Dict:
        """Delete SSL/SSH inspection profile"""
        return self._make_request('DELETE', f'cmdb/firewall/ssl-ssh-profile/{profile_name}', vdom=vdom)

    def get_dnsfilter_profiles(self, vdom: str = 'root') -> List[Dict]:
        """Get DNS filter profiles"""
        result = self._make_request('GET', 'cmdb/dnsfilter/profile', vdom=vdom)
        return result.get('results', [])

    def create_dnsfilter_profile(self, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Create DNS filter profile"""
        return self._make_request('POST', 'cmdb/dnsfilter/profile', vdom=vdom, data=profile_data)

    def update_dnsfilter_profile(self, profile_name: str, profile_data: Dict, vdom: str = 'root') -> Dict:
        """Update DNS filter profile"""
        return self._make_request('PUT', f'cmdb/dnsfilter/profile/{profile_name}', vdom=vdom, data=profile_data)

    def delete_dnsfilter_profile(self, profile_name: str, vdom: str = 'root') -> Dict:
        """Delete DNS filter profile"""
        return self._make_request('DELETE', f'cmdb/dnsfilter/profile/{profile_name}', vdom=vdom)

### User Management
    def get_local_users(self, vdom: str = 'root') -> List[Dict]:
        """Get local users"""
        result = self._make_request('GET', 'cmdb/user/local', vdom=vdom)
        return result.get('results', [])

    def create_local_user(self, user_data: Dict, vdom: str = 'root') -> Dict:
        """Create local user"""
        return self._make_request('POST', 'cmdb/user/local', vdom=vdom, data=user_data)

    def update_local_user(self, username: str, user_data: Dict, vdom: str = 'root') -> Dict:
        """Update local user"""
        return self._make_request('PUT', f'cmdb/user/local/{username}', vdom=vdom, data=user_data)

    def delete_local_user(self, username: str, vdom: str = 'root') -> Dict:
        """Delete local user"""
        return self._make_request('DELETE', f'cmdb/user/local/{username}', vdom=vdom)

    def get_user_groups(self, vdom: str = 'root') -> List[Dict]:
        """Get user groups"""
        result = self._make_request('GET', 'cmdb/user/group', vdom=vdom)
        return result.get('results', [])

    def create_user_group(self, group_data: Dict, vdom: str = 'root') -> Dict:
        """Create user group"""
        return self._make_request('POST', 'cmdb/user/group', vdom=vdom, data=group_data)

    def update_user_group(self, group_name: str, group_data: Dict, vdom: str = 'root') -> Dict:
        """Update user group"""
        return self._make_request('PUT', f'cmdb/user/group/{group_name}', vdom=vdom, data=group_data)

    def delete_user_group(self, group_name: str, vdom: str = 'root') -> Dict:
        """Delete user group"""
        return self._make_request('DELETE', f'cmdb/user/group/{group_name}', vdom=vdom)

    def get_auth_servers(self, vdom: str = 'root') -> List[Dict]:
        """Get authentication servers (LDAP)"""
        result = self._make_request('GET', 'cmdb/user/ldap', vdom=vdom)
        return result.get('results', [])

    def create_ldap_server(self, server_data: Dict, vdom: str = 'root') -> Dict:
        """Create LDAP authentication server"""
        return self._make_request('POST', 'cmdb/user/ldap', vdom=vdom, data=server_data)

    def update_ldap_server(self, server_name: str, server_data: Dict, vdom: str = 'root') -> Dict:
        """Update LDAP authentication server"""
        return self._make_request('PUT', f'cmdb/user/ldap/{server_name}', vdom=vdom, data=server_data)

    def delete_ldap_server(self, server_name: str, vdom: str = 'root') -> Dict:
        """Delete LDAP authentication server"""
        return self._make_request('DELETE', f'cmdb/user/ldap/{server_name}', vdom=vdom)

    def get_radius_servers(self, vdom: str = 'root') -> List[Dict]:
        """Get RADIUS authentication servers"""
        result = self._make_request('GET', 'cmdb/user/radius', vdom=vdom)
        return result.get('results', [])

    def create_radius_server(self, server_data: Dict, vdom: str = 'root') -> Dict:
        """Create RADIUS authentication server"""
        return self._make_request('POST', 'cmdb/user/radius', vdom=vdom, data=server_data)

    def delete_radius_server(self, server_name: str, vdom: str = 'root') -> Dict:
        """Delete RADIUS authentication server"""
        return self._make_request('DELETE', f'cmdb/user/radius/{server_name}', vdom=vdom)


class FortigateManager:
    """Manages multiple Fortigate devices"""

    def __init__(self):
        self.devices: Dict[str, FortigateAPI] = {}
        self.device_configs: Dict[str, Dict] = {}

    def add_device(self, device_id: str, host: str, token: str, vdoms: List[str] = None):
        """Add a new device"""
        api = FortigateAPI(host, token)
        self.devices[device_id] = api
        self.device_configs[device_id] = {
            'host': host,
            'vdoms': vdoms or ['root']
        }
        logger.info(f"Added device {device_id} at {host}")

    def get_device(self, device_id: str) -> FortigateAPI:
        """Get API instance for device"""
        if device_id not in self.devices:
            raise ValueError(f"Device {device_id} not found")
        return self.devices[device_id]

    def list_devices(self) -> List[Dict]:
        """List all configured devices"""
        return [
            {
                'device_id': device_id,
                'host': config['host'],
                'vdoms': config['vdoms']
            }
            for device_id, config in self.device_configs.items()
        ]