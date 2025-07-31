import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === LOCAL USERS ===

@mcp.tool()
def fortigate_get_local_users(device_id: str, vdom: str = "root") -> str:
    """
    Get all local users

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of local users
    """
    try:
        api = fortigate_manager.get_device(device_id)
        users = api.get_local_users(vdom)
        return json.dumps(users, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_local_user(device_id: str, name: str, password: str,
                               type: str = "password",
                               status: str = "enable",
                               email_to: Optional[str] = None,
                               sms_server: Optional[str] = None,
                               sms_phone: Optional[str] = None,
                               comments: Optional[str] = None,
                               vdom: str = "root") -> str:
    """
    Create local user

    Args:
        device_id: Device ID
        name: Username
        password: User password
        type: Authentication type (password, radius, tacacs+, ldap)
        status: User status (enable, disable)
        email_to: Email address for notifications
        sms_server: SMS server for notifications
        sms_phone: SMS phone number
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of user creation
    """
    try:
        user_data = {
            "name": name,
            "type": type,
            "status": status,
            "passwd": password
        }

        if email_to:
            user_data["email-to"] = email_to
        if sms_server:
            user_data["sms-server"] = sms_server
        if sms_phone:
            user_data["sms-phone"] = sms_phone
        if comments:
            user_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_local_user(user_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_update_local_user(device_id: str, username: str,
                               password: Optional[str] = None,
                               type: Optional[str] = None,
                               status: Optional[str] = None,
                               email_to: Optional[str] = None,
                               sms_server: Optional[str] = None,
                               sms_phone: Optional[str] = None,
                               comments: Optional[str] = None,
                               vdom: str = "root") -> str:
    """
    Update local user

    Args:
        device_id: Device ID
        username: Username to update
        password: New password (optional)
        type: Authentication type (optional)
        status: User status (optional)
        email_to: Email address (optional)
        sms_server: SMS server (optional)
        sms_phone: SMS phone number (optional)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of user update
    """
    try:
        user_data = {}

        if password:
            user_data["passwd"] = password
        if type:
            user_data["type"] = type
        if status:
            user_data["status"] = status
        if email_to:
            user_data["email-to"] = email_to
        if sms_server:
            user_data["sms-server"] = sms_server
        if sms_phone:
            user_data["sms-phone"] = sms_phone
        if comments:
            user_data["comment"] = comments

        if not user_data:
            return "Error: No fields provided to update"

        api = fortigate_manager.get_device(device_id)
        result = api.update_local_user(username, user_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_local_user(device_id: str, username: str, vdom: str = "root") -> str:
    """
    Delete local user

    Args:
        device_id: Device ID
        username: Username to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of user deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_local_user(username, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === USER GROUPS ===

@mcp.tool()
def fortigate_get_user_groups(device_id: str, vdom: str = "root") -> str:
    """
    Get all user groups

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of user groups
    """
    try:
        api = fortigate_manager.get_device(device_id)
        groups = api.get_user_groups(vdom)
        return json.dumps(groups, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_user_group(device_id: str, name: str,
                               auth_concurrent_override: str = "disable",
                               auth_concurrent_value: int = 0,
                               authtimeout: int = 0,
                               http_digest_realm: Optional[str] = None,
                               sso_attribute_value: Optional[str] = None,
                               comments: Optional[str] = None,
                               members: Optional[List[str]] = None,
                               vdom: str = "root") -> str:
    """
    Create user group

    Args:
        device_id: Device ID
        name: Group name
        auth_concurrent_override: Override concurrent authentication (enable, disable)
        auth_concurrent_value: Maximum concurrent authentications
        authtimeout: Authentication timeout (minutes)
        http_digest_realm: HTTP digest realm
        sso_attribute_value: SSO attribute value
        comments: Comments (optional)
        members: List of group members (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of group creation
    """
    try:
        group_data = {
            "name": name,
            "auth-concurrent-override": auth_concurrent_override,
            "auth-concurrent-value": auth_concurrent_value,
            "authtimeout": authtimeout
        }

        if http_digest_realm:
            group_data["http-digest-realm"] = http_digest_realm
        if sso_attribute_value:
            group_data["sso-attribute-value"] = sso_attribute_value
        if comments:
            group_data["comment"] = comments
        if members:
            group_data["member"] = [{"name": member} for member in members]

        api = fortigate_manager.get_device(device_id)
        result = api.create_user_group(group_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_user_group(device_id: str, group_name: str, vdom: str = "root") -> str:
    """
    Delete user group

    Args:
        device_id: Device ID
        group_name: Group name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of group deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_user_group(group_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === AUTHENTICATION SERVERS ===

@mcp.tool()
def fortigate_get_ldap_servers(device_id: str, vdom: str = "root") -> str:
    """
    Get all LDAP authentication servers

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of LDAP servers
    """
    try:
        api = fortigate_manager.get_device(device_id)
        servers = api.get_auth_servers(vdom)
        return json.dumps(servers, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_ldap_server(device_id: str, name: str, server: str,
                                dn: str,
                                cnid: str = "cn",
                                type: str = "simple",
                                username: Optional[str] = None,
                                password: Optional[str] = None,
                                port: int = 389,
                                secure: str = "disable",
                                comments: Optional[str] = None,
                                vdom: str = "root") -> str:
    """
    Create LDAP authentication server

    Args:
        device_id: Device ID
        name: Server name
        server: LDAP server IP/hostname
        cnid: Common name identifier
        dn: Distinguished name
        type: Authentication type (simple, anonymous, regular)
        username: Bind username (optional)
        password: Bind password (optional)
        port: LDAP port (default: 389)
        secure: Secure connection (enable, disable)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of server creation
    """
    try:
        server_data = {
            "name": name,
            "server": server,
            "cnid": cnid,
            "dn": dn,
            "type": type,
            "port": port,
            "secure": secure
        }

        if username:
            server_data["username"] = username
        if password:
            server_data["password"] = password
        if comments:
            server_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_ldap_server(server_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_ldap_server(device_id: str, server_name: str, vdom: str = "root") -> str:
    """
    Delete LDAP authentication server

    Args:
        device_id: Device ID
        server_name: Server name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of server deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_ldap_server(server_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_radius_servers(device_id: str, vdom: str = "root") -> str:
    """
    Get all RADIUS authentication servers

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of RADIUS servers
    """
    try:
        api = fortigate_manager.get_device(device_id)
        servers = api.get_radius_servers(vdom)
        return json.dumps(servers, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_radius_server(device_id: str, name: str, server: str,
                                  secret: str,
                                  auth_type: str = "auto",
                                  port: int = 1812,
                                  timeout: int = 5,
                                  all_usergroup: str = "disable",
                                  use_management_vdom: str = "disable",
                                  nas_ip: Optional[str] = None,
                                  comments: Optional[str] = None,
                                  vdom: str = "root") -> str:
    """
    Create RADIUS authentication server

    Args:
        device_id: Device ID
        name: Server name
        server: RADIUS server IP/hostname
        secret: Shared secret
        auth_type: Authentication type (auto, ms_chap_v2, ms_chap, chap, pap)
        port: RADIUS port (default: 1812)
        timeout: Timeout in seconds (default: 5)
        all_usergroup: Include all user groups (enable, disable)
        use_management_vdom: Use management VDOM (enable, disable)
        nas_ip: NAS IP address (optional)
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of server creation
    """
    try:
        server_data = {
            "name": name,
            "server": server,
            "secret": secret,
            "auth-type": auth_type,
            "port": port,
            "timeout": timeout,
            "all-usergroup": all_usergroup,
            "use-management-vdom": use_management_vdom
        }

        if nas_ip:
            server_data["nas-ip"] = nas_ip
        if comments:
            server_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_radius_server(server_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_radius_server(device_id: str, server_name: str, vdom: str = "root") -> str:
    """
    Delete RADIUS authentication server

    Args:
        device_id: Device ID
        server_name: Server name to delete
        vdom: Target VDOM (default: root)

    Returns:
        Result of server deletion
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_radius_server(server_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"