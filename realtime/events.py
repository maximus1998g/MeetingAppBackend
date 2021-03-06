WEBSOCKET_DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class RequestEvent:
    def __init__(self, id, event, title, from_user, to_user, decision, created):
        self._type = "request_event"
        self._id = id
        self._event = event
        self._title = title
        self._from_user = from_user
        self._to_user = to_user
        self._decision = decision
        self._created = created

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def event(self):
        return str(self._event)

    @property
    def title(self):
        return self._title

    @property
    def from_user(self):
        return self._from_user

    @property
    def to_user(self):
        return self._to_user

    @property
    def decision(self):
        return str(self._decision)

    @property
    def created(self):
        return self._created.strftime(WEBSOCKET_DATE_TIME_FORMAT)

    @property
    def properties_dict(self):
        return dict(
            type=self.type,
            id=self.id,
            event=self.event,
            title=self.title,
            from_user=self.from_user,
            to_user=self.to_user,
            decision=self.decision,
            created=self.created,
        )


class MessageEvent:
    def __init__(self, from_user, chat, id, text, created, event, is_systemic):
        self._type = "message_event"
        self._from_user = from_user
        self._chat = chat
        self._id = id
        self._text = text
        self._created = created
        self._event = event
        self._is_systemic = is_systemic

    @property
    def type(self):
        return self._type

    @property
    def from_user(self):
        return self._from_user

    @property
    def chat(self):
        return self._chat

    @property
    def id(self):
        return self._id

    @property
    def text(self):
        return self._text

    @property
    def created(self):
        return self._created.strftime(WEBSOCKET_DATE_TIME_FORMAT)

    @property
    def event(self):
        return str(self._event)

    @property
    def is_systemic(self):
        return self._is_systemic

    @property
    def properties_dict(self):
        return dict(
            type=self.type,
            from_user=self.from_user,
            chat=self.chat,
            id=self.id,
            text=self.text,
            created=self.created,
            event=self.event,
            is_systemic=self.is_systemic
        )


class PrivateMessageEvent:
    def __init__(self, from_user, user, text, created):
        self._type = "private_message_event"
        self._from_user = from_user
        self._user = user
        self._text = text
        self._created = created

    @property
    def type(self):
        return self._type

    @property
    def from_user(self):
        return str(self._from_user)

    @property
    def user(self):
        return str(self._user)

    @property
    def text(self):
        return self._text

    @property
    def created(self):
        return self._created.strftime(WEBSOCKET_DATE_TIME_FORMAT)

    @property
    def properties_dict(self):
        return dict(
            type=self.type,
            from_user=self.from_user,
            user=self.user,
            text=self.text,
            created=self.created,
        )
