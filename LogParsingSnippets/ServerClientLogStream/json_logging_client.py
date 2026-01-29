import json
import socket

SRV_HOST = "127.0.0.1"
SRV_PORT = 9090

# If None, prints all
FILTER_LEVEL = "notice"

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SRV_HOST, SRV_PORT))
    print(f"P2 connected to {SRV_HOST}:{SRV_PORT}", flush=True)

    # sock.makefile wraps a socket into a file-like object for line-by-line reads
    with sock, sock.makefile("r") as file:
        for event in file:
            payload = event.strip()
            if not payload:
                continue

            try:
                json_event = json.loads(payload)
            except json.JSONDecodeError:
                continue

            if FILTER_LEVEL is not None:
                # Only filter if the field exists; otherwise let it pass
                level = json_event.get("level")
                if level is not None and level != FILTER_LEVEL:
                    continue

            print(f"P2 getting {json_event}", flush=True)

if __name__ == "__main__":
    main()
