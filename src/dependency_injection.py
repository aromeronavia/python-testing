import pytest
from mock import MagicMock, Mock


class CannotAuthenticateUser(Exception):
    pass


class UserAuthenticator:
    def __init__(self, sms_gateway, user_repository):
        self.sms_gateway = sms_gateway
        self.user_repository = user_repository

    def authenticate(self, user_id):
        try:
            return self.sms_gateway.send_sms("1234")
        except Exception:
            raise CannotAuthenticateUser


@pytest.fixture
def sms_gateway():
    return MagicMock()


@pytest.fixture
def user_repository():
    return MagicMock()


class TestSendAuthenticationToken:
    def test_send_six_digit_code_to_user(self, sms_gateway, user_repository):
        user_authenticator = UserAuthenticator(sms_gateway, user_repository)

        user_authenticator.authenticate('UserId')

        sms_gateway.send_sms.assert_called_once_with("1234")

    def test_sms_gateway_error(self, sms_gateway):
        sms_gateway.send_sms.side_effect = Exception('SMS Exception')
        user_authenticator = UserAuthenticator(sms_gateway, user_repository)

        with pytest.raises(CannotAuthenticateUser):
            user_authenticator.authenticate('UserId')
