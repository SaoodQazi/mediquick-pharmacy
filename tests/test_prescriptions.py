import io

from app import create_app


def upload(name):
    data = {"file": (io.BytesIO(b"dummy"), name)}
    return create_app().test_client().post(
        "/prescriptions", data=data, content_type="multipart/form-data"
    )


def test_pdf_upload_accepted():
    assert upload("rx.pdf").status_code == 201


def test_invalid_file_type_rejected():
    assert upload("rx.exe").status_code == 400
