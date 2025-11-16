"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from vue.pages.homepage import *
from vue.pages.history_page import *


class State(rx.State):
    """The app state."""


app = rx.App()

