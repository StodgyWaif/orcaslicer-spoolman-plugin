# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests>=2.28.0",
# ]
# [project]
# name = "spoolman-api"
# version = "0.1.0"
# /// 

import json
import requests

class SpoolManClient:
    def __init__(self, settings):
        self.settings = settings
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _build_base_url(self):
        base_url = self.settings.get("spoolman_url", "").strip().rstrip("/")
        if not base_url:
            raise ValueError("SpoolMan URL is not configured")
        return base_url

    def _auth_headers(self):
        mode = self.settings.get("auth_mode", "none")
        headers = {}

        if mode == "api_key":
            api_key = self.settings.get("api_key", "").strip()
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"

        elif mode == "basic":
            username = self.settings.get("username", "").strip()
            password = self.settings.get("password", "").strip()
            if username and password:
                self.session.auth = (username, password)

        return headers

    def _request_json(self, url):
        headers = self._auth_headers()
        if headers:
            self.session.headers.update(headers)

        response = self.session.get(url, timeout=self.settings.get("timeout_seconds", 10))
        response.raise_for_status()

        response_text = response.text.strip()
        if not response_text:
            return []

        try:
            return response.json()
        except ValueError:
            try:
                return json.loads(response_text)
            except ValueError:
                raise ValueError("SpoolMan response is not valid JSON")

    def fetch_filaments(self):
        base_url = self._build_base_url()
        endpoints = self.settings.get("selected_endpoints", [
            "/api/v1/filaments",
            "/api/v1/spools",
            "/api/filaments",
            "/api/spools"
        ])

        last_error = None

        for endpoint in endpoints:
            url = base_url + endpoint
            try:
                data = self._request_json(url)
                items = self._normalize_filaments(data)
                if items:
                    return items
            except Exception as exc:
                last_error = exc
                continue

        if last_error:
            raise last_error

        return []

    def _normalize_filaments(self, payload):
        if isinstance(payload, list):
            records = payload
        elif isinstance(payload, dict):
            if "filaments" in payload:
                records = payload["filaments"]
            elif "data" in payload:
                records = payload["data"]
            elif "spools" in payload:
                records = payload["spools"]
            else:
                records = [payload]
        else:
            return []

        normalized = []
        for item in records:
            if not isinstance(item, dict):
                continue

            record = {
                "spool_id": item.get("spool_id") or item.get("id") or item.get("spoolId") or item.get("name"),
                "brand": item.get("brand") or item.get("manufacturer") or item.get("vendor") or "Unknown",
                "type": item.get("type") or item.get("material") or item.get("material_type") or item.get("filament_type") or "Unknown",
                "material": item.get("material") or item.get("filament_type") or item.get("type") or "Unknown",
                "color": item.get("color") or item.get("colour") or item.get("filament_color") or "Unknown",
                "weight": item.get("weight") or item.get("remaining_weight") or item.get("spool_weight"),
                "remaining_weight": item.get("remaining_weight") or item.get("weight") or item.get("spool_weight"),
                "diameter": item.get("diameter") or item.get("filament_diameter"),
                "density": item.get("density") or item.get("filament_density"),
                "nozzle_temp": item.get("nozzle_temp") or item.get("nozzle_temperature"),
                "bed_temp": item.get("bed_temp") or item.get("bed_temperature"),
                "price": item.get("price"),
                "notes": item.get("notes") or item.get("comment") or "",
                "raw": item
            }

            record["raw"] = item
            normalized.append(record)
        return normalized
