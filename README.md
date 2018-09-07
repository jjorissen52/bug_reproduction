# bug_reproduction
repository for sharing bug reproduction projects

### Call Gateway Bug
1) virtual environment
2) `pip install -r requirements.txt`
3) add a file called `secrets.ini` within the folder `bug_reproduction` that looks like: 
    ```angular2html
    [twilio]
    TWILIO_ACCOUNT_SID = <your SID>
    TWILIO_AUTH_TOKEN = <your token>
    TWILIO_CALLER_ID = <your number>
    ```
4) `python manage.py createsuperuser`
5) `python manage.py runserver localhost:8000`
6) visit [http://localhost:8000/account/login](http://localhost:8000/account/login)
7) login normally, attempt to add a number to call

```angular2html
[07/Sep/2018 17:26:33] "POST /account/two_factor/setup/ HTTP/1.1" 200 1995
Could not generate challenge
Traceback (most recent call last):
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/django/urls/base.py", line 77, in reverse
    extra, resolver = resolver.namespace_dict[ns]
KeyError: 'two_factor_twilio'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/two_factor/views/core.py", line 274, in render_next_step
    self.get_device().generate_challenge()
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/two_factor/models.py", line 114, in generate_challenge
    make_call(device=self, token=token)
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/two_factor/gateways/__init__.py", line 11, in make_call
    gateway.make_call(device=device, token=token)
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/two_factor/gateways/twilio/gateway.py", line 53, in make_call
    url = reverse('two_factor_twilio:call_app', kwargs={'token': token})
  File "/home/jp/Projects/venvs/venv_call_gateway_bug/lib/python3.6/site-packages/django/urls/base.py", line 87, in reverse
    raise NoReverseMatch("%s is not a registered namespace" % key)
django.urls.exceptions.NoReverseMatch: 'two_factor_twilio' is not a registered namespace
```
