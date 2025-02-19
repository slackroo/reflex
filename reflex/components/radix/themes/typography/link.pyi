"""Stub file for reflex/components/radix/themes/typography/link.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.component import MemoizationLeaf
from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el.elements.inline import A
from reflex.components.markdown.markdown import MarkdownComponentMap
from reflex.components.next.link import NextLink
from reflex.event import EventType
from reflex.style import Style
from reflex.utils.imports import ImportDict
from reflex.vars.base import Var

from ..base import RadixThemesComponent

LiteralLinkUnderline = Literal["auto", "hover", "always", "none"]
next_link = NextLink.create()

class Link(RadixThemesComponent, A, MemoizationLeaf, MarkdownComponentMap):
    def add_imports(self) -> ImportDict: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        ],
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        weight: Optional[
            Union[
                Breakpoints[str, Literal["bold", "light", "medium", "regular"]],
                Literal["bold", "light", "medium", "regular"],
                Var[
                    Union[
                        Breakpoints[str, Literal["bold", "light", "medium", "regular"]],
                        Literal["bold", "light", "medium", "regular"],
                    ]
                ],
            ]
        ] = None,
        trim: Optional[
            Union[
                Breakpoints[str, Literal["both", "end", "normal", "start"]],
                Literal["both", "end", "normal", "start"],
                Var[
                    Union[
                        Breakpoints[str, Literal["both", "end", "normal", "start"]],
                        Literal["both", "end", "normal", "start"],
                    ]
                ],
            ]
        ] = None,
        underline: Optional[
            Union[
                Literal["always", "auto", "hover", "none"],
                Var[Literal["always", "auto", "hover", "none"]],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
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
                ],
                Var[
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
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[Var[bool], bool]] = None,
        is_external: Optional[Union[Var[bool], bool]] = None,
        download: Optional[Union[Var[Union[bool, str]], bool, str]] = None,
        href: Optional[Union[Var[str], str]] = None,
        href_lang: Optional[Union[Var[str], str]] = None,
        media: Optional[Union[Var[str], str]] = None,
        ping: Optional[Union[Var[str], str]] = None,
        referrer_policy: Optional[
            Union[
                Literal[
                    "",
                    "no-referrer",
                    "no-referrer-when-downgrade",
                    "origin",
                    "origin-when-cross-origin",
                    "same-origin",
                    "strict-origin",
                    "strict-origin-when-cross-origin",
                    "unsafe-url",
                ],
                Var[
                    Literal[
                        "",
                        "no-referrer",
                        "no-referrer-when-downgrade",
                        "origin",
                        "origin-when-cross-origin",
                        "same-origin",
                        "strict-origin",
                        "strict-origin-when-cross-origin",
                        "unsafe-url",
                    ]
                ],
            ]
        ] = None,
        rel: Optional[Union[Var[str], str]] = None,
        target: Optional[
            Union[
                Literal["_blank", "_parent", "_self", "_top"],
                Var[Union[Literal["_blank", "_parent", "_self", "_top"], str]],
                str,
            ]
        ] = None,
        access_key: Optional[Union[Var[str], str]] = None,
        auto_capitalize: Optional[
            Union[
                Literal["characters", "none", "off", "on", "sentences", "words"],
                Var[Literal["characters", "none", "off", "on", "sentences", "words"]],
            ]
        ] = None,
        content_editable: Optional[
            Union[
                Literal["inherit", "plaintext-only", False, True],
                Var[Literal["inherit", "plaintext-only", False, True]],
            ]
        ] = None,
        context_menu: Optional[Union[Var[str], str]] = None,
        dir: Optional[Union[Var[str], str]] = None,
        draggable: Optional[Union[Var[bool], bool]] = None,
        enter_key_hint: Optional[
            Union[
                Literal["done", "enter", "go", "next", "previous", "search", "send"],
                Var[
                    Literal["done", "enter", "go", "next", "previous", "search", "send"]
                ],
            ]
        ] = None,
        hidden: Optional[Union[Var[bool], bool]] = None,
        input_mode: Optional[
            Union[
                Literal[
                    "decimal",
                    "email",
                    "none",
                    "numeric",
                    "search",
                    "tel",
                    "text",
                    "url",
                ],
                Var[
                    Literal[
                        "decimal",
                        "email",
                        "none",
                        "numeric",
                        "search",
                        "tel",
                        "text",
                        "url",
                    ]
                ],
            ]
        ] = None,
        item_prop: Optional[Union[Var[str], str]] = None,
        lang: Optional[Union[Var[str], str]] = None,
        role: Optional[
            Union[
                Literal[
                    "alert",
                    "alertdialog",
                    "application",
                    "article",
                    "banner",
                    "button",
                    "cell",
                    "checkbox",
                    "columnheader",
                    "combobox",
                    "complementary",
                    "contentinfo",
                    "definition",
                    "dialog",
                    "directory",
                    "document",
                    "feed",
                    "figure",
                    "form",
                    "grid",
                    "gridcell",
                    "group",
                    "heading",
                    "img",
                    "link",
                    "list",
                    "listbox",
                    "listitem",
                    "log",
                    "main",
                    "marquee",
                    "math",
                    "menu",
                    "menubar",
                    "menuitem",
                    "menuitemcheckbox",
                    "menuitemradio",
                    "navigation",
                    "none",
                    "note",
                    "option",
                    "presentation",
                    "progressbar",
                    "radio",
                    "radiogroup",
                    "region",
                    "row",
                    "rowgroup",
                    "rowheader",
                    "scrollbar",
                    "search",
                    "searchbox",
                    "separator",
                    "slider",
                    "spinbutton",
                    "status",
                    "switch",
                    "tab",
                    "table",
                    "tablist",
                    "tabpanel",
                    "term",
                    "textbox",
                    "timer",
                    "toolbar",
                    "tooltip",
                    "tree",
                    "treegrid",
                    "treeitem",
                ],
                Var[
                    Literal[
                        "alert",
                        "alertdialog",
                        "application",
                        "article",
                        "banner",
                        "button",
                        "cell",
                        "checkbox",
                        "columnheader",
                        "combobox",
                        "complementary",
                        "contentinfo",
                        "definition",
                        "dialog",
                        "directory",
                        "document",
                        "feed",
                        "figure",
                        "form",
                        "grid",
                        "gridcell",
                        "group",
                        "heading",
                        "img",
                        "link",
                        "list",
                        "listbox",
                        "listitem",
                        "log",
                        "main",
                        "marquee",
                        "math",
                        "menu",
                        "menubar",
                        "menuitem",
                        "menuitemcheckbox",
                        "menuitemradio",
                        "navigation",
                        "none",
                        "note",
                        "option",
                        "presentation",
                        "progressbar",
                        "radio",
                        "radiogroup",
                        "region",
                        "row",
                        "rowgroup",
                        "rowheader",
                        "scrollbar",
                        "search",
                        "searchbox",
                        "separator",
                        "slider",
                        "spinbutton",
                        "status",
                        "switch",
                        "tab",
                        "table",
                        "tablist",
                        "tabpanel",
                        "term",
                        "textbox",
                        "timer",
                        "toolbar",
                        "tooltip",
                        "tree",
                        "treegrid",
                        "treeitem",
                    ]
                ],
            ]
        ] = None,
        slot: Optional[Union[Var[str], str]] = None,
        spell_check: Optional[Union[Var[bool], bool]] = None,
        tab_index: Optional[Union[Var[int], int]] = None,
        title: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
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
    ) -> "Link":
        """Create a Link component.

        Args:
            *children: The children of the component.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Text size: "1" - "9"
            weight: Thickness of text: "light" | "regular" | "medium" | "bold"
            trim: Removes the leading trim space: "normal" | "start" | "end" | "both"
            underline: Sets the visibility of the underline affordance: "auto" | "hover" | "always" | "none"
            color_scheme: Overrides the accent color inherited from the Theme.
            high_contrast: Whether to render the text with higher contrast color
            is_external: If True, the link will open in a new tab
            download: Specifies that the target (the file specified in the href attribute) will be downloaded when a user clicks on the hyperlink.
            href: Specifies the URL of the page the link goes to
            href_lang: Specifies the language of the linked document
            media: Specifies what media/device the linked document is optimized for
            ping: Specifies which referrer is sent when fetching the resource
            referrer_policy: Specifies the relationship between the current document and the linked document
            rel: Specifies the relationship between the linked document and the current document
            target: Specifies where to open the linked document
            access_key: Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Raises:
            ValueError: in case of missing children

        Returns:
            Component: The link component
        """
        ...

link = Link.create
