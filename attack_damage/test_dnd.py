from dnd import attack_damage
from unittest import mock

@mock.patch("dnd.randint", return_value=6, autospec=True)
def test_attack_damage(mock_randint):
    assert attack_damage(3) == 9
    mock_randint.assert_called_once_with(1, 8)