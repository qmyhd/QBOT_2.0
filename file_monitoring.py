# Import necessary modules
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import data_ingestion  # Import the data_ingestion script to update data

# Watcher class to monitor changes in a directory
class Watcher:

    # Define the directory you want to watch
    DIRECTORY_TO_WATCH = r"C:\Users\qaism\OneDrive - University of Virginia\Documents\GPT INFOBASE\QBOT_Jobs"

    # Initialize Watcher
    def __init__(self):
        self.observer = Observer()

    # Run the Watcher
    def run(self):
        # Instantiate the Handler class to handle events
        event_handler = Handler()
        
        # Schedule the observer to watch the directory
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        
        # Start the observer
        self.observer.start()

        # Keep running
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:  # Stop when KeyboardInterrupt occurs (Ctrl+C)
            self.observer.stop()
            print("Observer stopped")
        
        # Wait until the observer thread terminates
        self.observer.join()

# Handler class to handle file modification and creation events
class Handler(FileSystemEventHandler):

    # Method to process events
    def process(self, event):
        """
        Event handler that will be invoked when a file is modified or created.
        """
        print(f"Event occurred: {event.event_type} at {event.src_path}")
        
        # Update the data using the data_ingestion script
        data_ingestion.ingest_data_from_directory(Watcher.DIRECTORY_TO_WATCH)

    # When a file is modified, process the event
    def on_modified(self, event):
        self.process(event)

    # When a file is created, process the event
    def on_created(self, event):
        self.process(event)

# Entry point for the script
if __name__ == '__main__':
    w = Watcher()  # Instantiate the Watcher
    w.run()  # Run the Watcher