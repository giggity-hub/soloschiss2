from typing import NamedTuple, List

class DialogueTurn(NamedTuple):
    user: str
    system: str
    belief: str = ""


Dialogue = List[DialogueTurn]