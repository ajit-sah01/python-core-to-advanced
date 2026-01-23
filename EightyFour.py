from unittest.mock import Mock

api = Mock()
api.fetch.return_value = {"status": "ok"}

print(api.fetch())
