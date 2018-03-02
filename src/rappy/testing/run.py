import os
import requests
from rappy.radiomics import Tag2Dcm

TAG_FILE = '/Users/ralph/GoogleDrive/Dbx/Gregory/HP003.tag'
DCM_FILE = '/Users/ralph/GoogleDrive/Dbx/Gregory/HP003.dcm'


def test_tag2dcm_rest():
    print('Running test_tag2dcm()...')
    url = 'http://0.0.0.0:8000/tag2dcm'
    response = requests.get(url)
    print(response.json()['info'])
    files = [
        ('files', ('tag_file', open(TAG_FILE, 'rb'), 'application/octet-stream')),
        ('files', ('dcm_file', open(DCM_FILE, 'rb'), 'application/octet-stream'))]
    response = requests.post(url, files=files)
    output_file_id = response.json()['output_file_id']
    url = 'http://0.0.0.0:8000/tag2dcm/{}'.format(output_file_id)
    response = requests.get(url)
    output_file_path = os.path.join('/tmp', output_file_id)
    with(open(output_file_path, 'wb')) as f:
        for chunk in response.iter_content(1024 * 1024):
            f.write(chunk)
    print(os.path.getsize(output_file_path))


def test_tag2dcm():
    n = Tag2Dcm()
    n.set_input('tag_file', TAG_FILE)
    n.set_input('dcm_file', DCM_FILE)
    n.set_param('output_dir', '/Users/ralph/GoogleDrive/Dbx/Test')
    n.set_param('overwrite', True)
    print(n.get_output('output_file'))


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
