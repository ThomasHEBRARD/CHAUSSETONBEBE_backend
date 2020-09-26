def create_if_non_existent(apps, app_name, model_name, params):
    model = apps.get_model(app_name, model_name)
    model.objects.get_or_create(**params)
