"""To previous page redirection state for previous button logic"""
import reflex as rx
from typing import List

class BaseState(rx.State):
    """A base state that all other states inherit from."""
    previous_paths: List[str] = []

    def add_path(self):
        """Add the current path to the history."""
        current_path = self.router.url.path
        if not self.previous_paths or self.previous_paths[-1] != current_path:
            self.previous_paths.append(current_path)

    def go_back(self):
        """Navigate to the previous page and remove it from history."""
        if self.previous_paths:
            # Pop the current page
            self.previous_paths.pop()
            if self.previous_paths:
                # Get the previous page and navigate
                previous_path = self.previous_paths.pop()
                return rx.redirect(previous_path)
        # Fallback to homepage if no history
        return rx.redirect("/")