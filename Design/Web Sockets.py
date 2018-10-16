# REF
# https://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# Use following html in browser to talk to the service
"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>WebSocket demo</title>
        </head>
        <body>
            <script>
                var ws = new WebSocket("ws://127.0.0.1:5678/"),
                    messages = document.createElement('ul');
                ws.onmessage = function (event) {
                    var messages = document.getElementsByTagName('ul')[0],
                        message = document.createElement('li'),
                        content = document.createTextNode(event.data);
                    message.appendChild(content);
                    messages.appendChild(message);
                };
                document.body.appendChild(messages);
            </script>
        </body>
    </html>
"""