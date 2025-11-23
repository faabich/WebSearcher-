"""Homepage state."""
import reflex as rx
import time
from typing import List, Dict, Any

class SearchTerm(rx.Base):
    """A single search term."""
    id: str
    value: str
    type: str  # "normal" or "exact"

class HomeState(rx.State):
    """The state for the homepage."""
    search_engine: str = "google"
    search_terms: List[SearchTerm] = [SearchTerm(id="1", value="", type="normal")]
    file_type: str = ""
    custom_file_type: str = ""
    site: str = ""
    in_title: str = ""
    in_url: str = ""
    in_text: str = ""
    exclude_words: str = ""
    include_words: str = ""
    operator: str = "AND"
    # ... other fields from App.tsx ...

    search_engines: Dict[str, Dict[str, str]] = {
        "google": {"name": "Google", "url": "https://www.google.com/search?q="},
        "duckduckgo": {"name": "DuckDuckGo", "url": "https://duckduckgo.com/?q="},
        "bing": {"name": "Bing", "url": "https://www.bing.com/search?q="},
        # ... other search engines ...
    }

    @rx.var
    def generated_query(self) -> str:
        """The generated search query."""
        query_parts = []
        # Build search terms
        terms = [
            f'"{term.value}"' if term.type == "exact" else term.value
            for term in self.search_terms if term.value.strip()
        ]
        if terms:
            query_parts.append(f" {self.operator} ".join(terms))

        # Build other filters
        if self.file_type:
            ft = self.custom_file_type if self.file_type == "autre" else self.file_type
            if ft:
                query_parts.append(f"filetype:{ft}")
        if self.site:
            query_parts.append(f"site:{self.site}")
        if self.in_title:
            query_parts.append(f"intitle:{self.in_title}")
        # ... other filters ...

        return " ".join(query_parts)

    def add_search_term(self):
        """Add a new search term."""
        self.search_terms.append(SearchTerm(id=str(time.time()), value="", type="normal"))

    def remove_search_term(self, term_id: str):
        """Remove a search term."""
        if len(self.search_terms) > 1:
            self.search_terms = [term for term in self.search_terms if term.id != term_id]

    def update_search_term_value(self, term_id: str, value: str):
        """Update the value of a search term."""
        for i, term in enumerate(self.search_terms):
            if term.id == term_id:
                self.search_terms[i].value = value
                break

    def toggle_search_term_type(self, term_id: str):
        """Toggle the type of a search term."""
        for i, term in enumerate(self.search_terms):
            if term.id == term_id:
                self.search_terms[i].type = "normal" if term.type == "exact" else "exact"
                break

    def search(self):
        """Perform the search."""
        if not self.generated_query:
            return rx.toast.error("Please enter at least one search term")
        
        # In a real app, you would save to history here
        
        url = self.search_engines[self.search_engine]["url"] + self.generated_query
        return rx.redirect(url, external=True)

    def reset(self):
        """Reset the form."""
        self.search_terms = [SearchTerm(id="1", value="", type="normal")]
        self.file_type = ""
        self.custom_file_type = ""
        self.site = ""
        self.in_title = ""
        self.in_url = ""
        self.in_text = ""
        self.exclude_words = ""
        self.include_words = ""
        self.operator = "AND"
        # ... reset other fields ...
