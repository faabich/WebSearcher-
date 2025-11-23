"""History page state."""
import reflex as rx
import time
from typing import List, Dict, Any
from pydantic import BaseModel

class HistoryEntry(BaseModel):
    """A single history entry."""
    id: str
    query: str
    timestamp: float
    searchEngine: str
    parameters: Dict[str, Any]

# Dummy data for now, similar to what the TSX example would have in localStorage
initial_history = [
    HistoryEntry(
        id="1",
        query="reflex web framework",
        timestamp=time.time(),
        searchEngine="Google",
        parameters={"fileType": "pdf", "site": "reflex.dev"}
    ),
    HistoryEntry(
        id="2",
        query="python web ui",
        timestamp=time.time() - 86400, # 1 day ago
        searchEngine="DuckDuckGo",
        parameters={}
    ),
]

class HistoryState(rx.State):
    """The state for the history page."""
    history: List[HistoryEntry] = initial_history

    def clear_history(self):
        """Clear the search history."""
        self.history = []
        # In a real app, you'd also clear this from localStorage or a database
        return rx.toast.success("History cleared")

    def delete_entry(self, entry_id: str):
        """Delete a single history entry."""
        self.history = [entry for entry in self.history if entry.id != entry_id]
        return rx.toast.success("Entry deleted")

    def copy_query(self, query: str):
        """Copy the search query to the clipboard."""
        return [rx.set_clipboard(query), rx.toast.success("Query copied!")]
