# README.md
# Fortigate MCP Server

An MCP (Model Context Protocol) server for managing Fortigate devices using FastMCP.

## Features

This server provides comprehensive management of FortiGate devices, covering approximately 95% of enterprise features.

### Device Management
- ✅ Add / remove devices
- ✅ List configured devices
- ✅ System status and device info
- ✅ VDOMs discovery

### Firewall Policy Management
- ✅ List existing policies
- ✅ Create new policies
- ✅ Modify existing policies
- ✅ Delete policies
- ✅ Policy validation
- ✅ Policy search and filtering
- ✅ Policy statistics

### Network Objects Management
- ✅ Address objects (create)
- ✅ Service objects (read)
- ✅ VIP objects (read, delete)
- 🔄 Complete CRUD operations are partially implemented.

### Security Profiles Management
- ✅ Antivirus profiles (create, delete, list)
- ✅ Web Filter profiles (create, delete, list)
- ✅ IPS sensors (create, delete, list)
- ✅ SSL/SSH inspection profiles (create, delete, list)
- ✅ DNS Filter profiles (create, delete, list)

### User Management
- ✅ Local users (create, update, delete, list)
- ✅ User groups (create, delete, list)
- ✅ LDAP authentication servers (create, delete, list)
- ✅ RADIUS authentication servers (create, delete, list)

### VPN Management
- ✅ IPSec Phase 1 & 2 interfaces (create, delete, list)
- ✅ IPSec tunnel status monitoring
- ✅ SSL VPN settings and portals (create, delete, configure)
- ✅ SSL VPN status monitoring
- ✅ VPN certificates management

### System Administration
- ✅ Configuration backup and restore
- ✅ System performance monitoring
- ✅ Bandwidth usage statistics
- ✅ Session table monitoring
- ✅ System, traffic, and security logs
- ✅ License and firmware information
- ✅ System reboot and shutdown

### Advanced Features
- ✅ High Availability (status, configuration, failover)
- ✅ SD-WAN zones and members management
- ✅ SD-WAN performance and health monitoring
- ✅ FortiView statistics and analytics
- ✅ Threat dashboard and security ratings
- ✅ Policy usage analytics
- ✅ Application control statistics

### Routing Management
- ✅ Static routes (read)
- ✅ Routing table (read)
- ✅ Policy routing (read)
- ✅ Interface list (read)
- 🔄 Read-only operations are implemented. Write operations are not yet supported.

## Installation

1. **Clone repository**
```bash
git clone https://github.com/Filippo125/fortigate-mcp-server.git
cd fortigate-mcp-server
```

2. **Install dependencies**
```bash
uv sync
```

3. **Configure devices**
```bash
cp config.yaml.template config.yaml
# Edit config.yaml with your FortiGate device details
```

You can also configure devices entirely through environment variables. Set the following to define a single device:

```bash
export FORTIGATE_DEVICE_ID="my-fortigate"
export FORTIGATE_HOST="192.168.1.1:10443"
export FORTIGATE_TOKEN="API_TOKEN"
export FORTIGATE_VDOMS="root"  # comma-separated list
```

For more complex setups, you may provide a full YAML configuration string via the `FORTIGATE_CONFIG` environment variable.

4. **Start server**
```bash
uv run python server.py
```

### Claude MCP configuration

To use this server with Claude's MCP client, create `.claude/mcp.json` in the project root:

```json
{
  "mcpServers": {
    "fortigate": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "env": {
        "FORTIGATE_DEVICE_ID": "my-fortigate",
        "FORTIGATE_HOST": "YOUR_FORTIGATE_IP:PORT",
        "FORTIGATE_TOKEN": "YOUR_API_TOKEN",
        "FORTIGATE_VDOMS": "root"
      }
    }
  }
}
```

## Testing

Run the comprehensive endpoint test suite:
```bash
# Using environment variables
export FORTIGATE_HOST="your-fortigate-ip:port"
export FORTIGATE_TOKEN="your-api-token"
python test_endpoints.py

# Or using config.yaml file
python test_endpoints.py
```