import requests

TAG_FILE = '/Users/ralph/Data/tag_file.txt'
DCM_FILE = '/Users/ralph/Data/dcm_file.txt'


def run_tests():

    url = 'http://0.0.0.0:8000/tag2dcm'
    response = requests.get(url)
    print(response.status_code)
    files = [
        ('files', ('tag_file', open(TAG_FILE, 'rb'), 'application/octet-stream')),
        ('files', ('dcm_file', open(DCM_FILE, 'rb'), 'application/octet-stream'))]
    response = requests.post(url, files=files)
    print(response.status_code)


if __name__ == '__main__':
    run_tests()
