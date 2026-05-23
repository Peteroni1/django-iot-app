import json
import time
import random
import websocket

# For local deployment testing environment
WS_URL = "ws://127.0.0.1:8000/ws/sensor/"

# Swap to this once you go live on Render:
# WS_URL = "wss://your-app-name.onrender.com/ws/sensor/"

def run_simulator():
    print(f"Targeting server socket at: {WS_URL}")
    try:
        ws = websocket.create_connection(WS_URL)
        print("Telemetry pipe linked up securely! Dispatching streams...\n")

        while True:
            # Simulate slight ambient changes
            simulated_temp = round(random.uniform(23.5, 29.8), 1)
            simulated_hum = round(random.uniform(60.0, 80.0), 1)

            payload = {
                "temperature": simulated_temp,
                "humidity": simulated_hum
            }

            ws.send(json.dumps(payload))
            print(f"[MOCK_ESP32] Sent Data -> Temp: {simulated_temp}°C | Humidity: {simulated_hum}%")
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nSimulator closed down safely.")
        if 'ws' in locals():
            ws.close()
    except Exception as e:
        print(f"\nPipe breakdown encountered: {e}")
        print("Attempting to re-establish connection in 5 seconds...")
        time.sleep(5)
        run_simulator()

if __name__ == "__main__":
    run_simulator()