import uuid


def gen_uuid(prefix):
    return prefix + "-" + uuid.uuid4().__str__()
