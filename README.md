# Anisette Server List

A personal list of Anisette servers for SideStore.

## Server List

The server list is hosted on GitHub Pages:

**https://stjl.github.io/anisette-ss/servers.json**

## About

This repository contains a manually maintained list of Anisette servers, including personal and third-party servers.

The list is provided in JSON format and can be used as a server source for compatible applications.

## Disclaimer

- This is a personal project and is not affiliated with or endorsed by SideStore.
- Third-party servers are operated independently by their respective owners.
- Server availability and reliability are not guaranteed.
- Use third-party servers at your own discretion.

<!-- SERVER_STATUS_START -->
## Server Status

| Server | Address | Status | Details |
|---|---|---|---|
| STJL's Server | https://anisette-v3-server-ypjk.onrender.com | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SideStore | https://ani.sidestore.io | UNKNOWN | ERROR: TimeoutError: The read operation timed out |
| SideStore (.app) | https://ani.sidestore.app | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SideStore (.zip) | https://ani.sidestore.zip | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SideStore (.xyz) | https://ani.846969.xyz | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SideStore (New) | https://new.ani.sidestore.io | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| jkcoxson | https://mac-ani.jkcoxson.com | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| jkcoxson (Windows ADI) | https://ani.jkcoxson.com | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SideStore (Windows ADI) | https://win.ani.sidestore.io | DEGRADED | HTTP ERROR 502 Bad Gateway |
| nythepegasus | https://ani.npeg.us | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| Macley | http://5.249.163.88:6969 | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| WE. Studio | https://anisette.wedotstud.io | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| SteX | https://ani.xu30.top | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| owoellen | https://ani.owoellen.rocks | OFFLINE | ERROR: URLError: TimeoutError: timed out |
| iDH Server | https://ani.idevicehacked.com | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| neoarz | https://ani.neoarz.com | OFFLINE | ERROR: URLError: TimeoutError: timed out |
| pythonplayer123 | https://ani3server.fly.dev | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| Jayden's Server | https://ani.jaydenha.uk | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| crystall1nedev's server | https://anisette.crystall1ne.dev | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| ethxn's omnisette server :3 | https://omni.ethxn.xyz | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| koremi | https://ani.sjwon0368.dpdns.org | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| uwucloud | https://ani.uwucloud.fun | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |
| Lill q | https://anisette.lillq.me | ONLINE | GET /v3/client_info: HTTP 200; client_info and user_agent present. Apple provisioning not tested. |

### Status Meanings

- **ONLINE**: V3 client information endpoint responded successfully with the required fields.
- **DEGRADED**: Server responded, but the API or response had an error.
- **OFFLINE**: Connection could not be established.
- **UNKNOWN**: Insufficient information, unsupported endpoint, access restriction, or inconclusive result.

### Health Check Limitations

- Checks run once a week, sequentially, with no retries.
- Each server receives at most one HTTP GET request.
- Only `/v3/client_info` is queried. The legacy `/` endpoint is intentionally not requested because it may generate one-time Anisette headers.
- `/v3/get_headers` and `/v3/provisioning_session` are never called.
- No Apple ID, credentials, cookies, or user sessions are used.
- No requests are sent to Apple.
- Apple authentication and provisioning are not tested.
- HTTP 401, 403, and 429 are not treated as proof that a server is offline.
- Rate limits and access restrictions are respected. No retries or bypass attempts are made.

**Important:** ONLINE does not guarantee successful SideStore authentication or Apple approval.

<!-- SERVER_STATUS_END -->
