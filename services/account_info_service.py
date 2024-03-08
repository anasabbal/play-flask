import logging
from models.account_info import AccountInformation



# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AccountInfoService:

    @staticmethod
    def find_by_email(email: str):
        logger.info(f"Searching for account with email: {email}")
        account = AccountInformation.query.filter(AccountInformation.email == email).first()
        if account:
            logger.info(f"Account found with email: {email}")
            return account
        else:
            logger.info(f"No account found with email: {email}")
            return None