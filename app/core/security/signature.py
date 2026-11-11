from itsdangerous import Signer, HMACAlgorithm


SECRERT_KEY="FastAPI Course Lesson 13"

__all__ = ("signature", )


class Signature(Signer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def generate(self, value: str | bytes) -> str:
        return super().get_signature(value).decode("utf-8")

    def verify(self, value: str | bytes, sig: str | bytes) -> bool:
        return super().verify_signature(value, sig)


signature = Signature(
    secret_key=SECRERT_KEY,
    algorithm=HMACAlgorithm(),
)
