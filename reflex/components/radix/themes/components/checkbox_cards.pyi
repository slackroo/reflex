"""Stub file for reflex/components/radix/themes/components/checkbox_cards.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from types import SimpleNamespace
from typing import Any, Literal, Optional, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent

class CheckboxCardsRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Breakpoints[str, Literal["1", "2", "3"]]
        | Literal["1", "2", "3"]
        | Var[Breakpoints[str, Literal["1", "2", "3"]] | Literal["1", "2", "3"]]
        | None = None,
        variant: Literal["classic", "surface"]
        | Var[Literal["classic", "surface"]]
        | None = None,
        color_scheme: Literal[
            "amber",
            "blue",
            "bronze",
            "brown",
            "crimson",
            "cyan",
            "gold",
            "grass",
            "gray",
            "green",
            "indigo",
            "iris",
            "jade",
            "lime",
            "mint",
            "orange",
            "pink",
            "plum",
            "purple",
            "red",
            "ruby",
            "sky",
            "teal",
            "tomato",
            "violet",
            "yellow",
        ]
        | Var[
            Literal[
                "amber",
                "blue",
                "bronze",
                "brown",
                "crimson",
                "cyan",
                "gold",
                "grass",
                "gray",
                "green",
                "indigo",
                "iris",
                "jade",
                "lime",
                "mint",
                "orange",
                "pink",
                "plum",
                "purple",
                "red",
                "ruby",
                "sky",
                "teal",
                "tomato",
                "violet",
                "yellow",
            ]
        ]
        | None = None,
        high_contrast: Var[bool] | bool | None = None,
        columns: Breakpoints[
            str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"] | str
        ]
        | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        | Var[
            Breakpoints[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"] | str]
            | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            | str
        ]
        | str
        | None = None,
        gap: Breakpoints[
            str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"] | str
        ]
        | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        | Var[
            Breakpoints[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"] | str]
            | Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            | str
        ]
        | str
        | None = None,
        style: Style | None = None,
        key: Any | None = None,
        id: Any | None = None,
        class_name: Any | None = None,
        autofocus: bool | None = None,
        custom_attrs: dict[str, Var | Any] | None = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "CheckboxCardsRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: The size of the checkbox cards: "1" | "2" | "3"
            variant: Variant of button: "classic" | "surface" | "soft"
            color_scheme: Override theme color for button
            high_contrast: Uses a higher contrast color for the component.
            columns: The number of columns:
            gap: The gap between the checkbox cards:
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class CheckboxCardsItem(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Style | None = None,
        key: Any | None = None,
        id: Any | None = None,
        class_name: Any | None = None,
        autofocus: bool | None = None,
        custom_attrs: dict[str, Var | Any] | None = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "CheckboxCardsItem":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class CheckboxCards(SimpleNamespace):
    root = staticmethod(CheckboxCardsRoot.create)
    item = staticmethod(CheckboxCardsItem.create)

checkbox_cards = CheckboxCards()
