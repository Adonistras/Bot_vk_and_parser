import os
from main import my_token_vk
import requests
import time


"""VK-BOT that parses hot vacancies from the set of groups by using keywords"""
def get_wall_posts(group_name, keywords, days=7):
    days_in_seconds = 60 * 60 * 24 * days
    url = f'https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={my_token_vk}&v=5.131'
    req = requests.get(url)
    src = req.json()
    posts = src['response']['items']

    if not os.path.exists('Hot Vacancy - Python'):
        os.mkdir('Hot Vacancy - Python')


    """Writing data into the file"""
    with open(f'Hot Vacancy - Python/{time.strftime("%d %m", time.localtime(time.time()))}.txt', "a", encoding='utf-8') as file:
            for post in posts:
                if days_in_seconds < time.time() - post['date']:
                    break
                if set.intersection(set(keywords), set(post['text'].lower().split())):
                    file.write(f'vk.com/{group_name}\n{post["text"]}\n{time.strftime("%m/%d %H:%M", time.localtime(post["date"]))}')
                    file.write('\n\n\n________________________________________________________\n\n\n')


def main():

    """Enter list of groups"""
    groups = input().split()
    """Enter keywords"""
    keywords = input().split()


    for group_name in groups:
        get_wall_posts(group_name, keywords)


if __name__ == '__main__':
    main()