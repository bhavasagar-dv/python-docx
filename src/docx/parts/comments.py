"""|CommentsPart| and closely related objects."""

from typing import TYPE_CHECKING, cast

from docx.opc.constants import CONTENT_TYPE
from docx.opc.packuri import PackURI
from docx.oxml.parser import OxmlElement
from docx.opc.part import XmlPart
from docx.oxml.ns import nsmap

if TYPE_CHECKING:
    from docx.oxml.comments import (
        CT_Comments,
        CT_CommentsExtended,
    )
    from docx.package import Package


class CommentsPart(XmlPart):
    """Proxy for the comments.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w:comments>`` element."""
        partname = PackURI("/word/comments.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS
        element = cast("CT_Comments", OxmlElement("w:comments", nsdecls=nsmap))
        return cls(partname, content_type, element, package)


class CommentsIdsPart(XmlPart):
    """Proxy for the commentsIds.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w16cid:commentsIds>`` element."""
        partname = PackURI("/word/commentsIds.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS_IDS
        element = cast("CT_CommentsIds", OxmlElement("w16cid:commentsIds"))
        return cls(partname, content_type, element, package)


class CommentsExtendedPart(XmlPart):
    """Proxy for the commentsExtended.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w15:commentsEx>`` element."""
        partname = PackURI("/word/commentsExtended.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS_EXTENDED
        element = cast("CT_CommentsExtended", OxmlElement("w15:commentsEx"))
        return cls(partname, content_type, element, package)


class CommentsExtensiblePart(XmlPart):
    """Proxy for the commentsExtensible.xml part containing comments definitions for a document
    or glossary."""

    @classmethod
    def new(cls, package: "Package"):
        """Return newly created empty comments part, containing only the root
        ``<w16cex:commentsExtensible>`` element."""
        partname = PackURI("/word/commentsExtensible.xml")
        content_type = CONTENT_TYPE.WML_COMMENTS_EXTENSIBLE
        element = cast("CT_CommentsExtensible", OxmlElement("w16cex:commentsExtensible"))
        return cls(partname, content_type, element, package)
