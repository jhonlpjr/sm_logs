from werkzeug.datastructures import MultiDict

class FindLogsRequestDto:
    def __init__(self, filter: MultiDict[str, str]):
        self.filter = filter.to_dict()