import yaml
import sys
import os
from pathlib import Path

from mcptool import fortigate_manager, mcp

# Fix the import path
sys.path.append(str(Path(__file__).parent))



def load_config(config_file="config.yaml"):
        """Load configuration from YAML file or environment variables"""
        devices = {}

        config_path = Path(config_file)
        if config_path.exists():
                try:
                        with open(config_path, 'r') as f:
                                file_config = yaml.safe_load(f) or {}
                                devices.update(file_config.get('devices', {}))
                except yaml.YAMLError as e:
                        print(f"❌ Error parsing config file: {e}")
        else:
                print(f"⚠️  Config file {config_file} not found")

        env_config = os.environ.get("FORTIGATE_CONFIG")
        if env_config:
                try:
                        env_data = yaml.safe_load(env_config) or {}
                        devices.update(env_data.get('devices', {}))
                except yaml.YAMLError as e:
                        print(f"❌ Error parsing FORTIGATE_CONFIG: {e}")

        device_id = os.environ.get("FORTIGATE_DEVICE_ID")
        host = os.environ.get("FORTIGATE_HOST")
        token = os.environ.get("FORTIGATE_TOKEN")
        if device_id and host and token:
                vdoms = os.environ.get("FORTIGATE_VDOMS", "root")
                description = os.environ.get("FORTIGATE_DESCRIPTION", host)
                devices[device_id] = {
                        "host": host,
                        "token": token,
                        "vdoms": [v.strip() for v in vdoms.split(',') if v.strip()],
                        "description": description,
                }

        if not devices:
                print("Starting with empty configuration - use fortigate_add_device to add devices")
                return

        devices_loaded = 0
        for device_id, device_config in devices.items():
                try:
                        fortigate_manager.add_device(
                                device_id=device_id,
                                host=device_config['host'],
                                token=device_config['token'],
                                vdoms=device_config.get('vdoms', ['root'])
                        )
                        print(f"✅ Loaded device: {device_id} - {device_config.get('description', device_config['host'])}")
                        devices_loaded += 1
                except Exception as e:
                        print(f"❌ Error loading device {device_id}: {e}")

        print(f"📡 Loaded {devices_loaded} devices successfully")


def main():
	print("🚀 Starting Fortigate MCP Server with FastMCP...")
	print("=" * 50)

	load_config()

	print("=" * 50)
	print("🔧 Available tools:")
	print("  - Device Management: add_device, list_devices, get_system_status")
	print("  - Firewall Policies: get, create, update, delete, search, validate, statistics")
	print("  - Security Profiles: AV, Web Filter, IPS, SSL/SSH, DNS Filter profiles")
	print("  - User Management: local users, groups, LDAP/RADIUS servers")
	print("  - VPN Management: IPSec tunnels, SSL VPN portals, certificates")
	print("  - System Admin: backup/restore, logs, performance, reboot/shutdown")
	print("  - Advanced Features: HA, SD-WAN, FortiView, threat dashboard")
	print("  - Network Objects: address/service objects, VIPs")
	print("  - Routing: static routes, routing tables, interfaces")
	print("=" * 50)
	print("📡 Server ready - connect your MCP client!")

	# Start server
	mcp.settings.host = '0.0.0.0'
	mcp.settings.port = 8456
	mcp.run(transport="streamable-http")

if __name__ == "__main__":
	main()




