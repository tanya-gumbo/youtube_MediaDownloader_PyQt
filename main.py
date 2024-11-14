import asyncio
import sys
import threading

from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop
import uvicorn
from User_Interface.Backend.fastapi_endpoints import app, start_fastapi
from User_Interface.Frontend.MainApplication.main_window import MainWindow

async def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    # Start the FastAPI server in a separate thread
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()

    main_window = MainWindow()
    main_window.show()

    with loop:
        sys.exit(loop.run_forever()) # Runs the event loop

if __name__ == "__main__":
    asyncio.run(main())