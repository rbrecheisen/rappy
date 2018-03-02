import os
import requests

TAG_FILE = '/Users/ralph/GoogleDrive/Dbx/Gregory/HP003.tag'
DCM_FILE = '/Users/ralph/GoogleDrive/Dbx/Gregory/HP003.dcm'


def test_tag2dcm():

    print('Running test_tag2dcm()...')

    # POST TAG and DICOM file for conversion
    url = 'http://0.0.0.0:8000/tag2dcm'
    files = [
        ('files', ('tag_file', open(TAG_FILE, 'rb'), 'application/octet-stream')),
        ('files', ('dcm_file', open(DCM_FILE, 'rb'), 'application/octet-stream'))]
    response = requests.post(url, files=files)
    output_file_name = response.json()['output_file_name']

    # Retrieve converted TAG file and print its size. After retrieval the file
    # will be automatically deleted.
    url = 'http://0.0.0.0:8000/tag2dcm/{}'.format(output_file_name)
    response = requests.get(url)
    output_file_path = os.path.join('/tmp', output_file_name)
    with(open(output_file_path, 'wb')) as f:
        for chunk in response.iter_content(1024 * 1024):
            f.write(chunk)
    print(os.path.getsize(output_file_path))


def test_dcm2masks():
    print('Running test_dcm2masks()...')
    pass


if __name__ == '__main__':

    tests = [
        test_tag2dcm,
        test_dcm2masks,
    ]

    for t in tests:
        t()
