
import random
import requests
import re
import base64
import os

pat = os.getenv('PAT')
random_id = random.randint(1, 100000000)
branch_name = f"bump-version-{random_id}"

def exists_pr():
    url = 'https://api.github.com/repos/weilinfox/ruyi-mugen/pulls'
    headers = {'Authorization': pat}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for pr in response.json():
        if pr['user']['login'] == 'Cyl18-Bot':
            return True
    return False

def get_latest_release_version():
    url = 'https://api.github.com/repos/ruyisdk/ruyi/releases/latest'
    headers = {'Authorization': pat}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    regex_str = "0\\.(\\d+)\\.0"
    return re.search(regex_str, response.json()['tag_name']).group(1)

new_version = int(get_latest_release_version())

def get_file_version():
    url = 'https://github.com/weilinfox/ruyi-mugen/raw/ruyisdk/testcases/cli-test/ruyi/common/common_lib.sh'
    response = requests.get(url)
    response.raise_for_status()
    regex_str = "version=\"0\\.(\\d+)\\.0\""
    return re.search(regex_str, response.text).group(1)


def create_branch_from_upstream():
    # get upstream sha
    url = 'https://api.github.com/repos/weilinfox/ruyi-mugen/git/ref/heads/ruyisdk'
    headers = {'Authorization': pat}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    sha = response.json()['object']['sha']
    # create branch to forked repo
    url = 'https://api.github.com/repos/Cyl18-Bot/ruyi-mugen/git/refs'
    headers = {'Authorization': pat}
    data = {
        "ref": f"refs/heads/{branch_name}",
        "sha": sha
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
def update_file_version():
    # get file blob sha
    url = f'https://api.github.com/repos/Cyl18-Bot/ruyi-mugen/contents/testcases/cli-test/ruyi/common/common_lib.sh?ref={branch_name}'
    headers = {'Authorization': pat}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    sha = response.json()['sha']
    
    content_base64 = response.json()['content']
    content = base64.b64decode(content_base64).decode('utf-8')
    new_content = re.sub("version=\"0\\.\\d+\\.0\"", f"version=\"0.{new_version}.0\"", content)
    new_content_base64 = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    # update file
    url = f'https://api.github.com/repos/Cyl18-Bot/ruyi-mugen/contents/testcases/cli-test/ruyi/common/common_lib.sh'
    headers = {'Authorization': pat}
    data = {
        "message": f"Bump version to 0.{new_version}.0",
        "content": new_content_base64,
        "sha": sha,
        "branch": branch_name
    }
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    
def create_pr():
    url = 'https://api.github.com/repos/weilinfox/ruyi-mugen/pulls'
    headers = {'Authorization': pat}
    data = {
        "title": f"Bump version to 0.{new_version}.0",
        "head": f"Cyl18-Bot:{branch_name}",
        "base": "ruyisdk"
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()


if __name__ == '__main__':
    if (get_latest_release_version() == get_file_version()) or exists_pr():
        print("No need to bump version")
    else:
        create_branch_from_upstream()
        update_file_version()
        create_pr()