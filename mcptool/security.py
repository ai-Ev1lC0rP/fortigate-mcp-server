import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === ANTIVIRUS PROFILES ===

@mcp.tool()
def fortigate_get_av_profiles(device_id: str, vdom: str = "root") -> str:
    """
    Get all antivirus profiles

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of antivirus profiles
    """
    try:
        api = fortigate_manager.get_device(device_id)
        profiles = api.get_av_profiles(vdom)
        return json.dumps(profiles, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_av_profile(device_id: str, name: str, 
                               inspection_mode: str = "proxy",
                               http_scan: str = "enable",
                               ftp_scan: str = "enable", 
                               imap_scan: str = "enable",
                               pop3_scan: str = "enable",
                               smtp_scan: str = "enable",
                               mapi_scan: str = "enable",
                               nntp_scan: str = "enable",
                               comments: Optional[str] = None,
                               vdom: str = "root") -> str:
    """
    Create antivirus profile

    Args:
        device_id: Device ID
        name: Profile name
        inspection_mode: Inspection mode (proxy, flow-based)
        http_scan: HTTP scanning (enable, disable)
        ftp_scan: FTP scanning (enable, disable)
        imap_scan: IMAP scanning (enable, disable)
        pop3_scan: POP3 scanning (enable, disable)
        smtp_scan: SMTP scanning (enable, disable)
        mapi_scan: MAPI scanning (enable, disable)
        nntp_scan: NNTP scanning (enable, disable)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile creation
    """
    try:
        profile_data = {
            "name": name,
            "inspection-mode": inspection_mode,
            "http": {"scan": http_scan},
            "ftp": {"scan": ftp_scan},
            "imap": {"scan": imap_scan},
            "pop3": {"scan": pop3_scan},
            "smtp": {"scan": smtp_scan},
            "mapi": {"scan": mapi_scan},
            "nntp": {"scan": nntp_scan}
        }

        if comments:
            profile_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_av_profile(profile_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_av_profile(device_id: str, profile_name: str, vdom: str = "root") -> str:
    """
    Delete antivirus profile

    Args:
        device_id: Device ID
        profile_name: Profile name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_av_profile(profile_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === WEB FILTER PROFILES ===

@mcp.tool()
def fortigate_get_webfilter_profiles(device_id: str, vdom: str = "root") -> str:
    """
    Get all web filter profiles

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of web filter profiles
    """
    try:
        api = fortigate_manager.get_device(device_id)
        profiles = api.get_webfilter_profiles(vdom)
        return json.dumps(profiles, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_webfilter_profile(device_id: str, name: str,
                                     inspection_mode: str = "proxy",
                                     https_replacemsg: str = "enable",
                                     log_all_url: str = "disable",
                                     web_flow_log_encoding: str = "utf-8",
                                     safe_search: str = "disable",
                                     youtube_restrict: str = "none",
                                     comments: Optional[str] = None,
                                     vdom: str = "root") -> str:
    """
    Create web filter profile

    Args:
        device_id: Device ID
        name: Profile name
        inspection_mode: Inspection mode (proxy, flow-based)
        https_replacemsg: HTTPS replacement message (enable, disable)
        log_all_url: Log all URLs (enable, disable)
        web_flow_log_encoding: Web flow log encoding
        safe_search: Safe search (enable, disable)
        youtube_restrict: YouTube restriction (none, strict, moderate)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile creation
    """
    try:
        profile_data = {
            "name": name,
            "inspection-mode": inspection_mode,
            "https-replacemsg": https_replacemsg,
            "log-all-url": log_all_url,
            "web-flow-log-encoding": web_flow_log_encoding,
            "safe-search": safe_search,
            "youtube-restrict": youtube_restrict
        }

        if comments:
            profile_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_webfilter_profile(profile_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_webfilter_profile(device_id: str, profile_name: str, vdom: str = "root") -> str:
    """
    Delete web filter profile

    Args:
        device_id: Device ID
        profile_name: Profile name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_webfilter_profile(profile_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === IPS SENSORS ===

@mcp.tool()
def fortigate_get_ips_sensors(device_id: str, vdom: str = "root") -> str:
    """
    Get all IPS sensors

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of IPS sensors
    """
    try:
        api = fortigate_manager.get_device(device_id)
        sensors = api.get_ips_sensors(vdom)
        return json.dumps(sensors, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ips_sensor(device_id: str, name: str,
                              block_malicious_url: str = "enable",
                              scan_botnet_connections: str = "enable", 
                              extended_log: str = "disable",
                              comments: Optional[str] = None,
                              vdom: str = "root") -> str:
    """
    Create IPS sensor

    Args:
        device_id: Device ID
        name: Sensor name
        block_malicious_url: Block malicious URLs (enable, disable)
        scan_botnet_connections: Scan botnet connections (enable, disable)
        extended_log: Extended logging (enable, disable)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of sensor creation
    """
    try:
        sensor_data = {
            "name": name,
            "block-malicious-url": block_malicious_url,
            "scan-botnet-connections": scan_botnet_connections,
            "extended-log": extended_log
        }

        if comments:
            sensor_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ips_sensor(sensor_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ips_sensor(device_id: str, sensor_name: str, vdom: str = "root") -> str:
    """
    Delete IPS sensor

    Args:
        device_id: Device ID
        sensor_name: Sensor name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of sensor deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ips_sensor(sensor_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SSL/SSH INSPECTION PROFILES ===

@mcp.tool()
def fortigate_get_ssl_ssh_profiles(device_id: str, vdom: str = "root") -> str:
    """
    Get all SSL/SSH inspection profiles

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of SSL/SSH inspection profiles
    """
    try:
        api = fortigate_manager.get_device(device_id)
        profiles = api.get_ssl_ssh_profiles(vdom)
        return json.dumps(profiles, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ssl_ssh_profile(device_id: str, name: str,
                                   ssl_inspect_all: str = "disable",
                                   https_inspection: str = "disable",
                                   ftps_inspection: str = "disable",
                                   imaps_inspection: str = "disable",
                                   pop3s_inspection: str = "disable",
                                   smtps_inspection: str = "disable",
                                   ssh_inspection: str = "disable",
                                   comments: Optional[str] = None,
                                   vdom: str = "root") -> str:
    """
    Create SSL/SSH inspection profile

    Args:
        device_id: Device ID
        name: Profile name
        ssl_inspect_all: Inspect all SSL (enable, disable)
        https_inspection: HTTPS inspection (enable, disable)
        ftps_inspection: FTPS inspection (enable, disable)
        imaps_inspection: IMAPS inspection (enable, disable)
        pop3s_inspection: POP3S inspection (enable, disable)
        smtps_inspection: SMTPS inspection (enable, disable)
        ssh_inspection: SSH inspection (enable, disable)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile creation
    """
    try:
        profile_data = {
            "name": name,
            "ssl": {
                "inspect-all": ssl_inspect_all
            },
            "https": {
                "status": https_inspection
            },
            "ftps": {
                "status": ftps_inspection
            },
            "imaps": {
                "status": imaps_inspection
            },
            "pop3s": {
                "status": pop3s_inspection
            },
            "smtps": {
                "status": smtps_inspection
            },
            "ssh": {
                "status": ssh_inspection
            }
        }

        if comments:
            profile_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ssl_ssh_profile(profile_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ssl_ssh_profile(device_id: str, profile_name: str, vdom: str = "root") -> str:
    """
    Delete SSL/SSH inspection profile

    Args:
        device_id: Device ID
        profile_name: Profile name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ssl_ssh_profile(profile_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === DNS FILTER PROFILES ===

@mcp.tool()
def fortigate_get_dnsfilter_profiles(device_id: str, vdom: str = "root") -> str:
    """
    Get all DNS filter profiles

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of DNS filter profiles
    """
    try:
        api = fortigate_manager.get_device(device_id)
        profiles = api.get_dnsfilter_profiles(vdom)
        return json.dumps(profiles, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_dnsfilter_profile(device_id: str, name: str,
                                     block_action: str = "block",
                                     log_all_domain: str = "disable",
                                     safe_search: str = "disable",
                                     youtube_restrict: str = "none",
                                     comments: Optional[str] = None,
                                     vdom: str = "root") -> str:
    """
    Create DNS filter profile

    Args:
        device_id: Device ID
        name: Profile name
        block_action: Block action (block, redirect)
        log_all_domain: Log all domains (enable, disable)
        safe_search: Safe search (enable, disable)
        youtube_restrict: YouTube restriction (none, strict, moderate)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile creation
    """
    try:
        profile_data = {
            "name": name,
            "block-action": block_action,
            "log-all-domain": log_all_domain,
            "safe-search": safe_search,
            "youtube-restrict": youtube_restrict
        }

        if comments:
            profile_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_dnsfilter_profile(profile_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_dnsfilter_profile(device_id: str, profile_name: str, vdom: str = "root") -> str:
    """
    Delete DNS filter profile

    Args:
        device_id: Device ID
        profile_name: Profile name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of profile deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_dnsfilter_profile(profile_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"