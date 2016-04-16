from mondo import MondoClient


class MondoClientStaging(MondoClient):
    BASE_API_URL = 'https://staging-api.gmon.io'
