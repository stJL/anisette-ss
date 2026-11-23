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

_Last checked: 2026-11-23 21:06:06 UTC_

| Server | Address | Status | Details |
|---|---|---|---|
| STJL's Server | https://anisette-v3-server-ypjk.onrender.com | OFFLINE | Connection/read timeout (TimeoutError): The read operation timed out |
| SideStore | https://ani.sidestore.io | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SideStore (.app) | https://ani.sidestore.app | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SideStore (.zip) | https://ani.sidestore.zip | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SideStore (.xyz) | https://ani.846969.xyz | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SideStore (New) | https://new.ani.sidestore.io | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| jkcoxson | https://mac-ani.jkcoxson.com | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| jkcoxson (Windows ADI) | https://ani.jkcoxson.com | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SideStore (Windows ADI) | https://win.ani.sidestore.io | OFFLINE | HTTP 502 Bad Gateway; Content-Type: missing; response: (empty response body) |
| nythepegasus | https://ani.npeg.us | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| Macley | http://5.249.163.88:6969 | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| WE. Studio | https://anisette.wedotstud.io | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| SteX | https://ani.xu30.top | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| owoellen | https://ani.owoellen.rocks | OFFLINE | Connection/read timeout (URLError-&gt;TimeoutError): timed out |
| iDH Server | https://ani.idevicehacked.com | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| neoarz | https://ani.neoarz.com | OFFLINE | Connection/read timeout (URLError-&gt;TimeoutError): timed out |
| pythonplayer123 | https://ani3server.fly.dev | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| Jayden's Server | https://ani.jaydenha.uk | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| crystall1nedev's server | https://anisette.crystall1ne.dev | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| ethxn's omnisette server :3 | https://omni.ethxn.xyz | UNKNOWN | GET /v3/client_info: HTTP 200 OK; Content-Type: text/plain; charset=utf-8; unexpected Content-Type (expected JSON); response: {"client_info":"&lt;MacBookPro13,2&gt; &lt;macOS;13.1;22C65&gt; &lt;com.apple.AuthKit/1 (com.apple.dt.Xcode/3594.4.19)&gt;","user_agent":"akd/1.0 CFNetwork/808.1.4"} |
| koremi | https://ani.sjwon0368.dpdns.org | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| uwucloud | https://ani.uwucloud.fun | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |
| Lill q | https://anisette.lillq.me | ONLINE | GET /v3/client_info: HTTP 200; valid JSON with required fields. Apple provisioning not tested. |

### Status Meanings

- **ONLINE**: `/v3/client_info` returned HTTP 200 with a valid JSON object containing non-empty `client_info` and `user_agent` strings and no error indicators.
- **OFFLINE**: Clear evidence that the service is unavailable (HTTP 5xx, proxy/5xx error page, DNS failure, connection refused/reset/aborted, remote disconnect, or timeout).
- **UNKNOWN**: Server health could not be confirmed (HTTP 3xx redirect, 401/403/429 access or rate limits, 4xx/other non-200 status, TLS/SSL error, empty/invalid/truncated response, JSON error or schema mismatch, or unexpected runtime error).

### Health Check Limitations

- Checks run once a week and are performed sequentially.
- Each server receives at most one HTTP GET request per run. Redirects are not followed; no retries or IP changes are performed.
- Only `/v3/client_info` is queried. The legacy `/` endpoint is intentionally not requested because it may generate one-time Anisette headers.
- `/v3/get_headers` and `/v3/provisioning_session` are never called.
- No Apple ID, credentials, cookies, or user sessions are used.
- No requests are sent to Apple. Apple authentication and provisioning are not tested.
- HTTP status codes, Content-Type, redirect locations, and available response bodies (capped at 8 KB with explicit truncation notice) are recorded. Sensitive values such as credentials, cookies, tokens, and private keys are redacted.
- HTTP 401, 403, and 429 are reported as UNKNOWN rather than proof that a server is offline. Access restrictions and rate limits are respected.

**Important:** ONLINE means only that the `/v3/client_info` fail-closed check passed. It does not mean Apple has approved the server or guarantee successful SideStore authentication.

<!-- SERVER_STATUS_END -->
