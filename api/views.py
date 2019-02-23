from django.shortcuts import render


def index(license: str, version: str):
    return f'<h1>{license}: {version}</h1>'
