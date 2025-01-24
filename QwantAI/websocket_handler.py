import websocket
import json
import time


def connect_to_websocket(token_detailed, session, callback=None, debug=False):
    """
    Connect to Qwant WebSocket and process the results.

    Args:
        token_detailed (str): The token for WebSocket communication.
        session (requests.Session): The session with cookies.
        callback (function, optional): A function to handle streamed data. If None, prints data directly.
    """
    if not token_detailed:
        print("Qwant doesn't have any response for this query.")
        return

    websocket_url = "wss://api.qwant.com/v3/socket.io/?EIO=4&transport=websocket"

    ws = websocket.create_connection(
        websocket_url,
        cookie="; ".join([f"{name}={value}" for name, value in session.cookies.get_dict().items()]),
        timeout=3000
    )

    ws.send("40")
    ws.send(f'42["answer",{{"token":"{token_detailed}"}}]')
    if debug:
        print("WebSocket connection established. Waiting for messages...")
    while True:
        try:
            message = ws.recv()

            if message == "2":
                ws.send("3")  
                continue

            if message.startswith('42["answer",'):
                try:
                    payload = json.loads(message[2:])
                    if payload[0] == "answer" and isinstance(payload[1], dict):
                        data = payload[1]
                        if data.get("type") == "delta":
                            delta = data.get("delta", "")
                            if delta:  # Only process if there is data to output
                                if callback:
                                    callback(delta)
                                else:
                                    print(delta, end="", flush=True)
                        elif data.get("type") == "end":
                            print("\n")
                            break
                except json.JSONDecodeError:
                    if debug:
                        print("Error decoding JSON from message:", message)
        except websocket.WebSocketConnectionClosedException:
            if debug:
                print("WebSocket connection closed. Reconnecting...")
            time.sleep(1)
            connect_to_websocket(token_detailed, session, callback=callback, debug=debug)
            break
        except Exception as e:
            if debug:
                print(f"Unexpected error: {e}")
            break

    ws.close()
