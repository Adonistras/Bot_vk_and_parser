from main import my_token_vk
import requests


"""Parses members of intersects groups"""
def cross_groups(list_of_groups):
    previous_members = None
    for group in list_of_groups:
        group_url = f'https://api.vk.com/method/groups.getMembers?group_id={group}&fields=domain&access_token={my_token_vk}&v=5.131'
        req = requests.get(group_url)
        src = req.json()
        members = src['response']['items']

        if previous_members:
            previous_members = [i for i in previous_members if i in members]
        else:
            previous_members = members
    return [f'vk.com/{_["domain"]}/' for _ in previous_members]



if __name__ == '__main__':
    groups = input().split()
    print(cross_groups(groups))


