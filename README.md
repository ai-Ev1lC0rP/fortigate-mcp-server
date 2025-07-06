# README.md
# Fortigate MCP Server

An MCP (Model Context Protocol) server for managing Fortigate devices using FastMCP.

## Features

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
- ✅ Address objects (IP, range, FQDN)
- ✅ Service objects (TCP / UDP)
- ✅ VIP objects management
- 🔄 Complete CRUD operations (partially implemented)

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
- ✅ IPSec Phase 1 interfaces (create, delete, list)
- ✅ IPSec Phase 2 interfaces (create, delete, list)
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
- ✅ Static routes
- ✅ Routing table
- ✅ Policy routing
- ✅ Interface list

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
cp config.yaml.example config.yaml
```

4. **Start server**
```bash
uv run python server.py
```