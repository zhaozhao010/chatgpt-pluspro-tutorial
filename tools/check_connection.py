#!/usr/bin/env python3
"""Check HTTP reachability without credentials or third-party packages."""

import argparse
import math
import time
import urllib.error
import urllib.parse
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public HTTP(S) URL to check")
    parser.add_argument("--timeout", type=float, default=10, help="Seconds (default: 10)")
    args = parser.parse_args()
    try:
        target = urllib.parse.urlsplit(args.url)
        target.port  # Validate explicit ports before sending the request.
    except ValueError:
        parser.error("Invalid URL or port")
    if target.scheme not in ("http", "https") or not target.hostname:
        parser.error("An absolute HTTP(S) URL is required")
    if target.username is not None or target.password is not None or target.query or target.fragment:
        parser.error("Use a public URL without credentials, query parameters or fragments")
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("Timeout must be a finite positive number")

    request = urllib.request.Request(args.url, headers={"User-Agent": "ConnectionCheck/1.0"})
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        status = error.code
        error.close()
    except (urllib.error.URLError, OSError, ValueError) as error:
        # Do not print exception messages that may contain proxy credentials.
        reason = getattr(error, "reason", error)
        print("Network request failed:", type(reason).__name__)
        return 1

    print(f"HTTP {status}; response headers received in {time.monotonic() - started:.2f}s")
    if status >= 400:
        print("An HTTP server responded, but rejected or could not serve the request.")
        return 1
    print("HTTP request succeeded. Account, payment and authenticated API access are untested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
