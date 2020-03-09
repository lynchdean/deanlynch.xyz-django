import json
import os
import requests
import yaml
import django


def get_projects():
    with open("secrets.yml", 'r') as file:
        secrets = yaml.load(file, Loader=yaml.FullLoader)

    gh = secrets['github']
    response_text = requests.get(gh['repos-url'], auth=(gh['username'], gh['token'])).text
    return json.loads(response_text)


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dl-xyz.settings'
    django.setup()

    from projects.models import Project

    projects = get_projects()
    Project.objects.all().delete()

    for p_data in projects:
        p = Project()
        p.title = p_data['name']
        p.description = p_data['description']
        p.technology = p_data['language']
        p.image = 'img/code-slash.svg'
        p.save()


if __name__ == '__main__':
    main()
