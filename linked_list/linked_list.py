"""A simple implementation of a list."""


class Link:
    """A link in a linked list.

    Parameters
    ----------
    value :
        The value to be stored in the link.
    link : Link
        The next link in the list.
    """

    def __init__(self, value, next=None):
        """Init module setting value and next."""
        self.value = value
        self.next = next

    def insert(self, link):
        """Insert a new link after this one."""
        link.next = self.next
        self.next = link

    def __iter__(self):
        """Allow usage of LinkIterator modules."""
        return LinkIterator(self)


class LinkIterator:
    """A LinkIterator in a linked list, allow for iteration.

    Parameters
    ----------
    link : LinkIterator
        The next link in the list.
    """

    def __init__(self, link):
        """Init module setting link."""
        self.link = link

    def __iter__(self):
        """Allow iter self."""
        return self

    def __next__(self):
        """Return value of next in list."""
        if not self.link:
            raise StopIteration
        value = self.link.value
        self.link = self.link.next
        return value
