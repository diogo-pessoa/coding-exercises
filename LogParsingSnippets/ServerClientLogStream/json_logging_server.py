import socket
import time
from pathlib import Path

HOST = "127.0.0.1"
PORT = 9090
INTERVAL_S = 1
N = 20  # limit the num of messages

def main():
    """
    Server: accepts one client and streams JSONL lines over TCP.
    """
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"Server Listening on {HOST}:{PORT}", flush=True)

    conn, addr = srv.accept()
    print(f"P1 connection established from {addr}", flush=True)

    data_path = Path(__file__).resolve().parent / "data" / "Apache_2k.jsonl"

    with conn, conn.makefile("w", buffering=1) as out, data_path.open("r", encoding="utf-8") as json_file:
        for i, line in enumerate(json_file):
            if i >= N:
                break

            payload = line.strip()
            if not payload:
                continue

            # Send the JSON object exactly as it exists in the JSONL file
            print(f"P1 writing line {i}", flush=True)
            out.write(payload + "\n")
            time.sleep(INTERVAL_S)

    print("P1 finished", flush=True)

if __name__ == "__main__":
    main()
