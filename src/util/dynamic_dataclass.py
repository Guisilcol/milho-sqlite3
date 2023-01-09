from dataclasses import dataclass, fields, asdict

@dataclass(init=False)
class DynamicDataclass:
    def __init__(self, **kwargs):
        fields_name = set([field.name for field in fields(self)])
        for key, value in kwargs.items():
            if key in fields_name:
                setattr(self, key, value)

    def dict(self):
        return asdict(self)