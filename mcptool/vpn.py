import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === IPSEC VPN ===

@mcp.tool()
def fortigate_get_ipsec_phase1(device_id: str, vdom: str = "root") -> str:
    """
    Get all IPSec phase 1 configurations

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of IPSec phase 1 configurations
    """
    try:
        api = fortigate_manager.get_device(device_id)
        phase1 = api.get_ipsec_phase1(vdom)
        return json.dumps(phase1, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ipsec_phase1(device_id: str, name: str, interface: str,
                                 remote_gw: str, psk: str,
                                 proposal: str = "aes128-sha256 aes256-sha256",
                                 dhgrp: str = "14 5",
                                 nattraversal: str = "enable",
                                 keepalive: int = 10,
                                 dead_peer_detection: str = "on-idle",
                                 mode: str = "main",
                                 peertype: str = "any",
                                 comments: Optional[str] = None,
                                 vdom: str = "root") -> str:
    """
    Create IPSec phase 1 interface

    Args:
        device_id: Device ID
        name: Interface name
        interface: Physical interface
        remote_gw: Remote gateway IP
        psk: Pre-shared key
        proposal: Encryption proposal
        dhgrp: Diffie-Hellman groups
        nattraversal: NAT traversal (enable, disable)
        keepalive: Keepalive frequency
        dead_peer_detection: DPD setting (on-idle, on-demand, disable)
        mode: IKE mode (main, aggressive)
        peertype: Peer type (any, one, dialup, peer, peergrp)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of phase 1 creation
    """
    try:
        phase1_data = {
            "name": name,
            "interface": interface,
            "remote-gw": remote_gw,
            "psksecret": psk,
            "proposal": proposal,
            "dhgrp": dhgrp,
            "nattraversal": nattraversal,
            "keepalive": keepalive,
            "dpd": dead_peer_detection,
            "mode": mode,
            "peertype": peertype
        }

        if comments:
            phase1_data["comments"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ipsec_phase1(phase1_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ipsec_phase1(device_id: str, interface_name: str, vdom: str = "root") -> str:
    """
    Delete IPSec phase 1 interface

    Args:
        device_id: Device ID
        interface_name: Interface name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of phase 1 deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ipsec_phase1(interface_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_ipsec_phase2(device_id: str, vdom: str = "root") -> str:
    """
    Get all IPSec phase 2 configurations

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of IPSec phase 2 configurations
    """
    try:
        api = fortigate_manager.get_device(device_id)
        phase2 = api.get_ipsec_phase2(vdom)
        return json.dumps(phase2, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ipsec_phase2(device_id: str, name: str, phase1name: str,
                                 proposal: str = "aes128-sha1 aes256-sha256",
                                 dhgrp: str = "14 5",
                                 pfs: str = "enable",
                                 keepalive: str = "enable",
                                 auto_negotiate: str = "enable",
                                 src_subnet: str = "0.0.0.0/0",
                                 dst_subnet: str = "0.0.0.0/0",
                                 comments: Optional[str] = None,
                                 vdom: str = "root") -> str:
    """
    Create IPSec phase 2 interface

    Args:
        device_id: Device ID
        name: Interface name
        phase1name: Associated phase 1 interface
        proposal: Encryption proposal
        dhgrp: Diffie-Hellman groups
        pfs: Perfect Forward Secrecy (enable, disable)
        keepalive: Keepalive (enable, disable)
        auto_negotiate: Auto negotiate (enable, disable)
        src_subnet: Source subnet
        dst_subnet: Destination subnet
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of phase 2 creation
    """
    try:
        phase2_data = {
            "name": name,
            "phase1name": phase1name,
            "proposal": proposal,
            "dhgrp": dhgrp,
            "pfs": pfs,
            "keepalive": keepalive,
            "auto-negotiate": auto_negotiate,
            "src-subnet": src_subnet,
            "dst-subnet": dst_subnet
        }

        if comments:
            phase2_data["comments"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ipsec_phase2(phase2_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ipsec_phase2(device_id: str, interface_name: str, vdom: str = "root") -> str:
    """
    Delete IPSec phase 2 interface

    Args:
        device_id: Device ID
        interface_name: Interface name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of phase 2 deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ipsec_phase2(interface_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_ipsec_tunnel_status(device_id: str, vdom: str = "root") -> str:
    """
    Get IPSec tunnel status

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        IPSec tunnel status information
    """
    try:
        api = fortigate_manager.get_device(device_id)
        status = api.get_ipsec_tunnels_status(vdom)
        return json.dumps(status, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SSL VPN ===

@mcp.tool()
def fortigate_get_ssl_vpn_settings(device_id: str, vdom: str = "root") -> str:
    """
    Get SSL VPN settings

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        SSL VPN settings
    """
    try:
        api = fortigate_manager.get_device(device_id)
        settings = api.get_ssl_vpn_settings(vdom)
        return json.dumps(settings, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_update_ssl_vpn_settings(device_id: str,
                                    status: Optional[str] = None,
                                    port: Optional[int] = None,
                                    source_interface: Optional[List[str]] = None,
                                    source_address: Optional[List[str]] = None,
                                    default_portal: Optional[str] = None,
                                    tunnel_ip_pools: Optional[List[str]] = None,
                                    dns_server1: Optional[str] = None,
                                    dns_server2: Optional[str] = None,
                                    wins_server1: Optional[str] = None,
                                    wins_server2: Optional[str] = None,
                                    vdom: str = "root") -> str:
    """
    Update SSL VPN settings

    Args:
        device_id: Device ID
        status: SSL VPN status (enable, disable)
        port: SSL VPN port (default: 443)
        source_interface: Source interfaces
        source_address: Source addresses
        default_portal: Default portal
        tunnel_ip_pools: Tunnel IP pools
        dns_server1: Primary DNS server
        dns_server2: Secondary DNS server
        wins_server1: Primary WINS server
        wins_server2: Secondary WINS server
        vdom: Target VDOM (default: root)

    Returns:
        Result of settings update
    """
    try:
        settings_data = {}

        if status:
            settings_data["status"] = status
        if port:
            settings_data["port"] = port
        if source_interface:
            settings_data["source-interface"] = [{"name": intf} for intf in source_interface]
        if source_address:
            settings_data["source-address"] = [{"name": addr} for addr in source_address]
        if default_portal:
            settings_data["default-portal"] = default_portal
        if tunnel_ip_pools:
            settings_data["tunnel-ip-pools"] = [{"name": pool} for pool in tunnel_ip_pools]
        if dns_server1:
            settings_data["dns-server1"] = dns_server1
        if dns_server2:
            settings_data["dns-server2"] = dns_server2
        if wins_server1:
            settings_data["wins-server1"] = wins_server1
        if wins_server2:
            settings_data["wins-server2"] = wins_server2

        if not settings_data:
            return "Error: No settings provided to update"

        api = fortigate_manager.get_device(device_id)
        result = api.update_ssl_vpn_settings(settings_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_ssl_vpn_portals(device_id: str, vdom: str = "root") -> str:
    """
    Get SSL VPN portals

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of SSL VPN portals
    """
    try:
        api = fortigate_manager.get_device(device_id)
        portals = api.get_ssl_vpn_portals(vdom)
        return json.dumps(portals, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ssl_vpn_portal(device_id: str, name: str,
                                  tunnel_mode: str = "enable",
                                  web_mode: str = "enable",
                                  ip_pools: Optional[List[str]] = None,
                                  exclusive_routing: str = "disable",
                                  auto_connect: str = "disable",
                                  keep_alive: str = "enable",
                                  save_password: str = "disable",
                                  split_tunneling: str = "enable",
                                  theme: str = "blue",
                                  comments: Optional[str] = None,
                                  vdom: str = "root") -> str:
    """
    Create SSL VPN portal

    Args:
        device_id: Device ID
        name: Portal name
        tunnel_mode: Tunnel mode (enable, disable)
        web_mode: Web mode (enable, disable)
        ip_pools: IP pools for clients
        exclusive_routing: Exclusive routing (enable, disable)
        auto_connect: Auto connect (enable, disable)
        keep_alive: Keep alive (enable, disable)
        save_password: Save password (enable, disable)
        split_tunneling: Split tunneling (enable, disable)
        theme: Portal theme (blue, green, red, melongene, mariner)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of portal creation
    """
    try:
        portal_data = {
            "name": name,
            "tunnel-mode": tunnel_mode,
            "web-mode": web_mode,
            "exclusive-routing": exclusive_routing,
            "auto-connect": auto_connect,
            "keep-alive": keep_alive,
            "save-password": save_password,
            "split-tunneling": split_tunneling,
            "theme": theme
        }

        if ip_pools:
            portal_data["ip-pools"] = [{"name": pool} for pool in ip_pools]
        if comments:
            portal_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ssl_vpn_portal(portal_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ssl_vpn_portal(device_id: str, portal_name: str, vdom: str = "root") -> str:
    """
    Delete SSL VPN portal

    Args:
        device_id: Device ID
        portal_name: Portal name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of portal deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ssl_vpn_portal(portal_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_ssl_vpn_status(device_id: str, vdom: str = "root") -> str:
    """
    Get SSL VPN status

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        SSL VPN status information
    """
    try:
        api = fortigate_manager.get_device(device_id)
        status = api.get_ssl_vpn_status(vdom)
        return json.dumps(status, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === VPN CERTIFICATES ===

@mcp.tool()
def fortigate_get_vpn_certificates(device_id: str, vdom: str = "root") -> str:
    """
    Get VPN certificates

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of VPN certificates
    """
    try:
        api = fortigate_manager.get_device(device_id)
        certificates = api.get_vpn_certificates(vdom)
        return json.dumps(certificates, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"