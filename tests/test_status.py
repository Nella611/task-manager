from django.urls import reverse_lazy
from task_manager.statuses.models import Status
import pytest
from tests.assert_ import redirect_to_login
from task_manager.logger_config import logger

CREATE_URL = reverse_lazy('task_create')
UPDATE_URL = 'tasks/{id}/update'
DELETE_URL = 'tasks/{id}/delete'
INPUT_DATA = dict(name='task_test')


@pytest.fixture
def model():
    logger.error(Status)
    return Status


@pytest.mark.usefixtures('authorized')
@pytest.mark.django_db
def test_create(client, model, input_data):
    client.post(CREATE_URL, input_data)
    assert model.objects.get(name=input_data['name'])


@pytest.mark.usefixtures('authorized')
@pytest.mark.django_db
def test_update(client, model, input_data, created_object):
    old_name = created_object.name
    url = UPDATE_URL.format(id=created_object.id)
    logger.error(url)
    input_data['name'] = 'new_name'
    client.post(url, input_data)
    assert model.objects.filter(name=old_name).count() == 0
    assert model.objects.get(name=input_data['name'])


@pytest.mark.usefixtures('authorized')
@pytest.mark.django_db
def test_delete(client, model, input_data, created_object):
    client.post(DELETE_URL.format(id=created_object.id))
    assert model.objects.filter(name=created_object.id).count() == 0


@pytest.mark.parametrize(
    ('url', 'params'),
    [(UPDATE_URL, {'name': 'other'}), (DELETE_URL, {})]
)
@pytest.mark.django_db
def test_unauthorized(
        client, model, created_object, url, params, input_data
):
    current_params = ({**input_data, **params} if params else {})
    response = client.post(url.format(id=created_object.id), current_params)
    assert redirect_to_login(response)
    current_status = model.objects.get(id=created_object.id)
    assert current_status == created_object